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
div.view {
  /** show on bottom as dock*/
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  top: 14%;
}

div.header {
  margin-top: 10px;
  align-items: center;
  vertical-align: top;
  justify-content: center;
}
div.main{
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  min-width: 100vh;
  background-color: var(--color-background);
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

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
  }

  nav {
    text-align: left;
    justify-self: center;
  }
}
</style>
