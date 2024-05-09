import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '@/views/UserView.vue'
import LoginView from '@/views/LoginView.vue'
import UserProfile from '@/components/UserProfile.vue'
import UserPosts from '@/components/UserPosts.vue'
import UserHome from '@/components/UserHome.vue'

const isAuthenticated = true

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/user/:id',
      // name: 'user',
      component: UserView,
      // beforeEnter: (to, from) => {
      //   console.log(to)
      //   console.log(from)
      // },
      children: [
        { path: '', name: 'user', component: UserHome },
        { path: 'profile', name: 'user-profile', component: UserProfile},
        { path: 'posts', name: 'user-posts', component: UserPosts},
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      beforeEnter: (to, from) => {
        if (isAuthenticated === true) {
          console.log('이미 로그인 상태입니다.')
          return { name: 'home' }
        }
      }
    }
  ]
})

// router.beforeEach((to, from) => {
//   // console.log(to)
//   // console.log(from)
//   const isAuthenticated = false

//   if (!isAuthenticated && to.name !== 'login') {
//     console.log('로그인이 필요합니다.')
//     return { name: 'login' }
//   }
// })

export default router
