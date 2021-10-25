import Vue from 'vue';
import Vuex from 'vuex';
Vue.use(Vuex);
 
const store = new Vuex.Store({
 
  state: {
    // 存储token
    Authorization: sessionStorage.getItem('Authorization') ? sessionStorage.getItem('Authorization') : '',
    userId:sessionStorage.getItem('userId') ? sessionStorage.getItem('userId') : '',
    userName:sessionStorage.getItem('userName') ? sessionStorage.getItem('userName') : '',
    
  },
 
  mutations: {
    // 修改token，并将token存入sessionStorage
    changeLogin (state, user) {
      state.Authorization = user.Authorization;
      sessionStorage.setItem('Authorization', user.Authorization);
    },
    saveUserInfo (state, user){
      state.userId = user.user[0];
      sessionStorage.setItem('userId', user.user[0]);
      state.userName = user.user[1];
      sessionStorage.setItem('userName', user.user[1]);
    }

  }
});
 
export default store;