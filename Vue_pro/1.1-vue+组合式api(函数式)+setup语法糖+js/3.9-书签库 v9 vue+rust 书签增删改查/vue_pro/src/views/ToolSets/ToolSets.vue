<template>
    <ul>
        <li><router-link to="/">返回主页</router-link></li>
    </ul>

    <div>
        <button>button</button>
        <button>开启任务</button>
    </div>
</template>

<script setup>

</script>

<style scoped>
button {
    /* 相对定位 */
    position: relative;
    width: 150px;
    height: 50px;

    line-height: 25px;
    text-align: center;
    text-decoration: none;
    text-transform: uppercase;

    font-size: 13px;
    color: #fff;
    /* 渐变背景 */
    background: linear-gradient(to right, #03a9f4, #f441a5, #ffeb3b, #4e0796);
    /* 背景渐变色大小 */
    background-size: 400%;
    /* 圆角 */
    border-radius: 10px;
    z-index: 1;
}

/* 发光效果 */
button::before {
    content: "";
    position: absolute;
    top: -5px;
    left: -5px;
    bottom: -5px;
    right: -5px;
    /* 渐变背景 */
    background: linear-gradient(to right, #03a9f4, #f441a5, #ffeb3b, #09a8f4);
    /* 背景渐变色大小 */
    background-size: 400%;
    /* 圆角 */
    border-radius: 10px;
    /* 位于按钮之下 */
    z-index: -1;
    /* 设置模糊度 显示发光效果 */
    filter: blur(20px);
}

/* 鼠标移入执行动画 */
button:hover {
    /* 动画：名称 时间 infinite是无限次播放 */
    animation: streamer 8s infinite;
}

button:hover::before {
    animation: streamer 8s infinite;
}

/* 接下来定义动画 */
@keyframes streamer {
    100% {
        /* 背景位置 */
        background-position: -400% 0;
    }
}
</style>