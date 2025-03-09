// 获取 start-end的随机数 包含 start end
function get_rand_int_num(start, end) {
    return Math.floor(
        Math.random() * (end - start + 1)
    ) + start
}

//  picsum.photos  图片占位服务
// https://picsum.photos/id/1023/200/300
// `https://picsum.photos/id/${num}/200/300`
// document.body.style.backgroundImage = `./images/${num}.webp`  // 本地写法

let num = get_rand_int_num(1, 1000)
// 引用网络的 picsum
// document.body.style.backgroundImage = `url(https://picsum.photos/id/${num}/200/300)`  // 可以显示
// document.body.style.backgroundImage = `url(https://picsum.photos/id/${num}/800/800)`  // 可以
document.body.style.backgroundImage = `url(https://picsum.photos/id/${num}/1920/920)`  // 可以 1920*920尺寸是可以的
// document.body.style.backgroundImage = `url(https://picsum.photos/id/${num}/1920/920) no-repeat top center cover`  // 可以 1920*920尺寸是可以的

// 引用网络的 holders
// https://holders.cf/200x300
// document.body.style.backgroundImage = "url(https://holders.cf/200x300)"


// 引用本地也可以额
// document.body.style.backgroundImage = `url(./001.png) no-repeat top center / cover`;  // 这样连写没有成功

// document.body.style.backgroundImage = `url(./001.png) `;  // 可以 1920*920尺寸是可以的  分开写成功了
// document.body.style.backgroundRepeat = "no-repeat";
// document.body.style.backgroundPosition = "top center";
// document.body.style.backgroundSize = "cover";

