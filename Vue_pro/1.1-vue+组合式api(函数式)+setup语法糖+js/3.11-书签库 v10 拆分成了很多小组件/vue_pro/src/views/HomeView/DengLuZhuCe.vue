<template>
    <div class="auth-buttons">
        <button class="auth-button">登录</button>
        <button class="auth-button">注册</button>
    </div>
</template>

<script setup>

</script>

<style scoped>
.auth-buttons {
  display: flex;
}

.auth-button {
  padding: 8px 15px;
  background-color: #333;
  color: #fff;
  border: 1px solid #4df9ff;
  margin: 0 5px;
  cursor: pointer;
}
</style>

<!-- 登录按钮样式 -->
<style scoped>
/* 登录按钮样式 */
.auth-button {
  position: relative;
  padding: 6px 6px;
  font-size: 1.2em;
  color: #4df9ff; /* 青色发光文字 */
  text-transform: uppercase;
  border: none;
  background: transparent; /* 透明背景 */
  border-radius: 15px; /* 圆角设计 */
  overflow: hidden;
  transition: 0.5s;
  cursor: pointer;

  /* 默认状态光效 */
  /* box-shadow: 0 0 8px rgba(77, 249, 255, 0.3), 0 0 16px rgba(77, 249, 255, 0.2); /* 淡淡光晕 */
  /* transition: all 0.5s ease; */

  /* 内发光效果 */
  box-shadow: inset 0 0 16px rgba(77, 249, 255, 0.3), inset 0 0 16px rgba(77, 249, 255, 0.2); /* 内部淡淡光效 */
  transition: all 0.5s ease;
}

.auth-button:hover {
  background: #4df9ff; /* 悬停时青色填充 */
  color: #111; /* 悬停时文字变深色 */
  box-shadow: 0 0 10px #4df9ff, 0 0 30px #4df9ff, 0 0 60px #4df9ff, 0 0 120px #4df9ff; /* 青色光晕效果 */
  -webkit-box-reflect: below 2px linear-gradient(transparent, #0005); /* 悬停时反射效果 */
}

.auth-button::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(45deg, #000, #4df9ff, #000); /* 青色渐变线条 */
  z-index: -1;
  transition: 0.5s;
  background-size: 400%;
}

.auth-button:hover::before {
  filter: blur(8px); /* 悬停时动态模糊光效 */
  background-position: 100% 0;
}

</style>