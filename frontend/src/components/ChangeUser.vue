<template>
  <div id="content" class="editUser" v-if="user">
    <el-form ref="form" :model="user" label-width="80px" :rules="addFormRules">
      <el-input type="hidden" v-model="user.userid"></el-input>
      <el-form-item label="姓名" class="label" prop="username">
        <el-input class="input" v-model="user.username"></el-input>
      </el-form-item>
      <el-form-item label="电话" class="label" prop="usertel">
        <el-input class="input" v-model="user.usertel"></el-input>
      </el-form-item>
      <el-form-item label="生日" class="label" prop="userbirth">
        <el-col :span="11">
          <el-date-picker
            class="input"
            type="date"
            placeholder="选择日期"
            default-value="2000-01-01"
            :picker-options="dateOption"
            v-model="user.userbirth"
          ></el-date-picker>
        </el-col>
      </el-form-item>
      <el-form-item label="部门" class="label" prop="userdepart">
        <el-select
          class="input"
          v-model="user.userdepart"
          placeholder="请选择部门"
        >
          <el-option
            v-for="item in departs"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          >
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="职位" class="label" prop="userposition">
        <el-select
          class="input"
          v-model="user.userposition"
          placeholder="请选择职位"
        >
          <el-option
            v-for="item in positions"
            :key="item.value"
            :value="item.value"
            :label="item.label"
          ></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="登录名" class="label" prop="userloginname">
        <el-input
          class="input"
          v-model="user.userloginname"
          placeholder="2-10位英文数字"
        ></el-input>
      </el-form-item>
      <el-form-item label="密码" class="label" prop="userpass">
        <el-input
          placeholder="长度大于6位"
          class="input"
          v-model="user.userpass"
          show-password
        ></el-input>
      </el-form-item>
      <el-form-item label="备注" class="label" prop="memo">
        <el-input class="input" v-model="user.memo"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="editUser()">修改</el-button>
        <el-button @click="cancel()">取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: "user",
  data() {
    //自定义验证
    var checkMobile = (rule, value, callback) => {
      if (!value) {
        callback(new Error("请设置格式正确的手机号"));
      } else {
        const regMobile =
          /^(0|86|17951)?(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$/;
        if (regMobile.test(value)) {
          // 合法的手机号码
          return callback();
        } else {
          callback(new Error("手机号码格式不正确"));
        }
      }
    };
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
      user: {
        username: "",
        usertel: "",
        userbirth: "",
        userdepart: "",
        userposition: "",
        userloginname: "",
        userpass: "",
        memo: "",
        userid: "",
      },
      departs: [
        {
          value: 1,
          label: "营业部",
        },
        {
          value: 2,
          label: "后勤部",
        },
        {
          value: 3,
          label: "管理部",
        },
      ],
      positions: [
        {
          value: 1,
          label: "经理",
        },
        {
          value: 2,
          label: "组长",
        },
        {
          value: 3,
          label: "员工",
        },
      ],
      //验证
      addFormRules: {
        username: [{ required: true, message: "必须项", trigger: "blur" }],
        usertel: [
          { required: true, message: "必须项", trigger: "blur" },
          { validator: checkMobile, trigger: "blur" },
        ],
        userbirth: [{ required: true, message: "必须项", trigger: "blur" }],
        userdepart: [{ required: true, message: "必须项", trigger: "blur" }],
        userposition: [{ required: true, message: "必须项", trigger: "blur" }],
        userloginname: [
          { required: true, message: "必须项", trigger: "blur" },
          { validator: checkLoginName, trigger: "blur" },
        ],
        userpass: [
          { required: true, message: "必须项", trigger: "blur" },
          { validator: checkPass, trigger: "blur" },
        ],
      },
      //不可以点今年到前18年（不能雇佣童工）
      dateOption: {
        disabledDate(date) {
          let d = new Date();
          let year = d.getFullYear();
          let month = d.getMonth() + 1;
          let day = d.getDate();
          let okDate = year - 18 + "-" + month + "-" + day;
          return date.getTime() >= Date.parse(okDate);
        },
      },
    };
  },
  created: function () {
    this.showUsers();
  },
  methods: {
    
    editUser() {
      this.$refs["form"].validate((valid) => {
        if (!valid) {
          return;
        } else {
          //JSON.stringify会造成日期格式的数据错误
          //日期先转换为string，后台再改为日期格式可以避免
         this.user.userbirth = this.user.userbirth.toString();
          let formData = JSON.stringify(this.user);
          this.$http
            .post("http://127.0.0.1:8000/users/edit_user/", formData, {
              emulateJSON: true,
            })
            .then((response) => {
              var res = response.data;
              if (res.error_num === 0) {
                this.$message.error("修改用户成功");
                //清除表单
                //this.$refs["form"].resetFields();
                let obj = this.user;
                for(let k in obj){
                obj[k]=""
                }
              }else if(res.error_num === 2) {
                this.$message.error("用户名已存在");
              }else{
                this.$message.error("修改用户失败，请重试");
              }
            });
        }
      });
    },
    showUsers() {
      var res = this.$route.params.user;
      if (res.error_num === 0) {
        console.log(res);
        this.user = res["list"][0]["fields"];
        this.user.userid = res["list"][0]["pk"];
      } else {
        this.$message.error("获取用户失败");
      }
    },
    cancel(){
      this.$http
        .get("http://127.0.0.1:8000/users/")
        .then((response) => {
          this.$router.push({
            name: "UserList",
          });
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
