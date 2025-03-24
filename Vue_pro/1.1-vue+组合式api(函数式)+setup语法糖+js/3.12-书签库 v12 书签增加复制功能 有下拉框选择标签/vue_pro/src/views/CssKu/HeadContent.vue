<template>
    <!-- css部分 作为演示区域 -->

    <!-- 作为CSS 横向 水平菜单 -->
    <div class="content">
        <ul id="cssList">
            <li>标签元素</li>
            <li>样式属性</li>
            <li>样式预设</li>
        </ul>
    </div>
</template>

<script setup>

</script>

<style scoped>
.content {
    margin-top: 1px;
    /* margin-top: 20px; */
    /* padding: 10px; */
    /* background-color: #f9f9f9; */
    /* border: 1px solid #ccc; */
}

ul {
    display: flex;
    gap: 10px;
    /* 列表项之间的间距 */
}

li {
    cursor: pointer;
    padding: 8px;
    margin-bottom: 5px;
    background-color: #72787e;
    color: aliceblue;
    /* border: 1px solid #ddd; */
}

li:hover {
    /* background-color: #e0e0e0; */
    color: #d19a66;
}
</style>