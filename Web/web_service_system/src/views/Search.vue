<template>
  <Header></Header>
  <input id="search-input" aria-label="Search the Collection" type="search" autocomplete="off"
    placeholder="Search the Collection"
    class="xsm:pr-11 md:pr-80 group-hover:text-blue-02 xsm:text-25 sm:text-[1.563rem] -tracking-[0.066rem] md:-tracking-[0.095rem] pr-[80px] pl-[5px] w-full bg-transparent md:text-76 text-4xl border-b-4 xsm:pb-2 md:pb-4 border-black text-black placeholder:text-grey-03 relative font-roboto-serif order-1 appearance-none rounded-none font-medium"
    value="" control-id="ControlID-3" style=" margin:2% 5%; width: 80%;">
    <button class="md:text-76 text-4xl border-b-4">Search</button>
  <!-- manifestation -->
  <div id="card-container" class="mt-4 grid gap-x-4 gap-y-6 lg:grid-cols-4 md:grid-cols-3 sm:grid-cols-2"
    style="margin: 0 5%;">
    <card v-for="(item, index) in listdata" :key="index" :picUrl="item.imageUrl" :artworkTitle="item.name"
      :artworkMaterial="item.material" :id="String(item.id)"></card>
  </div>
</template>

<script>
import { ref } from 'vue';
import Header from '@/components/Header.vue';
import Card from '@/components/Card.vue';
import axios from 'axios';
export default {
  name: 'SearchView',
  components: {
    Header,
    Card,
  },
  data() {
    return {
      searchQuery: '',
      listdata: [],
    };
  },
  created() {
    this.tuijian()
  },
  methods: {

    tuijian() {
      this.inpage = false
      this.show = false
      this.showinfo = true
      // this.show = !this.show 
      // this.showinfo = !this.showinfo 
      axios.post('http://8.130.122.31:8000/artifact/getRandom/', {
        number: 16,
      })
        .then(res => {
          this.listdata = res.data;
        })
    },
    handleSizeChange(val) {
      this.pageinfo.size = val
      this.tableData = this.resdata.slice((this.pageinfo.page - 1) * this.pageinfo.size, this.pageinfo.page * this.pageinfo.size)

    },
    search() {
      this.inpage = true
      console.log(111);
      if (this.searchQuery == '') {
        console.log('123');
        alert('请输入所要查询的文物')
      }
      this.showinfo = false
      this.show = true
      axios.post('http://8.130.122.31:8000/artifact/search/', {
        prompt: this.searchQuery,
        number: -1
      })
        .then(res => {
          this.listdata = res.data;
        })

    }
  },

}


</script>

<style scoped>
.example-pagination-block {
  margin-top: 90px;
}

.example-pagination-block .example-demonstration {
  margin-bottom: 16px;
}

.wenwu_left {
  width: 30%;
  height: 100%;
}

.wenwu_right {
  width: 70%;
  height: 100%;
  margin-top: 5px;
  margin-left: 5%;
}

.wenwu {
  display: flex;
  border-radius: 12px;
  margin-top: 15px;
  margin-left: 5%;
  width: 90%;
  height: 160px;
  /* background-color: aqua; */
}

.scrollbar-demo-item:hover {
  cursor: pointer;
}
</style>
