<template>
    <div>
        <nav class="navbar">
            <ul class="nav-list">
                <li class="nav-item"><a href="#" class="nav-link">标签元素</a></li>
                <li class="nav-item"><a href="#" class="nav-link">样式属性</a></li>
                <li class="nav-item"><a href="#" class="nav-link">样式预设</a></li>
                <!-- <li class="nav-item"><a href="#" class="nav-link"></a></li> -->
                <!-- <li class="nav-item"><a href="#" class="nav-link"></a></li> -->
            </ul>
        </nav>
    </div>
</template>

<script setup>

</script>

<style scoped>
.navbar {
    background-color: #303841;
    /* 导航栏背景颜色 */
    overflow: hidden;
    /* 防止子元素溢出 */
}

.nav-list {
    list-style-type: none;
    /* 去除列表默认样式 */
    margin: 0;
    padding: 0;
    display: flex;
    /* 使用 Flexbox 布局 */
}

.nav-item {
    flex-grow: 1;
    /* 平均分配空间 */
}

.nav-link {
    display: block;
    /* 使链接占据整个列表项 */
    color: white;
    /* 链接文字颜色 */
    text-align: center;
    /* 文字居中 */
    padding: 14px 16px;
    /* 内边距 */
    text-decoration: none;
    /* 去除下划线 */
    transition: background-color 0.3s ease;
    /* 背景颜色过渡效果 */
}

.nav-link:hover {
    background-color: #111;
    /* 鼠标悬停时的背景颜色 */
}
</style>