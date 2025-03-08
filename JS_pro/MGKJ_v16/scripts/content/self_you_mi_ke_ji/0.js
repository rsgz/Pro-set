// 延迟函数
function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// 随机数组元素
function getRandomElement(arr) {
    // getRandomElement(arr=title_l_bras)
    if (arr && arr.length) {
        const randomIndex = Math.floor(Math.random() * arr.length);
        return arr[randomIndex];
    } else {
        return null; // 或者抛出错误，取决于你的需求
    }
}

// textarea 赋值函数
function textarea_value(textarea2, value) {
    textarea2.value = value;
    var event2 = document.createEvent('Event');
    event2.initEvent('input', true, true);
    textarea2.dispatchEvent(event2);
}

// input 输入框 赋值函数
function input_value(input2, value) {
    // input2 = $(str_selector)[0]
    input2.value = value;
    var event2 = document.createEvent('HTMLEvents');
    event2.initEvent("input", true, true);
    event2.eventType = 'message';
    input2.dispatchEvent(event2);
}
// 注入
inject_jq = () => {
    var script = document.createElement('script');
    script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
    script.id = 'script_jq_0'
    document.getElementsByTagName('head')[0].appendChild(script);
}

// 移除
remove_jq = () => {
    jq = document.getElementById('script_jq_0')
    document.head.removeChild(jq);
}

(async () => {
    // 先进入这个界面
    start = 514
    // 🌸 🍁 🍄 🐥 🍓 🍅 🍑 🦞 🧊 🏺 🔥 ☀️ 🎀 🎉 
    // 🧡 💛 💚 ❤️ 💙 💜 🤎 🖤 🤍 👾 
    beizhu = '2024-12-19 星期四 💚 模板15'
    mingcheng_miaoshu = '女内衣'
    zuojige = 8
    muban_set = {
        14: [(1500, 321), (1000, 550), (1500, 234), (700, 700), (1500, 325), (950, 650)]
    }
    muban = 14

    inject_jq();

    muban_l = muban_set.get(14)
    for (var i = 0; i < muban_l; i++) {
        kuan = muban_l[i][0]
        gao = muban_l[i][1]
        mingcheng = `${kuan}*${gao}`

        await delay(ms = 300);
        if (i === 0) {
            $(`div.business-ps-functional-zone__button:contains(新建项目)`)[0].click()
            $(`button:contains(文件)`)[0].click()
            await delay(ms = 300);
        } else {
            btn = $(`button:contains(文件)`)[0].click()
            // 或者触发一个点击事件
            var event = new MouseEvent('click', {
                'view': window,
                'bubbles': true,
                'cancelable': true
            });
            // 使用原生JavaScript尝试点击
            btn.dispatchEvent(event);
        }


        input1 = $(`span.fitem.rangedropinput label:contains(宽度:)`).parent().find(`input`)[0]
        input_value(input1, kuan)
        await delay(ms = 300);
        input1 = $(`span.fitem.rangedropinput label:contains(高度:)`).parent().find(`input`)[0]
        input_value(input1, gao)
        await delay(ms = 300);
        input1 = $(`span.fitem.rangedropinput label:contains(名称:)`).parent().find(`input`)[0]
        input_value(input1, mingcheng)
        await delay(ms = 300);
        $(`button.fitem.spread.bbtn:contains(创建)`)[0].click()
        await delay(ms = 700);
    }



    /*    
    for (var i = 1; i <= zuojige; i++) {
    
        await delay(ms = 100);
        // 打开编辑
        $(`table tbody tr td:contains(${start})`).filter(function () {
            return $(this).text().trim() === `${start}`;
        }).parent().find(`td:eq(11)`).find(`button span:contains(编辑)`).click();
        await delay(ms = 200);
        // 输入框
        input1 = $(`div[role="dialog"] div[tabindex="-1"] div.el-dialog__body form.el-form--label-right div label:contains(备注)`).parent().find('input')
    
        input_value(input2 = input1[0], value = beizhu)
        await delay(ms = 100);
    
        // 名称描述 输入框
        input2 = $(`div[role="dialog"] div[tabindex="-1"] div.el-dialog__body form.el-form--label-right div label:contains(名称/描述)`).parent().find('input')
        input_value(input2 = input2[0], value = mingcheng_miaoshu + (8 - i + 1))
        await delay(ms = 100);
    
        button1 = $(`div[role="dialog"] div[tabindex="-1"] footer button:contains(保存)`).click()
        start++;
    }
        */
    await delay(ms = 300);
    remove_jq();
})();