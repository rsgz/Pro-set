use actix_cors::Cors; // actix-cors = "0.6.4"
use actix_web::{web, App, HttpResponse, HttpServer, Responder}; // actix_web::*: 包含了构建 Web 应用所需的核心组件。
use serde::{Deserialize, Serialize}; // serde::*: 提供了序列化和反序列化的功能，用于处理 JSON 数据。
use std::sync::Mutex; // std::sync::Mutex: 提供线程安全的方式来访问共享数据。
use uuid::Uuid; //uuid::Uuid: 用于生成唯一标识符。

// 定义了一个 BookMark 结构体来表示一个书签，并且实现了 Serialize, Deserialize, 和 Clone trait，以便可以序列化为 JSON 格式，从 JSON 解析，以及进行克隆操作
#[derive(Serialize, Deserialize, Clone, Debug)]
struct BookMark {
    id: String,
    name: String,
    url: String,
    source: String,
    purpose: String,
    tag: String,
}

// 定义查询参数结构体
#[derive(Serialize, Deserialize, Clone, Debug)]
struct SearchParams {
    name: Option<String>,
    source: Option<String>,
    tag: Option<String>,
    page: Option<usize>,
    limit: Option<usize>,
}

// 定义了 AppState 结构体，其中包含一个 Mutex 保护的 Vec<BookMark>，用于存储所有的书签信息，确保在并发环境下对书签列表的安全访问
struct AppState {
    bookmarks: Mutex<Vec<BookMark>>,
}
// get_bookmarks 函数异步获取所有书签
// 使用 lock() 方法锁定 Mutex 并返回一个 MutexGuard，然后解引用这个 MutexGuard 来访问实际的数据
// 返回 HTTP 响应，状态码为 200（OK），并将书签列表作为 JSON 发送回客户端。
async fn get_bookmarks1(data: web::Data<AppState>) -> impl Responder {
    println!("请求 书签信息");
    // 如果请求中带有查询参数，就执行搜索；否则返回所有书签。下面是改进后的代码：
    let bookmarks = data.bookmarks.lock().unwrap();
    HttpResponse::Ok().json(&*bookmarks) // 解引用 MutexGuard
}

async fn get_bookmarks2(
    data: web::Data<AppState>,
    query: web::Query<SearchParams>, // 提取查询参数
) -> impl Responder {
    println!("请求 书签信息");

    let bookmarks = data.bookmarks.lock().unwrap();
    let mut filtered: Vec<BookMark> = bookmarks.clone();

    // 如果存在查询参数，则过滤书签数据
    if let Some(name) = &query.name {
        filtered.retain(|b| b.name.contains(name));
    }
    if let Some(source) = &query.source {
        if !source.is_empty() {
            filtered.retain(|b| b.source.contains(source));
        }
    }
    if let Some(tag) = &query.tag {
        if !tag.is_empty() {
            filtered.retain(|b| b.tag.contains(tag));
        }
    }

    // 分页处理
    if let Some(limit) = query.limit {
        let page = query.page.unwrap_or(1);
        let start = (page - 1) * limit;
        // let end = start + limit;

        filtered = filtered
            .into_iter()
            .skip(start)
            .take(limit)
            .collect::<Vec<_>>();
    }

    // 返回结果
    HttpResponse::Ok().json(&filtered)
}

async fn get_bookmarks(
    data: web::Data<AppState>,
    query: web::Query<SearchParams>, // 提取查询参数
) -> impl Responder {
    println!("请求书签信息");

    let bookmarks = data.bookmarks.lock().unwrap();
    let mut filtered: Vec<BookMark> = bookmarks.clone();

    if query.name.as_ref().map_or(true, |name| name.is_empty())
        && query
            .source
            .as_ref()
            .map_or(true, |source| source.is_empty())
        && query.tag.as_ref().map_or(true, |tag| tag.is_empty())
    {
        // 如果所有条件为空，直接返回所有内容的第 page 页
        return paginate_results(
            &bookmarks,
            query.page.unwrap_or(1),
            query.limit.unwrap_or(10),
        );
    }

    // 分别对每个搜索条件判断和过滤
    if let Some(name) = &query.name {
        if !name.is_empty() {
            filtered.retain(|b| b.name.contains(name));
        }
    }
    if let Some(source) = &query.source {
        if !source.is_empty() {
            filtered.retain(|b| b.source.contains(source));
        }
    }
    if let Some(tag) = &query.tag {
        if !tag.is_empty() {
            filtered.retain(|b| b.tag.contains(tag));
        }
    }

    // 返回过滤后的结果并分页
    paginate_results(
        &filtered,
        query.page.unwrap_or(1),
        query.limit.unwrap_or(10),
    )
}

// 辅助函数：进行分页处理
fn paginate_results1<T: Clone + serde::Serialize>(
    items: &[T],
    page: usize,
    limit: usize,
) -> HttpResponse {
    let start = (page - 1) * limit;
    // let end = start + limit;

    let paginated_items = items
        .iter()
        .skip(start)
        .take(limit)
        .cloned()
        .collect::<Vec<_>>();

    HttpResponse::Ok().json(paginated_items)
}

// 辅助函数：进行分页处理  v2 版本 实现了 返回 更加详细的 json数据
fn paginate_results<T: Clone + serde::Serialize>(
    items: &[T],
    page: usize,
    limit: usize,
) -> HttpResponse {
    let total = items.len(); // 总记录数
    let start = (page - 1) * limit;
    let paginated_items = items
        .iter()
        .skip(start)
        .take(limit)
        .cloned()
        .collect::<Vec<_>>();
    HttpResponse::Ok().json(serde_json::json!({
        "data": paginated_items, // 当前页的数据
        "total": total,          // 总记录数
        "page": page,            // 当前页码
        "limit": limit           // 每页大小
    }))
}

// add_bookmark 函数异步处理添加新书签的请求
// 通过 into_inner() 方法将 web::Json<BookMark> 转换为 BookMark 实例
//为新书签生成一个新的 UUID 作为其 ID
//将新的书签添加到 bookmarks 列表中，并返回更新后的书签列表
async fn add_bookmark(
    data: web::Data<AppState>,
    new_bookmark: web::Json<BookMark>,
) -> impl Responder {
    println!("触发了  添加书签动作");
    let mut bookmarks = data.bookmarks.lock().unwrap(); // 先获取书签实例
    let mut bookmark = new_bookmark.into_inner();
    bookmark.id = Uuid::new_v4().to_string();

    // 打印各个属性值
    println!("ID: {}", bookmark.id);
    println!("Name: {}", bookmark.name);
    println!("URL: {}", bookmark.url);
    println!("Source: {}", bookmark.source);
    println!("Purpose: {}", bookmark.purpose);
    println!("Tag: {}", bookmark.tag);

    bookmarks.push(bookmark);
    HttpResponse::Ok().json(&*bookmarks) // 解引用 MutexGuard
}

// delete_bookmark 函数异步处理删除指定 ID 的书签
// 使用 retain 方法过滤掉与给定 ID 不匹配的所有书签
// 返回更新后的书签列表
async fn delete_bookmark(data: web::Data<AppState>, id: web::Path<String>) -> impl Responder {
    println!("删除 书签信息");
    let mut bookmarks = data.bookmarks.lock().unwrap();
    bookmarks.retain(|b| b.id != *id);
    HttpResponse::Ok().json(&*bookmarks) // 解引用 MutexGuard
}

// 更新书签信息的函数
async fn update_bookmark(
    data: web::Data<AppState>,
    id: web::Path<String>,
    updated_bookmark: web::Json<BookMark>,
) -> impl Responder {
    println!("更新 书签信息");
    let mut bookmarks = data.bookmarks.lock().unwrap();
    // 查找并更新匹配的书签
    if let Some(bookmark) = bookmarks.iter_mut().find(|b| b.id == *id) {
        bookmark.name = updated_bookmark.name.clone();
        bookmark.url = updated_bookmark.url.clone();
        bookmark.source = updated_bookmark.source.clone();
        bookmark.purpose = updated_bookmark.purpose.clone();
        bookmark.tag = updated_bookmark.tag.clone();
        println!("书签已更新: {:#?}", bookmark);
        HttpResponse::Ok().json(bookmark) // 返回更新后的书签
    } else {
        println!("未找到书签 ID: {}", id);
        HttpResponse::NotFound().body("Bookmark not found")
    }
}

// 搜索功能

// 使用 actix_web::main 宏标记主函数，使其能够以异步方式运行。
// 创建 AppState 的实例并将其包装在 web::Data 中，以便在整个应用程序中共享。
// 设置 HttpServer，配置路由：
// /bookmarks GET 请求映射到 get_bookmarks 函数。
// /bookmarks POST 请求映射到 add_bookmark 函数。
// /bookmarks/{id} DELETE 请求映射到 delete_bookmark 函数。
// 绑定服务器到 127.0.0.1:8080 地址，并启动服务器。
#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let app_state = web::Data::new(AppState {
        bookmarks: Mutex::new(Vec::new()),
    });

    HttpServer::new(move || {
        App::new()
            .wrap(Cors::default()) // 允许所有来源的跨域请求  use actix_cors::Cors;
            .app_data(app_state.clone())
            .route("/api/bookmarks", web::post().to(add_bookmark)) // 增
            .route("/api/bookmarks/{id}", web::delete().to(delete_bookmark)) // 删
            .route("/api/bookmarks/{id}", web::put().to(update_bookmark)) // 改
            .route("/api/bookmarks", web::get().to(get_bookmarks)) // 查+搜索
    })
    .bind("127.0.0.1:8000")?
    .run()
    .await
}

// 上面的代码 其实是操作内存中的 直接操作内存中的 Vec<BookMark>  来模拟数据库 并不是真正的 实现和数据库的交互
