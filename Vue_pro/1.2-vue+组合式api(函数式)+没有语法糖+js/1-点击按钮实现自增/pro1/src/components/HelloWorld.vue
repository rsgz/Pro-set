<template>
  <div id="app">
    <button @click="increment">
      Count is: {{ count }}
    </button>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const count = ref(1);
    const increment = () => {
      count.value++;
    };
    return {
      count,
      increment
    };
  }
};
</script>


<style scoped>
button {
  padding: 10px;
  font-size: 16px;
}
</style>