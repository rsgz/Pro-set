<template>
  <div>
    <nav class="extended-nav">
      <div class="nav-left">
        <ShouYeLoGo />
      </div>

      <div class="nav-center">
        <SouSuoAnNiu />
      </div>

      <div class="nav-right">
        <DengLuZhuCe />
        <TouXiang />
      </div>
    </nav>

    <hr />

    <AppList />

  </div>
</template>

<script setup>
// import { ref } from 'vue';
import SouSuoAnNiu from "./SouSuoAnNiu.vue";
import ShouYeLoGo from "./ShouYeLoGo.vue";
import DengLuZhuCe from "./DengLuZhuCe.vue";
import TouXiang from "./TouXiang.vue";
import AppList from "./AppList.vue";


</script>


<style scoped>
.extended-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  background-color: #262d34; /* 保持你的背景色 */
  color: #fff;
}

.nav-left,
.nav-right {
  display: flex;
  align-items: center;
}





</style>