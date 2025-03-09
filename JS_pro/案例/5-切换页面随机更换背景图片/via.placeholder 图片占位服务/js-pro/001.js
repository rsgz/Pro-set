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
// document.body.style.backgroundImage = `url(https://picsum.photos/id/${num}/200/300)`  // 可以显示
// document.body.style.backgroundImage = `url(https://picsum.photos/id/${num}/800/800)`  // 可以
// document.body.style.backgroundImage = `url(https://picsum.photos/id/${num}/1920/920)`  // 可以 1920*920尺寸是可以的
// document.body.style.backgroundImage = `url(https://picsum.photos/id/${num}/1920/920) no-repeat top center`  // 可以 1920*920尺寸是可以的

// https://via.placeholder.com/600x400
document.body.style.backgroundImage = "url(https://dummyimage.com/600x400/000/fff)"
document.body.style.border = "3px solid red";