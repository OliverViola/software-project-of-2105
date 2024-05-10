<script>
export default {
  props: {
    picUrl: String,
    artworkTitle: String,
    artworkMaterial: String,
    id: String
  },
  methods : {
    goToDetailPage() {
      this.$router.push({ name: 'DetailsPage', params: {id: this.id}})
    }
  }
}
</script>

<template>
  <div class="shadow-right-bottom flex flex-col p-4" :style="{height: '360px'}" @click="goToDetailPage">
    <img :src="picUrl" :style="{height: '200px'}">
    <div class="mt-2 flex flex-col gap-3">
      <p class="title-text">{{artworkTitle}}</p>
      <p class="text">{{artworkMaterial}}</p>
    </div>
  </div>
</template>

<style scoped>
.shadow-right-bottom {
  box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.3); /* 只在右下方显示阴影 */
}

.title-text {
  font-size: 20px;
  font-weight: 500;
  text-decoration: underline;
}

.text {
  overflow: hidden;
}
</style>