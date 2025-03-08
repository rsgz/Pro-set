<template>
  <ServerList />
  <DatabaseQuery />
</template>

<script setup>
import ServerList from "./components/ServerList.vue";
import DatabaseQuery from "./components/DatabaseQuery.vue";
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>