<template>
  <div>
    <el-table :data="recordList" style="width: 100%" border>
        <el-table-column prop="userid" label="用户姓名" min-width="70">
          <template> {{ this.username }} </template>
        </el-table-column>
        <el-table-column prop="work_begin" label="开始学习" min-width="100">
          <template slot-scope="scope">
            {{ scope.row.fields.work_begin }}  
          </template>
        </el-table-column>
        <el-table-column prop="work_end" label="结束学习" min-width="100">
          <template slot-scope="scope">
            {{ scope.row.fields.work_end }}
          </template>
        </el-table-column>
        <el-table-column prop="total" label="总数" min-width="100">
          <template slot-scope="scope">
            {{ scope.row.fields.total }}
          </template>
        </el-table-column>
      </el-table>
  </div>
</template>

<script>
export default {
  name: "",
  data() {
    return {
      userid: "",
      username: "",
      recordList: [],
    };
  },
  mounted: function () {
    this.load();
    
  },
  methods: {
    load(){
      this.userid = sessionStorage.getItem("userId");
      this.username = sessionStorage.getItem("userName");
      this.$http
        .get("http://127.0.0.1:8000/record/check_record/?userid=" + sessionStorage.getItem("userId"))
        .then((response) => {
          var res = response.data;
          if (res.error_num === 0) {
            this.recordList = res.list;
          } else {
            this.$message.error("查询用户失败，请重试");
          }
        });
    },
  },
};
</script>