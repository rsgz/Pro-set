use actix_cors::Cors; // actix-cors = "0.6.4"
use actix_web::{web, App, HttpResponse, HttpServer, Responder}; // actix_web::*: 包含了构建 Web 应用所需的核心组件。
use serde::{Deserialize, Serialize}; // serde::*: 提供了序列化和反序列化的功能，用于处理 JSON 数据。
use sqlx::mysql::MySqlPool;
use sqlx::query;
use sqlx::FromRow;
use sqlx::Row;
use std::sync::Mutex; // std::sync::Mutex: 提供线程安全的方式来访问共享数据。
use uuid::Uuid; //uuid::Uuid: 用于生成唯一标识符。 // O: for<'r> FromRow<'r, DB::Row>, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ required by this bound in `query_as`

/*
创建 MySQL 数据表
运行以下 SQL 脚本创建 bookmarks 表

CREATE TABLE bookmarks (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    url TEXT NOT NULL,
    source VARCHAR(255),
    purpose TEXT,
    tag VARCHAR(255)
);
*/

// 定义了一个 BookMark 结构体来表示一个书签，并且实现了 Serialize, Deserialize, 和 Clone trait，以便可以序列化为 JSON 格式，从 JSON 解析，以及进行克隆操作
#[derive(Serialize, Deserialize, Clone, Debug, FromRow)]
struct BookMark {
    id: String,
    name: String,
    url: String,
    // source: String, // 数据库中的某些字段允许为空（例如 source 或 purpose） 字段的类型改为 Option<String>
    // purpose: String,
    // tag: String,
    source: Option<String>,  // 修改为 Option<String>
    purpose: Option<String>, // 修改为 Option<String>
    // tag: Option<String>, // 修改为 Option<String>  当这些字段是 NULL 时，Rust 会将它们映射为 None，而不是直接尝试转换为 String 类型。
    // tag: Option<Vec<String>>, // tag: Option<Vec<String>>, // 支持标签的 JSON 数组结构
    tag: Option<serde_json::Value>, // 使用 serde_json::Value 处理 JSON 数据
    // clicks: i32,         // 新增点击量字段
    clicks: Option<i32>, // 新增点击量字段
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
#[allow(dead_code)] // To remove the warning.  这个可以去除警告 故意保留一个结构体
struct AppState {
    bookmarks: Mutex<Vec<BookMark>>,
}

// 添加书签
async fn add_bookmark(
    pool: web::Data<MySqlPool>,
    new_bookmark: web::Json<BookMark>,
) -> impl Responder {
    println!("添加书签!");
    let bookmark = new_bookmark.into_inner();
    let id = Uuid::new_v4().to_string();
    // let query = r#"
    //     INSERT INTO bookmarks (id, name, url, source, purpose, tag)
    //     VALUES (?, ?, ?, ?, ?, ?)
    // "#;

    match query!(
        r#"
    INSERT INTO bookmarks (id, name, url, source, purpose, tag)
    VALUES (?, ?, ?, ?, ?, ?)
    "#,
        id,
        bookmark.name,
        bookmark.url,
        bookmark.source,
        bookmark.purpose,
        // bookmark.tag
        serde_json::to_value(bookmark.tag).unwrap() // 转换标签为 JSON 格式
    )
    .execute(pool.get_ref())
    .await
    {
        // Ok(_) => HttpResponse::Ok().json("Bookmark 添加成功!"),
        Ok(_) => {
            // 在插入成功后查询所有书签
            let bookmarks = sqlx::query_as!(
                BookMark,
                r#"SELECT id, name, url, source, purpose, tag, clicks FROM bookmarks"#
            )
            .fetch_all(pool.get_ref())
            .await
            .unwrap_or_else(|_| vec![]); // 如果查询失败，返回空数组

            // 示例：将 tag 从 serde_json::Value 转换为 Vec<String>
            let parsed_bookmarks: Vec<BookMark> = bookmarks
                .into_iter()
                .map(|mut bookmark| {
                    if let Some(tag_value) = &bookmark.tag {
                        // 尝试将 tag 的 JSON 数据解析为 Vec<String>
                        bookmark.tag = Some(
                            tag_value
                                .as_array()
                                .unwrap_or(&vec![])
                                .iter()
                                .filter_map(|v| v.as_str().map(|s| s.to_string()))
                                .collect(),
                        );
                    }
                    bookmark
                })
                .collect();

            HttpResponse::Ok().json(parsed_bookmarks) // 返回完整书签列表
        }
        Err(err) => HttpResponse::InternalServerError().body(format!("添加失败: {}", err)),
        Err(err) => HttpResponse::InternalServerError().body(format!("添加失败: {}", err)),
    }
}

// 获取书签  无效
async fn get_bookmarks1(
    pool: web::Data<MySqlPool>,
    query: web::Query<SearchParams>,
) -> impl Responder {
    println!("获取/查看书签!");
    let mut sql_query = String::from("SELECT * FROM bookmarks WHERE 1 = 1");
    if let Some(name) = &query.name {
        sql_query.push_str(&format!(" AND name LIKE '%{}%'", name));
    }
    if let Some(source) = &query.source {
        sql_query.push_str(&format!(" AND source LIKE '%{}%'", source));
    }
    if let Some(tag) = &query.tag {
        sql_query.push_str(&format!(" AND tag LIKE '%{}%'", tag));
    }

    match sqlx::query_as::<_, BookMark>(&sql_query)
        .fetch_all(pool.get_ref())
        .await
    {
        Ok(bookmarks) => HttpResponse::Ok().json(bookmarks),
        Err(err) => HttpResponse::InternalServerError().body(format!("Error: {}", err)),
    }
}

// 获取书签 v2
async fn get_bookmarks(
    pool: web::Data<MySqlPool>,
    query: web::Query<SearchParams>,
) -> impl Responder {
    println!("请求书签信息");

    let page = query.page.unwrap_or(1); // 默认第一页
    let limit = query.limit.unwrap_or(10); // 默认每页 10 条数据
    let offset = (page - 1) * limit; // 偏移量计算

    let mut sql_query = String::from("SELECT * FROM bookmarks WHERE 1 = 1");
    // let mut sql_query = String::from("SELECT id, name, url, source, purpose, tag, clicks FROM bookmarks WHERE 1 = 1");

    let mut count_query = String::from("SELECT COUNT(*) as total FROM bookmarks WHERE 1 = 1");

    // 动态拼接 SQL 语句
    if let Some(name) = &query.name {
        if !name.is_empty() {
            sql_query.push_str(" AND name LIKE ?");
            count_query.push_str(" AND name LIKE ?");
        }
    }

    if let Some(source) = &query.source {
        if !source.is_empty() {
            sql_query.push_str(" AND source LIKE ?");
            count_query.push_str(" AND source LIKE ?");
        }
    }

    // if let Some(tag) = &query.tag {
    //     if !tag.is_empty() {
    //         sql_query.push_str(" AND tag LIKE ?");
    //         count_query.push_str(" AND tag LIKE ?");
    //     }
    // }

    if let Some(tag) = &query.tag {
        if !tag.is_empty() {
            sql_query.push_str(" AND JSON_CONTAINS(tag, ?)");
        }
    }

    // 添加分页逻辑
    sql_query.push_str(" LIMIT ? OFFSET ?");

    // 动态绑定查询参数（逐个绑定）
    let mut bookmarks_query = sqlx::query_as::<_, BookMark>(&sql_query);
    let mut count_query_exec = sqlx::query_scalar::<_, i64>(&count_query);

    if let Some(name) = &query.name {
        if !name.is_empty() {
            bookmarks_query = bookmarks_query.bind(format!("%{}%", name));
            count_query_exec = count_query_exec.bind(format!("%{}%", name));
        }
    }

    if let Some(source) = &query.source {
        if !source.is_empty() {
            bookmarks_query = bookmarks_query.bind(format!("%{}%", source));
            count_query_exec = count_query_exec.bind(format!("%{}%", source));
        }
    }

    // if let Some(tag) = &query.tag {
    //     if !tag.is_empty() {
    //         bookmarks_query = bookmarks_query.bind(format!("%{}%", tag));
    //         count_query_exec = count_query_exec.bind(format!("%{}%", tag));
    //     }
    // }

    if let Some(tag) = &query.tag {
        if !tag.is_empty() {
            bookmarks_query = bookmarks_query.bind(serde_json::to_string(&tag).unwrap());
        }
    }

    // 在这里进行类型转换
    bookmarks_query = bookmarks_query
        .bind(limit as i64) // 转换 limit 为 i64
        .bind(offset as i64); // 转换 offset 为 i64

    // 执行查询
    let bookmarks_result = bookmarks_query.fetch_all(pool.get_ref()).await;
    let total_result = count_query_exec.fetch_one(pool.get_ref()).await;

    match (bookmarks_result, total_result) {
        (Ok(bookmarks), Ok(total)) => {
            HttpResponse::Ok().json(serde_json::json!({
                "data": bookmarks, // 当前页数据
                "total": total,    // 总记录数
                "page": page,      // 当前页码
                "limit": limit     // 每页大小
            }))
        }
        (Err(err), _) => HttpResponse::InternalServerError().body(format!("获取书签失败: {}", err)),
        (_, Err(err)) => {
            HttpResponse::InternalServerError().body(format!("获取书签总数失败: {}", err))
        }
    }
}

// 删除书签
async fn delete_bookmark(pool: web::Data<MySqlPool>, id: web::Path<String>) -> impl Responder {
    println!("删除书签!");
    let query = "DELETE FROM bookmarks WHERE id = ?";
    match sqlx::query(query).bind(&*id).execute(pool.get_ref()).await {
        Ok(_) => HttpResponse::Ok().body("Bookmark deleted successfully"),
        Err(err) => HttpResponse::InternalServerError().body(format!("Failed to delete: {}", err)),
    }
}

// 更新书签
async fn update_bookmark(
    pool: web::Data<MySqlPool>,
    id: web::Path<String>,
    updated_bookmark: web::Json<BookMark>,
) -> impl Responder {
    println!("更新书签!");
    let query = r#"
        UPDATE bookmarks
        SET name = ?, url = ?, source = ?, purpose = ?, tag = ?
        WHERE id = ?
    "#;

    match sqlx::query(query)
        .bind(&updated_bookmark.name)
        .bind(&updated_bookmark.url)
        .bind(&updated_bookmark.source)
        .bind(&updated_bookmark.purpose)
        // .bind(&updated_bookmark.tag)
        .bind(serde_json::to_value(&updated_bookmark.tag).unwrap()) // 转换标签为 JSON 格式
        .bind(&*id)
        .execute(pool.get_ref())
        .await
    {
        Ok(_) => HttpResponse::Ok().body("Bookmark updated successfully"),
        Err(err) => HttpResponse::InternalServerError().body(format!("Failed to update: {}", err)),
    }
}

// 更新点击量
async fn increment_clicks(pool: web::Data<MySqlPool>, id: web::Path<String>) -> impl Responder {
    println!("更新书签点击量: {}", id);
    // 更新点击量的 SQL 查询
    let query = r#"
        UPDATE bookmarks
        SET clicks = clicks + 1
        WHERE id = ?
    "#;
    match sqlx::query(query)
        .bind(&*id) // 绑定书签 ID
        .execute(pool.get_ref())
        .await
    {
        Ok(_) => HttpResponse::Ok().body("点击量已更新"),
        Err(err) => HttpResponse::InternalServerError().body(format!("更新点击量失败: {}", err)),
    }
}

// 在 main 函数中使用 sqlx 创建一个连接池。
#[actix_web::main]
async fn main() -> std::io::Result<()> {
    // 创建 MySQL 数据库连接池
    // let database_url = "mysql://username:password@localhost:3306/your_database"; // 替换为你的 MySQL 信息
    let database_url = "mysql://root:xueFei1998@localhost:3306/rsgz_01"; // 替换为你的 MySQL 信息
    let pool = MySqlPool::connect(database_url)
        .await
        .expect("无法连接到数据库,如果mysql服务没有开启,请开启：net start MySQL84");
    println!("==========================连接数据库成功!!!==========================");
    HttpServer::new(move || {
        App::new()
            .wrap(Cors::default())
            .app_data(web::Data::new(pool.clone())) // 将数据库连接池添加到应用状态中
            .route("/api/bookmarks", web::post().to(add_bookmark))
            .route("/api/bookmarks/{id}", web::delete().to(delete_bookmark))
            .route("/api/bookmarks/{id}", web::put().to(update_bookmark))
            .route("/api/bookmarks", web::get().to(get_bookmarks))
            .route(
                "/api/bookmarks/{id}/incrementClicks",
                web::post().to(increment_clicks),
            )
    })
    .bind("127.0.0.1:8000")?
    .run()
    .await
}
