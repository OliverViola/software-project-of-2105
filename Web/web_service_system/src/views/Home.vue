<template>
  <!--  轮播图-->
  <Header></Header>
  <el-card class="box-card">
    <el-carousel :interval="4000" type="card" height="300px">
      <el-carousel-item v-for="(item,index) in image" :key="index">
        <img :src="item" class="home" alt=""/>
      </el-carousel-item>
    </el-carousel>
  </el-card>

  <el-row :gutter="20" style="margin-left:auto">
    <el-col v-for="(group, index) in artifact" :key="index" :span="6">
      <div class="grid-content">
        <img :src="group.imageUrl" alt="" class="picture" />
        文物名称：{{ group.name }}<br>
        出土时间：{{ group.time }}<br>
        文物尺寸：{{ group.size }}<br>
        博物馆：{{ group.museum }}<br>
        材料：{{ group.material }}<br>
      </div>
    </el-col>
  </el-row>


</template>

<script>
// import {getCookie} from "@/utils/cookie";
// import request from "@/utils/request";

import axios from "axios";
import Header from "@/components/Header.vue";


export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "home",
  components: {Header},
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
      number: 12,
      artifact:{
        name:"",
        time:"",
        museum:"",
        size:"",
        material:"",
        imageUrl:""
      }
    };
  },
  mounted() {
    this.change(); // 在组件挂载后调用 change 方法
  },
  methods: {
    change() {
      axios.post('http://8.130.122.31:8000/artifact/getRandom/', {
        number:this.number,
      })
          .then(response => {
            if (response.status === 200) {
              const dataList = response.data;
              const artifactGroups = [];

              dataList.forEach(group => {
                const artifact = {
                  name: group.name,
                  time: group.time,
                  museum: group.museum,
                  size: group.size,
                  material: group.material,
                  imageUrl: group.imageUrl
                };
                artifactGroups.push(artifact);
              });

              this.artifact = artifactGroups;
            }
          })
          .catch(error => {
            console.error('Error fetching data:', error);
          })
          .finally(() => {
            this.loading = false; // 关闭加载状态
          });
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
.el-carousel__item h3 {
  color: #475669;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
  text-align: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}


.grid-content {
  border-radius: 4px; /* 圆角边框 */
  min-height: 36px; /* 最小高度 */
  background-color: white; /* 设置背景色为白色 */
  color: #030111; /* 文字颜色 */
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); /* 添加边框阴影 */
  margin-top: 10px;
}
.picture{
  width: 100%; /* 让图片宽度填满其父容器 */
  height: 100%; /* 让图片高度填满其父容器 */
  //object-fit: cover; /* 让图片保持比例并填充整个容器，可能会裁剪部分图片 */
}
</style>