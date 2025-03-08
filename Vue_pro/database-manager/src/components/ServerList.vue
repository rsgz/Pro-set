<template>
  <div>
    <h2>服务器列表</h2>
    <ul>
      <li v-for="(server, index) in servers" :key="index">
        {{ server.name }} - {{ server.address }}:{{ server.port }}
        <button @click="editServer(index)">编辑</button>
        <button @click="deleteServer(index)">删除</button>
      </li>
    </ul>
    <button @click="addServer">添加服务器</button>

    <dialog ref="serverDialog">
      <form @submit.prevent="saveServer">
        <label>服务器名称：</label>
        <input v-model="currentServer.name" /><br />
        <label>服务器地址：</label>
        <input v-model="currentServer.address" /><br />
        <label>端口：</label>
        <input type="number" v-model="currentServer.port" /><br />
        <button type="submit">保存</button>
        <button type="button" @click="closeDialog">取消</button>
      </form>
    </dialog>
  </div>
</template>

<script setup>
import { ref, onMounted, reactive } from 'vue';

const servers = ref(JSON.parse(localStorage.getItem("servers")) || []);
const currentServer = reactive({ name: "", address: "", port: "" });
let currentIndex = -1;
const serverDialog = ref(null);

onMounted(() => {
  serverDialog.value.addEventListener('close', () => {
    currentIndex = -1;
    Object.assign(currentServer, { name: "", address: "", port: "" });
  });
});

function addServer() {
  serverDialog.value.showModal();
}

function editServer(index) {
  currentIndex = index;
  Object.assign(currentServer, servers.value[index]);
  serverDialog.value.showModal();
}

function deleteServer(index) {
  servers.value.splice(index, 1);
  saveServersToLocalStorage();
}

function saveServer() {
  if (currentIndex === -1) {
    servers.value.push({ ...currentServer });
  } else {
    servers.value.splice(currentIndex, 1, { ...currentServer });
  }
  saveServersToLocalStorage();
  serverDialog.value.close();
}

function closeDialog() {
  serverDialog.value.close();
}

function saveServersToLocalStorage() {
  localStorage.setItem("servers", JSON.stringify(servers.value));
}
</script>