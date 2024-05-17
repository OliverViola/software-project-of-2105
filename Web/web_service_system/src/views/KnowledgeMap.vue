<template>
  <el-card class="box-card">

  </el-card>
</template>


<script setup>
import Header from "../components/Header.vue";
import NeoVis from 'neovis.js';
import { onMounted } from "vue";

onMounted(() => {
  draw();
})

var viz;

function draw() {
  var config = {
    container_id: "viz",
    server_url: "bolt://101.200.145.59:7474",
    server_user: "neo4j",
    server_password: "12345678",
    labels: {
      "info": {
        "caption": "name",
        "font": {
          "size": 15,
          "color": "#100000"
        },


      },
      "relic": {
        "caption": "name",
        "font": {
          "size": 25,
          "color": "#000000"
        },
        "community": "community"
      },

    },
    relationships: {
      "年代": {
        "thickness": "count",
        "caption": true
      },
      "现藏博物馆": {
        "thickness": "count",
        "caption": true
      },
      "类型": {
        "thickness": "count",
        "caption": true
      },
      "藏品原产地": {
        "thickness": "count",
        "caption": true
      },
      "藏品材质": {
        "thickness": "count",
        "caption": true
      },
      "藏品等级": {
        "thickness": "count",
        "caption": true
      },
    },
    arrows: true,
    hierarchical: false,
    initial_cypher: "MATCH p=()-[]->() RETURN p LIMIT 300"

  };

  viz = new NeoVis(config);
  viz.render();
  console.log(viz);

}


</script>