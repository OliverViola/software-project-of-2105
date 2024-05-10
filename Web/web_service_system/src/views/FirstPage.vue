<template>
  <div style="
    display: flex;
    background-color: white;
    font-family: Arial, sans-serif;
    height: 70px
    ">
    <div style="padding-top: 15px;margin-left: 1%">
      <el-icon style="font-size: 40px"><Management /></el-icon>
    </div>
    <div style="padding-top: 10px;margin-left: 0.2%">
      <el-text style="font-weight: 550; font-size: 35px; color: black;">
        海外文物知识系统
      </el-text>
    </div>
    <div style="padding-top: 20px; margin-left: 72%">
      <el-button @click="login" link style="font-weight: 500; font-size: 20px; color: black; " >
        登录注册
      </el-button>
    </div>
    <div style="flex: 1" />

  </div>
  <el-card class="box-card"

  >

    <el-carousel :interval="4000" type="card" height="600px">

      <el-carousel-item v-for="(item,index) in image" :key="index">

        <img :src="item" class="home"/>
      </el-carousel-item>

    </el-carousel>
  </el-card>
</template>

<script>
// import {getCookie} from "@/utils/cookie";
// import request from "@/utils/request";

import {Management} from "@element-plus/icons-vue";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "home",
  components: {Management},
  data(){
    return{
      image:[
        require("../assets/image/3.png"),
        require("../assets/image/4.png"),
        require("../assets/image/5.png"),
        require("../assets/image/6.png"),
        require("../assets/image/7.png"),
        require("../assets/image/8.png"),
      ],
    };
  },
  methods: {
    login() {
      this.$router.push("/login")
    }
  }
};
</script>
<style>
.home{
  height: 600px;
  widrh:800px;
  position: relative;
  display: block; /* 设置图片为块级元素 */
  margin: auto; /* 设置外边距为自动，实现水平居中 */
  max-width: 100%; /* 让图片最大宽度为父容器的宽度 */
  max-height: 100%; /* 让图片最大高度为父容器的高度 */
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}

</style>