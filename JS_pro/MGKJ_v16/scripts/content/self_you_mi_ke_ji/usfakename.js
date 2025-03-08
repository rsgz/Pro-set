var usfakename_url = "https://usfakename.com/";
var shop6888_url = "https://b08-admin.shop6888.com/"
var shop6888_kucun_url = "https://b08-admin.shop6888.com/#/goods/goodsManagement"
var shop6888_kucun_url_wangzhan = "https://b08-admin.shop6888.com/#/goods/shopGoodsManagement"

muban_xuhao = 11



// 复制文本
function copyTextToClipboard(text) {
    const textArea = document.createElement("textarea");
    textArea.value = text;
    document.body.appendChild(textArea);
    textArea.select();
    try {
        const successful = document.execCommand('copy');
        const msg = successful ? 'successful' : 'unsuccessful';
        console.log('Copying text command was ' + msg);
    } catch (err) {
        console.error('Oops, unable to copy', err);
    }
    document.body.removeChild(textArea);
}

// 颜色预设  编号 域名获取
window.onload = function () {
    if (window.location.href.startsWith(shop6888_url)) {
        // console.log("shop6888_url 颜色预设!");

        async function fun1() {
        }

        fun1();
    }
};


// $(document).ready(function() {

// });

// 内部预览 https://b08.shop6888.com/redirect?websiteid=264

// 任何网站都执行  注入jq
chrome.runtime.onMessage.addListener(async function (request, sender, sendResponse) {
    if (request.myshopify_zhuru_jq === "myshopify_zhuru_jq") {
        console.log("request.myshopify_zhuru_jq");
        (async () => {
            let s = `var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
document.getElementsByTagName('head')[0].appendChild(script);`
            console.log(s);
            copyTextToClipboard(s);
        })();
    }

    if (request.myshopify_2024_8_29_myshopify_wangzhi_renyi === "myshopify_2024_8_29_myshopify_wangzhi_renyi") {
        console.log("request.myshopify_2024_8_29_myshopify_wangzhi_renyi");
        var myshopify_url_all = '';
        $(`div cite`).each(function () {
            var myshopify_url = $(this).eq(0).text();
            if (myshopify_url.search("myshopify.com") != -1) {
                // console.log(myshopify_url);
                myshopify_url_all = myshopify_url + '\n' + myshopify_url_all;
            }
        })
        console.log(myshopify_url_all);
        copyTextToClipboard(myshopify_url_all);
        console.log('所有网址复制成功!!!');
        console.log('所有网址复制成功!!!');
        console.log('所有网址复制成功!!!');
        console.log('所有网址复制成功!!!');
        console.log('所有网址复制成功!!!');
    }

    // 谷歌更多结果
    if (request.myshopify_2024_8_29_myshopify_guge_gengduo_btn_click === "myshopify_2024_8_29_myshopify_guge_gengduo_btn_click") {
        console.log("request.myshopify_2024_8_29_myshopify_guge_gengduo_btn_click");
        for (var i = 0; i < 60; i++) {
            try {
                await $(`h3 span:contains(更多结果):eq(0)`).click();
                await delay(3000);
            }
            catch (e) {
                console.error('↓ ↓ ↓ ↓ ↓ ↓ 本帅哥发现一个超级错误: ↓ ↓ ↓ ↓ ↓ ↓ ', error);
                throw error;
            }
        }
    }


    /*
    (async ()=>{
        var script = document.createElement('script');
        script.src = 'https://code.jquery.com/jquery-3.6.0.min.js'; // 替换成你需要的版本
        document.getElementsByTagName('head')[0].appendChild(script);
    })();
    console.log('jq插入成功!');
    */
    // 库存序号
    if (request.myshopify_tianjia_kucun_xuhao === "myshopify_tianjia_kucun_xuhao") {
        console.log("request.myshopify_tianjia_kucun_xuhao");
        async function f1() {
            try {
                len = document.querySelectorAll(`table.el-table__body tr`).length;
                for (var i = 0; i < len; i++) {
                    var tr = document.querySelectorAll(`table.el-table__body tr`)[i];
                    var title = tr.querySelectorAll(`td`)[3]; // title
                    var id = tr.querySelectorAll(`td`)[1]; // id
                    var danxuankuang = tr.querySelectorAll(`td`)[0];  // 单选框

                    let new_title = String(i + 1) + "--->" + title.innerText;
                    title.innerText = new_title;
                }
            } catch (error) {
                console.error("出现错误:", error);
            }
        }

        f1();
    }
    // 库存连选
    if (request.myshopify_kucun_lianxuan === "myshopify_kucun_lianxuan") {
        console.log("request.myshopify_kucun_lianxuan");
        async function f1() {
            try {
                var xuanze_fanwei = request.xuanze_fanwei;
                const fanwei_start = xuanze_fanwei.trim().split('-')[0];
                const fanwei_end = xuanze_fanwei.trim().split('-')[1];

                console.log("选择范围:");
                console.log(fanwei_start);
                console.log(fanwei_end);

                len = document.querySelectorAll(`table.el-table__body tr`).length;
                for (var i = 0; i < len; i++) {
                    var tr = document.querySelectorAll(`table.el-table__body tr`)[i];
                    var title = tr.querySelectorAll(`td`)[3]; // title
                    var id = tr.querySelectorAll(`td`)[1]; // id
                    var danxuankuang = tr.querySelectorAll(`td`)[0];  // 单选框

                    // let new_title= String(i+1)+"--->"+title.innerText;
                    let flag_num = i + 1;
                    //title.innerText = new_title;
                    if (Number(fanwei_start) <= flag_num && flag_num <= Number(fanwei_end)) {
                        danxuankuang.querySelectorAll(`label`)[0].click();
                    }
                }
            } catch (error) {
                console.error("出现错误:", error);
            }
        }

        f1();
    }

    // 库存页面
    if (window.location.href.startsWith(shop6888_kucun_url)) {
        if (request.myshopify_guolv_dianji === "myshopify_guolv_dianji") {
            console.log("request.myshopify_guolv_dianji");
            async function f1() {
                try {

                    len = document.querySelectorAll(`table.el-table__body tr`).length;
                    /*
                    let key_paichu = [
                        "Sweatshirt",
                        "Top",
                        "V-Neck",
                        "Tee"
                    ]
                    */
                    key_paichu = request.key_paichu.toLowerCase();
                    key_paichu = key_paichu.split(',');
                    for (var i = 0; i < len; i++) {
                        var tr = document.querySelectorAll(`table.el-table__body tr`)[i];
                        var v3 = tr.querySelectorAll(`td`)[3]; // title
                        var v1 = tr.querySelectorAll(`td`)[1]; // id
                        var v0 = tr.querySelectorAll(`td`)[0];  // 单选框
                        let title = v3.innerText.toLowerCase();

                        click_flag = 1; // 默认所有点击
                        for (var j = 0; j < key_paichu.length; j++) {
                            let key = key_paichu[j];
                            let flag = title.includes(key);
                            if (flag == true) {  // 包含 主角
                                click_flag = 0;
                            }
                        }

                        if (click_flag == 1) {
                            v0.querySelectorAll(`label`)[0].click();
                        }
                    }

                } catch (error) {
                    console.error("出现错误:", error);
                }
            }

            f1();
        }

        if (request.myshopify_tianjia_pingbici === "myshopify_tianjia_pingbici") {
            console.log("request.myshopify_tianjia_pingbici");
            const xxxa_z = xxx => {
                let result = [];
                for (let i = 'a'.charCodeAt(0); i <= 'z'.charCodeAt(0); i++) {
                    result.push(`${xxx}${String.fromCharCode(i)}`);
                }
                return result;
            };
            const a_zxxx = xxx => {
                let result = [];
                for (let i = 'a'.charCodeAt(0); i <= 'z'.charCodeAt(0); i++) {
                    result.push(`${String.fromCharCode(i)}${xxx}`);
                }
                return result;
            };

            async function f1() {
                try {
                    paichu_str = request.key_paichu.toLowerCase();
                    console.log(`paichu_str:${paichu_str}`);
                    paichu_l = paichu_str.split(",");
                    console.log(`paichu_l:${paichu_l}`);
                    console.log('paichu_l:', paichu_l);


                    for (ele of paichu_l) {
                        for (xxxa_z_i of xxxa_z(ele)) {
                            // 添加按钮
                            $(`div.goods-management div.right-panel button:contains(添加)`).click()
                            await delay(ms = 200)
                            // input填充
                            var input_10 = $(`div.el-form-item label:contains(屏蔽关键词)`).next().find(`div[tabindex="-1"] input`)[0]
                            input_value(input2 = input_10, value = xxxa_z_i)
                            await delay(ms = 200)
                            // 加号
                            $(`div.el-form-item label:contains(屏蔽关键词)`).next().find(`div.el-input-group__append button`)[0].click()
                            await delay(ms = 200)
                        }

                        for (a_zxxx_i of a_zxxx(ele)) {
                            // 添加按钮
                            $(`div.goods-management div.right-panel button:contains(添加)`).click()
                            await delay(ms = 200)
                            // input填充
                            var input_10 = $(`div.el-form-item label:contains(屏蔽关键词)`).next().find(`div[tabindex="-1"] input`)[0]
                            input_value(input2 = input_10, value = a_zxxx_i)
                            await delay(ms = 200)
                            // 加号
                            $(`div.el-form-item label:contains(屏蔽关键词)`).next().find(`div.el-input-group__append button`)[0].click()
                            await delay(ms = 200)
                        }

                    }

                } catch (error) {
                    console.error("出现错误:", error);
                }
            }

            f1();
        }
    }
})




shang_ping_dao_ru = "https://b08-admin.shop6888.com/#/goods/shopGoodsDataImportTaskManagement"
jing_tai = "https://b08-admin.shop6888.com/#/goods/staticFileGenerateManagement"
// 商品导入管理 和 静态管理  两个页面着色
if (window.location.href.startsWith(shang_ping_dao_ru) || window.location.href.startsWith(jing_tai)) {
    chrome.runtime.onMessage.addListener(async function (request, sender, sendResponse) {
        if (request.myshopify_shangpingdaoru_jingtaiguanli_zhuose === "myshopify_shangpingdaoru_jingtaiguanli_zhuose") {
            chrome.storage.local.get(['column1', 'column2', 'column3', 'column4', 'column5', 'column6', 'column7', 'column8', 'column9', 'column10', 'column11'], async function (data) {
                // 检查是否成功检索到数据
                if (chrome.runtime.lastError) {
                    console.error(chrome.runtime.lastError);
                    return;
                }

                // async function start() {

                // }

                // start();
                // const yu_ming_curent = $('div[role="dialog"] div.el-dialog__title:contains("全局配置")').text().replace(' 全局配置','')
                // const yu_ming_curent = $('div[role="dialog"] div.el-dialog__title:contains("全局配置")').text().replace(' 全局配置','')
                // const yu_ming_zhi_web = 'https://'+yu_ming_curent
                yu_ming_s = '';
                for (var i = 0; i < data.column1.length - 2; i++) {
                    const wangzhan_bianhao_zhi = data.column1[i];
                    const yu_ming_zhi = data.column2[i];
                    const youxiang_zhi = data.column3[i];
                    const lianxi_dianhua_zhi = data.column4[i];
                    const gaoshiyu_zhi = data.column5[i];
                    const biaoti_zhi = data.column6[i];
                    const guanjianci_zhi = data.column7[i];
                    const miaoshu_zhi = data.column8[i];
                    const huan_deng_pian1_zhi = data.column9[i];
                    const huan_deng_pian2_zhi = data.column10[i];
                    const muban_zhi_xuhao = data.column11[i];


                    const obj = $(`td:contains(${yu_ming_zhi}):eq(0)`);
                    // obj= Array.from(document.querySelectorAll("td")).filter(v => v.textContent.includes(yu_ming_zhi))[0];
                    if (obj.length > 0) {
                        console.log('yu_ming_zhi', yu_ming_zhi);
                        obj.css("background-color", "rgb(211,227,253)");
                        let originalText = obj.text();
                        let newText = `<span style="color: red;font-size:40px;">${wangzhan_bianhao_zhi}</span> ${originalText}`;
                        obj.html(newText);
                        yu_ming_s = yu_ming_s + yu_ming_zhi + '\n';
                    }
                }

                if (yu_ming_s === '') {
                    alert('没有指定的域名!!!');
                }


                if (window.location.href.startsWith(shang_ping_dao_ru)) {
                    copyTextToClipboard('============= 商品导入域名 =============\n' + yu_ming_s);
                }

                if (window.location.href.startsWith(jing_tai)) {
                    copyTextToClipboard('============= 静态生成任务域名 =============\n' + yu_ming_s);
                }


            });
        }

    });
}

// 单个网站库存  shop6888_kucun_url_wangzhan
// https://b08-admin.shop6888.com/#/goods/shopGoodsManagement
if (window.location.href.startsWith(shop6888_kucun_url_wangzhan) || window.location.href.startsWith(shop6888_kucun_url)) {
    chrome.runtime.onMessage.addListener(async function (request, sender, sendResponse) {


        // shift 连选产品
        if (request.myshopify_lian_xuan_chan_ping === "myshopify_lian_xuan_chan_ping") {
            console.log("request.myshopify_lian_xuan_chan_ping");
            async function f1() {
                try {
                    function enableShiftCheck(checkboxs) {
                        let startChecked;

                        function handleCheck(e) {
                            let thisIndex = checkboxs.index(this);
                            console.log(thisIndex);
                            if (e.shiftKey) {
                                console.log("检测到shift!");
                                let thisIndex = checkboxs.index(this);
                                let startIndex = checkboxs.index(startChecked);
                                let startNum = thisIndex < startIndex ? thisIndex : startIndex;
                                let endNum = thisIndex > startIndex ? thisIndex : startIndex;
                                console.log("startNum,endNum:", startNum, endNum);
                                for (let i = startNum + 1; i <= endNum; i++) {
                                    /*  
                                    // 下面这个逻辑 只能连选 没有选择过得
                                    if(this.checked) {
                                        // checkboxs.eq(i).prop("checked", true);
                                        checkboxs.eq(i)[0].click();
                                    } else {
                                        //checkboxs.eq(i).prop("checked", false);
                                    }
                                   */
                                    // 连选 就会真的连选 管你选择过几次
                                    checkboxs.eq(i)[0].click();
                                }
                            }
                            startChecked = this;
                        }
                        checkboxs.click(handleCheck);
                    }

                    $(function () {
                        //  连选产品集合
                        input_set = $('table tr td input.el-checkbox__original')
                        enableShiftCheck(input_set);
                    });

                } catch (error) {
                    console.error("出现错误:", error);
                }
            }

            f1();
        }

        // console.log("content\self_you_mi_ke_ji\\usfakename.js");
        // 一键把商品 放置到杂类里面
        if (request.myshopify_qiehuan_zalei_leimu === "myshopify_qiehuan_zalei_leimu") {
            console.log("request.myshopify_qiehuan_zalei_leimu");
            async function f1() {
                try {
                    $(`table.el-table__header thead th input`)[0].click();  // 全选
                    await delay(300);
                    $(`button:contains(选择变更)`)[0].click();
                    await delay(300);
                    $(`div.el-dialog__title`).parent().next().find(`tr:contains(分类)`).find(`td input`)[0].click();
                    await delay(300);
                    $(`div.el-dialog__title`).parent().next().find(`tr:contains(分类)`).find(`td:contains(请选择) span`)[0].click();
                    await delay(300);
                    $(`div[aria-hidden="false"] div.el-scrollbar ul[role="listbox"] div li:contains(Wait 待定)`)[0].click();
                    await delay(300);
                    $(`footer.el-dialog__footer button:contains(修改)`)[0].click();
                    await delay(300);
                    $(`div.el-message-box.is-draggable[tabindex="-1"]`).find(`button:contains(确定)`)[0].click()

                    // $("input[value='  Generate  ']").click();
                    // await delay(300);
                    // $x_span_city = $("p:contains('City, State, Zip: ')").find('span').text();
                    // console.log("$x_span_city:", $x_span_city);

                    // $x_span_street = $("p:contains('Street: ')").find('span').text();
                    // console.log("$x_span_street:", $x_span_street);

                    // $x_span_country = $("p:contains('Country: ')").find('span').text();
                    // console.log("$x_span_country:", $x_span_country);

                    // $x_span_telephone = $("p:contains('Telephone: ')").find('span').text();
                    // console.log("$x_span_telephone:", "+1 "+$x_span_telephone);

                    // const txt1 = $x_span_city.trim()+','+$x_span_street.trim()+','+$x_span_country.trim()+';'+'+1 '+$x_span_telephone;
                    // copyTextToClipboard(txt1);

                } catch (error) {
                    console.error("出现错误:", error);
                }
            }

            f1();
        }
        // 单个网站库存  库存筛选
        if (request.myshopify_dange_wangzhan_kucun_kucun_shaixuan === "myshopify_dange_wangzhan_kucun_kucun_shaixuan") {
            async function f1() {
                try {
                    // 左删掉
                    //$(`div.el-scrollbar.vab-column-bar.vab-column-bar-card`)[0].remove()
                    // 头删掉
                    //$(`div.vab-layout-header.fixed-header`)[0].remove()
                    // 删除按钮下移
                    //btn_del = $(`div.left-panel button.el-button.el-button--danger`)[0];
                    //footer = $(`div.el-pagination.is-background`)[0]
                    //$(footer).append(btn_del);

                    // 上面第二部分删掉
                    //$(`div.el-row.vab-query-form`)[0].remove()
                    // footer部分删掉
                    //$(`footer.vab-footer`)[0].remove()

                    // elementToMove = $(`div.vab-app-main section div.shop-goods`)[0];
                    // $(elementToMove).css({
                    //     position: 'fixed',
                    //     top: '0',
                    //     left: '0',
                    //     // height: '100vh', // 设置高度为视口高度的100%
                    //     // height: '100%', // 设置高度为视口高度的100%
                    //     height:'900px',
                    //     // width: '100%',
                    //     zIndex: '9999' // 设置一个较高的 z-index 以确保元素在其他元素之上
                    // });
                    console.log('库存精简!!  myshopify_dange_wangzhan_kucun_kucun_shaixuan');


                    // 去掉多余的信息展示
                    $('tr').each(function () {
                        $('table').css({
                            'display': 'flex', // 使用flex布局
                            'flex-direction': 'row', // flex项应该沿着水平的主轴排列
                            'flex-wrap': 'wrap', // 允许flex项在需要时换行
                            'width': '100%' // 表格宽度为100%
                        });

                        $('tbody').css({
                            'display': 'flex', // 使用flex布局
                            'flex-direction': 'row', // flex项应该沿着水平的主轴排列
                            'flex-wrap': 'wrap', // 允许flex项在需要时换行
                            'width': '100%' // 表格宽度为100%
                        });



                        // 获取当前行的所有td元素
                        var tds = $(this).find('td');
                        // 遍历td元素，并保留第1、4、5个td，其他的移除
                        tds.each(function (index) {
                            if (index !== 0 && index !== 3) { // 注意索引是从0开始的
                                $(this).remove();
                            }

                            // 设置td样式
                            if (index == 3) { // 注意索引是从0开始的
                                $(this).css({
                                    'width': '120px',
                                    'margin': '0', // 去除边距
                                    'padding': '5px' // 设置内边距
                                });
                            }
                        });

                        // 设置tr为flex项，并调整样式
                        $('tr').css({
                            'display': 'flex', // 将tr设置为flex项
                            'flex': '0 0 auto', // flex项不放大也不缩小，宽度为其内容的宽度
                            'width': 'auto', // 宽度自动
                            'margin-right': '10px' // tr之间的间隔
                        });

                        /*
                        $('td').css({
                            'width': 'auto'
                        'margin': '0', // 去除边距
                        'padding': '5px' // 设置内边距
                        });
                        */
                    });
                } catch (error) {
                    console.error("出现错误:", error);
                }
            }

            await f1();
        }

        // 单个网站库存  库存筛选 2
        if (request.myshopify_dange_wangzhan_kucun_kucun_shaixuan2 === "myshopify_dange_wangzhan_kucun_kucun_shaixuan2") {
            async function f1() {
                try {
                    // 左删掉
                    // $(`div.el-scrollbar.vab-column-bar.vab-column-bar-card`)[0].remove()
                    // 头删掉
                    // $(`div.vab-layout-header.fixed-header`)[0].remove()
                    // 删除按钮下移
                    //btn_del = $(`div.left-panel button.el-button.el-button--danger`)[0];
                    //footer = $(`div.el-pagination.is-background`)[0]
                    //$(footer).append(btn_del);

                    // 上面第二部分删掉
                    //$(`div.el-row.vab-query-form`)[0].remove()
                    // footer部分删掉
                    // $(`footer.vab-footer`)[0].remove()

                    // elementToMove = $(`div.vab-app-main section div.shop-goods`)[0];
                    // $(elementToMove).css({
                    //     position: 'fixed',
                    //     top: '0',
                    //     left: '0',
                    //     // height: '100vh', // 设置高度为视口高度的100%
                    //     // height: '100%', // 设置高度为视口高度的100%
                    //     height:'900px',
                    //     // width: '100%',
                    //     zIndex: '9999' // 设置一个较高的 z-index 以确保元素在其他元素之上
                    // });
                    console.log('库存精简!!  myshopify_dange_wangzhan_kucun_kucun_shaixuan');


                    // 去掉多余的信息展示
                    $('tr').each(function () {
                        $('table').css({
                            'display': 'flex', // 使用flex布局
                            'flex-direction': 'row', // flex项应该沿着水平的主轴排列
                            'flex-wrap': 'wrap', // 允许flex项在需要时换行
                            'width': '100%' // 表格宽度为100%
                        });

                        $('tbody').css({
                            'display': 'flex', // 使用flex布局
                            'flex-direction': 'row', // flex项应该沿着水平的主轴排列
                            'flex-wrap': 'wrap', // 允许flex项在需要时换行
                            'width': '100%' // 表格宽度为100%
                        });



                        // 获取当前行的所有td元素
                        var tds = $(this).find('td');
                        // 遍历td元素，并保留第1、4、5个td，其他的移除
                        tds.each(function (index) {
                            if (index !== 0 && index !== 2) { // 注意索引是从0开始的
                                $(this).remove();
                            }

                            // 设置td样式
                            if (index == 2) { // 注意索引是从0开始的
                                $(this).css({
                                    'width': '120px',
                                    'margin': '0', // 去除边距
                                    'padding': '5px' // 设置内边距
                                });
                            }
                        });

                        // 设置tr为flex项，并调整样式
                        $('tr').css({
                            'display': 'flex', // 将tr设置为flex项
                            'flex': '0 0 auto', // flex项不放大也不缩小，宽度为其内容的宽度
                            'width': 'auto', // 宽度自动
                            'margin-right': '10px' // tr之间的间隔
                        });

                        /*
                        $('td').css({
                            'width': 'auto'
                        'margin': '0', // 去除边距
                        'padding': '5px' // 设置内边距
                        });
                        */
                    });
                } catch (error) {
                    console.error("出现错误:", error);
                }
            }

            await f1();
        }
    });
}

// if (window.location.href.startsWith(usfakename_url||shop6888_url)) {
if (window.location.href.startsWith(usfakename_url) || window.location.href.startsWith(shop6888_url)) {
    chrome.runtime.onMessage.addListener(async function (request, sender, sendResponse) {
        console.log("content\self_you_mi_ke_ji\\usfakename.js");

        // 售价+市场价  https://b08-admin.shop6888.com/#/goods/shopGoodsManagement
        if (window.location.href.startsWith("https://b08-admin.shop6888.com/#/goods/shopGoodsManagement/")) {


            // 随机售价 70-120
            if (request.myshopify_shoujia_xiugai_70_120 === "myshopify_shoujia_xiugai_70_120") {
                console.log("request.myshopify_shoujia_xiugai_70_120");
                async function f1() {
                    try {
                        await delay(300);
                        $(`button span:contains( 随机修改销售价 )`).click();
                        await delay(300);
                        let inp1 = $(`div[role="dialog"]:contains(批量随机修改销售价)`).find(`input[placeholder="变更后的最高价格"]`)[0];
                        input_value(input2 = inp1, value = '120');
                        await delay(300);
                        let inp2 = $(`div[role="dialog"]:contains(批量随机修改销售价)`).find(`input[placeholder="变更后的最低价格"]`)[0];
                        input_value(input2 = inp2, value = '70');
                        await delay(300);
                        $(`div[role="dialog"]:contains(批量随机修改销售价)`).find(`button:contains(修改售价)`).click();
                        await delay(900);
                        $(`div.el-message-box.is-draggable[tabindex="-1"]`).find(`button:contains(确定)`).click()

                    } catch (error) {
                        console.error("出现错误:", error);
                    }
                }

                f1();
            }

            // 随机售价 55-77
            if (request.myshopify_shoujia_xiugai_55_77 === "myshopify_shoujia_xiugai_55_77") {
                console.log("request.myshopify_shoujia_xiugai_55_77");
                async function f1() {
                    try {
                        await delay(300);
                        $(`button span:contains( 随机修改销售价 )`).click();
                        await delay(300);
                        let inp1 = $(`div[role="dialog"]:contains(批量随机修改销售价)`).find(`input[placeholder="变更后的最高价格"]`)[0];
                        input_value(input2 = inp1, value = '77');
                        await delay(300);
                        let inp2 = $(`div[role="dialog"]:contains(批量随机修改销售价)`).find(`input[placeholder="变更后的最低价格"]`)[0];
                        input_value(input2 = inp2, value = '55');
                        await delay(300);
                        $(`div[role="dialog"]:contains(批量随机修改销售价)`).find(`button:contains(修改售价)`).click();
                        await delay(900);
                        $(`div.el-message-box.is-draggable[tabindex="-1"]`).find(`button:contains(确定)`).click()

                    } catch (error) {
                        console.error("出现错误:", error);
                    }
                }

                f1();
            }

            // 随机售价 45-77
            if (request.myshopify_shoujia_xiugai_45_77 === "myshopify_shoujia_xiugai_45_77") {
                console.log("request.myshopify_shoujia_xiugai_45_77");
                async function f1() {
                    try {
                        await delay(300);
                        $(`button span:contains( 随机修改销售价 )`).click();
                        await delay(300);
                        let inp1 = $(`div[role="dialog"]:contains(批量随机修改销售价)`).find(`input[placeholder="变更后的最高价格"]`)[0];
                        input_value(input2 = inp1, value = '77');
                        await delay(300);
                        let inp2 = $(`div[role="dialog"]:contains(批量随机修改销售价)`).find(`input[placeholder="变更后的最低价格"]`)[0];
                        input_value(input2 = inp2, value = '45');
                        await delay(300);
                        $(`div[role="dialog"]:contains(批量随机修改销售价)`).find(`button:contains(修改售价)`).click();
                        await delay(900);
                        $(`div.el-message-box.is-draggable[tabindex="-1"]`).find(`button:contains(确定)`).click()

                    } catch (error) {
                        console.error("出现错误:", error);
                    }
                }

                f1();
            }

            // 随机售价 45-77
            if (request.myshopify_shoujia_xiugai_55_99 === "myshopify_shoujia_xiugai_55_99") {
                console.log("request.myshopify_shoujia_xiugai_55_99");
                async function f1() {
                    try {
                        await delay(300);
                        $(`button span:contains( 随机修改销售价 )`).click();
                        await delay(300);
                        let inp1 = $(`div[role="dialog"]:contains(批量随机修改销售价)`).find(`input[placeholder="变更后的最高价格"]`)[0];
                        input_value(input2 = inp1, value = '99');
                        await delay(300);
                        let inp2 = $(`div[role="dialog"]:contains(批量随机修改销售价)`).find(`input[placeholder="变更后的最低价格"]`)[0];
                        input_value(input2 = inp2, value = '55');
                        await delay(300);
                        $(`div[role="dialog"]:contains(批量随机修改销售价)`).find(`button:contains(修改售价)`).click();
                        await delay(900);
                        $(`div.el-message-box.is-draggable[tabindex="-1"]`).find(`button:contains(确定)`).click()

                    } catch (error) {
                        console.error("出现错误:", error);
                    }
                }

                f1();
            }

            // 随机售价 30_38
            if (request.myshopify_shoujia_xiugai_30_38 === "myshopify_shoujia_xiugai_30_38") {
                console.log("request.myshopify_shoujia_xiugai_30_38");
                async function f1() {
                    try {
                        await delay(300);
                        $(`button span:contains( 随机修改销售价 )`).click();
                        await delay(300);
                        let inp1 = $(`div[role="dialog"]:contains(批量随机修改销售价)`).find(`input[placeholder="变更后的最高价格"]`)[0];
                        input_value(input2 = inp1, value = '38');
                        await delay(300);
                        let inp2 = $(`div[role="dialog"]:contains(批量随机修改销售价)`).find(`input[placeholder="变更后的最低价格"]`)[0];
                        input_value(input2 = inp2, value = '30');
                        await delay(300);
                        $(`div[role="dialog"]:contains(批量随机修改销售价)`).find(`button:contains(修改售价)`).click();
                        await delay(900);
                        $(`div.el-message-box.is-draggable[tabindex="-1"]`).find(`button:contains(确定)`).click()

                    } catch (error) {
                        console.error("出现错误:", error);
                    }
                }

                f1();
            }
            // 随机售价 38_50
            if (request.myshopify_shoujia_xiugai_38_50 === "myshopify_shoujia_xiugai_38_50") {
                console.log("request.myshopify_shoujia_xiugai_38_50");
                async function f1() {
                    try {
                        await delay(300);
                        $(`button span:contains( 随机修改销售价 )`).click();
                        await delay(300);
                        let inp1 = $(`div[role="dialog"]:contains(批量随机修改销售价)`).find(`input[placeholder="变更后的最高价格"]`)[0];
                        input_value(input2 = inp1, value = '50');
                        await delay(300);
                        let inp2 = $(`div[role="dialog"]:contains(批量随机修改销售价)`).find(`input[placeholder="变更后的最低价格"]`)[0];
                        input_value(input2 = inp2, value = '38');
                        await delay(300);
                        $(`div[role="dialog"]:contains(批量随机修改销售价)`).find(`button:contains(修改售价)`).click();
                        await delay(900);
                        $(`div.el-message-box.is-draggable[tabindex="-1"]`).find(`button:contains(确定)`).click()

                    } catch (error) {
                        console.error("出现错误:", error);
                    }
                }

                f1();
            }

            // 随机售价 35_39
            if (request.myshopify_shoujia_xiugai_35_39 === "myshopify_shoujia_xiugai_35_39") {
                console.log("request.myshopify_shoujia_xiugai_35_39");
                async function f1() {
                    try {
                        await delay(300);
                        $(`button span:contains( 随机修改销售价 )`).click();
                        await delay(300);
                        let inp1 = $(`div[role="dialog"]:contains(批量随机修改销售价)`).find(`input[placeholder="变更后的最高价格"]`)[0];
                        input_value(input2 = inp1, value = '39');
                        await delay(300);
                        let inp2 = $(`div[role="dialog"]:contains(批量随机修改销售价)`).find(`input[placeholder="变更后的最低价格"]`)[0];
                        input_value(input2 = inp2, value = '35');
                        await delay(300);
                        $(`div[role="dialog"]:contains(批量随机修改销售价)`).find(`button:contains(修改售价)`).click();
                        await delay(900);
                        $(`div.el-message-box.is-draggable[tabindex="-1"]`).find(`button:contains(确定)`).click()

                    } catch (error) {
                        console.error("出现错误:", error);
                    }
                }

                f1();
            }
            // 随机售价 27_33
            if (request.myshopify_shoujia_xiugai_27_33 === "myshopify_shoujia_xiugai_27_33") {
                console.log("request.myshopify_shoujia_xiugai_35_39");
                async function f1() {
                    try {
                        await delay(300);
                        $(`button span:contains( 随机修改销售价 )`).click();
                        await delay(300);
                        let inp1 = $(`div[role="dialog"]:contains(批量随机修改销售价)`).find(`input[placeholder="变更后的最高价格"]`)[0];
                        input_value(input2 = inp1, value = '33');
                        await delay(300);
                        let inp2 = $(`div[role="dialog"]:contains(批量随机修改销售价)`).find(`input[placeholder="变更后的最低价格"]`)[0];
                        input_value(input2 = inp2, value = '27');
                        await delay(300);
                        $(`div[role="dialog"]:contains(批量随机修改销售价)`).find(`button:contains(修改售价)`).click();
                        await delay(900);
                        $(`div.el-message-box.is-draggable[tabindex="-1"]`).find(`button:contains(确定)`).click()

                    } catch (error) {
                        console.error("出现错误:", error);
                    }
                }

                f1();
            }

            // 随机 比例 市场价 105-120
            if (request.myshopify_shichangjia_xiugai === "myshopify_shichangjia_xiugai") {
                console.log("request.myshopify_shichangjia_xiugai");
                async function f1() {
                    try {
                        await delay(300);
                        $(`button span:contains( 批量比例修改市场价 )`).click();
                        // $(`div.shop-website button:contains( 批量比例修改市场价 )`).click();
                        await delay(300);
                        let inp3 = $(`div[role="dialog"]:contains(批量比例修改市场价)`).find(`input[placeholder="请输入最高比例"]`)[0];
                        input_value(input2 = inp3, value = '120');
                        await delay(300);
                        let inp4 = $(`div[role="dialog"]:contains(批量比例修改市场价)`).find(`input[placeholder="请输入最低比例"]`)[0];
                        input_value(input2 = inp4, value = '110');
                        await delay(300);
                        $(`div[role="dialog"]:contains(批量比例修改市场价)`).find(`button:contains(修改市场价)`).click();
                        await delay(900);
                        $(`div.el-message-box.is-draggable[tabindex="-1"]`).find(`button:contains(确定)`).click()
                    } catch (error) {
                        console.error("出现错误:", error);
                    }
                }

                f1();
            }

        }

        // 市场价


        // myshopify_huoqu_shenfen  获取身份
        if (window.location.href.startsWith(usfakename_url)) {
            if (request.myshopify_huoqu_shenfen === "myshopify_huoqu_shenfen") {
                console.log("request.myshopify_huoqu_shenfen");
                async function f1() {
                    try {
                        let txt_total = '';
                        let phone_num_total = '';
                        for (var i = 0; i < 10; i++) {
                            $("input[value='  Generate  ']").click();
                            await delay(1000);
                            $x_span_city = $("p:contains('City, State, Zip: ')").find('span').text();
                            console.log("$x_span_city:", $x_span_city);

                            $x_span_street = $("p:contains('Street: ')").find('span').text();
                            console.log("$x_span_street:", $x_span_street);

                            $x_span_country = $("p:contains('Country: ')").find('span').text();
                            console.log("$x_span_country:", $x_span_country);

                            $x_span_telephone = $("p:contains('Telephone: ')").find('span').text();
                            console.log("$x_span_telephone:", "+1 " + $x_span_telephone);

                            let txt1 = $x_span_city.trim() + ',' + $x_span_street.trim() + ',' + $x_span_country.trim() + ';' + '+1 ' + $x_span_telephone.replace('Telephone', '');
                            phone_num_total = '+1 ' + $x_span_telephone.replace('Telephone', '') + '\n' + phone_num_total;
                            txt_total = txt1 + '\n' + txt_total;
                        }
                        let sss = txt_total + '\n' + phone_num_total;
                        copyTextToClipboard(sss);
                        console.log('你复制了十个 城市 街道 国家 电话号码!!!!');


                    } catch (error) {
                        console.error("出现错误:", error);
                    }
                }
                await f1();
            }
        }

        // 小库存  伪装术
        if (window.location.href.startsWith(shop6888_kucun_url)) {
            if (request.myshopify_2024_8_29_kucun_xiao === "myshopify_2024_8_29_kucun_xiao") {
                console.log("request.myshopify_2024_8_29_kucun_xiao");
                // 适合缩小一次 因为 这个详情数量 并没有继续处理
                $(`div.shop-website div.el-scrollbar__view table tbody tr`).each(function () {
                    console.log($(this).find('td').eq(1).text());
                    // 上方商品数量详情
                    var new_bian = $(this).find('td').eq(1).text().trim().slice(2);
                    $(this).find('td').eq(1).text(new_bian);
                });

                // 设置总条数
                var old_s = $(`div.shop-website div.el-pagination.is-background span.el-pagination__total`).text();
                var num_s = old_s.replace(/[^0-9]/ig, "");
                var new_s = parseInt(Number(num_s) / 99).toString();
                var ss = old_s.replace(num_s, new_s)
                $(`div.shop-website div.el-pagination.is-background span.el-pagination__total`).text(ss);

                // 总页数
                var v2 = String(parseInt(Number(new_s) / 20));
                $(`div.shop-website div.el-pagination.is-background ul.el-pager li:eq(-1)`).text(v2);
            }
        }

        // 大库存  伪装术
        if (request.myshopify_2024_8_29_kucun_da === "myshopify_2024_8_29_kucun_da") {
            console.log("request.myshopify_2024_8_29_kucun_da");
            $(`div.shop-website div.el-scrollbar__view table tbody tr`).each(function () {
                console.log($(this).find('td').eq(1).text());
                // 上方商品数量详情
                var new_bian = '99' + $(this).find('td').eq(1).text().trim();
                $(this).find('td').eq(1).text(new_bian);
            });

            // 设置总条数
            var old_s = $(`div.shop-website div.el-pagination.is-background span.el-pagination__total`).text();
            var num_s = old_s.replace(/[^0-9]/ig, "");
            var new_s = parseInt(Number(num_s) * 99).toString();
            var ss = old_s.replace(num_s, new_s)
            $(`div.shop-website div.el-pagination.is-background span.el-pagination__total`).text(ss);

            // 总页数
            var v2 = String(parseInt(Number(new_s) / 20));
            $(`div.shop-website div.el-pagination.is-background ul.el-pager li:eq(-1)`).text(v2);
        }


        // myshopify_piliang_tian_jia_yu_ming  批量添加域名
        wang_zhan_guan_li = "https://b08-admin.shop6888.com/#/goods/shopWebsiteManagement"
        if (window.location.href.startsWith(wang_zhan_guan_li)) {

            // 批量增加打开按钮
            if (request.myshopify_zengjia_dakai_anniu === "myshopify_zengjia_dakai_anniu") {
                console.log("request.myshopify_zengjia_dakai_anniu");
                async function f1() {
                    try {
                        $('table tbody[tabindex="-1"] tr.el-table__row td span:contains(http)').each(function () {
                            // 获取当前 label 的父级的父级元素，通常是 tr
                            // var row = $(this).closest('tr');
                            // 获取 tr 的第一个单元格的文本，这里假设 id 在第一个单元格中
                            // var idText = row.find('td:eq(1)').text();
                            // 将获取到的文本添加到 ids 数组中
                            // ids.push(idText);
                            // console.log($(this));
                            var span = $(this);
                            var text = span.text();  // 这个就是链接
                            var url = span.text();  // 这个就是链接


                            // 创建一个新的a标签
                            var a1 = document.createElement('a');
                            // 设置a标签的href属性为span中的文本
                            a1.href = text;
                            // 设置a标签的目标属性为_blank，以便在新窗口中打开链接
                            a1.target = '_blank';
                            // 设置a标签的文本内容为span中的文本
                            a1.textContent = '|外';
                            a1.style.color = 'green'; // 设置文本颜色为绿色
                            a1.style.textShadow = '1px 1px 2px rgba(0, 0, 0, 0.5)'; // 设置文本阴影

                            // 创建一个新的a标签
                            var a2 = document.createElement('a');
                            // 设置a标签的href属性为span中的文本
                            var text2 = $(this).closest('tr').find('.el-table_1_column_3 div').text();  // 这个是获取id
                            console.log("text2", text2);
                            a2.href = `https://b08.shop6888.com/redirect?websiteid=${text2}`;  // https://b08.shop6888.com/redirect?websiteid=442
                            // 设置a标签的目标属性为_blank，以便在新窗口中打开链接
                            a2.target = '_blank';
                            // 设置a标签的文本内容为span中的文本
                            a2.textContent = '/内';
                            a2.style.color = 'red'; // 设置文本颜色为红色
                            a2.style.textShadow = '1px 1px 2px rgba(0, 0, 0, 0.5)'; // 设置文本阴影

                            // 创建一个新的a标签
                            var a3 = document.createElement('a');
                            // 设置a标签的href属性为span中的文本
                            console.log("当前url", text);  // 展示链接
                            a3.href = '#'
                            // 设置a标签的目标属性为_blank，以便在新窗口中打开链接
                            a3.target = '_blank';
                            // 设置a标签的文本内容为span中的文本
                            a3.textContent = '/Copy';
                            a3.style.color = 'blue'; // 设置文本颜色为红色
                            a3.style.textShadow = '1px 1px 2px rgba(0, 0, 0, 0.5)'; // 设置文本阴影

                            // 将a标签追加到span标签的末尾
                            span[0].appendChild(a1);
                            span[0].appendChild(a2);
                            span[0].appendChild(a3);

                            a3.onclick = async function (event) {
                                event.preventDefault(); // 阻止链接的默认行为
                                copyTextToClipboard(text = url)
                            }

                            $(a1).hover(
                                function () {
                                    $(this).css('color', 'yellow');
                                },
                                function () {
                                    $(this).css('color', 'green');
                                }
                            )

                            $(a2).hover(
                                function () {
                                    $(this).css('color', 'yellow');
                                },
                                function () {
                                    $(this).css('color', 'red');
                                }
                            )

                            $(a3).hover(
                                function () {
                                    $(this).css('color', 'yellow');
                                },
                                function () {
                                    $(this).css('color', 'blue');
                                }
                            )
                            // span[0].appendChild(a2);

                        });

                    } catch (error) {
                        console.error("出现错误:", error);
                    }
                }

                f1();
            }


            // 批量添加域名
            if (request.myshopify_piliang_tian_jia_yu_ming === "myshopify_piliang_tian_jia_yu_ming") {
                console.log("request.myshopify_piliang_tian_jia_yu_ming");
                async function f1() {
                    try {
                        // $("div.is-left span:contains('店铺')").click(); // 店铺
                        // await delay(200);
                        // $("ul[role='menubar'] span:contains('网站管理')").click();  // 网站管理
                        // await delay(300);
                        console.log("============== 自动添加域名 ==============");
                        $("button span:contains('批量添加')").click(); // 批量添加
                        await delay(300);
                        labels = $("header:contains('批量添加域名')").closest('div').find('form').find('label');
                        fuwuqi = labels[1];
                        wangzhi = labels[2];
                        yuyan = labels[3];

                        console.log("============== 1 服务器选择 ==============");
                        // 域名选择
                        fuwuqi.click();
                        await delay(300);
                        $("ul li span:contains('1 - 美国洛杉矶')").click();

                        console.log("============== 2 填写网址 textarea ==============");
                        // 填写网址
                        await delay(600);
                        function textarea_value2(textarea2, value) {
                            textarea2.value = value;
                            var event2 = new Event('input', { bubbles: true, cancelable: true });
                            textarea2.dispatchEvent(event2);
                        }

                        // textarea 赋值函数
                        function textarea_value(textarea2, value) {
                            textarea2.value = value;
                            var event2 = document.createEvent('Event');
                            event2.initEvent('input', true, true);
                            textarea2.dispatchEvent(event2);
                        }

                        url_set = 'https://1213212313.org\nhttps://1213212313.com\nhttps://1213212313.net\nhttps://1213212313.top'
                        textarea_t = $('textarea[placeholder="请输入域名(如：http://www.store.com)，每行一个"]');
                        console.log(textarea_t)
                        // textarea_t.text('https://1213212313.org\nhttps://1213212313.com\nhttps://1213212313.net\nhttps://1213212313.top');
                        textarea_value(textarea2 = textarea_t, value = url_set)

                        console.log("============== 3 语言选择 ==============");
                        // 语言选择
                        await delay(600);
                        $("div.el-form-item.asterisk-left:contains('语言') div.el-select").click();
                        await delay(300);
                        // $("div.el-form-item.asterisk-left:contains('语言') ul li:contains('英文')" );
                        $('div[id^="el-popper-container"] div.el-select-dropdown div.el-scrollbar ul[role="listbox"] li span:contains("英文")').click();

                        console.log("============== 4 执行添加按钮 ==============");
                        // 添加按钮
                        await delay(300);
                        $('div[role="dialog"] footer.el-dialog__footer button span:contains("添加")').click();

                    } catch (error) {
                        console.error("↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ 本帅逼发现的逆天错误,卧了个槽! ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓:", error);
                    }
                }

                await f1();
            }
        }

        // myshopify_xuanze_fenlei  选择分类  分步骤
        if (window.location.href.startsWith(wang_zhan_guan_li)) {
            if (request.myshopify_xuanze_fenlei === "myshopify_xuanze_fenlei") {
                console.log("request.myshopify_xuanze_fenlei");
                async function f1() {
                    try {

                        div_dao = $(`div[role="dialog"] header:contains("按分类导入商品")`).next();

                        // 导入最小值
                        await delay(300);
                        min_num_input = div_dao.find('label:contains(导入分类下商品最小数量（都填0表示全部导入）):eq(0)').next().find('input')[0];
                        input_value(input2 = min_num_input, value = '300');

                        // 导入最大值
                        await delay(300);
                        max_num_input = div_dao.find('label:contains(导入分类下商品最大数量（都填0表示全部导入）):eq(0)').next().find('input')[0];
                        input_value(input2 = max_num_input, value = '300');

                        // 已使用次数
                        await delay(300);
                        div_dao.find('label:contains(已使用次数):eq(0)').next().find('span:contains(请选择)').click();

                        // 分类  打开
                        await delay(300);
                        $(`div[role="dialog"] header:contains("按分类导入商品")`).next().find(`div.el-select__selected-item span:contains(请选择):eq(0)`).click();

                        // ============= 预打开 =============
                        await delay(300);
                        $(`li:contains(Women's Clothing 女装   _(直属商品数：0)`).prev().prev()?.click();
                        await delay(300);
                        $(`li:contains(Outerwear 外套   _(直属商品数：0)`).prev().prev()?.click();
                        await delay(300);
                        $(`li:contains(Sweaters 毛衣   _(直属商品数：0))`).prev().prev()?.click();
                        await delay(300);
                        $(`li:contains(Tops 上装   _(直属商品数：0))`).prev().prev()?.click();
                        await delay(300);
                        $(`li:contains(Bottoms 下装   _(直属商品数：0))`).prev().prev()?.click();
                        await delay(300);
                        $(`li:contains(Dresses 连衣裙   _(直属商品数：0))`).prev().prev()?.click();
                        await delay(300);
                        $(`li:contains(Swimwear 泳装   _(直属商品数：0))`).prev().prev()?.click()
                        await delay(300);
                        $(`li:contains(Denim 牛仔   _(直属商品数：0))`).prev().prev()?.click();
                        await delay(300);
                        $(`li:contains(Activewear 运动服饰   _(直属商品数：0))`).prev().prev()?.click();
                        await delay(300);
                        $(`li:contains(Underwear & Sleepwears 内衣&家居服   _(直属商品数：0))`).prev().prev()?.click();

                        // ============= 选择目标 =============
                        await delay(300);
                        $(`li span:contains(Hoodies & Sweatshirts 连帽衫和运动衫)`).parent().prev().click();
                        await delay(300);
                        $(`li span:contains(Women's Jackets 夹克)`).parent().prev().click();
                        await delay(300);
                        $(`li span:contains(Outerwears 外套)`).parent().prev().click();
                        await delay(300);
                        $(`li span:contains(Sweater 毛衣)`).parent().prev().click();
                        // $(`li span:contains(Blazers 西装外套)`).parent().prev().click();
                        // $(`li span:contains(Vest Coats 背心外套)`).parent().prev().click();
                        // $(`li span:contains(Woolen Sweater 羊毛衫)`).parent().prev().click();
                        await delay(300);
                        $(`li span:contains(T-Shirts T恤衫)`).parent().prev().click();
                        await delay(300);
                        $(`li span:contains(Top 上)`).parent().prev().click();
                        await delay(300);
                        $(`li span:contains(Shorts 短裤)`).parent().prev().click();
                        await delay(300);
                        $(`li span:contains(Bottom 下装   _)`).parent().prev().click();
                        await delay(300);
                        $(`li span:contains(Dress 连衣裙)`).parent().prev().click();
                        await delay(300);
                        $(`li span:contains(Swimsuit 泳装   _)`).parent().prev().click();
                        await delay(300);

                        // $(`li span:contains(Midi Dresses 中长连衣裙)`).parent().prev().click();

                        // Party Dress 派对礼服(直属商品数：15120)(全部商品数：15120)(个人商品数：15120)(可用商品数：15120)
                        // Skirt 裙子(直属商品数：12064)(全部商品数：12064)(个人商品数：12064)(可用商品数：12064)
                        // Swimsuit 泳装(直属商品数：10561)(全部商品数：10561)(个人商品数：10561)(可用商品数：10561)
                        // Denim Jeans 牛仔长裤(直属商品数：11139)(全部商品数：11139)(个人商品数：11139)(可用商品数：11139)



                    } catch (error) {
                        console.error("出现错误:", error);
                    }
                }

                f1();
            }
        }

        // myshopify_you_dain_gaoshi  // 设置全局的
        if (window.location.href.startsWith(wang_zhan_guan_li)) {

            // 获取网站 分类 的网络路径
            if (request.myshopify_huoqu_leimu_lujing === "myshopify_huoqu_leimu_lujing") {
                console.log("request.myshopify_huoqu_leimu_lujing");
                async function f1() {
                    try {
                        var path_set = $("header div.el-dialog__title:contains('头部菜单管理')").eq(0).parent().next().find(`div.el-tree-node__content`);
                        console.log('类目数量:', path_set.length)
                        var str_path = '';
                        for (var i = 0; i < path_set.length; i++) {
                            path_set.eq(i).find(`a:contains('编辑')`)[0].click();
                            await delay(ms = 250);
                            var path_i = $(`div.data-container div[role="dialog"]:contains(编辑菜单) div label:contains(链接地址)`).eq(0).parent().find('input')[0].value;
                            console.log(i, path_i);  // 获取路径成功
                            str_path = str_path + 'https://b08.shop6888.com' + path_i + '\n';
                            $("div header.el-dialog__header:contains('编辑菜单')").eq(0).find(`button`).click();
                            await delay(ms = 150);
                        }
                        copyTextToClipboard(text = str_path)
                    } catch (error) {
                        console.error("出现错误:", error);
                    }
                }
                f1();
            }

            // 外部预览
            if (request.myshopify_waibu_yulan === "myshopify_waibu_yulan") {
                console.log("request.myshopify_waibu_yulan");
                fanwei_start = request.fanwei_start
                fanwei_end = request.fanwei_end

            }

            // 获取来自service-worker.js 信息
            if (request.myshopify_huoqu_bianhao_yuming === "myshopify_huoqu_bianhao_yuming") {
                fanwei_start = request.fanwei_start
                fanwei_end = request.fanwei_end
                console.log("myshopify_huoqu_bianhao_yuming --> usfakename.js", fanwei_start, fanwei_end);

                var huoqu_bianhao_yuming = () => {
                    const bianhao_yuming_s1 = {};
                    // 遍历每个 tr 元素
                    $(`div.shop-website table tbody tr`).each(function () {
                        // 当前 tr 元素中查找索引为 2 的 td 元素
                        tdAtIndex2 = $(this).find('td').eq(2);  // 编号
                        tdAtIndex3 = $(this).find('td').eq(3);  // 域名
                        tdAtIndex2 = tdAtIndex2.text().trim()
                        tdAtIndex3 = tdAtIndex3.text().replace('模板预览', '').trim()
                        console.log("tdAtIndex2", tdAtIndex2);

                        if (tdAtIndex2.length > 0 && Number(tdAtIndex2) >= Number(fanwei_start) && Number(tdAtIndex2) <= Number(fanwei_end)) {
                            console.log(tdAtIndex2, tdAtIndex2);
                            bianhao_yuming_s1[tdAtIndex2] = tdAtIndex3;
                            // bianhao_yuming_s1.push(tdAtIndex2,tdAtIndex2);
                        } else {
                            console.log("当前 tr 元素没有索引位置为 2 的 td 元素");
                        }

                    });
                    sendResponse(bianhao_yuming_s1);
                };

                huoqu_bianhao_yuming();
            }

            // 着色
            if (request.myshopify_zhuo_se === "myshopify_zhuo_se") {
                console.log("request.myshopify_zhuo_se");
                async function f1() {
                    try {

                        const start = request.fanwei_start;
                        const end = request.fanwei_end;
                        console.log(start, end);

                        for (var i = start; i <= end; i++) {
                            // const obj=$(`td:contains('${i}'):eq(0)`);
                            console.log(i);
                            console.log($(`td:contains('${i}')`));
                            const obj = $(`td:contains('${i}')`).filter(function () {
                                return $(this).text().trim() === String(i);
                            });

                            console.log('obj', obj);
                            if (obj.length > 0) {
                                obj.css("background-color", "rgb(211,227,253)");
                                console.log(obj);
                            }
                        }
                        // copyTextToClipboard('============= 域名+邮箱 =============\n'+text_for_bianhao_yuming);

                    } catch (error) {
                        console.error("出现错误:", error);
                    }
                }
                f1();
            }

            // 复制 域名 网站编号
            if (request.myshopify_yuming_bianhao === "myshopify_yuming_bianhao") {
                console.log("request.myshopify_yuming_bianhao");
                async function f1() {
                    try {
                        start = Number(request.fanwei_start);
                        end = Number(request.fanwei_end);
                        text_for_bianhao_yuming = '';
                        for (var i = start; i <= end; i++) {
                            const obj = $(`td:contains('${i}')`).filter(function () {
                                return $(this).text().trim() === `${i}`;
                            });

                            if (obj.length > 0) {
                                const yuming = obj.parent().find('span:contains(http)').text();
                                const youxiang = yuming.replace('https://', '').replace('.', '') + '@gmail.com'
                                console.log(obj.text(), yuming);
                                s = obj.text() + ' ' + yuming + ' ' + youxiang + '\n';
                                text_for_bianhao_yuming = s + text_for_bianhao_yuming;
                            }
                        }

                        copyTextToClipboard('============= 域名+邮箱 =============\n' + text_for_bianhao_yuming);

                    } catch (error) {
                        console.error("出现错误:", error);
                    }
                }

                f1();
            }

            // 全局设置 邮电 告示
            if (request.myshopify_you_dain_gaoshi === "myshopify_you_dain_gaoshi") {
                console.log("request.myshopify_you_dain_gaoshi");
                async function f1() {
                    try {
                        // 读取谷歌数据
                        chrome.storage.local.get(['column1', 'column2', 'column3', 'column4', 'column5', 'column6', 'column7', 'column8', 'column9', 'column10', 'column11'], async function (data) {
                            // 检查是否成功检索到数据
                            if (chrome.runtime.lastError) {
                                console.error(chrome.runtime.lastError);
                                return;
                            }

                            // async function start() {

                            // }

                            // start();
                            const yu_ming_curent = $('div[role="dialog"] div.el-dialog__title:contains("全局配置")').text().replace(' 全局配置', '')
                            const yu_ming_zhi_web = 'https://' + yu_ming_curent
                            for (var i = 0; i < data.column1.length - 2; i++) {
                                const wangzhan_bianhao_zhi = data.column1[i];
                                const yu_ming_zhi = data.column2[i];
                                const youxiang_zhi = data.column3[i];
                                const lianxi_dianhua_zhi = data.column4[i];
                                const gaoshiyu_zhi = data.column5[i];
                                const biaoti_zhi = data.column6[i];
                                const guanjianci_zhi = data.column7[i];
                                const miaoshu_zhi = data.column8[i];
                                const huan_deng_pian1_zhi = data.column9[i];
                                const huan_deng_pian2_zhi = data.column10[i];
                                const muban_zhi_xuhao = data.column11[i];

                                if (yu_ming_zhi_web === yu_ming_zhi) {
                                    console.log(`你当前操作的域名:${wangzhan_bianhao_zhi} - ${yu_ming_zhi}`);

                                    // 点击基本设置
                                    await delay(300);
                                    $("div.el-tabs__nav-scroll div.el-tabs__item:contains('基本设置')")[0]?.click();
                                    obj1 = $("div.el-tabs__nav-scroll div.el-tabs__item:contains('基本设置')")[0]
                                    console.log('网站编号', wangzhan_bianhao_zhi);
                                    console.log('域名', yu_ming_zhi);

                                    // 设置邮箱地址 根本谷歌本地存储的值
                                    await delay(300);
                                    const youxiangdizhi = $(`div.config-container form div label:contains('邮箱地址')`).next().find('textarea')[0];
                                    console.log('youxiangdizhi', youxiangdizhi);
                                    console.log('邮箱地址', youxiang_zhi);
                                    textarea_value(textarea2 = youxiangdizhi, value = youxiang_zhi);

                                    // 联系电话
                                    await delay(300);
                                    const lian_xi_dian_hua = $(`div.config-container form div label:contains('联系电话')`).next().find('textarea')[0];
                                    console.log('lian_xi_dian_hua', lian_xi_dian_hua);
                                    console.log('联系电话', lianxi_dianhua_zhi);
                                    textarea_value(textarea2 = lian_xi_dian_hua, value = lianxi_dianhua_zhi);

                                    // 政策 告示语
                                    await delay(300);
                                    const ding_bu_gao_shi_yu = $(`div.config-container form div label:contains('顶部告示语')`).next().find('textarea')[0];
                                    console.log('ding_bu_gao_shi_yu', ding_bu_gao_shi_yu);
                                    console.log('政策顶部告示语', gaoshiyu_zhi);
                                    textarea_value(textarea2 = ding_bu_gao_shi_yu, value = gaoshiyu_zhi);

                                    // 保存
                                    await delay(300);
                                    $('div.right-panel button span:contains("保存")')[0]?.click();

                                    // 点击配置设置
                                    await delay(300);
                                    $("div.el-tabs__nav-scroll div.el-tabs__item:contains('配置设置')")[0]?.click();

                                    // 币种设置
                                    await delay(800);
                                    $('div.el-tabs__content:contains("币种设置") div>span:contains("请选择")')[0]?.click();

                                    // 欧元
                                    await delay(500);
                                    // $('div.el-tabs__content:contains("币种设置") div>span:contains("EUR (欧元:€)")')[0].click();
                                    $('li.el-select-dropdown__item:contains("USD (美元:$)")')[0]?.click();

                                    // logo生成
                                    /*
                                    // 界面已经发生变化
                                    await delay(300);
                                    let input1 = $('div label:contains("LOGO"):eq(0)').next().find(`div:contains(图片文字):eq(-1)`).next().find(`input`)[0]
                                    if(input1.value.length<=4){
                                        let daxie = input1.value.toUpperCase();
                                        input_value(input2=input1,value=daxie);
                                    }else{
                                        let a=input1.value;
                                        let shouzimudaxie = a[0].toUpperCase() + a.substr(1);
                                        input_value(input2=input1,value=shouzimudaxie);
                                    }
                                    await delay(300);
                                    $('button span:contains("LOGO自动随机生成")')[0]?.click();
                                    await delay(300);
                                    $('button span:contains("LOGO上传")')[0]?.click();
                                    */

                                    // 新的 全局 配置 那个 配置设置 那个 域名的logo 图片生成
                                    await delay(300);
                                    $('button span:contains("LOGO自动随机生成")')[0]?.click();
                                    await delay(300);
                                    let f1 = $(`div[role="dialog"] header[class="el-dialog__header show-close"]:contains("LOGO生成")`).next();
                                    let input1 = f1.find(`div.el-form-item__content div.el-input-group__prepend:contains("图片字符")`).next().find(`input`)[0];
                                    if (input1.value.length <= 4) {
                                        let daxie = input1.value.toUpperCase();
                                        input_value(input2 = input1, value = daxie);
                                    } else {
                                        let a = input1.value;
                                        let shouzimudaxie = a[0].toUpperCase() + a.substr(1);
                                        input_value(input2 = input1, value = shouzimudaxie);
                                    }
                                    await delay(100);
                                    var footer = $(`div[role="dialog"] header[class="el-dialog__header show-close"]:contains("LOGO生成")`).next().next()
                                    footer.find(`button:contains('生成')`)[0].click();
                                    await delay(200);
                                    // 这个逻辑循环检测 当前这个字体 是不是这个 Symbol
                                    while (1) {
                                        if ($(`div.el-dialog[tabindex="-1"] div.config-container div.el-dialog[tabindex="-1"] footer.el-dialog__footer span:contains(当前字体：Symbol)`)[0]) {
                                            await delay(200);
                                            footer.find(`button:contains('生成')`)[0].click();
                                        } else {
                                            break;
                                        }
                                    }

                                    footer.find(`button:contains('LOGO上传')`)[0].click();
                                    //await delay(100);

                                    // icon生成
                                    await delay(300);
                                    $('button span:contains("ICO自动随机生成")')[0]?.click();
                                    await delay(300);
                                    $('button span:contains("ICO上传")')[0]?.click();

                                    // 底部 logo
                                    await delay(100);
                                    // alert("点击上传 付款底部logo")
                                    await delay(1000);
                                    console.log(`这里我等待2秒来处理这个 付款底部logo`);
                                    // $(`div[role="dialog"] div.config-container form div.el-tabs__content div.el-form-item__label:contains(底部LOGO)`).next().find(`input`)[0].click()
                                    // $(`div.avatar-uploader div[tabindex="0"] i`)[0].click();
                                    // 一定要用户主动点击
                                    $(`div.avatar-uploader div[tabindex="0"] i`).click();
                                    // await delay(500);
                                    // $(`div.avatar-uploader div[tabindex="0"] i`).click();
                                    // await delay(500);
                                    // $(`div.avatar-uploader div[tabindex="0"] i`).click();


                                    // 皮肤
                                    await delay(300);
                                    $('div.el-tabs__content:contains("币种设置") div>span:contains("默认")')[0]?.click();

                                    // 皮肤我就不选择了  因为该没有设置好  选择 模板2
                                    await delay(300);
                                    // console.log('皮肤不选择了!');
                                    muban_xuhao = muban_zhi_xuhao
                                    console.log(`你选择的模板：${muban_xuhao}`);
                                    $(`li.el-select-dropdown__item:contains(模板${muban_xuhao})`)[0].click();

                                    // 保存
                                    await delay(300);
                                    $('div.right-panel button span:contains("保存")')[0]?.click();

                                    // 点击SEO
                                    await delay(300);
                                    $("div.el-tabs__nav-scroll div.el-tabs__item:contains('SEO')")[0]?.click();

                                    // 页面标题
                                    await delay(300);
                                    const ye_mian_biao_ti = $(`div.config-container form div label:contains('页面标题')`).next().find('textarea')[0];
                                    console.log('ye_mian_biao_ti', ye_mian_biao_ti);
                                    console.log('页面标题', biaoti_zhi);
                                    textarea_value(textarea2 = ye_mian_biao_ti, value = biaoti_zhi);

                                    // 页面关键词
                                    await delay(300);
                                    const ye_mian_guan_jian_ci = $(`div.config-container form div label:contains('页面关键词')`).next().find('textarea')[0];
                                    console.log('ye_mian_guan_jian_ci', ye_mian_guan_jian_ci);
                                    console.log('页面关键词', ye_mian_guan_jian_ci);
                                    textarea_value(textarea2 = ye_mian_guan_jian_ci, value = guanjianci_zhi);

                                    // 页面描述
                                    await delay(300);
                                    const ye_mian_miao_shu_ci = $(`div.config-container form div label:contains('页面描述')`).next().find('textarea')[0];
                                    console.log('ye_mian_miao_shu_ci', ye_mian_miao_shu_ci);
                                    console.log('页面描述', miaoshu_zhi);
                                    textarea_value(textarea2 = ye_mian_miao_shu_ci, value = miaoshu_zhi);

                                    // 保存
                                    await delay(300);
                                    $('div.right-panel button span:contains("保存")')[0]?.click();


                                    // 进入 首页幻灯片 模块 首页幻灯片
                                    await delay(200);
                                    $("div.el-tabs__nav-scroll div.el-tabs__item:contains('首页幻灯片')")[0]?.click();

                                    // 添加广告图
                                    await delay(800);
                                    $('thead:contains("广告图") th button:contains("添加")')[0]?.click();

                                    // 广告图标题
                                    await delay(300);
                                    const biaoti_guangaotu = $('div.el-dialog form.el-form div.el-form-item.is-required.asterisk-left:contains("标题") input.el-input__inner')[0];
                                    // textarea_value(textarea2 = biaoti_guangaotu, value = huan_deng_pian1_zhi.split(',')[0]);
                                    textarea_value(textarea2 = biaoti_guangaotu, value = ' ');
                                    console.log('广告图标题', huan_deng_pian1_zhi.split(',')[0]);

                                    // 广告图 链接地址
                                    await delay(300);
                                    const lianjie_dizhi_guangaotu = $('div.el-dialog form.el-form div.el-form-item.is-required.asterisk-left:contains("链接地址") input.el-input__inner')[0];
                                    textarea_value(textarea2 = lianjie_dizhi_guangaotu, value = huan_deng_pian1_zhi.split(',')[1]);
                                    console.log('广告图 链接地址', huan_deng_pian1_zhi.split(',')[1]);

                                    // 图片
                                    // await delay(500);
                                    // File chooser dialog can only be shoxn with a user aotivation
                                    // $('div.el-dialog form.el-form div.el-form-item.is-required.asterisk-left:contains("图片") div.avatar-uploader input')[0]?.click();  // 只能用户点击
                                    // $('div.el-dialog form.el-form div.el-form-item.is-required.asterisk-left:contains("图片") div.el-upload.el-upload--text')[0]?.click();  // 只能用户点击

                                    // 保存
                                    await delay(200);
                                    $(`div[tabindex="-1"] div.config-container div.right-panel button span:contains(更新缓存)`)[0].click()
                                    await delay(200);
                                    $(`div[tabindex="-1"] div.config-container div.right-panel button span:contains(保存)`)[0].click()
                                    // $('div[role="dialog"] div.el-dialog footer.el-dialog__footer button:contains("保存")')[0].click(async ()=>{
                                    //     await delay(2000);
                                    //     alert('准备二次添加!');
                                    //     console.log('时间到,准备二次添加!');
                                    //     $('thead:contains("广告图") th button:contains("添加")')[0]?.click();

                                    //     // 广告图标题
                                    //     await delay(200);
                                    //     const biaoti_guangaotu = $('div.el-dialog form.el-form div.el-form-item.is-required.asterisk-left:contains("标题") input.el-input__inner')[0];
                                    //     textarea_value(textarea2=biaoti_guangaotu,value=huan_deng_pian2_zhi.split(',')[0]);

                                    //     // 广告图 链接地址
                                    //     await delay(200);
                                    //     const lianjie_dizhi_guangaotu = $('div.el-dialog form.el-form div.el-form-item.is-required.asterisk-left:contains("链接地址") input.el-input__inner')[0];
                                    //     textarea_value(textarea2=lianjie_dizhi_guangaotu,value=huan_deng_pian2_zhi.split(',')[1]);

                                    //     // 图片
                                    //     await delay(200);
                                    //     $('div.el-dialog form.el-form div.el-form-item.is-required.asterisk-left:contains("图片") div.avatar-uploader input')[0]?.click();

                                    // });

                                    $('div[role="dialog"] div.el-dialog footer.el-dialog__footer').one('click', 'button:contains("保存")', async function () {
                                        // alert('准备二次添加!');
                                        console.log('时间到，准备二次添加!');
                                        await delay(800);
                                        $('thead:contains("广告图") th button:contains("添加")')[0]?.click();

                                        // 广告图标题
                                        await delay(200);
                                        const biaoti_guangaotu = $('div.el-dialog form.el-form div.el-form-item.is-required.asterisk-left:contains("标题") input.el-input__inner')[0];
                                        // textarea_value(textarea2 = biaoti_guangaotu, value = huan_deng_pian2_zhi.split(',')[0]);
                                        textarea_value(textarea2 = biaoti_guangaotu, value = ' ');

                                        // 广告图 链接地址
                                        await delay(200);
                                        const lianjie_dizhi_guangaotu = $('div.el-dialog form.el-form div.el-form-item.is-required.asterisk-left:contains("链接地址") input.el-input__inner')[0];
                                        textarea_value(textarea2 = lianjie_dizhi_guangaotu, value = huan_deng_pian2_zhi.split(',')[1]);

                                        // 图片
                                        await delay(200);
                                        // $('div.el-dialog form.el-form div.el-form-item.is-required.asterisk-left:contains("图片") div.avatar-uploader input')[0]?.click();
                                    });
                                    break;
                                }

                            }

                            // console.log('5 content.js show data.column1:', data.column1);
                            // console.log('6 content.js show data.column2:', data.column2);

                        });


                    } catch (error) {
                        console.error("出现错误:", error);
                    }
                }

                f1();
            }

            // 添加静态
            if (request.myshopify_tian_jia_jing_tai === "myshopify_tian_jia_jing_tai") {
                console.log("request.myshopify_tian_jia_jing_tai");
                async function f1() {
                    try {
                        const start = Number(request.fanwei_start);
                        const end = Number(request.fanwei_end);
                        console.log(start, end);

                        for (var i = start; i <= end; i++) {
                            const obj_td = $(`td:contains('${i}')`).filter(function () {
                                return $(this).text().trim() === `${i}`;
                            });;

                            if (obj_td.length > 0) {
                                // obj_td.css("background-color","rgb(102,148,197)");
                                await delay(300);
                                const obj_tr = obj_td.parent();
                                obj_tr.find('span:contains(http)').css("background-color", "rgb(102,148,197)");

                                alert(`网站编号:${i} 添加静态`);
                                await delay(300);
                                obj_tr.find('span:contains(添加静态任务)').click();
                                await delay(300);
                                $('div[role="dialog"] div.el-dialog footer.el-dialog__footer button:contains("添加")')[0].click()

                                await delay(300);
                                obj_tr.find('span:contains(http)').css("background-color", "rgb(255,255,255)");

                            }
                        }


                    } catch (error) {
                        console.error("出现错误:", error);
                    }
                }

                f1();
            }

            // 文章管理 底部菜单
            if (request.myshopify_wenzhang_guanli_dibu_caidan === "myshopify_wenzhang_guanli_dibu_caidan") {
                console.log("request.myshopify_wenzhang_guanli_dibu_caidan");
                async function f1() {
                    try {
                        'el-table__expand-icon'

                        const start = Number(request.fanwei_start);
                        const end = Number(request.fanwei_end);
                        console.log(start, end);
                        console.log('start', typeof (start));
                        console.log('end', typeof (end));

                        for (var i = start; i <= end; i++) {
                            console.log('i', i);
                            const obj_td = $(`td:contains('${i}')`).filter(function () {
                                return $(this).text().trim() === `${i}`;
                            });;

                            if (obj_td.length > 0) {
                                await delay(2000);
                                // alert(`文章管理 网站编号: ${i}`);
                                console.log(`文章管理 网站编号: ${i}`);

                                // 点击下拉按钮 显示 那个文章管理
                                await delay(300);
                                const obj_tr = obj_td.parent();
                                obj_tr.find('div.el-table__expand-icon').click();

                                // 下一个 tr就是文章管理 点击 文章管理
                                await delay(300);
                                obj_tr.next().find('button:contains(文章管理)')[0].click();

                                // 点击导入模板
                                // while (1) {
                                //     await delay(100);
                                //     s = `div[role="dialog"] div.left-panel button:contains("导入模板")`
                                //     let eles = $(s);
                                //     if (eles.length > 0) {
                                //         eles[0].click()
                                //         break;
                                //     }
                                // }


                                // await delay(300);
                                // 点击导入模板
                                await delay(500);
                                console.log("导入模板");
                                s = `div[role="dialog"] div.left-panel button:contains("导入模板")`
                                await waitForClick(s, 1, 5000)

                                // await waitForClick(s, 10000)

                                // 请选择
                                // await delay(300);
                                // $(`div.el-dialog:contains(导入文章模板) form span:contains(请选择)`)[0].click();
                                // ele = $(`div.el-dialog:contains(导入文章模板) form span:contains(请选择)`)[0];
                                // if (i === start + 1) {
                                //     console.log("开始第二次");
                                //     await delay(2000000);
                                // }
                                await delay(300);
                                console.log("请选择");
                                $(`header:contains(导入文章模板)`).parent().find(`div.el-select__selected-item span:contains(请选择)`)[0].click()
                                // $(`div[role="dialog"] div.el-dialog[tabindex="-1"] div.el-select__selected-item span:contains(请选择)`)[0].click()
                                // await waitForClick(`div.el-dialog[tabindex="-1"]:contains(导入文章模板) div.el-select__selected-item span:contains(请选择)`, 0, 5000)

                                // 分组8（女装）
                                // await delay(300);
                                // $(`div[role="tooltip"] div.el-scrollbar ul[role="listbox"] li[role="option"]:contains("分组8（女装）")`)[0].click();
                                // 生成 21-25的随机值   getRandomInt(21, 25) 
                                await delay(500);
                                var num_muban = getRandomInt(21, 25);
                                console.log(`${num_muban} 女装`);
                                $(`div[role="tooltip"][aria-hidden="false"] div.el-scrollbar ul[role="listbox"] li[role="option"]:contains("${num_muban} 女装")`)[0].click();
                                // await waitForClick(`div[role="tooltip"] div.el-scrollbar ul[role="listbox"] li[role="option"]:contains("${num_muban} 女装")`, 0, 5000)

                                // 全选 分组8（女装）
                                await delay(300);
                                console.log(`全选`);
                                $(`div.el-dialog[tabindex="-1"]:contains(导入文章模板) div label:contains('${num_muban} 女装')`)[0].click()
                                // $(`div.el-dialog:contains(导入文章模板) form label:contains('${num_muban} 女装')`)[0].click();
                                // await waitForClick(`div.el-dialog[tabindex="-1"]:contains(导入文章模板) div label:contains('${num_muban} 女装')`, 0, 5000)

                                // 点击保存 按钮
                                await delay(300);
                                console.log(`保存`);
                                $(`div[role="dialog"] div.el-dialog[tabindex="-1"] footer.el-dialog__footer button:contains('保存')`)[0].click()
                                // $(`div[role="dialog"][aria-label="导入文章模板"] div.el-dialog footer.el-dialog__footer button:contains('保存')`)[0].click();
                                // await waitForClick(`div[role="dialog"] div.el-dialog[tabindex="-1"] footer.el-dialog__footer button:contains('保存')`, 0, 5000)

                                // // 点击导入模板
                                // await delay(400);
                                // $('div[role="dialog"] div.left-panel button:contains("导入模板")')[0].click();

                                // // 请选择
                                // await delay(400);
                                // ele = $(`div.el-dialog:contains(导入文章模板) form span:contains(请选择)`)[0];
                                // waitForClick(ele,10000)

                                // // 分组8（女装）
                                // await delay(400);
                                // // $(`div[role="tooltip"] div.el-scrollbar ul[role="listbox"] li[role="option"]:contains("分组8（女装）")`)[0].click();
                                // // 生成 21-25的随机值   getRandomInt(21, 25) 
                                // var num_muban = getRandomInt(21, 25);
                                // $(`div[role="tooltip"] div.el-scrollbar ul[role="listbox"] li[role="option"]:contains("${num_muban} 女装")`)[0].click();

                                // // 全选 分组8（女装）
                                // await delay(300);
                                // $(`div.el-dialog:contains(导入文章模板) form label:contains('${num_muban} 女装')`)[0].click();

                                // // 点击保存 按钮
                                // await delay(300);
                                // $(`div[role="dialog"][aria-label="导入文章模板"] div.el-dialog footer.el-dialog__footer button:contains('保存')`)[0].click();

                                // 来一个循环监听
                                while (1) {
                                    await delay(300);
                                    const spanText = $(`div[role="dialog"] div.el-pagination span.el-pagination__total:contains(共 6 条)`);

                                    if (spanText.length > 0) {
                                        // alert('全选且关闭!');
                                        // alert("全选");
                                        // 全选
                                        console.log(`出现了 共6条!`);
                                        console.log(`全选`);
                                        $(`div[role="dialog"] table.el-table__header thead th label.el-checkbox:eq(0)`).click();

                                        // 加入网站 底部菜单
                                        console.log(`加入网站 底部菜单`);
                                        await delay(300);
                                        $(`div[role="dialog"] div.el-dialog[tabindex="-1"] div.right-panel button:contains(' 加入网站底部菜单 '):eq(0)`).click();

                                        // 关闭
                                        await delay(300);
                                        console.log(`关闭`);
                                        $('div.el-overlay:not([style*="display: none"]) div[role="dialog"] header.el-dialog__header.show-close:contains(文章管理) button[aria-label="el.dialog.close"]:eq(0)').click();
                                        break;
                                    }
                                }

                            }
                        }

                    } catch (error) {
                        console.error("出现错误:", error);
                    }
                }

                f1();
            }

            // 按分类导入商品  全部
            if (request.myshopify_an_fen_lei_dao_ru_shang_ping === "myshopify_an_fen_lei_dao_ru_shang_ping") {
                console.log("request.myshopify_an_fen_lei_dao_ru_shang_ping");


                async function f1() {
                    try {
                        const start = Number(request.fanwei_start);
                        const end = Number(request.fanwei_end);
                        console.log(start, end);
                        console.log('start', typeof (start));
                        console.log('end', typeof (end));

                        for (var i = start; i <= end; i++) {
                            console.log('i', i);
                            const obj_td = $(`td:contains('${i}')`);


                            if (obj_td) {
                                $(`td:contains('${i}')`).parent().css("color", "orange");
                                await delay(1000);
                                alert(`文章管理 网站编号: ${i} `);
                                // 点击下拉按钮 显示 那个文章管理
                                await delay(300);
                                const obj_tr = obj_td.parent();
                                obj_tr.find('button:contains(添加导入分类商品任务)').click();


                                // 找到模态框
                                await delay(300);
                                div_dao = $(`div[role="dialog"] header:contains("按分类导入商品")`).next();

                                // 导入最小值
                                await delay(300);
                                min_num_input = div_dao.find('label:contains(导入分类下商品最小数量（都填0表示全部导入）):eq(0)').next().find('input')[0];
                                input_value(input2 = min_num_input, value = '299');


                                // 导入最大值
                                await delay(300);
                                max_num_input = div_dao.find('label:contains(导入分类下商品最大数量（都填0表示全部导入）):eq(0)').next().find('input')[0];
                                input_value(input2 = max_num_input, value = '300');

                                // 已使用次数
                                await delay(300);
                                div_dao.find('label:contains(已使用次数):eq(0)').next().find('span:contains(请选择)').click();

                                // 选择 0
                                // div[role="tooltip"] div.el-select-dropdown ul[role="listbox"] li:contains(0)
                                $(`div[role="tooltip"] div.el-select-dropdown ul[role="listbox"] li:contains(0)`).filter(function () {
                                    return $(this).text().trim() === '0';
                                })[0].click();

                                // ============= 预打开 =============
                                // * 打开女装
                                await delay(300);
                                $(`li:contains(Women's Clothing 女装(直属商品数：0)(全部商品数：)`).prev().prev()?.click();  // ?.click();

                                // * 打开外套
                                await delay(300);
                                $(`li:contains(Outerwear 外套(直属商品数：)`).prev().prev()?.click()  // ?.click();

                                // * 打开毛衣
                                await delay(300);
                                $(`li:contains(Sweaters 毛衣(直属商品数：0))`).prev().prev()?.click()  // ?.click();

                                // * 打开上装
                                await delay(300);
                                $(`li:contains(Tops 上装(直属商品数：0))`).prev().prev()?.click()  // ?.click();

                                // * 打开下装
                                await delay(300);
                                $(`li:contains(Bottoms 下装(直属商品数：0))`).prev().prev()?.click()  // ?.click();

                                // * 打开连衣裙
                                await delay(300);
                                $(`li:contains(Dresses 连衣裙(直属商品数：0))`).prev().prev()?.click()  // ?.click();

                                // * 打开泳装
                                await delay(300);
                                $(`li:contains(Swimwear 泳装(直属商品数：0))`).prev().prev()?.click()  // ?.click();

                                // * 打开牛仔
                                await delay(300);
                                $(`li:contains(Denim 牛仔(直属商品数：0))`).prev().prev()?.click()  // ?.click();

                                // =========================== 详细选择 商品 ===========================
                                // 1 选择 连帽衫和运动衫
                                await delay(300);
                                $(`li span:contains(Hoodies & Sweatshirts 连帽衫和运动衫)`)?.click();
                                console.log($(`li span:contains(Hoodies & Sweatshirts 连帽衫和运动衫)`));

                                // 2 选择 夹克
                                await delay(300);
                                $(`li span:contains(Women's Jackets 夹克)`)?.click();
                                console.log($(`li span:contains(Women's Jackets 夹克)`));

                                // 3 选择 西装外套
                                await delay(300);
                                $(`li span:contains(Blazers 西装外套)`)?.click();
                                console.log($(`li span:contains(Blazers 西装外套)`));

                                // x 选择 背心外套
                                // await delay(300);
                                // $(`li span:contains(Vest Coats 背心外套)`)?.click();
                                // console.log($(`li span:contains(Vest Coats 背心外套)`));

                                // 4 外套
                                await delay(300);
                                $(`li span:contains(Outerwears 外套)`)?.click();
                                console.log($(`li span:contains(Outerwears 外套)`));


                                // 羊毛衫
                                // await delay(300);
                                // $(`li span:contains(Woolen Sweater 羊毛衫)`)?.click();
                                // console.log($(`li span:contains(Woolen Sweater 羊毛衫)`));

                                // 5 毛衣
                                await delay(300);
                                $(`li span:contains(Sweater 毛衣)`)?.click();
                                console.log($(`li span:contains(Sweater 毛衣)`));


                                // T-Shirts T恤衫(直属商品数：17396)(全部商品数：17396)(个人商品数：17396)(可用商品数：15117)
                                await delay(300);
                                $(`li span:contains(T-Shirts T恤衫)`)?.click();

                                // Top 上装(直属商品数：11354)(全部商品数：11354)(个人商品数：11354)(可用商品数：9108)
                                await delay(300);
                                $(`li span:contains(Top 上)`)?.click();

                                // Shorts 短裤(直属商品数：13932)(全部商品数：13932)(个人商品数：13932)(可用商品数：11949)
                                await delay(300);
                                $(`li span:contains(Shorts 短裤)`)?.click();

                                // Dress 连衣裙(直属商品数：106819)(全部商品数：106819)(个人商品数：106819)(可用商品数：106819)
                                await delay(300);
                                $(`li span:contains(Dress 连衣裙)`)?.click();

                                // Midi Dresses 中长连衣裙(直属商品数：12149)(全部商品数：12149)(个人商品数：12149)(可用商品数：12149)
                                await delay(300);
                                $(`li span:contains(Midi Dresses 中长连衣裙)`)?.click();


                                // Party Dress 派对礼服(直属商品数：15120)(全部商品数：15120)(个人商品数：15120)(可用商品数：15120)
                                // Skirt 裙子(直属商品数：12064)(全部商品数：12064)(个人商品数：12064)(可用商品数：12064)
                                // Swimsuit 泳装(直属商品数：10561)(全部商品数：10561)(个人商品数：10561)(可用商品数：10561)
                                // Denim Jeans 牛仔长裤(直属商品数：11139)(全部商品数：11139)(个人商品数：11139)(可用商品数：11139)

                                // 添加
                                await delay(5000);
                                $('div[role="dialog"] div.el-dialog footer.el-dialog__footer button:contains("添加")')[0].click();

                            }

                            // $(`td:contains('${i}')`).parent().css("background-color", "transparent");
                            $(`td:contains('${i}')`).parent().css("color", "black");
                        }





                    } catch (error) {
                        console.error("出现错误:", error);
                    }
                }

                f1();
            }

            // 一键导入菜单
            if (request.myshopify_yijian_daoru_caidan === "myshopify_yijian_daoru_caidan") {
                console.log("request.myshopify_yijian_daoru_caidan");
                async function f1() {
                    try {
                        // 'el-table__expand-icon'

                        const start = Number(request.fanwei_start);
                        const end = Number(request.fanwei_end);
                        console.log(start, end);
                        console.log('start', typeof (start));
                        console.log('end', typeof (end));

                        for (var i = start; i <= end; i++) {
                            console.log('i', i);
                            const obj_td = $(`td:contains('${i}')`).filter(function () {
                                return $(this).text().trim() === `${i}`;
                            });;

                            if (obj_td.length > 0) {
                                // alert(`文章管理 网站编号: ${i}`);
                                console.log(`文章管理 网站编号: ${i}`);
                                // 点击下拉按钮 显示 菜单
                                await delay(300);
                                const obj_tr = obj_td.parent();
                                obj_tr.find('div.el-table__expand-icon').click();

                                // 下一个 tr就是文章管理 点击 文章管理
                                await delay(400);
                                obj_tr.next().find('button:contains("一键导入菜单（新）")')[0].click();

                                // 点击确定
                                await delay(400);
                                $(`div[role="dialog"][aria-label="温馨提示  会清空原有菜单"] button:contains(确定):eq(0)`).click();

                            }
                        }
                        await delay(300);
                        $(`div.left-panel button span:contains(更新缓存)`)[0].click()

                    } catch (error) {
                        console.error("出现错误:", error);
                    }
                }

                f1();
            }

            // 复制上一次菜单 忽略 开头的第一个索引网站
            if (request.myshopify_fuzhi_shangyici_caidan === "myshopify_fuzhi_shangyici_caidan") {
                console.log("request.myshopify_fuzhi_shangyici_caidan");
                console.log("复制上一次菜单");
                async function f1() {
                    try {
                        // 'el-table__expand-icon'
                        const start = Number(request.fanwei_start);
                        const end = Number(request.fanwei_end);
                        console.log(start, end);
                        console.log('start', typeof (start));
                        console.log('end', typeof (end));

                        // start+1  这个就已经跳过了第一个了 
                        for (var i = start + 1; i <= end; i++) {
                            console.log('i', i);

                            const obj_td = $(`td:contains('${i}')`).filter(function () {
                                return $(this).text().trim() === `${i}`;
                            });;

                            if (obj_td.length > 0) {
                                alert(`文章管理 网站编号: ${i}`);
                                // 点击下拉按钮 显示 菜单
                                await delay(300);
                                const obj_tr = obj_td.parent();
                                obj_tr.find('div.el-table__expand-icon').click();  // 打开了 下拉菜单

                                // 下一个 tr就是文章管理 点击 文章管理
                                await delay(400);
                                obj_tr.next().find('button:contains("头部菜单配置")')[0].click();

                                // 复制上一次编辑
                                await delay(400);
                                $(`div.el-dialog[tabindex="-1"] div.data-container div.right-panel button:contains(复制上次编辑)`)[0].click();

                                // 全部保存
                                await delay(400);
                                $(`div.el-dialog[tabindex="-1"] div.data-container div.left-panel button:contains(全部保存)`)[0].click();

                                // 关闭
                                await delay(400);
                                $(`div.el-dialog[tabindex="-1"] header.el-dialog__header button[aria-label="el.dialog.close"]`)[0].click();

                                // 点击确定
                                // await delay(400);
                                // $(`div[aria-label="温馨提示  会清空原有菜单"] button:contains(确定):eq(0)`).click();

                            }
                        }
                        await delay(300);
                        $(`div.left-panel button span:contains(更新缓存)`)[0].click()

                    } catch (error) {
                        console.error("出现错误:", error);
                    }
                }

                f1();
            }

        }
    });
}

