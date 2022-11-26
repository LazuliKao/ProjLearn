import { createRouter, createWebHistory } from 'vue-router'
 import HomePanel from '../views/HomePanel.vue'
//import NotFound from '../views/NotFound.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePanel
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginPage.vue')
    },
    {
      path: '/login/goto',
      name: 'logingoto',
      component: () => import('../views/GoToLoginPage.vue')
    },
    {
      path: '/shop/center',
      name: 'shopcenter',
      component: () => import('../views/ShopCenter.vue')
    }
  ]
})

export default router
