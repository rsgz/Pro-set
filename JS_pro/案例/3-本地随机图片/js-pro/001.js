const pic = document.querySelector('img')
// 获取 start-end的随机数 包含 start end
function get_rand_int_num(start, end) {
    return Math.floor(
        Math.random() * (end - start + 1)
    ) + start
}

// num = 10
num = get_rand_int_num(1, 10)
pic.src = `./images/${num}.webp`
console.log(pic.src);  // http://127.0.0.1:5500/js-pro/images/1.webp
pic.title = "new pic"
pic.width = 200
pic.heigt = 200
pic.alt = "图片不见了"