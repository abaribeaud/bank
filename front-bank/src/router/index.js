import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/statistiques',
    name: 'statistiques',
    component: () => import('../views/StatistiquesView.vue')
  },
  {
    path: '/operations',
    name: 'operations',
    component: () => import('../views/OperationView.vue')
  },
  {
    path: '/',
    name: 'home',
    component: () => import('../views/HomeView.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
