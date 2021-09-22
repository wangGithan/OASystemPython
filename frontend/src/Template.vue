<template>
  <div id="frame">
    <el-container style="height: 700px; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu :default-openeds="['1', '3']">
          <el-submenu index="1">
             <template slot="title"><i class="el-icon-message"></i>导航一</template>
            <el-menu
                default-active="1"
                class="el-menu-vertical-demo"
                @open="handleOpen"
                @close="handleClose"
              >
                <el-menu-item index="1">
                  <i class="el-icon-menu"></i>
                  <span slot="title"
                    ><font color="#34495E" size="5px;">菜单</font></span
                  >
                </el-menu-item>
                <el-submenu index="2">
                  <template slot="title">
                    <i class="el-icon-location"></i>
                    <span>用户管理</span>
                  </template>
                  <el-menu-item index="2-1"
                    ><router-link to="/UserList"
                      >查找用户</router-link
                    ></el-menu-item
                  >
                  <el-menu-item index="2-2"
                    ><router-link to="/AddUser">添加用户</router-link></el-menu-item
                  >
                </el-submenu>
                <el-menu-item index="3">
                  <i class="el-icon-document"></i>
                  <span slot="title">查询用户</span>
                </el-menu-item>
                <el-menu-item index="4">
                  <i class="el-icon-document"></i>
                  <span slot="title">添加用户</span>
                </el-menu-item>
                <el-menu-item index="5" disabled>
                  <i class="el-icon-setting"></i>
                  <span slot="title">设置</span>
                </el-menu-item>
              </el-menu>
          </el-submenu>
        </el-menu>
      </el-aside>
      
      <el-container>
        <el-header style="text-align: right; font-size: 12px">
          <el-menu class="el-menu-demo" mode="horizontal" @select="handleSelect">
            <el-menu-item>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</el-menu-item>
            <el-menu-item index="1">处理中心</el-menu-item>
            <el-submenu index="2">
              <template slot="title">我的工作台</template>
              <el-menu-item index="2-1">选项1</el-menu-item>
              <el-menu-item index="2-2">选项2</el-menu-item>
              <el-menu-item index="2-3">选项3</el-menu-item>
              <el-submenu index="2-4">
                <template slot="title">选项4</template>
                <el-menu-item index="2-4-1">选项1</el-menu-item>
                <el-menu-item index="2-4-2">选项2</el-menu-item>
                <el-menu-item index="2-4-3">选项3</el-menu-item>
              </el-submenu>
            </el-submenu>
            <el-menu-item index="3" disabled>消息中心</el-menu-item>
            <el-menu-item index="4">订单管理</el-menu-item>
            <span>欢迎</span>
          </el-menu>
          
        </el-header>
        
        <el-main>
          <router-view />
        </el-main>
        <el-footer>
          <div></div>
        </el-footer>
      </el-container>
    </el-container>
  </div>
</template>
<script>
export default {
  name: "Template",
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
  },
};
</script>
<style>
.el-header {
  color: #333;
  line-height: 60px;
}

.el-aside {
  background-color: white;
}

</style>



