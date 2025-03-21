console.log("popup.js 已加载!!!")
const DXM01_SELECTOR = "input[value='dxm01']";
const merchant_SELECTOR = "input[value='merchant01']";
const ozon_SELECTOR = "input[value='ozon01']";
const rsgz_SELECTOR = "input[value='rsgz01']";
const dxm02 = "div.dxm02";


// 获取选项卡标签和内容元素
const tabLabels = document.querySelectorAll('.tabs label');
const tabContents = document.querySelectorAll('.tab-content');



// 为选项卡标签添加点击事件监听器
$(function () {
    tabLabels.forEach((label, index) => {
        label.addEventListener('click', () => {
            // 切换选项卡的选中状态
            tabLabels.forEach((label) => {
                label.classList.remove('selected');
            });
            label.classList.add('selected');

            // 切换对应选项卡内容的显示状态
            tabContents.forEach((content) => {
                content.classList.remove('active');
            });
            tabContents[index].classList.add('active');

            // 保存最后一次点击的选项卡
            chrome.storage.sync.set({ lastTab: index });
        });
    });
});

// 实现input历史恢复内容
$(function () {
    window.addEventListener('load', function () {
        console.log("popup.js 已加载")
        // alert("popup.js 已加载")
        try {
            // 监听所有input元素的change事件
            var inputs = document.querySelectorAll('input');
            console.log("inputs", inputs)
            for (var i = 0; i < inputs.length; i++) {
                var inputType = inputs[i].type;
                // console.log("inputType",inputType)
                if (inputType === 'text' || inputType === 'radio' || inputType === 'checkbox') {
                    inputs[i].addEventListener('input', handleInputChange);
                }
            }

            // 处理input元素改变的事件
            function handleInputChange(event) {
                // 获取所有input元素的状态，并保存到chrome.storage
                var inputsData = {};
                for (var i = 0; i < inputs.length; i++) {
                    var inputType = inputs[i].type;
                    var inputValue;
                    if (inputType === 'radio' || inputType === 'checkbox') {
                        inputValue = inputs[i].checked;
                    } else {
                        inputValue = inputs[i].value;
                    }
                    inputsData[inputs[i].id] = inputValue;
                    // console.log("inputs[i]",inputs[i],"点击动作被保存")
                }
                chrome.storage.sync.set({ inputs: inputsData }, function () {
                    console.log("inputs 键 保存成功!!!");
                });
            }

            // 恢复最近一次保存的input元素状态
            chrome.storage.sync.get(['inputs'], function (result) {
                var inputsData = result.inputs;
                if (inputsData) {
                    for (var id in inputsData) {
                        var inputType = document.getElementById(id).type;
                        if (inputType === 'radio' || inputType === 'checkbox') {
                            document.getElementById(id).checked = inputsData[id];
                        } else {
                            document.getElementById(id).value = inputsData[id];
                        }
                    }
                }
            });
        } catch (err) {
            console.log(err);
        }
    });
});

// 先复原Timu
// $(function(){
//     $("#a0020").click()
// });

// 恢复选项卡 补bug
// 加载最后一次点击的选项卡
chrome.storage.sync.get('lastTab', (data) => {
    const lastTab = data.lastTab;

    // 恢复最后一次点击的选项卡页面
    if (lastTab >= 0 && lastTab < tabLabels.length) {
        tabLabels.forEach((label) => {
            label.classList.remove('selected');
        });
        tabLabels[lastTab].classList.add('selected');

        tabContents.forEach((content) => {
            content.classList.remove('active');
        });
        tabContents[lastTab].classList.add('active');
    }
});

// ---------------------------------------------店小蜜---------------------------------------------
// 页首
$(function () {
    document.getElementById("yeshou").addEventListener("click", function () {
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            chrome.tabs.sendMessage(tabs[0].id, {
                action: "to_yeshou"
            });
        });
    });
});


// 页末
$(function () {
    document.getElementById("yemo").addEventListener("click", function () {
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            chrome.tabs.sendMessage(tabs[0].id, {
                action: "to_yemo"
            });
        });
    });
});


// 点击抓取数据
$(function () {
    document.getElementById("data_grap1").addEventListener("click", function () {
        //  alert("你点击了 抓取数据按钮")
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            var the_pic = false;
            var the_title = false;
            var the_productId = false;
            var the_shops = false;
            var the_level = false;
            var the_ren_ming = false;
            var the_shanghu_id = false;
            var the_sale = false;
            var the_fusku01 = false;
            var the_creat_time = false;
            var the_update_time = false;
            var the_audit_status = false;


            if (document.querySelector("input[name='pic']").checked) {
                the_pic = true;
            }
            if (document.querySelector("input[name='title']").checked) {
                the_title = true;
            }
            if (document.querySelector("input[name='prodoctId']").checked) {
                the_productId = true
            }
            if (document.querySelector("input[name='shops']").checked) {
                the_shops = true
            }
            if (document.querySelector("input[name='level']").checked) {
                the_level = true
            }
            if (document.querySelector("input[name='ren_ming']").checked) {
                the_ren_ming = true
            }
            if (document.querySelector("input[name='shanghu_id']").checked) {
                the_shanghu_id = true
            }
            if (document.querySelector("input[name='sale']").checked) {
                the_sale = true
            }
            if (document.querySelector("input[name='fusku01']").checked) {
                the_fusku01 = true
            }
            if (document.querySelector("input[name='creat_time']").checked) {
                the_creat_time = true
            }
            if (document.querySelector("input[name='update_time']").checked) {
                the_update_time = true
            }
            if (document.querySelector("input[name='audit_status']").checked) {
                the_audit_status = true
            }

            chrome.tabs.sendMessage(tabs[0].id, {
                action: "do_drap_data",
                pic: the_pic,
                title: the_title,
                id: the_productId,
                shop_name: the_shops,
                shop_level: the_level,
                ren_ming: the_ren_ming,
                shanghu_id: the_shanghu_id,
                sale: the_sale,
                fu_sku: the_fusku01,
                creat_time: the_creat_time,
                update_time: the_update_time,
                audit_status: the_audit_status
            });
        });
    });
});


// 点击广告按钮
$(function () {
    document.getElementById("advertising").addEventListener("click", function () {
        //  alert("你点击了 抓取数据按钮")
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            var clothing_type_value = document.getElementById("clothing_type").value;
            var startData_value = document.getElementById("startData").value;
            var endData_value = document.getElementById("endData").value;
            //    alert("发送了三个参数:clothing_type_value", clothing_type_value)

            chrome.tabs.sendMessage(tabs[0].id, {
                action: "do_advertising",
                clothing_type: clothing_type_value,
                startData: startData_value,
                endData: endData_value
            });
        });
    });
});


// 点击复制广告
$(function () {
    document.getElementById("advertisingCopy").addEventListener("click", function () {
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            //    var clothing_type_value = document.getElementById("clothing_type").value;
            //    var startData_value = document.getElementById("startData").value;
            //    var endData_value = document.getElementById("endData").value;
            //    alert("发送了三个参数:clothing_type_value", clothing_type_value)

            chrome.tabs.sendMessage(tabs[0].id, {
                action: "advertisingCopy"
            });
        });
    });
});


// 点击删除广告
$(function () {
    document.getElementById("advertisingDel").addEventListener("click", function () {
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            //    var clothing_type_value = document.getElementById("clothing_type").value;
            //    var startData_value = document.getElementById("startData").value;
            //    var endData_value = document.getElementById("endData").value;
            chrome.tabs.sendMessage(tabs[0].id, {
                action: "advertisingDel"
            });
        });
    });
});


// 配置广告词
$(function () {
    document.getElementById("advertisingDisposition").addEventListener("click", e => {
        window.open("../html/ad_keyword.html");
    });
});


// 替换sku
$(function () {
    document.getElementById("tihuan1").addEventListener("click", function () {
        //  alert("你点击了 抓取数据按钮")
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            var lao_sku_value = document.getElementById("lao_sku").value;
            var xin_sku_value = document.getElementById("xin_sku").value;
            //    alert("发送了三个参数:clothing_type_value", clothing_type_value)

            chrome.tabs.sendMessage(tabs[0].id, {
                action: "do_tihuan_sku",
                lao_sku_value: lao_sku_value,
                xin_sku_value: xin_sku_value
            });
        });
    });
});



// ---------------------------------------------360doc---------------------------------------------
// 进入撰写
// $(function(){
//     $("#360_write_1").click(function (){
//         window.open("http://www.360doc.com/edit/writeartnew.aspx");
//     });
// });

// 添加样式
$(function () {

    // ---> content.js
    $("#ohter_fuzhi_wenben").click(() => { send_to_content(message = { ohter_fuzhi_wenben: "ohter_fuzhi_wenben" }) });  // ohter_fuzhi_wenben ---> content.js
    $("#others_2024_8_27_genggai_beijing_tu").click(() => { send_to_content(message = { others_2024_8_27_genggai_beijing_tu: "others_2024_8_27_genggai_beijing_tu" }) });  // others_2024_8_27_genggai_beijing_tu ---> content.js
    $("#others_2024_8_27_buke_xiugai").click(() => { send_to_content(message = { others_2024_8_27_buke_xiugai: "others_2024_8_27_buke_xiugai" }) });  // others_2024_8_27_buke_xiugai ---> content.js
    $("#others_2024_8_27_renyi_xiugai").click(() => { send_to_content(message = { others_2024_8_27_renyi_xiugai: "others_2024_8_27_renyi_xiugai" }) });  // others_2024_8_27_renyi_xiugai ---> content.js

    $("#add_style_360").click(function () {
        console.log("--->")
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            // var title = "标题";
            // var description = "描述";
            var title = prompt()
            // var content = prompt()
            var content = title;  // 2024-10-30 修改一下  就是让标题和 content 内容一致 省得输入两次
            console.log("--->")
            chrome.tabs.sendMessage(tabs[0].id, { title: title, content: content, instruct: "add" });
            // chrome.runtime.sendMessage({title: title, description: description});
        });
    });

    $("#siyou_360doc").click(function () {
        console.log("--->")
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            // var title = "标题";
            // var description = "描述";
            var title = prompt()
            // var content = prompt()
            var content = title;  // 2024-10-30 修改一下  就是让标题和 content 内容一致 省得输入两次
            console.log("--->")
            chrome.tabs.sendMessage(tabs[0].id, { title: title, content: content, instruct: "siyou_360doc" });
            // chrome.runtime.sendMessage({title: title, description: description});
        });
    });

    $("#caogaoxiang_360").click(() => { send_to_content(message = { caogao: "caogao" }) });  // 草稿
    $("#shouyi_360").click(() => { send_to_content(message = { shouyi: "shouyi" }) });  // 收益
    // $("#360_write_1").click(()=>{send_to_content(message={to_360doc:"to_360doc"})});  // 进入360doc
});

// ---------------------------------------------wishpost---------------------------------------------
// wishpost
$(function () {
    // $("#wishpost_1").click(()=>{send_to_content(message={to_wishpost:"to_wishpost"})});  // 登录
    $("#wishpost_2").click(() => { send_to_content(message = { denglu: "wishpost" }) });  // 登录
    $("#wishpost_3").click(() => { send_to_content(message = { shensu: "shensu" }) });  // 申诉
    $("#wishpost_4").click(() => { send_to_content(message = { lishiyunfei: "lishiyunfei" }) });  // 查价格
    $("#wishpost_5").click(() => { send_to_content(message = { pingguyunfei: "pingguyunfei" }) });  // 查价格
});


// ---------------------------------------------myshopify---------------------------------------------
$(function () {
    // 我这边主动发送消息
    // 在 popup.html 中获取输入值并发送消息
    // const fanwei0 = $("#myshopify_wangzhan_bianhao_fanwei01")[0].value;
    // const fanwei_start0 = fanwei0.trim().split('-')[0];
    // const fanwei_end0 = fanwei0.trim().split('-')[1];

    // chrome.runtime.sendMessage({ fanwei_end0,fanwei_start0 }, function(response) {
    //     console.log('Message sent to content.js fanwei_start0 fanwei_end0');
    // });

    // 下面都是触发事件才发送消息
    // 沟通 ---> content.js
    // 这个是 单个站点库存精简


    $("#myshopify_tianjia_pingbici").click(() => {
        const key_paichu = $("#myshopify_paichu_key")[0].value;
        send_to_content(message = { myshopify_tianjia_pingbici: "myshopify_tianjia_pingbici", key_paichu })
    });  // myshopify_tianjia_pingbici ---> content.js  添加多个屏蔽关键词 
    $("#myshopify_fuzhi_shangyici_caidan").click(() => {
        const fanwei = $("#myshopify_wangzhan_bianhao_fanwei01")[0].value;
        const fanwei_start = fanwei.trim().split('-')[0];
        const fanwei_end = fanwei.trim().split('-')[1];
        send_to_content(message = { myshopify_fuzhi_shangyici_caidan: "myshopify_fuzhi_shangyici_caidan", fanwei_start, fanwei_end })
    });  // myshopify_fuzhi_shangyici_caidan ---> content.js
    $("#myshopify_zengjia_dakai_anniu").click(() => { send_to_content(message = { myshopify_zengjia_dakai_anniu: "myshopify_zengjia_dakai_anniu" }) });  // myshopify_zengjia_dakai_anniu ---> content.js
    $("#myshopify_lian_xuan_chan_ping").click(() => { send_to_content(message = { myshopify_lian_xuan_chan_ping: "myshopify_lian_xuan_chan_ping" }) });  // myshopify_lian_xuan_chan_ping ---> content.js  shift连选产品
    $("#myshopify_qiehuan_zalei_leimu").click(() => { send_to_content(message = { myshopify_qiehuan_zalei_leimu: "myshopify_qiehuan_zalei_leimu" }) });  // myshopify_qiehuan_zalei_leimu ---> content.js  一键把类目切换到杂类
    $("#myshopify_dange_wangzhan_kucun_kucun_shaixuan").click(() => { send_to_content(message = { myshopify_dange_wangzhan_kucun_kucun_shaixuan: "myshopify_dange_wangzhan_kucun_kucun_shaixuan" }) });  // myshopify_dange_wangzhan_kucun_kucun_shaixuan ---> content.js
    $("#myshopify_dange_wangzhan_kucun_kucun_shaixuan2").click(() => { send_to_content(message = { myshopify_dange_wangzhan_kucun_kucun_shaixuan2: "myshopify_dange_wangzhan_kucun_kucun_shaixuan2" }) });  // myshopify_dange_wangzhan_kucun_kucun_shaixuan ---> content.js
    $("#myshopify_huoqu_leimu_lujing").click(() => { send_to_content(message = { myshopify_huoqu_leimu_lujing: "myshopify_huoqu_leimu_lujing" }) });  // myshopify_huoqu_leimu_lujing ---> content.js
    $("#myshopify_tianjia_kucun_xuhao").click(() => { send_to_content(message = { myshopify_tianjia_kucun_xuhao: "myshopify_tianjia_kucun_xuhao" }) });  // myshopify_tianjia_kucun_xuhao ---> content.js
    // 沟通 ---> content.js
    $("#myshopify_kucun_lianxuan").click(() => {
        const xuanze_fanwei = $("#myshopify_kucun_lianxuan_fanwei")[0].value;
        send_to_content(message = { myshopify_kucun_lianxuan: "myshopify_kucun_lianxuan", xuanze_fanwei })
    });  // myshopify_kucun_lianxuan ---> content.js
    $("#myshopify_guolv_dianji").click(() => {
        const key_paichu = $("#myshopify_paichu_key")[0].value;
        send_to_content(message = { myshopify_guolv_dianji: "myshopify_guolv_dianji", key_paichu })
    });  // myshopify_guolv_dianji ---> content.js
    // ---> content.js
    $("#myshopify_yijian_daoru_caidan").click(() => {
        const fanwei = $("#myshopify_wangzhan_bianhao_fanwei01")[0].value;
        const fanwei_start = fanwei.trim().split('-')[0];
        const fanwei_end = fanwei.trim().split('-')[1];
        send_to_content(message = { myshopify_yijian_daoru_caidan: "myshopify_yijian_daoru_caidan", fanwei_start, fanwei_end })
    });  // myshopify_yijian_daoru_caidan ---> content.js

    $("#myshopify_shoujia_xiugai_70_120").click(() => { send_to_content(message = { myshopify_shoujia_xiugai_70_120: "myshopify_shoujia_xiugai_70_120" }) });  // myshopify_shoujia_xiugai ---> content.js
    $("#myshopify_shoujia_xiugai_35_39").click(() => { send_to_content(message = { myshopify_shoujia_xiugai_35_39: "myshopify_shoujia_xiugai_35_39" }) });  // myshopify_shoujia_xiugai ---> content.js
    $("#myshopify_shoujia_xiugai_27_33").click(() => { send_to_content(message = { myshopify_shoujia_xiugai_27_33: "myshopify_shoujia_xiugai_27_33" }) });  // myshopify_shoujia_xiugai ---> content.js
    $("#myshopify_shoujia_xiugai_30_38").click(() => { send_to_content(message = { myshopify_shoujia_xiugai_30_38: "myshopify_shoujia_xiugai_30_38" }) });  // myshopify_shoujia_xiugai ---> content.js
    $("#myshopify_shoujia_xiugai_38_50").click(() => { send_to_content(message = { myshopify_shoujia_xiugai_38_50: "myshopify_shoujia_xiugai_38_50" }) });  // myshopify_shoujia_xiugai ---> content.js
    $("#myshopify_shoujia_xiugai_55_77").click(() => { send_to_content(message = { myshopify_shoujia_xiugai_55_77: "myshopify_shoujia_xiugai_55_77" }) });  // myshopify_shoujia_xiugai ---> content.js
    $("#myshopify_shoujia_xiugai_45_77").click(() => { send_to_content(message = { myshopify_shoujia_xiugai_45_77: "myshopify_shoujia_xiugai_45_77" }) });  // myshopify_shoujia_xiugai ---> content.js
    $("#myshopify_shoujia_xiugai_55_99").click(() => { send_to_content(message = { myshopify_shoujia_xiugai_55_99: "myshopify_shoujia_xiugai_55_99" }) });  // myshopify_shoujia_xiugai ---> content.js
    // $("#myshopify_shoujia_xiugai").click(()=>{send_to_content(message={myshopify_shoujia_xiugai:"myshopify_shoujia_xiugai"})});  // myshopify_shoujia_xiugai ---> content.js
    $("#myshopify_shichangjia_xiugai").click(() => { send_to_content(message = { myshopify_shichangjia_xiugai: "myshopify_shichangjia_xiugai" }) });  // myshopify_shichangjia_xiugai ---> content.js
    $("#myshopify_2024_8_29_myshopify_guge_gengduo_btn_click").click(() => { send_to_content(message = { myshopify_2024_8_29_myshopify_guge_gengduo_btn_click: "myshopify_2024_8_29_myshopify_guge_gengduo_btn_click" }) });  // myshopify_2024_8_29_myshopify_guge_gengduo_btn_click ---> content.js
    $("#myshopify_2024_8_29_myshopify_wangzhi_renyi").click(() => { send_to_content(message = { myshopify_2024_8_29_myshopify_wangzhi_renyi: "myshopify_2024_8_29_myshopify_wangzhi_renyi" }) });  // myshopify_2024_8_29_myshopify_wangzhi_renyi ---> content.js
    $("#myshopify_2024_8_29_kucun_da").click(() => { send_to_content(message = { myshopify_2024_8_29_kucun_da: "myshopify_2024_8_29_kucun_da" }) });  // myshopify_2024_8_29_kucun_da ---> content.js
    $("#myshopify_2024_8_29_kucun_xiao").click(() => { send_to_content(message = { myshopify_2024_8_29_kucun_xiao: "myshopify_2024_8_29_kucun_xiao" }) });  // myshopify_2024_8_29_kucun_xiao ---> content.js
    $("#myshopify_zhuru_jq").click(() => { send_to_content(message = { myshopify_zhuru_jq: "myshopify_zhuru_jq" }) });  // myshopify_zhuru_jq ---> content.js
    $("#myshopify_huoqu_shenfen").click(() => { send_to_content(message = { myshopify_huoqu_shenfen: "myshopify_huoqu_shenfen" }) });  // myshopify_huoqu_shenfen
    $("#myshopify_piliang_tian_jia_yu_ming").click(() => { send_to_content(message = { myshopify_piliang_tian_jia_yu_ming: "myshopify_piliang_tian_jia_yu_ming" }) });  // myshopify_piliang_tian_jia_yu_ming ---> content.js
    $("#myshopify_xuanze_fenlei").click(() => { send_to_content(message = { myshopify_xuanze_fenlei: "myshopify_xuanze_fenlei" }) });  // myshopify_xuanze_fenlei ---> content.js
    $("#myshopify_you_dain_gaoshi").click(() => { send_to_content(message = { myshopify_you_dain_gaoshi: "myshopify_you_dain_gaoshi" }) });  // myshopify_you_dain_gaoshi ---> content.js
    $("#myshopify_tian_jia_jing_tai").click(() => {
        const fanwei = $("#myshopify_wangzhan_bianhao_fanwei01")[0].value;
        const fanwei_start = fanwei.trim().split('-')[0];
        const fanwei_end = fanwei.trim().split('-')[1];
        send_to_content(message = { myshopify_tian_jia_jing_tai: "myshopify_tian_jia_jing_tai", fanwei_start, fanwei_end })
    });  // myshopify_tian_jia_jing_tai ---> content.js
    $("#myshopify_wenzhang_guanli_dibu_caidan").click(() => {
        const fanwei = $("#myshopify_wangzhan_bianhao_fanwei01")[0].value;
        const fanwei_start = fanwei.trim().split('-')[0];
        const fanwei_end = fanwei.trim().split('-')[1];
        send_to_content(message = { myshopify_wenzhang_guanli_dibu_caidan: "myshopify_wenzhang_guanli_dibu_caidan", fanwei_start, fanwei_end })
    });  // myshopify_wenzhang_guanli_dibu_caidan ---> content.js

    $("#myshopify_an_fen_lei_dao_ru_shang_ping").click(() => {
        const fanwei = $("#myshopify_wangzhan_bianhao_fanwei01")[0].value;
        const fanwei_start = fanwei.trim().split('-')[0];
        const fanwei_end = fanwei.trim().split('-')[1];
        send_to_content(message = { myshopify_an_fen_lei_dao_ru_shang_ping: "myshopify_an_fen_lei_dao_ru_shang_ping", fanwei_start, fanwei_end })
    });  // myshopify_an_fen_lei_dao_ru_shang_ping ---> content.js
    $("#myshopify_zhuo_se").click(() => {
        const fanwei = $("#myshopify_wangzhan_bianhao_fanwei01")[0].value;
        const fanwei_start = fanwei.trim().split('-')[0];
        const fanwei_end = fanwei.trim().split('-')[1];
        send_to_content(message = { myshopify_zhuo_se: "myshopify_zhuo_se", fanwei_start, fanwei_end })
    });  // myshopify_zhuo_se ---> content.js
    $("#myshopify_yuming_bianhao").click(() => {
        const fanwei = $("#myshopify_wangzhan_bianhao_fanwei01")[0].value;
        const fanwei_start = fanwei.trim().split('-')[0];
        const fanwei_end = fanwei.trim().split('-')[1];
        send_to_content(message = { myshopify_yuming_bianhao: "myshopify_yuming_bianhao", fanwei_start, fanwei_end })
    });  // myshopify_yuming_bianhao ---> content.js

    $("#myshopify_shangpingdaoru_jingtaiguanli_zhuose").click(() => { send_to_content(message = { myshopify_shangpingdaoru_jingtaiguanli_zhuose: "myshopify_shangpingdaoru_jingtaiguanli_zhuose" }) });  // myshopify_shangpingdaoru_jingtaiguanli_zhuose ---> content.js


    // ---> service-worker.js
    $("#myshopify_neibu_yulan").click(() => { chrome.runtime.sendMessage({ myshopify_neibu_yulan: "myshopify_neibu_yulan" }); });  // myshopify_neibu_yulan ---> service-worker.js
    $("#myshopify_jin_ru_kucun").click(() => { chrome.runtime.sendMessage({ myshopify_jin_ru_kucun: "myshopify_jin_ru_kucun" }); });  // myshopify_jin_ru_kucun ---> service-worker.js
    $("#myshopify_jin_ru_wang_zhan_guan_li").click(() => { chrome.runtime.sendMessage({ myshopify_jin_ru_wang_zhan_guan_li: "myshopify_jin_ru_wang_zhan_guan_li" }); });  // myshopify_jin_ru_wang_zhan_guan_li ---> service-worker.js
    $("#myshopify_shangping_shuliang").click(() => {
        const fanwei = $("#myshopify_wangzhan_bianhao_fanwei01")[0].value;
        const fanwei_start = fanwei.trim().split('-')[0];
        const fanwei_end = fanwei.trim().split('-')[1];
        chrome.runtime.sendMessage({ myshopify_shangping_shuliang: "myshopify_shangping_shuliang", fanwei_start, fanwei_end });
    });  // myshopify_shangping_shuliang ---> service-worker.js

    $("#myshopify_waibu_yulan").click(() => {
        const fanwei = $("#myshopify_wangzhan_bianhao_fanwei01")[0].value;
        const fanwei_start = fanwei.trim().split('-')[0];
        const fanwei_end = fanwei.trim().split('-')[1];
        chrome.runtime.sendMessage({ myshopify_waibu_yulan: "myshopify_waibu_yulan", fanwei_start, fanwei_end });
    });  // myshopify_waibu_yulan ---> service-worker.js

    // 这是网站 上传数据的配置文件
    $("#myshopify_peizhi").click(() => { window.open("../html/myshopify_shop6888_peizhi.html"); });

});

// ---------------------------------------------虾皮---------------------------------------------
$(function () {
    $("#xiapi_2").click(() => { send_to_content(message = { xiapi2: "xiapi2" }) });  // 广告搜索关键词
    $("#xiapi_3").click(() => { send_to_content(message = { xiapi3: "xiapi3" }) });  // 关键词搜索量
    $("#xiapi_4").click(() => { send_to_content(message = { xiapi4: "xiapi4" }) });  // 站点关键词
    $("#xiapi_5").click(() => { send_to_content(message = { xiapi5: "xiapi5" }) });  // 店铺产品 获取信息
    $("#xiapi_6").click(() => {
        xiapi6 = $("#xiapi_price1")[0].value; // 设置虾皮价格
        send_to_content(message = { xiapi6: "xiapi6", xiapi6_input: xiapi6 });
    });  // 设置虾皮价格

    // ---------------------------------------------拼多多---------------------------------------------
    $("#pinduoduo_2").click(() => { send_to_content(message = { pinduoduo_2: "pinduoduo_2" }) });  // 复制拼多多商品图
    // ---------------------------------------------1688---------------------------------------------
    $("#1688_rsgz_2").click(() => { send_to_content(message = { a1688_rsgz_2: "a1688_rsgz_2" }) });  // 复制1688商品图1
    $("#1688_rsgz_3").click(() => { send_to_content(message = { a1688_rsgz_3: "a1688_rsgz_3" }) });  // 复制1688商品图2

    // ---------------------------------------------抖音---------------------------------------------
    $("#douyin_rsgz_2").click(() => { send_to_content(message = { douyin_rsgz_2: "douyin_rsgz_2" }) });  // 抖音1

});
// ---------------------------------------------店小蜜客服---------------------------------------------
$(function () {
    // $("#wishpost_1").click(()=>{send_to_content(message={to_wishpost:"to_wishpost"})});  // 登录
    $("#dian_1").click(() => { chrome.runtime.sendMessage({ kefu: "dian_kefu" }) });  // 客服
    $("#dian_2").click(() => { send_to_content(message = { daifabu: "dian_daifabu" }) });  // 待发布
    $("#dian_3").click(() => { send_to_content(message = { zaixian_pro: "dian_zaixian_pro" }) });  // 在线产品
    $("#dian_4").click(() => { send_to_content(message = { d: "d" }) });  // ...
    $("#dian_8").click(() => { send_to_content(message = { dxm_xiajia_wish: "dxm_xiajia_shaixuan" }) });  // 高级筛选
    $("#dian_5").click(() => { send_to_content(message = { dxm_xiajia_wish: "dxm_xiajia_ce0" }) });  // 测试销量是否为0
    $("#dian_6").click(() => { send_to_content(message = { dxm_xiajia_wish: "dxm_xiajia_xiajia" }) });  // 下架操作
    $("#dian_7").click(() => { send_to_content(message = { dxm_xiajia_wish: "dxm_xiajia_xiayiye" }) });  // 下一页
    $("#dian_9").click(() => { send_to_content(message = { dxm_xiajia_wish: "dxm_xiajia_300" }) });  // 300分页
    $("#dian_10").click(() => { send_to_content(message = { dxm_xiajia_wish: "dxm_xiajia_3xia" }) });  // 300分页
    $("#dian_11").click(() => { send_to_content(message = { dxm_xiajia_wish: "dxm_xiajia_3del" }) });  // 300分页 删除产品

    $("#dxm_id_kefu_1").click(() => { sendText_kefu('Hello, how can I help you?') });  // ...
    $("#dxm_id_kefu_2").click(() => { sendText_kefu('My pleasure.') });  // ...
    $("#dxm_id_kefu_3").click(() => { sendText_kefu('I\'m very sorry for the wait.') });  // ...
    $("#dxm_id_kefu_4").click(() => { sendText_kefu('Which product are you looking at? Can you send me a picture or other iconic information? I\'m having a problem with the backend and I can\'t see your product.') });  // ...
    $("#dxm_id_kefu_5").click(() => { sendText_kefu('God bless you!') });  // ...
    $("#dxm_id_kefu_6").click(() => { sendText_kefu('God bless you! I wish you a happy life!') });  // ...
    $("#dxm_id_kefu_7").click(() => { sendText_kefu('You can refer to the size chart below, they are measured in centimeters.') });  // ...
    $("#dxm_id_kefu_8").click(() => { sendText_kefu('We recommend that you measure your bust Oh, our unit is centimeters!') });  // ...
    $("#dxm_id_kefu_9").click(() => { sendText_kefu('We recommend that you measure your waist Oh, our unit is centimeters!') });  // ...
    $("#dxm_id_kefu_10").click(() => { sendText_kefu('to bring you trouble, I am very sorry') });  // ...
    $("#dxm_id_kefu_11").click(() => { sendText_kefu('Hello, you can rest assured that the general day of the order on the same day to start shipping, please wait patiently Oh.') });  // ...
    $("#dxm_id_kefu_12").click(() => { sendText_kefu('Hello, thank you for your patience Oh, your products have been shipped Oh, just logistics information will be delayed!') });  // ...
    $("#dxm_id_kefu_13").click(() => { sendText_kefu('Hello, generally the day of the order on the same day began shipping, due to cross-border transportation, the business can not remotely interfere with the logistics of the package, please understand that you can Oh!') });  // ...
    $("#dxm_id_kefu_14").click(() => { sendText_kefu('Hello, the way to set up the delivery address is wish platform constraints Oh, this merchant can not help you. Please communicate with other wish consumers to see if there are other solutions') });  // ...
    $("#dxm_id_kefu_15").click(() => { sendText_kefu('This garment is made of polyester fiber.') });  // ...
    $("#dxm_id_kefu_16").click(() => { sendText_kefu('You can refer to the price Oh, does not include shipping costs') });  // ...
    $("#dxm_id_kefu_17").click(() => { sendText_kefu('The reason for this is that the price of the product itself does not include shipping costs. The reason for this is that the price of the product itself does not include shipping costs, and the higher price is due to the addition of cross-border shipping costs.') });  // ...
    $("#dxm_id_kefu_18").click(() => { sendText_kefu('Hello, it usually shows the currency of the country you are in') });  // ...
    $("#dxm_id_kefu_19").click(() => { sendText_kefu('Shipping part, when you choose to pay the corresponding shipping costs will be detailed Oh!') });  // ...
    $("#dxm_id_kefu_20").click(() => { sendText_kefu('The current Wish platform payment methods are PayPal, AllPay, Linkage Payment (UMPAY)') });  // ...
    $("#dxm_id_kefu_21").click(() => { sendText_kefu('Hello, due to the problem of translation software, I did not understand what you mean, I\'m very sorry, this is the translation software to bring trouble, please understand more oh, can you try to change the language or easy to understand words it!') });  // ...
    $("#dxm_id_kefu_22").click(() => { sendText_kefu('Hello, some of the customers\' products are not displaying the product information in the background of wish. There are some unknown bugs, so in order to be able to provide the correct information, please send the wish product link to me, this side will give the product related help information.') });  // ...
    $("#dxm_id_kefu_23").click(() => { sendText_kefu('You first enter the product page to select the size and then select the color click on Add to Cart You can buy!') });  // ...
    $("#dxm_id_kefu_24").click(() => { sendText_kefu('Hello, our sets are sold separately Oh!') });  // ...
    $("#dxm_id_kefu_25").click(() => { sendText_kefu('Hello, you can choose 2pic said tops and bottoms of a set, if you choose only 1pic said a top or pants, you can carefully check the time to buy Choose the size of the time there will be prompts Oh!') });  // ...
    $("#dxm_id_kefu_26").click(() => { sendText_kefu('Hello, very understand your feelings, but this side does not recommend that you refund Oh. The value of the long-distance postage has exceeded the value of a dress, if you do not like can be gifted to their friends Oh, harvest a sincere friendship. Leave a true love on earth') });  // ...
    $("#dxm_id_kefu_27").click(() => { sendText_kefu('Maybe your situation is more complicated, this side in thinking of a solution, please be patient Oh!') });  // ...
    $("#dxm_id_kefu_28").click(() => { sendText_kefu('Hello, can you provide a logistics single number and product pictures to prove it, the trouble you caused, I\'m very sorry!') });  // ...

});

// 发送客服
function sendText_kefu(text) {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        chrome.tabs.sendMessage(tabs[0].id, { dxm_kefu_text: text });
    });
}

// --------------------------------------------- Timu ---------------------------------------------
$(function () {
    // 开始结束 抢发货台
    $("#a0024").click(() => {
        const jiange_kaishi_v = $("#a0022")[0].value;  // 点击频率
        const jiange_jieshu_v = $("#a0023")[0].value;
        const runtime_v = $("#a0026")[0].value;  // 开始运行时间
        const taihao_v = $("#a0029")[0].value;  // 台号
        console.log(jiange_kaishi_v, jiange_jieshu_v, taihao_v)
        send_to_content(message = { fahuotai1: "qiang", jiange_kaishi: jiange_kaishi_v, jiange_jieshu: jiange_jieshu_v, runtime: runtime_v, taihao: taihao_v });
    });  //   抢发货台
    $("#a0025").click(() => {
        console.log({ fahuotai2: "qiang_stop" })
        send_to_content(message = { fahuotai2: "qiang_stop" });
    });  // 结束发货台

    // 自动发货
    $("#a0027").click(() => { send_to_content(message = { fahuo1: "fahuo" }); });  // 确认自动发货
    // $("#a0028").click(()=>{send_to_content(message={fahuo2:"fahuo_stop"});});  // 停止自动发货

    // 进入一些相关链接
    $("#timu_1").click(() => { chrome.runtime.sendMessage({ to_timu1: "to_timu1" }); });  // 后台 
    $("#timu_2").click(() => { chrome.runtime.sendMessage({ to_timu2: "to_timu2" }); });  // 普通备货单
    $("#timu_3").click(() => { chrome.runtime.sendMessage({ to_timu3: "to_timu3" }); });  // 发货台
    $("#a0038").click(() => { send_to_content(message = { temu_paihangbang1: "temu_paihangbang1" }); });  // 排行榜数据
});

// --------------------------------------------- merchant ---------------------------------------------
$(function () {
    $("#a0030").click(() => {
        var huilv = $("#a0033")[0].value;
        console.log("当前汇率:", huilv);
        send_to_content({ wish_1: "SIZE XS", hui: huilv });
    });    // size xs
    $("#a0031").click(() => {
        var huilv = $("#a0033")[0].value;
        console.log("当前汇率:", huilv);
        send_to_content({ wish_2: "SIZE 70cm", hui: huilv });
    });  // size 70cm
    $("#a0032").click(() => {
        var huilv = $("#a0033")[0].value;
        console.log("当前汇率:", huilv);
        send_to_content({ wish_3: "SIZE 70", hui: huilv });
    });    // size 70

    $("#a0034").click(() => {
        send_to_content({ baimiao_biao: "copy" });
    });    // 复制 图片转表格
});

// --------------------------------------------- 芒果店长 ---------------------------------------------
// 订单-已发货页面
$(function () {
    $("#mangguo_8").click(() => { send_to_content(message = { fahuo1: "yifahuo_wish" }) });  // 已发货
    $("#mangguo_2").click(() => { send_to_content(message = { pingtai: "wish_wish" }) });  // 平台 wish
    $("#mangguo_12").click(() => { send_to_content(message = { pingtai: "ozon_wish" }) });  // 平台 ozon
    $("#mangguo_9").click(() => { send_to_content(message = { dayin_time: "today_wish" }) });  // 今天
    $("#mangguo_4").click(() => { send_to_content(message = { dayin_time: "yesterday_wish" }) });  // 昨天
    $("#mangguo_3").click(() => { send_to_content(message = { dayin_time: "1month_wish" }) });  // 近1个月
    $("#mangguo_10").click(() => { send_to_content(message = { dayin_time: "2month_wish" }) });  // 近2个月
    $("#mangguo_11").click(() => { send_to_content(message = { dayin_time: "3month_wish" }) });  // 近3个月
    $("#mangguo_5").click(() => { send_to_content(message = { order_status: "tuikuan_wish" }) });  // 已退款
    $("#mangguo_6").click(() => { send_to_content(message = { order_status: "daichuli_wish" }) });  // 待处理
    $("#mangguo_13").click(() => { send_to_content(message = { baoguo_ozon: "daochu" }) });  // 导出
    $("#mangguo_14").click(() => { send_to_content(message = { fahuo_time_mangguo: "wu" }) });  // 发货时间 叉掉
    $("#mangguo_15").click(() => { send_to_content(message = { jiazaishuju_mangguo: "jiazaishuju_all" }) });  // 加载全部数据
    $("#mangguo_16").click(() => { send_to_content(message = { diaji_red_mangguo: "diaji_red_mangguo_40" }) });  // 低价小于40
    $("#mangguo_17").click(() => { send_to_content(message = { diaji_red_mangguo: "diaji_red_mangguo_50" }) });  // 低价小于50
    $("#mangguo_18").click(() => { send_to_content(message = { diaji_red_mangguo: "diaji_red_mangguo_80" }) });  // 低价小于50
    $("#mangguo_19").click(() => { send_to_content(message = { wish_excel_daoru: "wish_excel_daoru" }) });  // 导入excel
    $("#mangguo_20").click(() => { send_to_content(message = { wish_btn_xuanzefenlei: "wish_btn_xuanzefenlei" }) });  // 选择产品分类
    $("#mangguo_21").click(() => { send_to_content(message = { wish_btn_zidongyunfei: "wish_btn_zidongyunfei" }) });  // 自动运费
    $("#mangguo_22").click(() => { send_to_content(message = { wish_guojiayunfei: "wish_guojiayunfei" }) });  // 自动运费
    $("#mangguo_23").click(() => { send_to_content(message = { wish_quanxin: "wish_quanxin" }) });  // 全新
    $("#mangguo_24").click(() => {
        const ke = $("#a0017")[0].value;
        send_to_content(message = { wish_wuliu1: "wish_wuliu1", ke: ke })
    });  // 物流1
    $("#mangguo_25").click(() => { send_to_content(message = { wish_pic_all: "wish_pic_all" }) });  // 所有图片
    $("#mangguo_26").click(() => {
        const color_num = $("#a0018")[0].value;
        const xpath1 = $("#a0019")[0].value;
        send_to_content(message = {
            wish_yingyongchicun_color_num: color_num,
            wish_yingyongchicun_xpath1: xpath1,
            wish_size_yingyong_all: "wish_size_yingyong_all"
        })
    });  // 应用尺寸
    $("#mangguo_27").click(() => { send_to_content(message = { wish_pic_dansetu: "wish_pic_dansetu" }) });  // 单色图
    $("#mangguo_28").click(() => {
        const gao = $("#a0028")[0].value;
        const di = $("#a0035")[0].value;
        const wish_xpath_3XL = $("#a0036")[0].value;
        const color_num2 = $("#a0018")[0].value;
        send_to_content(message = {
            wish_size_3XL_8XL: "wish_size_3XL_8XL",
            wish_size_3XL_8XL_gao_weight: gao,
            wish_size_3XL_8XL_di_weight: di,
            wish_xpath_3XL: wish_xpath_3XL,
            color_num2: color_num2
        })
    });  // 3XL-8XL高重
    $("#mangguo_29").click(() => { send_to_content(message = { wish3XL: "wish3XL" }) });  // 滑动至wish3XL
    $("#mangguo_30").click(() => { send_to_content(message = { wish_yemo: "wish_yemo" }) });  // 滑动至页末

    // --------------------------------------------- 其他 ---------------------------------------------
    $("#xiazai_douyin").click(() => { send_to_content(message = { douyin_url: "douyin_url" }) });  // 下载抖音
    // 沟通 ---> content.js
    $("#qita_rsgz_fuzhi_guge_cite").click(() => { send_to_content(message = { qita_rsgz_fuzhi_guge_cite: "qita_rsgz_fuzhi_guge_cite" }) });  // qita_rsgz_fuzhi_guge_cite ---> content.js
    $("#qita_rsgz_qingchu_huancun").click(() => { send_to_content(message = { qita_rsgz_qingchu_huancun: "qita_rsgz_qingchu_huancun" }) });  // qita_rsgz_qingchu_huancun ---> content.js
    // $("#qita_rsgz_dakai_zhantieban_lianjie").click(() => { send_to_content(message = { qita_rsgz_dakai_zhantieban_lianjie: "qita_rsgz_dakai_zhantieban_lianjie" }) });  // qita_rsgz_dakai_zhantieban_lianjie ---> content.js
    // 读取 粘贴板 链接 然后批量打开  =============== 谷歌===============
    document.getElementById('qita_rsgz_dakai_zhantieban_lianjie').addEventListener('click', () => {
        navigator.clipboard.readText().then(text => {
            const urls = text.split('\n').filter(url => url.trim() !== '');
            urls.forEach(url => {
                chrome.tabs.create({ url: url.trim() });
            });
        }).catch(err => {
            console.error('无法读取剪贴板：', err);
        });
    });

    // 复制地址栏上面所有标签 =============== 谷歌/必应 ===============
    //$("#qita_rsgz_fuzhi_dizhilan_lianjie")
    const copyButton = document.getElementById('qita_rsgz_fuzhi_dizhilan_lianjie');

    copyButton.addEventListener('click', function () {
        chrome.tabs.query({}, function (tabs) {
            const tabData = tabs.map(tab => `${tab.title}:::${tab.url}`).join('\n');
            console.log(tabData);
            navigator.clipboard.writeText(tabData).then(() => {
                console.log('网址和标题已复制到剪贴板！');
            }, (err) => {
                console.error('无法复制到剪贴板：', err);
            });
        });
    });

    // =============== 必应抓取域名 ===============
    const startButton = document.getElementById('qita_rsgz_biying_sousuo_yuming_zhuaqu'); // qita_rsgz_biying_sousuo_yuming_zhuaqu 开始抓取域名
    const stopButton = document.getElementById('qita_rsgz_biying_sousuo_yuming_zhuaqu_stop');  // qita_rsgz_biying_sousuo_yuming_zhuaqu_stop  停止抓取域名 
    let isRunning = false;

    startButton.addEventListener('click', function () {
        isRunning = true;
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            chrome.scripting.executeScript({
                target: { tabId: tabs[0].id },
                function: startExtraction
            });
        });
    });

    stopButton.addEventListener('click', function () {
        isRunning = false;
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            chrome.scripting.executeScript({
                target: { tabId: tabs[0].id },
                function: stopExtraction
            });
        });
    });

    function startExtraction() {
        window.postMessage({ type: 'START_EXTRACTION' }, '*');
    }

    function stopExtraction() {
        window.postMessage({ type: 'STOP_EXTRACTION' }, '*');
    }
    // =============== 必应域名下载 到本地 results.json ===============
    // 主要是 获取 chrome.storage.local.get  这些数据存储 
    document.getElementById('qita_rsgz_biying_sousuo_yuming_jeiguo_xiazai_bendi').addEventListener('click', function () {
        chrome.storage.local.get(['results'], function (data) {
            const jsonData = JSON.stringify(data.results, null, 2);
            const blob = new Blob([jsonData], { type: 'application/json' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'results.json';
            a.click();
            URL.revokeObjectURL(url);
        });
    });

    // =============== 必应域名 清空  ===============
    const clearButton = document.getElementById('qita_rsgz_biying_sousuo_yuming_jeiguo_qingkong_result'); // 获取清空按钮

    clearButton.addEventListener('click', function () { // 添加清空按钮的点击事件
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            chrome.scripting.executeScript({
                target: { tabId: tabs[0].id },
                function: clearResults
            });
        });
    });

    function clearResults() { // 添加清空函数
        window.postMessage({ type: 'CLEAR_RESULTS' }, '*');
    }

    // =============== 其他部分 可能是下载什么东西 忘记了 ===============
    $("#xiazai").click(() => {
        chrome.runtime.sendMessage({ xiazai: "xiazai" }, function (response) {
            console.log(response);
        });
    });  // 实验下载

});
