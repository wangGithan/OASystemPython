import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import UserList from '@/components/UserList'
import AddUser from '@/components/AddUser'
import MyPage from '@/components/MyPage'
import ChangeUser from '@/components/ChangeUser'

Vue.use(Router)

export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'HelloWorld',
    //   component: HelloWorld
    // },
    {
      path: '/',
      name: 'MyPage',
      component: MyPage
      //http://localhost:8080/#/UserList
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
    }
  ]
})
