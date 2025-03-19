<template>
    <div class="fu">
        <ul>
            <li><router-link class="styled-link" to="/">返回主页</router-link></li>
            <li><router-link class="styled-link" to="/BookMarks">书签</router-link></li>
        </ul>
        <div class="search-box">
            <input type="text" class="search-input" placeholder="请输入搜索内容">
            <button class="search-button">搜索</button>
        </div>
    </div>

</template>

<script setup>

</script>

<style scoped>
.fu {
    display: flex;
}

.search-box {
    display: flex;
    /* 使用 Flexbox 布局 */
    width: 600px;
    margin: 0px auto;
    border: 1px solid #ddd;
    border-radius: 8px;
    overflow: hidden;
    /* 隐藏超出容器的元素 */
}

.search-input {
    flex-grow: 1;
    /* 输入框占据剩余空间 */
    padding: 12px 15px;
    border: none;
    font-size: 16px;
    outline: none;
    outline: none;
    /* 去除默认聚焦边框 */
    transition: border-color 0.3s ease;
    /* 边框颜色过渡效果 */
}

.search-box:focus {
    border-color: #4CAF50;
    /* 聚焦时边框颜色 */
    box-shadow: 0 0 5px rgba(76, 175, 80, 0.5);
    /* 聚焦时阴影效果 */
}

/* 添加一个漂亮的伪元素作为底部线条效果 */
.search-input::after {
    content: '';
    position: absolute;
    left: 50%;
    bottom: 0;
    width: 0;
    height: 2px;
    background-color: #4CAF50;
    /* 底部线条颜色 */
    transition: width 0.3s ease, left 0.3s ease;
    /* 宽度和位置过渡效果 */
}

.search-button {
    background-color: #4CAF50;
    color: white;
    padding: 12px 20px;
    border: none;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.search-button:hover {
    background-color: #45a049;
}

/* placeholder样式 */
.search-input::placeholder {
    color: #aaa;
    font-style: italic;
}
</style>