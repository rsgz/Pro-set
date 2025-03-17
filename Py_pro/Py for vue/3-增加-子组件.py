# 多页面 多层次 版本
r"""
这个使用的时候 需要判断 是否创建父目录
"""
import os

chuang=0  # 创建父目录吗
name = "ZiZuJian"
pro_path=r"C:\Users\Administrator\Desktop\vue_pro"
file_name=f"{name}.vue"
fu_zujian = r"CssKu"
# file_name_path = r"C:\Users\Administrator\Desktop\vue_pro\src\views\CssKu\CssKu.vue"
fu_dir = fr"{pro_path}\src\views\{fu_zujian}"
file_name_path = fr"{pro_path}\src\views\{fu_zujian}\{file_name}"

print(f"子组件:\t\t\t{file_name}")
print(f"父组件：\t\t\t{fu_zujian}")
print("vue 文件放置路径:",file_name_path)

print(fr"↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ {file_name} ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
s=fr"""
<template>
</template>

<script setup>
</script>

<style scoped>
</style>
"""
print(s)