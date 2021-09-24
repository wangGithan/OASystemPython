<template>
  <div id="content" class="UserList">
    <el-row display="margin-top:10px">
      <el-input
        v-model="input"
        placeholder="请输入用户名"
        style="display: inline-table; width: 30%; float: left"
      ></el-input>
      <el-button type="primary" @click="searchUser()" style="float: left; margin: 2px">查询</el-button>
    </el-row>
    <el-row>
      <el-table :data="userList" style="width: 100%" border>
        <el-table-column label="操作" min-width="100" >
          <template slot-scope="scope">
          <el-button type="primary" style="width:5px;float:left" icon="el-icon-edit" @click="editUser(scope.row.pk)"></el-button>
          <el-button type="danger" style="width:5px;float:right" icon="el-icon-delete" @click="delUser(scope.row.pk)"></el-button>
          </template>
        </el-table-column>
        <el-table-column prop="userid" label="编号" min-width="70">
          <template slot-scope="scope"> {{ scope.row.pk }} </template>
        </el-table-column>
        <el-table-column prop="user_name" label="姓名" min-width="100">
          <template slot-scope="scope">
            {{ scope.row.fields.username }}
          </template>
        </el-table-column>
        <el-table-column prop="user_tel" label="电话" min-width="100">
          <template slot-scope="scope">
            {{ scope.row.fields.usertel }}
          </template>
        </el-table-column>
        <el-table-column prop="user_age" label="年龄" min-width="50">
          <template slot-scope="scope">
            {{ scope.row.fields.userage }}
          </template>
        </el-table-column>
        <el-table-column prop="user_birth" label="生日" min-width="100">
          <template slot-scope="scope">
            {{ scope.row.fields.userbirth }}
          </template>
        </el-table-column>
        <el-table-column prop="user_depart" label="部门" min-width="100">
          <template slot-scope="scope">
            {{ scope.row.departname }}
          </template>
        </el-table-column>
        <el-table-column prop="user_position" label="职位" min-width="100">
          <template slot-scope="scope">
            {{ scope.row.positionname }}
          </template>
        </el-table-column>
        <el-table-column prop="user_login_name" label="登录名" min-width="100">
          <template slot-scope="scope">
            {{ scope.row.fields.userloginname }}
          </template>
        </el-table-column>
        <el-table-column prop="user_pass" label="密码" min-width="100">
          <template slot-scope="scope">
            {{ scope.row.fields.userpass }}
          </template>
        </el-table-column>
        <el-table-column prop="memo" label="备注" min-width="100">
          <template slot-scope="scope"> {{ scope.row.fields.memo }} </template>
        </el-table-column>
      </el-table>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "UserList",
  data() {
    return {
      input: "",
      userList: [],
    };
  },
  mounted: function () {
    this.showUsers();
  },
  methods: {
    searchUser() {
      this.$http
        .get("http://127.0.0.1:8000/users/search_user/?user_name=" + this.input)
        .then((response) => {
          var res = JSON.parse(response.bodyText);
          if (res.error_num === 0) {
            var list = this.getDepartName(res["list"]);
            list = this.getPosition(list);
            this.userList = list;
          } else {
            this.$message.error("查询用户失败，请重试");
            console.log(res["msg"]);
          }
        });
    },
    showUsers() {
      this.$http.get("http://127.0.0.1:8000/users/").then((response) => {
        var res = JSON.parse(response.bodyText);
        console.log(res);
        if (res.error_num === 0) {
          var list = this.getDepartName(res["list"]);
          list = this.getPosition(list);
          this.userList = list;
        } else {
          this.$message.error("查询用户失败");
          console.log(res["msg"]);
        }
      });
    },
    getDepartName(list) {
      list.forEach(function (item, index, list) {
        if (list[index]["fields"]["userdepart"] == 1) {
          list[index]["departname"] = "营业部";
        } else if (list[index]["fields"]["userdepart"] == 2) {
          list[index]["departname"] = "后勤部";
        } else if (list[index]["fields"]["userdepart"] == 3) {
          list[index]["departname"] = "管理部";
        }
      });
      return list;
    },
    getPosition(list) {
      list.forEach(function (item, index, list) {
        if (list[index]["fields"]["userposition"] == 1) {
          list[index]["positionname"] = "经理";
        } else if (list[index]["fields"]["userposition"] == 2) {
          list[index]["positionname"] = "组长";
        } else if (list[index]["fields"]["userposition"] == 3) {
          list[index]["positionname"] = "员工";
        }
      });
      return list;
    },
    editUser(id){
      this.$http.get("http://127.0.0.1:8000/users/edit_user/?userid="+id).then((response) => {
        this.$router.push({
          name:'ChangeUser',
          params:{
            user:response.bodyText
          }
        })
      });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
.UserList {
  margin-left: 10px;
  margin-right: 10px;
}
#content {
  width: 1250px;
  margin-left: 30px;
  margin-top: 20px;
}
</style>
