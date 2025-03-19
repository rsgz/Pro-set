<template>
    <div class="search-box">
          <input type="text" placeholder="搜索..." class="search-input" />
          <button class="search-button">确认</button>
        </div>
</template>

<script setup>

</script>

<style scoped>
.search-box {
  display: flex;
}

/* .search-button {
  padding: 8px 15px;
  background-color: #4df9ff;
  color: #111;
  border: none;
  cursor: pointer;
} */
</style>

<!-- 输入框样式 -->
<style scoped>
/* 高科技未来风格的搜索框 */
.search-input {
  width: 300px; /* 设置宽度 */
  height: 45px; /* 设置高度 */
  padding: 0 15px;
  font-size: 1rem;
  border: none;
  border-radius: 15px; /* 圆角设计 */
  outline: none;
  color: #00ffff; /* 青色字体 */
  background: rgba(255, 255, 255, 0.1); /* 半透明背景 */
  /*backdrop-filter: blur(8px); 磨玻璃效果*/
  box-shadow: 0 4px 10px rgba(0, 255, 255, 0.3), 0 0 10px rgba(0, 255, 255, 0.5); /* 外部阴影 */
  transition: all 0.3s ease;
}

.search-input::placeholder {
  color: rgba(0, 255, 255, 0.7); /* 占位符高科技颜色 */
  font-style: italic;
}

.search-input:focus {
  background: rgba(0, 0, 0, 0.7); /* 聚焦时深色背景 */
  box-shadow: 0 6px 15px rgba(0, 153, 255, 0.4), 0 0 15px rgba(0, 162, 255, 0.6); /* 聚焦时紫色光效 */
  color: #40e9b1; /* 聚焦时白色字体 */
}
</style>

<!-- 输入框 -->
<style scoped>
/* 鼠标悬浮时的动态反应 */
.search-input:hover {
  background: rgba(238, 157, 157, 0.1); /* 更深的背景颜色，增加对比 */
  box-shadow: 0 8px 20px rgba(3, 221, 236, 0.904), 0 0 25px hsla(204, 98%, 47%, 0.829); /* 强化光晕效果 */
  transform: scale(1.05); /* 微微放大，增加悬停的动感 */
  border: 1px solid rgba(0, 255, 255, 0.8); /* 外框增加发光边缘 */
  transition: all 0.3s ease; /* 平滑过渡效果 */
}

/* 鼠标悬浮时占位符颜色变化 */
.search-input:hover::placeholder {
  color: rgba(255, 255, 255, 0.8); /* 更亮的占位符颜色 */
}

/* 鼠标悬浮时带光环的动画 */
.search-input::before {
  content: "";
  position: absolute;
  top: -10px;
  left: -10px;
  width: calc(100% + 20px);
  height: calc(100% + 20px);
  border-radius: 50px; /* 光环圆润效果 */
  background: linear-gradient(45deg, rgba(0, 255, 255, 0.4), rgba(255, 0, 255, 0.4));
  z-index: -1; /* 放置在输入框后 */
  opacity: 0;
  transition: opacity 0.3s ease;
}

.search-input:hover::before {
  opacity: 1; /* 鼠标悬浮时激活光环 */
}
</style>


<!-- 按钮 -->
<style scoped>
/* 前所未有炫酷按钮样式 */
.search-button {
  position: relative;
  display: inline-block;
  padding: 0.8rem 1.5rem;
  margin: 0rem 1rem;
  font-size: 1.2rem;
  font-weight: bold;
  color: #fff; /* 按钮文本为白色 */
  text-transform: uppercase;
  background: linear-gradient(135deg, #00ffff, #ff00ff); /* 青紫渐变背景 */
  border: none;
  border-radius: 30px; /* 圆润边角 */
  box-shadow: 0 5px 15px rgba(0, 255, 255, 0.4), 0 0 20px rgba(255, 0, 255, 0.6); /* 光晕阴影 */
  cursor: pointer;
  overflow: hidden;
  z-index: 1;
  transition: all 0.3s ease;
}

.search-button::before {
  content: "";
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(0, 255, 255, 0.3), transparent);
  z-index: -1;
  transform: rotate(0deg);
  animation: button-glow 6s infinite linear;
}

.search-button:hover {
  background: linear-gradient(135deg, #ff00ff, #00ffff); /* 悬停时渐变色倒置 */
  box-shadow: 0 8px 20px rgba(255, 0, 255, 0.5), 0 0 30px rgba(0, 255, 255, 0.7); /* 悬停时强化光效 */
  transform: scale(1.05); /* 悬停时轻微放大 */
}

.search-button:hover::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.1); /* 增加光膜效果 */
  border-radius: inherit;
  z-index: -1;
}

/* @keyframes button-glow {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg); 
  }
} */
</style>