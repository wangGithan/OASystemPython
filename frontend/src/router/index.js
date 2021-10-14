import Vue from 'vue'
import Router from 'vue-router'
import UserList from '@/components/UserList'
import AddUser from '@/components/AddUser'
import ChangeUser from '@/components/ChangeUser'
import Login from '@/components/Login'
import WorkTime from '@/components/WorkTime'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/Login',
      name: 'Login',
      component: Login
      //http://localhost:8080/#/
    },

    {
      path: '/UserList',
      name: 'UserList',
      component: UserList
      //http://localhost:8080/#/UserList
    },

    {
      path: '/AddUser',
      name: 'AddUser',
      component: AddUser
      //http://localhost:8080/#/AddUser
    },

    {
      path: '/ChangeUser',
      name: 'ChangeUser',
      component: ChangeUser
    },

    {
      path: '/WorkTime',
      name: 'WorkTime',
      component: WorkTime
    },
  ]
})

// 导航守卫
// 使用 router.beforeEach 注册一个全局前置守卫，判断用户是否登陆
router.beforeEach((to, from, next) => {
  if (to.path === '/Login') {
    next();
  } else {
    let token = sessionStorage.getItem('Authorization');
    if (token === null || token === '') {
      next('/Login');
    } else {
      next();
    }
  }
});


// router.beforeEach((to, from, next) => {
//   if (to.name !== 'Login' && !isAuthenticated) next({ name: 'Login' })
//   else next()
// })
export default router;
