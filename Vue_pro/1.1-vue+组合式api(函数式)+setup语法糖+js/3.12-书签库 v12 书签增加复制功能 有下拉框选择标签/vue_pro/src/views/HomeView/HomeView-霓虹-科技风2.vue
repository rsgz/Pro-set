<template>
  <div>
    <!-- 独立的导航栏 -->
    <nav>
      <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
      </ul>
    </nav>
    <hr/>
    <nav>
      <ul class="ul_top">
        <li class="neon-button"><span>App:</span></li>
        <li class="neon-button"><router-link to="/BookMarks">书签</router-link></li>
        <li class="neon-button"><router-link to="/MeiTiChuangZuo">媒体创作</router-link></li>
        <li class="neon-button"><router-link to="/DaiMaKu">代码库</router-link></li>
        <li class="neon-button"><router-link to="/CssKu">Css库</router-link></li>
        <li class="neon-button"><router-link to="/ToolSets">Tools6站在</router-link></li>
      </ul>
    </nav>

    <!-- 页面内容 -->
    <div>
      <!-- <h2>6666666666</h2> -->
      <!-- <p>22222222222</p> -->
    </div>
  </div>
</template>

<script setup>
// 主页的逻辑
</script>

<style scoped>
/* 主页的样式 */
/* nav { */
  /* background-color: #f0f0f0; */
  /* padding: 1px; */
/* } */
.ul_top{
  margin-top: 10px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline;
  margin: 0 3px;
}

a {
  text-decoration: none;
  color: #42b983;
}

a:hover {
  text-decoration: none;
}

.neon-button {
    position: relative;
    padding: 5px 8px;
    color: #4df9ff;
    font-size: 1.2em;
    text-decoration: none;
    text-transform: uppercase;
    overflow: hidden;
    transition: 0.5s;
    /* letter-spacing: 4px; */
    /* border: 1px solid #4df9ff; */
}

.neon-button:hover {
    background: #4df9ff;
    color: #111;
    box-shadow: 0 0 5px #4df9ff,
        0 0 25px #4df9ff,
        0 0 50px #4df9ff,
        0 0 200px #4df9ff;
    -webkit-box-reflect: below 1px linear-gradient(transparent, #0005);
}

.neon-button::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(45deg, #000, #4df9ff, #000);
    z-index: -1;
    transition: 0.5s;
    background-size: 400%;
}

.neon-button:hover::before {
    filter: blur(5px);
    background-position: 100% 0;
}
</style>