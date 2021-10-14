<template>
  <div style="margin-left:200px;margin-top:100px;">
    <el-form ref="form" :model="form" label-width="80px" :rules="addFormRules">
      <el-form-item label="登录名" class="label" prop="userloginname">
        <el-input class="input" v-model="form.userloginname"></el-input>
      </el-form-item>
      <el-form-item label="密　码" class="label" prop="userpass">
        <el-input
          class="input"
          v-model="form.userpass"
          show-password
        ></el-input>
      </el-form-item>
      <el-button style="margin-left: 70px" type="primary" @click="login()">登录</el-button>
      <el-button @click="cancel()">取消</el-button>
    </el-form>
  </div>
</template>

<script>
import { mapMutations } from 'vuex';
export default {
  name: "AddUser",
  data() {
    //自定义验证
    var checkLoginName = (rule, value, callback) => {
      if (!value) {
        callback(new Error("请设置格式正确的账户名"));
      } else if (value.length < 2 || value.length > 10) {
        callback(new Error("账户名为2-10位的英文字母"));
      } else {
        return callback();
      }
    };
    var checkPass = (rule, value, callback) => {
      if (!value) {
        callback(new Error("请设置格式正确的密码"));
      } else if (value.length < 6) {
        callback(new Error("密码长度最小6位"));
      } else {
        return callback();
      }
    };

    return {
      form: {
        userloginname: "",
        userpass: "",
      },
      //验证
      addFormRules: {
        userloginname: [
          { required: true, message: "必须项", trigger: "blur" },
          { validator: checkLoginName, trigger: "blur" },
        ],
        userpass: [
          { required: true, message: "必须项", trigger: "blur" },
          { validator: checkPass, trigger: "blur" },
        ],
      },
    };
  },
  mounted: function () {},
  methods: {
    ...mapMutations(['changeLogin']),
    ...mapMutations(['saveUserInfo']),
    login() {
      this.$refs["form"].validate((valid) => {
        if (!valid) {
          return;
        } else {
          let formData = JSON.stringify(this.form);
          this.$http
            .post("http://127.0.0.1:8000/login/login_form/", formData, {
              emulateJSON: true,
            })
            .then((response) => {
              var res = JSON.parse(response.bodyText);
              if (res.error_num === 0) {
                this.userToken = 'Bearer ' + res.token;
                // 将用户token保存到vuex中
                this.changeLogin({ Authorization: this.userToken });
                this.saveUserInfo({ user:[res.userId, res.userName] });
                this.$http
                  .get("http://127.0.0.1:8000/users/")
                  .then((response) => {
                    this.$router.push({
                      name: "UserList",
                    });
                  });
              } else if (res.error_num === 2) {
                this.$message.error("登录名或者密码错误");
              } else {
                this.$message.error("登录失败，请重试");
              }
            });
        }
      });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.label {
  width: 50px;
  margin-left: 50px;
}
.input {
  width: 200px;
  margin-left: 20px;
}
#content {
  width: 1000px;
  margin-left: 50px;
  margin-top: 10px;
}
</style>
