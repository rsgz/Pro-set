$(() => {
    // ========== 抓取Bing域名===========
    // 2025-03-05  抓取Bing域名
    let isRunning = false;
    let results = [];
    function extractDomains() {
        if (!isRunning) return;
        const domainElements = document.querySelectorAll('cite');
        domainElements.forEach(element => {
            let domain = element.textContent;
            if (domain) {
                const index = domain.indexOf('›');
                if (index > -1) {
                    domain = domain.substring(0, index).trim();
                }
                // console.log("必应domain:", ...domain.slice(Math.max(0, domain.length - 5), domain.length));
                results.push(domain);
            }
        });
        chrome.storage.local.set({ results: results }, function () {
            // console.log('域名已经保存:', results);
            //console.log(`域名已经保存!!!----->${results.length}`);
            console.log(`域名已经保存!!!----->${results.length}`);
        });
        const nextButton = document.querySelector('.sb_pagN');
        if (nextButton) {
            setTimeout(() => {
                nextButton.click();
                setTimeout(extractDomains, 2000); // 延迟 2 秒后继续
            }, 4000); // 延迟 1 秒后点击
        } else {
            isRunning = false;
            console.log('Extraction complete.');
        }
    }

    // 这个是一个信息 专门用来判断 是开始抓取 还是 停止抓取
    window.addEventListener('message', function (event) {
        if (event.source !== window) return;
        if (event.data.type === 'START_EXTRACTION') {
            isRunning = true;
            results = [];
            extractDomains();
            console.log('开始抓取!');
        } else if (event.data.type === 'STOP_EXTRACTION') {
            isRunning = false;
            console.log('Extraction stopped.  停止抓取');
        } else if (event.data.type === 'CLEAR_RESULTS') { // 添加清空消息的处理
            results = [];
            chrome.storage.local.set({ results: [] }, function () {
                console.log('Results cleared. 抓取结果清空');
            });
        }
    });


    // 任何网站都执行
    chrome.runtime.onMessage.addListener(async function (request, sender, sendResponse) {


        // 复制谷歌cite
        if (request.qita_rsgz_fuzhi_guge_cite === "qita_rsgz_fuzhi_guge_cite") {
            console.log("request.qita_rsgz_fuzhi_guge_cite");
            async function f1() {
                try {
                    // 获取谷歌cite 标签里面的文本 因为里面包含了网址 然后再来切割一下 > 这是特征符号 最后得到 纯净的网址 
                    function getGoogleSearchResultsFromCite() {
                        const results = [];
                        const citeElements = document.querySelectorAll('cite');
                        citeElements.forEach(cite => {
                            let url = cite.textContent;
                            if (url) {
                                const index = url.indexOf('›');
                                if (index > -1) {
                                    url = url.substring(0, index).trim();
                                }
                                results.push(url);
                            }
                        });
                        return results;
                    }
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
                    // 获取搜索结果并转换为字符串
                    const searchResults = getGoogleSearchResultsFromCite();
                    const resultsString = searchResults.join('\n'); // 使用换行符分隔每个URL
                    // 复制到剪贴板
                    copyTextToClipboard(resultsString);
                    console.log("搜索结果已复制到剪贴板");

                } catch (error) {
                    console.error("出现错误:", error);
                }
            }

            f1();
        }

        // 清除缓存
        if (request.qita_rsgz_qingchu_huancun === "qita_rsgz_qingchu_huancun") {
            console.log("request.qita_rsgz_qingchu_huancun");
            async function f1() {
                try {
                    localStorage.clear();
                    console.log("清除 Local Storage.");
                    sessionStorage.clear();
                    console.log("清除 Session Storage");
                    document.cookie.split(";").forEach(cookie => {
                        const cookieName = cookie.split("=")[0].trim();
                        document.cookie = `${cookieName}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/`;
                    });
                    console.log("清除 Cookies");
                    console.log("清除 IndexedDB");
                    (async () => {
                        const databases = await window.indexedDB.databases();
                        for (const db of databases) {
                            const request = indexedDB.deleteDatabase(db.name);
                            request.onsuccess = () => console.log(`Deleted IndexedDB: ${db.name}`);
                            request.onerror = () => console.error(`Failed to delete IndexedDB: ${db.name}`);
                        }
                    })();

                } catch (error) {
                    console.error("出现错误:", error);
                }
            }

            f1();
        }

        // 任意网页修改
        if (request.others_2024_8_27_renyi_xiugai === "others_2024_8_27_renyi_xiugai") {
            console.log("request.others_2024_8_27_renyi_xiugai");
            (async () => {
                console.log('执行 others.js');
                console.log('当前网页内容可随意修改!');
                document.body.contentEditable = 'true';
            })();
        }

        // 禁止修改
        if (request.others_2024_8_27_buke_xiugai === "others_2024_8_27_buke_xiugai") {
            console.log("request.others_2024_8_27_buke_xiugai");
            (async () => {
                console.log('执行 others.js');
                console.log('网页内容不可修改!');
                document.body.contentEditable = 'false';
            })();
        }

        // 更换背景
        if (request.others_2024_8_27_genggai_beijing_tu === "others_2024_8_27_genggai_beijing_tu") {
            console.log("request.others_2024_8_27_genggai_beijing_tu");
            (async () => {
                console.log('执行 others.js');
                console.log('更改网页背景图!');

                $('*').each(function () {
                    $(this).css('background-color', 'transparent');
                });

                // 随机图片
                // let n_index=Math.ceil(Math.random()*20); // 1--10 随机整数
                // let n_index=Math.ceil(Math.random()*20); // 1--10 随机整数
                const imgUrl = chrome.runtime.getURL(`images/bg_body/${n_index}.jpg`);
                console.log(imgUrl);

                // $('body:eq(0)').css('background-image', `url(images/bg_body/${n_index}.jpg)`);  // GET https://www.remove.bg/images/bg_body/2.jpg 404 (Not Found)
                $('body:eq(0)').css('background-image', `url(${imgUrl})`);  // chrome-extension://adgoedbokpojecgmcepihcjbghlehgnf/images/bg_body/2.jpg

                // others.js:30 Uncaught (in promise) TypeError: chrome.extension.getURL is not a function   content.js不能使用这个接口？？
                // const imgUrl = chrome.extension.getURL(`../../../images/bg_body/${n_index}.jpg`);


            })();
        }

        // 复制文本
        if (request.ohter_fuzhi_wenben === "ohter_fuzhi_wenben") {
            console.log("request.ohter_fuzhi_wenben");
            let s = `var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
document.getElementsByTagName('head')[0].appendChild(script);

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
}`
            console.log(s);
            copyTextToClipboard(s);
        }



    })
});



