# key_words = "myshopify_shichangjia_xiugai"
# url = "https://b08-admin.shop6888.com/#/goods/shopWebsiteManagement"
# des = "市场价"

key_words = "qita_rsgz_biying_sousuo_yuming_jeiguo_qingkong_result"
url = "xxx"
des = "必应域名抓取"


popup_html = f"""↓↓↓↓↓↓↓ popup.html ↓↓↓↓↓↓↓
<span class="a" target="_blank" id="{key_words}">{des}</span>|
"""

content_js = f"""↓↓↓↓↓↓↓ content.js ↓↓↓↓↓↓↓
        if(request.{key_words}==="{key_words}"){{
            console.log("request.{key_words}");
            async function f1() {{
                try {{
                    $("input[value='  Generate  ']").click();
                    await delay(300);
                    $x_span_city = $("p:contains('City, State, Zip: ')").find('span').text();
                    console.log("$x_span_city:", $x_span_city);

                    $x_span_street = $("p:contains('Street: ')").find('span').text();
                    console.log("$x_span_street:", $x_span_street);

                    $x_span_country = $("p:contains('Country: ')").find('span').text();
                    console.log("$x_span_country:", $x_span_country);

                    $x_span_telephone = $("p:contains('Telephone: ')").find('span').text();
                    console.log("$x_span_telephone:", "+1 "+$x_span_telephone);

                    const txt1 = $x_span_city.trim()+','+$x_span_street.trim()+','+$x_span_country.trim()+';'+'+1 '+$x_span_telephone;
                    copyTextToClipboard(txt1);

                }} catch (error) {{
                    console.error("出现错误:", error);
                }}
            }}

            f1();
        }}
"""

popup_js = f"""↓↓↓↓↓↓↓ popup.js ↓↓↓↓↓↓↓
// 沟通 ---> content.js
$("#{key_words}").click(()=>{{send_to_content(message={{{key_words}:"{key_words}"}})}});  // {key_words} ---> {"content.js"}

// 沟通 --->service-worker.js
$("#{key_words}").click(()=>{{chrome.runtime.sendMessage({{{key_words}:"{key_words}"}});}});  // {key_words} ---> {"service-worker.js"}
"""

service_worker_js = f"""↓↓↓↓↓↓↓ service-worker.js ↓↓↓↓↓↓↓
    // {key_words}
    if(request.{key_words}==="{key_words}"){{
        chrome.tabs.create({{ url: '{url}' }});
        console.log('进入{url}')
    }}
"""

if __name__ == '__main__':
    print(popup_html)
    print(content_js)
    print(popup_js)
    print(service_worker_js)