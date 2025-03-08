console.log("run_directly.js 被加载")
var dianxiaomi_url = "https://www.dianxiaomi.com";
var a_360_doc_url = "http://www.360doc.com/"
var a_360_doc_url_edit = "http://www.360doc.com/edit/"
var a_xiapi = "https://seller.shopee.cn/"
a_myshopify_url = "https://b08-admin.shop6888.com/"
/*
* 下面的模块将会直接加载到页面中
*/

current_url = window.location.href
console.log("当前网址:", current_url)
// ==================任何网址 优化==================
kai = 0
if (kai === 1) {
    try {
        // <span id="state_4">161900</span>
        setTimeout(() => {

            // 创建并插入样式
            var style = document.createElement('style');
            style.type = 'text/css';
            style.innerHTML = `
            .alert {
                display: none; /* 默认不显示 */
                width: 560px;
                height: 396px;
                border-radius: 3px;
                background-color: rgba(80, 227, 194, 0.45);
                background-image: none;
                background-position-x: 0%;
                background-repeat: no-repeat;
                padding: 10px;
                margin-top: 10px;
                color: #721c24;
                border: 1px solid #f5c6cb;
                text-align: center;
                line-height: 396px;
            }
            `;
            document.head.appendChild(style);

            // 创建悬浮按钮  复制按钮
            var button = document.createElement('button');
            button.id = 'rsgz_btn001';
            button.textContent = '复制';
            button.style.position = 'fixed';
            // 老式写法
            button.style.top = '700px';
            button.style.right = '1780px';
            button.style.zIndex = 9999;
            button.style.backgroundColor = '#000000'; // 设置背景颜色为黑色
            button.style.color = 'white';           // 设置文字颜色为白色
            button.style.padding = '10px 27px 10px 37px';  // 设置内边距

            var button2 = document.createElement('button');
            button2.textContent = '进入';
            button2.style.position = 'fixed';
            button2.style.top = '750px';
            button2.style.right = '1780px';
            button2.style.zIndex = 9999;
            button2.style.backgroundColor = '#000000'; // 设置背景颜色为黑色
            button2.style.color = 'white';           // 设置文字颜色为白色
            button2.style.padding = '10px 27px 10px 37px';  // 设置内边距

            // 复制当前页网址
            var button3 = document.createElement('button');
            button3.textContent = '当前';
            button3.style.position = 'fixed';
            button3.style.top = '800px';
            button3.style.right = '1780px';
            button3.style.zIndex = 9999;
            button3.style.backgroundColor = '#000000'; // 设置背景颜色为黑色
            button3.style.color = 'white';           // 设置文字颜色为白色
            button3.style.padding = '10px 27px 10px 37px';  // 设置内边距

            // 所有已经打开的页面
            var button4 = document.createElement('button');
            button4.textContent = '标签';
            button4.style.position = 'fixed';
            button4.style.top = '850px';
            button4.style.right = '1780px';
            button4.style.zIndex = 9999;
            button4.style.backgroundColor = '#000000'; // 设置背景颜色为黑色
            button4.style.color = 'white';           // 设置文字颜色为白色
            button4.style.padding = '10px 27px 10px 37px';  // 设置内边距

            // 添加悬浮按钮到页面  进入网址按钮 来源粘贴板的网址
            document.body.appendChild(button);
            document.body.appendChild(button2);
            document.body.appendChild(button3);
            document.body.appendChild(button4);

            // 设置页面上所有元素的文本可复制
            function makeTextCopyable() {
                const allElements = document.querySelectorAll('*');
                allElements.forEach(element => {
                    element.style.userSelect = 'auto';
                    element.style.webkitUserSelect = 'auto';
                    element.style.MozUserSelect = 'auto';
                    element.style.msUserSelect = 'auto';
                });
            }

            // 添加点击事件监听器
            button.addEventListener('click', async function () {
                var selection = window.getSelection();
                console.log("点击了复制");

                // 创建新的div元素 
                var alertBox = document.createElement('div');
                alertBox.className = 'alert'; // 添加CSS类名
                alertBox.textContent = '复制成功!'; // 设置提示文本
                document.body.appendChild(alertBox); // 将div添加到页面中

                // 显示提示信息
                alertBox.style.display = 'block';

                // 一秒后隐藏提示信息并从DOM中移除
                setTimeout(function () {
                    alertBox.style.display = 'none'; // 隐藏提示信息
                    alertBox.parentNode.removeChild(alertBox); // 从DOM中移除提示信息
                }, 500);

                if (selection.rangeCount > 0) {
                    var range = selection.getRangeAt(0);
                    var objs = range.cloneContents();
                    var tempElement = document.createElement("div");
                    tempElement.appendChild(objs);
                    var links = tempElement.getElementsByTagName("a");
                    var allText = '';

                    for (var i = 0; i < links.length; i++) {
                        allText += links[i].innerText.trim() + ':' + links[i].href + '\n';
                    }

                    copyTextToClipboard(allText);
                }
            });

            // 添加点击事件监听器
            button2.addEventListener('click', async function () {
                // 创建新的div元素 
                var alertBox = document.createElement('div');
                alertBox.className = 'alert'; // 添加CSS类名
                alertBox.textContent = '进入!'; // 设置提示文本
                document.body.appendChild(alertBox); // 将div添加到页面中

                // 显示提示信息
                alertBox.style.display = 'block';

                // 一秒后隐藏提示信息并从DOM中移除
                setTimeout(function () {
                    alertBox.style.display = 'none'; // 隐藏提示信息
                    alertBox.parentNode.removeChild(alertBox); // 从DOM中移除提示信息
                }, 500);

                try {
                    // 获取剪贴板内容
                    console.log("点击了进入");
                    const clipboardText = await navigator.clipboard.readText();
                    // 将浏览器当前页面跳转到剪贴板中的网址
                    window.location.href = clipboardText;
                } catch (error) {
                    console.error('无法从剪贴板读取内容:', error);
                    alert('无法从剪贴板读取内容，请确保剪贴板中包含有效的URL。');
                }
            });

            // 添加点击事件监听器
            button3.addEventListener('click', function () {
                console.log("点击了btn3");

                // 创建新的div元素 
                var alertBox = document.createElement('div');
                alertBox.className = 'alert'; // 添加CSS类名
                alertBox.textContent = '复制当前页!'; // 设置提示文本
                document.body.appendChild(alertBox); // 将div添加到页面中

                // 显示提示信息
                alertBox.style.display = 'block';

                // 一秒后隐藏提示信息并从DOM中移除
                setTimeout(function () {
                    alertBox.style.display = 'none'; // 隐藏提示信息
                    alertBox.parentNode.removeChild(alertBox); // 从DOM中移除提示信息
                }, 500);

                // 获取当前网页的标题和网址
                const pageTitle = document.title;
                const pageUrl = window.location.href;
                // 将标题和网址组合，中间用冒号分隔
                const textToCopy = `${pageTitle}:${pageUrl}`;

                // 将组合后的文本复制到剪贴板
                navigator.clipboard.writeText(textToCopy).then(function () {
                    // 复制成功后的操作，例如可以弹出一个提示
                    // alert('Title and URL copied to clipboard.');
                    console.log('Title and URL copied to clipboard.');
                }, function (err) {
                    // 处理复制失败的情况
                    console.error('Could not copy text: ', err);
                    // alert('Failed to copy Title and URL.');
                });
            });


            // 添加点击事件监听器
            button4.addEventListener('click', async function () {
                try {
                    console.log("点击了进入btn4");
                    // 向background发送消息请求所有标签页的信息
                    chrome.runtime.sendMessage({ method: "getTabs" }, function (response) {
                        console.log(response.tabsInfo); // 这将打印所有标签页的标题和URL
                        var tabs_self = response.tabsInfo;

                        // 使用map创建一个包含所有标签页信息的字符串数组
                        var tabsInfoString = tabs_self.map(function (tab) {
                            return tab.title + " - " + tab.url;
                        }).join("\n"); // 使用join将数组连接成一个字符串，每个信息之间用换行符分隔

                        copyTextToClipboard(tabsInfoString);

                        // 这里是处理tabsInfoString的代码，例如可以将其显示在页面上或进行其他操作
                        // 例如，你可以创建一个文本节点并添加到infos元素中
                        var textNode = document.createTextNode(tabsInfoString);


                        // 创建新的div元素 
                        var infos = document.createElement('div');
                        infos.className = 'infos'; // 添加CSS类名
                        // infos.textContent = 'infos'; // 设置提示文本
                        infos.textContent = tabsInfoString;
                        infos.style.position = 'absolute';

                        infos.style.top = '50%';
                        infos.style.left = '50%';
                        infos.style.transform = 'translate(-50%, -50%)';

                        // infos.style.top = '200px';
                        // infos.style.right = '500px';
                        infos.style.width = '1200px';
                        infos.style.height = '800px';
                        infos.style.backgroundColor = 'rgba(80, 227, 194, 0.55)';
                        infos.style.color = "black";
                        infos.style.borderRadius = "6px";
                        infos.style.padding = "15px";
                        // infos.style.backgroundColor = '#50E3C2';
                        document.body.appendChild(infos); // 将div添加到页面中

                        // 显示提示信息
                        // infos.appendChild(textNode);
                        infos.style.display = 'block';

                        // 一秒后隐藏提示信息并从DOM中移除
                        setTimeout(function () {
                            infos.style.display = 'none'; // 隐藏提示信息
                            infos.parentNode.removeChild(infos); // 从DOM中移除提示信息
                        }, 1000);


                        document.body.appendChild(infos); // 将infos元素添加到页面中

                    });


                } catch (error) {
                    console.error('btn4 无法获取tabs！');
                }
            });

            // 监听键盘事件来触发按钮点击
            document.addEventListener('keydown', function (event) {
                if (event.ctrlKey && event.shiftKey && event.key === '1') {
                    console.log("你触发了btn1！");
                    button.click(); // 触发按钮点击
                    event.preventDefault(); // 防止默认快捷键行为
                }
            });

            // 复制文本到剪贴板的函数
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

            // 设置页面上所有元素的文本可复制
            function makeTextCopyable() {
                const allElements = document.querySelectorAll('*');
                allElements.forEach(element => {
                    element.style.userSelect = 'auto';
                    element.style.webkitUserSelect = 'auto';
                    element.style.MozUserSelect = 'auto';
                    element.style.msUserSelect = 'auto';
                });
            }

            // 在页面加载完毕后执行函数
            document.addEventListener('DOMContentLoaded', makeTextCopyable);

            // text = document.querySelector("#state_4").innerText
            // document.querySelector("#state_4").style.color="red";
            // document.querySelector("#state_4").style.fontSize="30px";
            // document.querySelector("#state_4").innerText = text +" ---> 28号到现在已下架 "+String(parseInt(text)-180801)+" ---> "+ String((parseInt(text)-180801)/10000).slice(0,4)+"w" + " --->  已删除"+ String((957082-parseInt(text))/10000).slice(0,4)+"w"
        }, 500)

    } catch (e) {
        // ...
    }
}


// ==================店小蜜 优化==================
if (window.location.href.startsWith(dianxiaomi_url)) {
    try {
        // <span id="state_4">161900</span>
        setTimeout(() => {
            text = document.querySelector("#state_4").innerText
            document.querySelector("#state_4").style.color = "red";
            document.querySelector("#state_4").style.fontSize = "30px";
            document.querySelector("#state_4").innerText = text + " ---> 28号到现在已下架 " + String(parseInt(text) - 180801) + " ---> " + String((parseInt(text) - 180801) / 10000).slice(0, 4) + "w" + " --->  已删除" + String((957082 - parseInt(text)) / 10000).slice(0, 4) + "w"
        }, 500)

    } catch (e) {
        // ...
    }

}

// ==================虾皮 优化==================
if (window.location.href.startsWith(a_xiapi)) {
    if (window.location.href.startsWith(a_xiapi)) {
        // 按了 快捷键Ctrl+y 执行js  就会添加链接
        setTimeout(() => {
            a_l = Array.from(document.querySelectorAll('a.product-name-wrap'))
            a_l = a_l.map((url) => { return url.getAttribute('href').replace('/portal/product/', '') })
            //like_set = Array.from(document.querySelectorAll('div.product-list-item__td.product-variation__sales div.text-overflow2'))
            //for(var i=0;i<like_set.length;i++){                   product-list-item__td product-variation__sales
            //    like = like_set[i]
            //    like.innerText = like.innerText + '---' +a_l[i]
            //}

            tbody = document.querySelectorAll('tbody')[0]
            console.log("tbody", tbody)
            i = 0
            tbody.querySelectorAll('tr').forEach(function (tr) {
                // 获取当前行的第二个td元素
                var secondTd = tr.children[1];

                // 创建一个新的div元素
                var newDiv = document.createElement('div');

                // 设置div的内容或属性（例如class、id等）
                newDiv.textContent = a_l[i];
                // 或者
                newDiv.className = 'myDivClass';

                // 将新创建的div元素添加到第二个td内部
                secondTd.appendChild(newDiv);
                i++;
            });
        }, 4000)

    }
}

// ==================360doc 优化==================
if (window.location.href.startsWith(a_360_doc_url)) {
    // 快捷键Ctrl+y 执行js
    if (window.location.href.startsWith(a_360_doc_url_edit)) {
        // 按了 快捷键Ctrl+y 执行js  就会添加链接
        document.addEventListener('keydown', function (event) {
            if (event.ctrlKey && event.keyCode === 89) { // 89 是 Y 的 ASCII 码
                document.querySelector("#insertlink").click();
            }
        });
    }


    // if (window.location.href === 'http://www.360doc.com/myfiles.aspx') {
    if (window.location.href.startsWith('http://www.360doc.com/myfiles.aspx')) {

        (async () => {
            await delay(1700);
            console.log("复制链接脚本加载了!!!");

            // 这个就是 复制 a标签
            document.querySelectorAll('div.listmain div.listwz1 a').forEach(a => {
                console.log(a.href);
                console.log(a.innerText);
                const span = document.createElement('span');
                span.innerText = 'Title';
                span.style.color = 'blue';
                span.style.marginLeft = '5px';
                span.style.cursor = 'pointer';

                span.addEventListener('click', () => {
                    // // 创建一个新的 <a> 标签
                    const newLink = document.createElement('a');
                    newLink.href = a.href; // 复制 href
                    newLink.innerText = a.innerText; // 复制文本
                    newLink.target = '_blank'; // 添加 target="_blank" 属性
                    newLink.style.fontSize = '21.33px'; // 设置字号为 16号 字体 
                    // // 去除样式
                    newLink.removeAttribute('class');
                    newLink.removeAttribute('style');
                    // 
                    copy(newLink);
                    // copy(a)
                    console.log(`${a.innerText}`);

                });
                a.insertAdjacentElement('afterend', span);
            });

            // 这个就是 复制 a 文本
            document.querySelectorAll('div.listmain div.listwz1 a').forEach(a => {
                console.log(a.href);
                console.log(a.innerText);
                const span = document.createElement('span');
                span.innerText = 'Link';
                span.style.color = 'blue';
                span.style.marginLeft = '5px';
                span.style.cursor = 'pointer';

                span.addEventListener('click', () => {
                    copyTextToClipboard(a.href);
                    console.log(`${a.href}`);
                });
                a.insertAdjacentElement('afterend', span);
            });
        })();

    }

}



// ================== myshopify 优化==================
if (window.location.href.startsWith(a_myshopify_url)) {
    async function lianxuan_myshopify() {
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
                        if (this.checked) {
                            // checkboxs.eq(i).prop("checked", true);
                            checkboxs.eq(i)[0].click();
                        } else {
                            //checkboxs.eq(i).prop("checked", false);
                        }
                    }
                }
                startChecked = this;
            }
            checkboxs.click(handleCheck);
        }

        $(function () {
            input_set = $('table tr td input.el-checkbox__original')
            enableShiftCheck(input_set);
        });

    }
    lianxuan_myshopify();


    // 实现了 页面上增加几个自动分类的 按钮 方便多了  但是架不住产品数量实在是太多了
    async function fenlei() {
        await delay(ms = 3000);
        let fu = document.querySelectorAll(`section div.el-row.vab-query-form`)[0];  // 链接创建在哪里
        var inp1 = document.querySelectorAll('input.el-input__inner[placeholder="请输入批次号"]')[0]; // 请输入批次号
        var btn1 = find_ele(where = 'button', text = ' 批量变更 ');  // 批量变更  那个按钮

        // 批量变更
        creat_id_copy("复制id|")  // 复制页面  选中状态的商品id
        creat_a(str = '鞋子|', n = 0)
        creat_a(str = '高跟鞋|', n = 1)
        creat_a(str = '运动鞋|', n = 2)
        creat_a(str = '拖鞋|', n = 3)
        creat_a(str = '凉鞋|', n = 4)
        creat_a(str = '帽子|', n = 5)
        creat_a(str = '雨伞|', n = 6)
        creat_a(str = '杂|', n = 7)
        creat_a(str = '手镯|', n = 8)
        creat_a(str = '戒指|', n = 9)
        creat_a(str = '耳环|', n = 10)
        creat_a(str = '项链|', n = 11)
        creat_a(str = '手链|', n = 12)
        creat_a(str = '香水|', n = 13)
        creat_a(str = '围裙|', n = 14)
        creat_a(str = '胸罩配饰|', n = 15)
        creat_a(str = '胸针|', n = 16)
        creat_a(str = '眼镜|', n = 17)
        creat_a(str = '女包|', n = 18)
        creat_a(str = '围巾|', n = 19)
        creat_a(str = '领带|', n = 20)
        creat_a(str = '手套|', n = 21)
        creat_a(str = '健身|', n = 22)
        creat_a(str = '枕头|', n = 23)
        creat_a(str = '篮子|', n = 24)
        creat_a(str = '袜子|', n = 25)
        creat_a(str = '杯子|', n = 26)
        creat_a(str = '胸罩|', n = 27)
        creat_a(str = '比基尼|', n = 28)
        creat_a(str = '手表|', n = 29)
        creat_a(str = '丝袜|', n = 30)
        creat_a(str = '皮带|', n = 31)
        creat_a(str = '皮带扣|', n = 32)
        creat_a(str = '休闲鞋|', n = 33)
        creat_a(str = '靴子|', n = 34)
        creat_a(str = '保暖鞋|', n = 35)
        creat_a(str = '长袖|', n = 36)
        creat_a(str = '短袖|', n = 37)
        creat_a(str = '夹克外套|', n = 38)
        creat_a(str = '长裤|', n = 39)
        creat_a(str = '短裤|', n = 40)
        creat_a(str = '内裤|', n = 41)
        creat_a(str = '内衣|', n = 42)
        creat_a(str = '内衣套装|', n = 43)
        creat_a(str = '牛仔|', n = 44)
        creat_a(str = '保暖衣|', n = 45)
        creat_a(str = '大衣|', n = 46)
        creat_a(str = '瑜伽|', n = 47)
        creat_a(str = '衬衫|', n = 48)
        creat_a(str = '长裙|', n = 49)
        creat_a(str = '短裙|', n = 50)
        creat_a(str = '连体衣|', n = 51)
        creat_a(str = '运动服|', n = 52)
        creat_a(str = '套装|', n = 53)
        creat_a(str = '披肩|', n = 54)
        creat_a(str = '浴袍|', n = 55)
        creat_a(str = '鞋带|', n = 56)
        creat_a(str = '袋子|', n = 57)
        creat_a(str = '黑丝|', n = 58)
        creat_a(str = '头部装饰|', n = 59)
        creat_a(str = '背心薄|', n = 60)
        creat_a(str = '背心厚|', n = 61)
        creat_a(str = '配饰套装|', n = 62)
        creat_a(str = '半身裙|', n = 63)
        creat_a(str = '睡衣|', n = 64)
        creat_a(str = '紧身衣裤|', n = 65)
        creat_a(str = '毛衣|', n = 66)
        creat_a(str = '胸衣|', n = 67)
        creat_a(str = '西服|', n = 68)
        creat_a(str = 'Blazer|', n = 69)
        creat_a(str = '杂|', n = 70)
        creat_a(str = '儿童|', n = 71)



        // input 输入框 赋值函数
        function input_value(input2, value) {
            // input2 = $(str_selector)[0]
            input2.value = value;
            var event2 = document.createEvent('HTMLEvents');
            event2.initEvent("input", true, true);
            event2.eventType = 'message';
            input2.dispatchEvent(event2);
        }

        // 延迟函数
        function delay(ms) {
            return new Promise(resolve => setTimeout(resolve, ms));
        }

        // js字符串包含
        function find_ele(where, text) {
            /**
             * where 是一个元素
             * text 是文本
             */
            // return Array.from(document.querySelectorAll('div.el-form-item__content button')).filter(v => v.textContent.includes('添加'))[0];
            return Array.from(document.querySelectorAll(where)).filter(v => v.textContent.includes(text))[0];
        }

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

        // https://b08-admin.shop6888.com/#/goods/shopWebsiteManagement
        // 这个地方是 网站管理 希望 网址旁边增加打开按钮
        /*
        $('table tbody[tabindex="-1"] tr.el-table__row td span:contains(http)').each(function () {
            // 获取当前 label 的父级的父级元素，通常是 tr
            // var row = $(this).closest('tr');
            // 获取 tr 的第一个单元格的文本，这里假设 id 在第一个单元格中
            // var idText = row.find('td:eq(1)').text();
            // 将获取到的文本添加到 ids 数组中
            // ids.push(idText);
            console.log($(this));
            var span = $(this);
            var text = span.text();
            var url = span.text();
            // 创建一个新的a标签
            var a1 = document.createElement('a');
            // 设置a标签的href属性为span中的文本
            a1.href = text;
            // 设置a标签的目标属性为_blank，以便在新窗口中打开链接
            a1.target = '_blank';
            // 设置a标签的文本内容为span中的文本
            a1.textContent = '|外';
            a1.style.color = 'green'; // 设置文本颜色为绿色
            a1.style.padding = "2px 0px"
            a1.style.textShadow = '1px 1px 2px rgba(0, 0, 0, 0.5)'; // 设置文本阴影


            // 创建一个新的a标签
            var a2 = document.createElement('a');
            // 设置a标签的href属性为span中的文本
            var text2 = $(this).closest('tr').find('.el-table_1_column_3 div').text();
            console.log("text2", text2);
            a2.href = `https://b08.shop6888.com/redirect?websiteid=${text2}`;  // https://b08.shop6888.com/redirect?websiteid=442
            // 设置a标签的目标属性为_blank，以便在新窗口中打开链接
            a2.target = '_blank';
            // 设置a标签的文本内容为span中的文本
            a2.textContent = '/内';
            a2.style.color = 'red'; // 设置文本颜色为红色
            a2.style.padding = "2px 0px"
            a2.style.textShadow = '1px 1px 2px rgba(0, 0, 0, 0.5)'; // 设置文本阴影

            // 创建一个新的a标签
            var a3 = document.createElement('a');
            // 设置a标签的href属性为span中的文本
            console.log("当前url", text);  // 展示链接
            a3.href = '#';  // #
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

            // 第三个链接点击的时候 直接复制当前域名网址
            a3.onclick = async function (event) {
                event.preventDefault(); // 阻止链接的默认行为
                copyTextToClipboard(text = url)
            }

            // 设置鼠标 悬浮颜色
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

            // 将a标签追加到span标签的末尾
            // span[0].appendChild(a);

        });
        */

        // 创建一个 a 获取 选中状态的商品id
        function creat_id_copy(str = "复制id|") {
            var a = document.createElement('a');
            a.href = 'javascript:void(0)';
            a.textContent = str;
            a.style.margin = '2px';

            a.onclick = async function () {
                var ids = [];
                $('table tbody[tabindex="-1"] tr.el-table__row td label.is-checked').each(function () {
                    // 获取当前 label 的父级的父级元素，通常是 tr
                    var row = $(this).closest('tr');
                    // 获取 tr 的第一个单元格的文本，这里假设 id 在第一个单元格中
                    var idText = row.find('td:eq(1)').text();
                    // 将获取到的文本添加到 ids 数组中
                    ids.push(idText);
                });
                console.log('选中id', ids);
                copyTextToClipboard(text = ids)
            }
            fu.appendChild(a);
        }

        // 页面上创建标签
        function creat_a(str, n) {
            // str  创建的a的名字
            // click_v 你想点击到那一层 分类
            var a = document.createElement('a');
            a.href = 'javascript:void(0)';
            a.textContent = str;
            a.style.margin = '2px';

            a.onclick = async function () {
                const copy_text = await navigator.clipboard.readText();
                // 如果能 有勾选的 按照 选择变更来操作
                if ($(`table.el-table__header thead th label>span`).eq(0).hasClass('is-indeterminate') || $(`table.el-table__header thead th label>span`).eq(0).hasClass('is-checked')) {
                    console.log("检测到  选择变更操作");
                    time_wait = 10000
                    ele = `div#app button span:contains(选择变更)` //.click();  // 选择变更
                    await waitForClick(ele, time_wait)
                    await delay(ms = 300);
                    ele = $(`table.el-table__body tbody[tabindex="-1"] tr.el-table__row:contains(分类) td`).eq(0).find(`input`)//.click();  // 勾选单选框
                    ele[0].click()
                    // await waitForClick(ele, time_wait)
                    await delay(ms = 300);
                    ele = $(`table.el-table__body tbody[tabindex="-1"] tr.el-table__row:contains(分类) td`).eq(4).find('input')//.click();  // 请选择
                    ele[0].click()
                    // await waitForClick(ele, time_wait)
                    await delay(ms = 100);
                    ele = `div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(Wait 待定) i`  //.click();  // 待定
                    await waitForClick(ele, time_wait)
                    await delay(ms = 100);
                    鞋子 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(shoes 鞋子) li`)[0]
                    高跟鞋 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b19 高跟鞋) li`)[0]
                    运动鞋 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b16 运动鞋) li`)[0]
                    拖鞋 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b17 拖鞋) li`)[0]
                    凉鞋 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b18 凉鞋) li`)[0]
                    帽子 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b9 帽子) li`)[0]
                    雨伞 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b10 雨伞) li`)[0]
                    杂 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(Za 杂) li`)[0]
                    手镯 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b20 手镯) li`)[0]
                    戒指 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(a9 戒指) li`)[0]
                    耳环 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b1.4 耳环) li`)[0]
                    项链 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b5 项链) li`)[0]
                    手链 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b6 手链) li`)[0]
                    香水 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b7 香水) li`)[0]
                    围裙 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b11 Apron 女士围裙) li`)[0]
                    胸罩配饰 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b12 胸罩配饰) li`)[0]
                    胸针 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b13 胸针) li`)[0]
                    眼镜 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b14 眼镜) li`)[0]
                    女包 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b15 女包) li`)[0]
                    围巾 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b21 围巾) li`)[0]
                    领带 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b22 领带) li`)[0]
                    手套 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b23 手套) li`)[0]
                    健身 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b24 健身) li`)[0]
                    枕头 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b25 枕头) li`)[0]
                    篮子 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b26 篮子) li`)[0]
                    袜子 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b27 袜子) li`)[0]
                    杯子 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b28 杯子) li`)[0]
                    胸罩 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b29 胸罩) li`)[0]
                    比基尼 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b30 比基尼) li`)[0]
                    手表 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b31 手表) li`)[0]
                    丝袜 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b32 丝袜) li`)[0]
                    皮带 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b33 皮带) li`)[0]
                    皮带扣 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b34 皮带扣) li`)[0]
                    休闲鞋 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b35 休闲鞋) li`)[0]
                    靴子 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b36 靴子) li`)[0]
                    保暖鞋 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b37 保暖鞋) li`)[0]
                    长袖 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b38 长袖) li`)[0]
                    短袖 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b39 短袖) li`)[0]
                    夹克外套 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b40 夹克外套) li`)[0]
                    长裤 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b41 长裤) li`)[0]
                    短裤 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b42 短裤) li`)[0]
                    内裤 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b43 内裤) li`)[0]
                    内衣 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b44 内衣) li`)[0]
                    内衣套装 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b45 内衣套装) li`)[0]
                    牛仔 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b46 牛仔) li`)[0]
                    保暖衣 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b47 保暖衣) li`)[0]
                    大衣 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b48 大衣) li`)[0]
                    瑜伽 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b49 瑜伽) li`)[0]
                    衬衫 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b50 衬衫) li`)[0]
                    长裙 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b51 长裙) li`)[0]
                    短裙 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b52 短裙) li`)[0]
                    连体衣 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b53 连体衣) li`)[0]
                    运动服 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b54 运动服) li`)[0]
                    套装 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b55 套装) li`)[0]
                    披肩 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b56 披肩) li`)[0]
                    浴袍 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b57 浴袍) li`)[0]
                    鞋带 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b58 鞋带) li`)[0]
                    袋子 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b59 袋子) li`)[0]
                    黑丝 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b60 黑丝) li`)[0]
                    头部装饰 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b61 头部装饰) li`)[0]
                    背心薄 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b62 背心薄) li`)[0]
                    背心厚 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b63 背心厚) li`)[0]
                    配饰套装 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b64 配饰套装) li`)[0]
                    半身裙 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b65 半身裙) li`)[0]
                    睡衣 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b66 睡衣) li`)[0]
                    紧身衣裤 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b67 紧身衣裤) li`)[0]
                    毛衣 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b68 毛衣) li`)[0]
                    胸衣 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b69 胸衣) li`)[0]
                    西服 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b70 西服) li`)[0]
                    Blazer = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b71 Blazer) li`)[0]
                    杂 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b72 杂) li`)[0]
                    儿童 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b1.1 儿童类) li`)[0]

                    v_l = [鞋子, 高跟鞋, 运动鞋, 拖鞋, 凉鞋, 帽子, 雨伞, 杂, 手镯, 戒指, 耳环, 项链, 手链, 香水, 围裙, 胸罩配饰, 胸针, 眼镜, 女包, 围巾, 领带, 手套, 健身, 枕头, 篮子, 袜子, 杯子, 胸罩, 比基尼,
                        手表, 丝袜, 皮带, 皮带扣, 休闲鞋, 靴子, 保暖鞋, 长袖, 短袖, 夹克外套, 长裤, 短裤, 内裤, 内衣, 内衣套装, 牛仔, 保暖衣, 大衣, 瑜伽, 衬衫, 长裙, 短裙, 连体衣, 运动服, 套装, 披肩, 浴袍, 鞋带,
                        袋子, 黑丝, 头部装饰, 背心薄, 背心厚, 配饰套装, 半身裙, 睡衣, 紧身衣裤, 毛衣, 胸衣, 西服, Blazer, 杂, 儿童
                    ]
                    console.log(v_l[n]);
                    ele = v_l[n]//.click();  // 点击最终目标分类
                    ele.click()

                    await delay(ms = 600);
                    ele = $(`div.el-dialog[tabindex="-1"] footer.el-dialog__footer button:contains(修改)`)[0]//.click();
                    ele.click()

                    await delay(ms = 100);
                    ele = $(`div[aria-label="温馨提示"][role="dialog"] div[tabindex="-1"] button:contains(确定)`)[0]//.click();
                    ele.click()

                }



                // 批量id 操作  能分隔就是批量操作
                else if (copy_text.includes(',')) {
                    console.log("copy_text 包含逗号,有多个id");
                    let id_set = copy_text.split(',');

                    async function processId(id) {
                        console.log("Processing ID: " + id);
                        // let numericId = parseInt(id);
                        // console.log("Numeric ID: " + numericId);
                        // copy_text = id;
                        input_value(input2 = inp1, value = id);  // 批次号 方框赋值
                        await delay(ms = 300);
                        btn1.click(); // 点击批量 变更
                        await delay(ms = 100);

                        // 批量按钮点击之后 你才有这些结构
                        var inp2_str = `form.el-form--label-right tbody[tabindex="-1"] tr.el-table__row`  // 分类界面的选择了
                        inp2_set = document.querySelectorAll(inp2_str)[0].querySelectorAll('input')
                        var dainji_fenlei_input = inp2_set[0]  //  分类单选框
                        var xuanze_leimu_input = inp2_set[2]  //   触发选择类目

                        dainji_fenlei_input.click();  // 勾选了 分类单选框
                        await delay(ms = 100);
                        xuanze_leimu_input.click();   //   触发选择类目
                        await delay(ms = 100);
                        待定 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(Wait 待定) i`)[0]
                        待定.click();  // 点击 待定  
                        await delay(ms = 100);
                        鞋子 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(shoes 鞋子) li`)[0]
                        高跟鞋 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b19 高跟鞋) li`)[0]
                        运动鞋 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b16 运动鞋) li`)[0]
                        拖鞋 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b17 拖鞋) li`)[0]
                        凉鞋 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b18 凉鞋) li`)[0]
                        帽子 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b9 帽子) li`)[0]
                        雨伞 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b10 雨伞) li`)[0]
                        杂 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(Za 杂) li`)[0]
                        手镯 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b20 手镯) li`)[0]
                        戒指 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(a9 戒指) li`)[0]
                        耳环 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b1.4 耳环) li`)[0]
                        项链 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b5 项链) li`)[0]
                        手链 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b6 手链) li`)[0]
                        香水 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b7 香水) li`)[0]
                        围裙 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b11 Apron 女士围裙) li`)[0]
                        胸罩配饰 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b12 胸罩配饰) li`)[0]
                        胸针 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b13 胸针) li`)[0]
                        眼镜 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b14 眼镜) li`)[0]
                        女包 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b15 女包) li`)[0]
                        围巾 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b21 围巾) li`)[0]
                        领带 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b22 领带) li`)[0]
                        手套 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b23 手套) li`)[0]
                        健身 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b24 健身) li`)[0]
                        枕头 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b25 枕头) li`)[0]
                        篮子 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b26 篮子) li`)[0]
                        袜子 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b27 袜子) li`)[0]
                        杯子 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b28 杯子) li`)[0]
                        胸罩 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b29 胸罩) li`)[0]
                        比基尼 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b30 比基尼) li`)[0]
                        手表 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b31 手表) li`)[0]
                        丝袜 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b32 丝袜) li`)[0]
                        皮带 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b33 皮带) li`)[0]
                        皮带扣 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b34 皮带扣) li`)[0]
                        休闲鞋 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b35 休闲鞋) li`)[0]
                        靴子 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b36 靴子) li`)[0]
                        保暖鞋 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b37 保暖鞋) li`)[0]
                        长袖 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b38 长袖) li`)[0]
                        短袖 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b39 短袖) li`)[0]
                        夹克外套 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b40 夹克外套) li`)[0]
                        长裤 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b41 长裤) li`)[0]
                        短裤 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b42 短裤) li`)[0]
                        内裤 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b43 内裤) li`)[0]
                        内衣 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b44 内衣) li`)[0]
                        内衣套装 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b45 内衣套装) li`)[0]
                        牛仔 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b46 牛仔) li`)[0]
                        保暖衣 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b47 保暖衣) li`)[0]
                        大衣 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b48 大衣) li`)[0]
                        瑜伽 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b49 瑜伽) li`)[0]
                        衬衫 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b50 衬衫) li`)[0]
                        长裙 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b51 长裙) li`)[0]
                        短裙 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b52 短裙) li`)[0]
                        连体衣 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b53 连体衣) li`)[0]
                        运动服 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b54 运动服) li`)[0]
                        套装 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b55 套装) li`)[0]
                        披肩 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b56 披肩) li`)[0]
                        浴袍 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b57 浴袍) li`)[0]
                        鞋带 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b58 鞋带) li`)[0]
                        袋子 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b59 袋子) li`)[0]
                        黑丝 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b60 黑丝) li`)[0]

                        v_l = [鞋子, 高跟鞋, 运动鞋, 拖鞋, 凉鞋, 帽子, 雨伞, 杂, 手镯, 戒指, 耳环, 项链, 手链, 香水, 围裙, 胸罩配饰, 胸针, 眼镜, 女包, 围巾, 领带, 手套, 健身, 枕头, 篮子, 袜子, 杯子, 胸罩, 比基尼,
                            手表, 丝袜, 皮带, 皮带扣, 休闲鞋, 靴子, 保暖鞋, 长袖, 短袖, 夹克外套, 长裤, 短裤, 内裤, 内衣, 内衣套装, 牛仔, 保暖衣, 大衣, 瑜伽, 衬衫, 长裙, 短裙, 连体衣, 运动服, 套装, 披肩, 浴袍, 鞋带,
                            袋子, 黑丝
                        ]
                        console.log(v_l[n]);
                        v_l[n].click();  // 点击最终目标分类
                        await delay(ms = 100);
                        $(`div.el-dialog[tabindex="-1"] footer.el-dialog__footer button:contains(修改)`)[0].click();
                        await delay(ms = 100);
                        $(`div[aria-label="温馨提示"][role="dialog"] div[tabindex="-1"] button:contains(确定)`)[0].click();
                        await delay(ms = 150);
                    }

                    // 这个并不能阻塞
                    // id_set.forEach(await processId);
                    // 使用 for...of 循环来等待每个异步操作完成
                    async function processAllIds() {
                        for (let id of id_set) {
                            await processId(id);
                        }
                    }

                    // 调用 processAllIds 函数
                    processAllIds();


                    // 单个id 操作
                }

                // 没法分隔的  一次性操作一个   (copy_text.includes(',')===false)
                else {
                    console.log("copy_text 不包含逗号,就一个id");
                    // alert('剪贴板内容: ' + text);
                    input_value(input2 = inp1, value = copy_text);  // 输入批次号
                    await delay(ms = 300);

                    btn1.click();  // 批量变更
                    await delay(ms = 100);
                    // 批量按钮点击之后 你才有这些结构
                    var inp2_str = `form.el-form--label-right tbody[tabindex="-1"] tr.el-table__row`  // 分类界面的选择了
                    inp2_set = document.querySelectorAll(inp2_str)[0].querySelectorAll('input')
                    var dainji_fenlei_input = inp2_set[0]  //  分类单选框
                    var xuanze_leimu_input = inp2_set[2]  //   触发选择类目

                    dainji_fenlei_input.click();  // 勾选了 分类单选框
                    await delay(ms = 100);
                    xuanze_leimu_input.click();   //   触发选择类目
                    await delay(ms = 100);
                    待定 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(Wait 待定) i`)[0]
                    待定.click();  // 点击 待定  
                    await delay(ms = 100);
                    鞋子 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(shoes 鞋子) li`)[0]
                    高跟鞋 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b19 高跟鞋) li`)[0]
                    运动鞋 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b16 运动鞋) li`)[0]
                    拖鞋 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b17 拖鞋) li`)[0]
                    凉鞋 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b18 凉鞋) li`)[0]
                    帽子 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b9 帽子) li`)[0]
                    雨伞 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b10 雨伞) li`)[0]
                    杂 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(Za 杂) li`)[0]
                    手镯 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b20 手镯) li`)[0]
                    戒指 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(a9 戒指) li`)[0]
                    耳环 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b1.4 耳环) li`)[0]
                    项链 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b5 项链) li`)[0]
                    手链 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b6 手链) li`)[0]
                    香水 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b7 香水) li`)[0]
                    围裙 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b11 Apron 女士围裙) li`)[0]
                    胸罩配饰 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b12 胸罩配饰) li`)[0]
                    胸针 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b13 胸针) li`)[0]
                    眼镜 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b14 眼镜) li`)[0]
                    女包 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b15 女包) li`)[0]
                    围巾 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b21 围巾) li`)[0]
                    领带 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b22 领带) li`)[0]
                    手套 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b23 手套) li`)[0]
                    健身 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b24 健身) li`)[0]
                    枕头 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b25 枕头) li`)[0]
                    篮子 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b26 篮子) li`)[0]
                    袜子 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b27 袜子) li`)[0]
                    杯子 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b28 杯子) li`)[0]
                    胸罩 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b29 胸罩) li`)[0]
                    比基尼 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b30 比基尼) li`)[0]
                    手表 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b31 手表) li`)[0]
                    丝袜 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b32 丝袜) li`)[0]
                    皮带 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b33 皮带) li`)[0]
                    皮带扣 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b34 皮带扣) li`)[0]
                    休闲鞋 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b35 休闲鞋) li`)[0]
                    靴子 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b36 靴子) li`)[0]
                    保暖鞋 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b37 保暖鞋) li`)[0]
                    长袖 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b38 长袖) li`)[0]
                    短袖 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b39 短袖) li`)[0]
                    夹克外套 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b40 夹克外套) li`)[0]
                    长裤 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b41 长裤) li`)[0]
                    短裤 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b42 短裤) li`)[0]
                    内裤 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b43 内裤) li`)[0]
                    内衣 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b44 内衣) li`)[0]
                    内衣套装 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b45 内衣套装) li`)[0]
                    牛仔 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b46 牛仔) li`)[0]
                    保暖衣 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b47 保暖衣) li`)[0]
                    大衣 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b48 大衣) li`)[0]
                    瑜伽 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b49 瑜伽) li`)[0]
                    衬衫 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b50 衬衫) li`)[0]
                    长裙 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b51 长裙) li`)[0]
                    短裙 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b52 短裙) li`)[0]
                    连体衣 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b53 连体衣) li`)[0]
                    运动服 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b54 运动服) li`)[0]
                    套装 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b55 套装) li`)[0]
                    披肩 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b56 披肩) li`)[0]
                    浴袍 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b57 浴袍) li`)[0]
                    鞋带 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b58 鞋带) li`)[0]
                    袋子 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b59 袋子) li`)[0]
                    黑丝 = $(`div[aria-hidden="false"] div.el-tree div[role="treeitem"][tabindex="-1"] div.el-tree-node__content:contains(b60 黑丝) li`)[0]

                    v_l = [鞋子, 高跟鞋, 运动鞋, 拖鞋, 凉鞋, 帽子, 雨伞, 杂, 手镯, 戒指, 耳环, 项链, 手链, 香水, 围裙, 胸罩配饰, 胸针, 眼镜, 女包, 围巾, 领带, 手套, 健身, 枕头, 篮子, 袜子, 杯子, 胸罩, 比基尼,
                        手表, 丝袜, 皮带, 皮带扣, 休闲鞋, 靴子, 保暖鞋, 长袖, 短袖, 夹克外套, 长裤, 短裤, 内裤, 内衣, 内衣套装, 牛仔, 保暖衣, 大衣, 瑜伽, 衬衫, 长裙, 短裙, 连体衣, 运动服, 套装, 披肩, 浴袍, 鞋带,
                        袋子, 黑丝
                    ]
                    console.log(v_l[n]);
                    v_l[n].click();  // 点击最终目标分类
                    await delay(ms = 100);
                    $(`div.el-dialog[tabindex="-1"] footer.el-dialog__footer button:contains(修改)`)[0].click();
                    await delay(ms = 100);
                    $(`div[aria-label="温馨提示"][role="dialog"] div[tabindex="-1"] button:contains(确定)`)[0].click();
                }


            };

            // document.body.appendChild(a);    
            fu.appendChild(a);
        }


    }

    fenlei()
}