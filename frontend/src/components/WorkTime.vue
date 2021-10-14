<template>
  <div style="margin-top:150px;margin-left:250px;">
    <p><label>现在时间:{{ nowTime }}</label></p>
    <p><label>工号:{{ userid }}</label> <label>姓名:{{ username }}</label> </p>
    <el-row>
      <el-button type="primary" plain @click="startStudy()">开始学习</el-button>
      <el-button type="success" plain @click="endStudy()" >结束学习</el-button>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "",
  data() {
    return {
      userid: "",
      username: "",
      nowTime:"",
    };
  },
  mounted: function () {
    this.load();
    
  },
  methods: {
    load(){
      this.userid = sessionStorage.getItem("userId");
      this.username = sessionStorage.getItem("userName");
      //获取当前时间并打印
  　　let yy = new Date().getFullYear();
  　　let mm = new Date().getMonth()+1;
  　　let dd = new Date().getDate();
  　　let hh = new Date().getHours();
  　　let mf = new Date().getMinutes()<10 ? '0'+new Date().getMinutes() : new Date().getMinutes();
    　this.nowTime = yy+'/'+mm+'/'+dd+' '+hh+':'+mf; 
    }
  },
};
</script>