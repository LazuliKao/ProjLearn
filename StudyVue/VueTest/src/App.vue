<script setup lang="ts">
import LoginPage from './pages/LoginPage.vue'
import GoToLoginPage from './pages/GoToLoginPage.vue'
import Home from './pages/HomePanel.vue'
import NotFound from './NotFound.vue'
</script>
<script lang="ts">
const routes = {
  '/': Home,
  '/login': LoginPage,
  '/login/goto': GoToLoginPage
}
export default {
  data() {
    return {
      currentPath: window.location.hash
    }
  },
  computed: {
    currentView() {
      let target: any = this.currentPath.slice(1) || '/';
      console.log("current : "+target);
      return routes[target as keyof typeof routes] || NotFound;
    }
  },
  mounted() {
    window.addEventListener('hashchange', () => {
      this.currentPath = window.location.hash
    })
  }
}
</script>
<template>
  <div>
    <a href="#/">主页</a> |
    <a href="#/login">登录</a> |
    <a href="#/non-existent-path">404测试</a>
  </div>
  <br>
  <component :is="currentView" />
</template>
<style scoped>
</style>
