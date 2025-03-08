inject_jq = () => {
    var script = document.createElement('script');
    script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
    script.id = 'script_jq_0'
    document.getElementsByTagName('head')[0].appendChild(script);
}
inject_jq()

var $iframe =$('#demo-iframe');
var $iframeContent =$iframe.contents();
var $muban_set =$iframeContent.find('div.data-block');
for(var i=0;i<$muban_set.length;i++){
    console.log(i);
    
    // 模板名字
    muban_name= $muban_set.eq(i).find(`i:contains(模块)`)[0].innerText
    console.log(muban_name);
    // 
    pic_size_l = $muban_set.eq(i).find(`div.ad-items div.pic i`)
    for(var j=0;j<pic_size_l.length;j++){
        pic_size=pic_size_l.eq(j)[0].innerText
        console.log(pic_size);
    }
}
