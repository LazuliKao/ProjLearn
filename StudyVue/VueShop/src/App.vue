<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="main">
    <div class="header">
      <nav>
        <RouterLink to="/">主页</RouterLink>
        <RouterLink to="/shop/center">商店</RouterLink>
        <RouterLink to="/login">登录</RouterLink>
      </nav>
    </div>
    <div class="view">
      <RouterView />
    </div>
  </div>
</template>

<style scoped>

div.header {
  background-color: var(--color-header);
  padding: 1rem;
}
div.view {  
  display: flex;
  flex-direction: column;
  height: 80vh;
  width: 80vw;
}
div.main{
  flex: 1;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

nav {
  font-size: large;
  /* align to center */
  display: flex;
  justify-content: center;
  align-items: center;
}

nav a.router-link-exact-active {
  color: var(--color-text);
  border-bottom: 4px solid var(--color-border);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  padding: 0 1rem;
}

</style>
