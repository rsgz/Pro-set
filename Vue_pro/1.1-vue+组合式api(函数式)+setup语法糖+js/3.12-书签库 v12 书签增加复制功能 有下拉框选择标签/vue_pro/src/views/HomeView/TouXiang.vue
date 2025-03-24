<template>
    <div class="avatar-container">
          <div class="avatar" :class="{ 'avatar-online': isLoggedIn }"></div>
          <div class="avatar-dropdown">
            <ul>
              <li>一级菜单1</li>
              <li>一级菜单2
                <ul>
                  <li>二级菜单1</li>
                  <li>二级菜单2</li>
                </ul>
              </li>
              <li>退出</li>
            </ul>
          </div>
        </div>
</template>

<script setup>
import { ref } from 'vue';
// 模拟登录状态
const isLoggedIn = ref(true); // 初始为true，表示已登录

</script>

<style scoped>
.avatar-container {
  position: relative;
  margin-left: 20px;
}

.avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background-color: gray; /* 默认灰色 */
  cursor: pointer;
}

.avatar-online {
  background-color: green; /* 登录时显示绿色 */
}

.avatar-dropdown {
  position: absolute;
  top: 40px;
  right: 0;
  background-color: #333;
  border: 1px solid #4df9ff;
  border-radius: 5px;
  padding: 10px;
  display: none;
}

.avatar-container:hover .avatar-dropdown {
  display: block;
}

.avatar-dropdown ul {
  list-style: none;
  padding: 0;
}

.avatar-dropdown li {
  padding: 5px 10px;
  color: #fff;
  cursor: pointer;
}

.avatar-dropdown li ul {
  padding-left: 20px;
  display: none;
}

.avatar-dropdown li:hover ul {
  display: block;
}
</style>