<template>
<div>
  <Header></Header>
  <iframe src='https://cdn.knightlab.com/libs/timeline3/latest/embed/index.html?source=1zkxMfsAv1w0HMXHPF8wraYLSnZngi3oKM9u8ZeINn1s&font=Default&lang=zh-cn&initial_zoom=2&height=650&optimal_tick_width=200' width='100%' height='650' webkitallowfullscreen mozallowfullscreen allowfullscreen frameborder='0'></iframe>
</div>
</template>


<script>
// import {getCookie} from "@/utils/cookie";
// import request from "@/utils/request";

import Header from "@/components/Header.vue";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "TimeLine",
  components: {
    Header
  },
}
</script>