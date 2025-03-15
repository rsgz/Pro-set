<script setup>
import { ref } from 'vue'
import AsideMenu from '@/views/AsideMenu.vue'
</script>

<template>
    <div class="common-layout">
        <el-container>
            <AsideMenu />
            <el-container>
                <el-header>Header</el-header>
                <el-main>Main</el-main>
            </el-container>
        </el-container>
    </div>
</template>

<style scoped>
div {
    color: red;
}
</style>