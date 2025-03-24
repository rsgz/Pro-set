
<template>
    <span class="website-name">517</span>
    <router-link to="/" class="nav-link">
        <span class="glow-text">首页</span>
    </router-link>
</template>

<script setup>

</script>

<!-- 517 -->
<style scoped>
.website-name {
  font-size: 1.5em;
  font-weight: bold;
  margin-right: 10px;
}

.website-name {
    font-size: 2em; /* 调整字体大小 */
    font-family: 'Courier New', monospace; /* 选择科技感字体 */
    color: #4df9ff; /* 霓虹蓝 */
    text-shadow: 0 0 5px #4df9ff, 0 0 15px #4df9ff, 0 0 25px #4df9ff; /* 发光效果 */
    animation: neon-flicker 2s infinite alternate; /* 闪烁动画 */
}

@keyframes neon-flicker {
    0%, 100% {
        text-shadow: 0 0 5px #4df9ff, 0 0 15px #4df9ff, 0 0 25px #06e8f0;
    }
    50% {
        text-shadow: 0 0 2px #4df9ff, 0 0 8px #4df9ff, 0 0 15px #05f17b;
    }
}

/* 如果想加入扫描线效果，可以添加以下代码 */
.website-name {
    position: relative;
    overflow: hidden;
}

.website-name::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    animation: scan-line 1s linear infinite;
}

@keyframes scan-line {
    0% {
        left: -100%;
    }
    100% {
        left: 100%;
    }
}

</style>



<!-- 首页2 -->
<style scoped>
/* 未来科技风 + 磨玻璃效果样式 */
.nav-link {
  display: inline-block;
  text-decoration: none;
  position: relative;
  color: #00ffff; /* 科技感青色 */
  font-size: 1.1rem;
  font-weight: bold;
  padding: 0.5rem 1rem;
  background: rgba(255, 255, 255, 0.1); /* 半透明背景 */
  border-radius: 15px; /* 圆角 */
  backdrop-filter: blur(10px); /* 磨玻璃模糊效果 */
  box-shadow: 0 4px 10px rgba(0, 255, 255, 0.2); /* 光晕阴影 */
  transition: all 0.3s ease;
  overflow: hidden;
}

.nav-link:hover {
  background: rgba(255, 0, 255, 0.1); /* 悬停时紫色调 */
  /* box-shadow: 0 20px 25px rgba(9, 44, 240, 0.925); */

  box-shadow: 0 0 5px #9988e4, 0 0 25px #4df9ff, 0 0 50px #4df9ff, 0 0 200px #4df9ff;
  -webkit-box-reflect: below 1px linear-gradient(transparent, #0005);
}

.nav-link .glass-text {
  position: relative;
  z-index: 2;
  text-shadow: 0 0 5px #00ffff, 0 0 15px #00ffff; /* 青色文字光辉 */
}

.nav-link:hover .glass-text {
  /* text-shadow: 0 0 10px #ff00ff, 0 0 20px #ff00ff; */  /* 悬停时的紫色光辉 */
  text-shadow: 0 0 10px rgb(26, 255, 255), 0 0 20px rgba(26, 255, 255, 0.7); /* 悬停时冷青色光辉 */
}



.nav-link::before {
  content: "";
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(0, 255, 255, 0.3), transparent);
  transform: rotate(45deg);
  animation: futuristic-glow 4s infinite linear;
  z-index: 1;
}

@keyframes futuristic-glow {
  0% {
    transform: rotate(45deg);
  }
  100% {
    transform: rotate(405deg); /* 旋转发光效果 */
  }
}
</style>

