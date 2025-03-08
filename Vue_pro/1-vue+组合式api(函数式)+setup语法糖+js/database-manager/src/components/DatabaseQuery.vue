<template>
    <div>
      <h2>数据库查询</h2>
      <select v-model="selectedServer">
        <option v-for="(server, index) in servers" :key="index" :value="index">
          {{ server.name }}
        </option>
      </select>
      <textarea v-model="query" placeholder="输入 SQL 查询"></textarea>
      <button @click="executeQuery">执行查询</button>
      <div v-if="results">
        <h3>查询结果</h3>
        <pre>{{ results }}</pre>
      </div>
    </div>
</template>
  
<script setup>
import axios from "axios";
import { ref} from 'vue';

const servers=ref(JSON.parse(localStorage.getItem("servers")) || []);
const selectedServer=ref(0);
const query=ref("");
const results=ref(null);

async function executeQuery() {
  // 注意：在 <script setup> 中不需要使用 `this`
  const server = servers.value[selectedServer.value];
  const url = `http://${server.address}:${server.port}/query`;
  try {
    const response = await axios.post(url, { query: query.value });
    results.value = JSON.stringify(response.data, null, 2);
  } catch (error) {
    results.value = `Error: ${error.message}`;
  }
}

</script>