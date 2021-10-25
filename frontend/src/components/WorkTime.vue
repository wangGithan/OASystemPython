<template>
  <div style="margin-top:150px;margin-left:250px;">
    <p><label>现在时间:{{ nowTime }}</label></p>
    <p><label>工号:{{ userid }}</label> <label>姓名:{{ username }}</label> </p>
    <el-row>
      <el-button type="primary"  :disabled="startisable" plain @click="startStudy()">开始学习</el-button>
      <el-button type="success" :disabled="endisable" plain @click="endStudy()" >结束学习</el-button>
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
      startisable:"",
      endisable:"",
    };
  },
  mounted: function () {
    this.getStatus();
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
    },
    getStatus() {
      this.$http
        .get("http://127.0.0.1:8000/record/?userid=" + sessionStorage.getItem("userId"))
        .then((response) => {
          var res = response.data;
          if (res.status == "begin") {
            //已开始学习还未结束 开始按钮不能点击
            this.startisable = true;
            this.endisable =false;
          } else {
            //已结束上一次学习 开始按钮可以点击
            this.startisable = false;
            this.endisable = true;
          }
        });
    },
    startStudy(){
      this.$http
        .post("http://127.0.0.1:8000/record/make_record/", {userid: this.userid,startTime:this.nowTime,endTime:""}, {
          emulateJSON: true,
        })
        .then((response) => {
          var res = response.data;
          if (res.error_num === 0) {
            this.startisable = true;
            this.endisable = false;
            this.$message.error("开始学习时间已记录");
          }else{
            this.startisable = false;
            this.endisable = true;
            this.$message.error("学习开始时间记录失败");
          }
        });
    },
    endStudy(){
      this.$http
        .post("http://127.0.0.1:8000/record/make_record/", {userid: this.userid,startTime:"",endTime:this.nowTime}, {
          emulateJSON: true,
        })
        .then((response) => {
          var res = response.data;
          if (res.error_num === 0) {
            this.startisable = false;
            this.endisable = true;
            this.$message.error("结束学习时间已记录");
          }else{
            this.startisable = true;
            this.endisable = false;
            this.$message.error("学习结束时间记录失败");
          }
        });
    }
  },
};
</script>