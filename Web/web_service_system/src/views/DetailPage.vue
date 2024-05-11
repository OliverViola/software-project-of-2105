<script>
    import viewer from "../components/Viewer.vue"
    import card from "../components/Card.vue"
    import axios from 'axios'

    export default {
        components: {
           viewer,
            card
        },
        data() {
            return {
                artworkDetails: [],
                relatedArtworks: [],
                number: 16,
                id: '',
                url: "https://www.sxhm.com/Uploads/Picture/2021/11/11/s618c7eba48d28.png",
                name: "司母戊鼎",
                material: "青铜"
            };
        },
        created() {
            this.id = this.$route.params.id;
            // this.fetchArtworksDetails();
            this.fetchRelatedArtworks();
        },
        methods: {
            // fetchArtworksDetails() {
            //     axios.post('http://8.130.122.31:8000/artifact/getRandom/', {id:this.id})
            //         .then(response => {
            //             this.artworkDetails = response.data;
            //         })
            //         .catch(error => {
            //             console.log('Error fetching artwork details:', error);
            //         });
            // },

            fetchRelatedArtworks() {
                axios.post('http://8.130.122.31:8000/artifact/getRandom/', {number:this.number})
                    .then(response => {
                        this.relatedArtworks = response.data;
                    })
                    .catch(error => {
                        console.log('Error fetching related artifacts:', error);
                    });
            }
        }
    }
</script>

<template>
    <div id = "body">
        <div class = "header md:z-[9996] md:sticky md:top-0">
            <div class="custom-h3">header</div>
        </div>
        <div id = "main" class="flex flex-col relative pb-4">
            <!-- flex布局details and picture -->
            <div class="flex flex-col md:flex-row md:items-start">
                    <div class="basis-7/12 pb-5 md:pb-0 md:sticky md:top-[70px]">
                        <viewer></viewer>
                    </div>
                <div class="details-container basis-5/12 px-4 pb-5 md:px-16 md:pb-0">
                    <div class="navigator"></div>

                    <div class="mb-5 md:mb-0 flex-col flex">
                        <!-- 文物名 -->
                        <h3 class="custom-h3" >佛教僧侣的法衣（袈裟）</h3>
                        <!-- 文物形成时间 -->
                        <div :style = "{ fontSize: '16px' }">1643</div>
                    </div>
                    <div>
                        <div class="grid grid-cols-1 pb-4 gap-2 mt-2">
                            <div class="flex flex-col gap-2 item2-start">
                                <!-- 作者或文物产生年代 -->
                                <h3 class="custom-h3">中国 明朝</h3>
                                <!-- 作者生平 -->
                                <div>(1368-1644)</div>
                            </div>
                            <!-- 文物级别 -->
                            <div>一级文物</div>
                            <!-- 文物材质 -->
                            <div>丝绸和金线；刺绣</div>
                            <!-- 文物大小 -->
                            <div>长15.3厘米，宽3.5厘米</div>
                        </div>
                        <div class="py-4 gap-x-2 flex border-t-2 border-black">
                            <span :style="{fontWeight: 600}">出土地址：</span>
                            <span>1972年眉县杨家村铜器窑</span>
                        </div>
                        <div class="py-4 gap-x-2 flex border-b-2 border-t-2 border-black">
                            <span :style="{fontWeight: 600}">所在博物馆：</span>
                            <span>陕西博物馆</span>
                        </div>
                        <div class="mt-5 grid gap-2">
                            <h3 class="custom-h3">文物描述</h3>
                            <p class="leading-7">
                                1957年10月20日下午，北京明定陵地宫的最后一扇石门被开启，考古工作人员发现了静静摆在地宫里三具棺木，
                                分别属于万历皇帝、孝端皇后和后来被万历的孙子天启皇帝追封为皇太后的孝靖太后。其中万历和孝端的棺木保存较好，
                                孝靖的因为是迁葬来的，已腐朽不堪。经过清理，地宫里的29个随葬储物箱里共出土了2648件精美的文物，
                                包括纺织品、衣物、金器、银器、铜器、锡器、瓷器、琉璃器、玉器、石器、漆器、木器、首饰、宝石、珍珠、冠、带、佩饰、
                                钱币、武器等，其中大部分都堪称稀世之宝，全面直观地反映了明中后期高度发达的物质文化水平。特别是丝织工艺、
                                金属制作工艺等可谓是登峰造极，无与伦比。其中的4个储物箱内各有一个六角形的朱漆囊匣，匣内各装着1件凤冠，
                                出土时漆匣已朽，凤冠珠翠散乱，考古工作者根据原物修复成3龙2凤、12龙9凤、9龙9凤和6龙3凤的凤冠各一件，
                                其中这件属于孝端皇后的9龙9凤冠后入藏中国国家博物馆。根据《明史·舆服志》，
                                洪武三年定:“(皇后)受册、谒庙、朝会，服礼服。其冠圆匡，冒以翡翠，上饰九龙四凤，大花十二树，小花数如之。
                                两博十二钿。”永乐三年定制:“其冠饰翠龙九，金凤四，中一龙衔大珠一，上有翠盖，下垂珠结，余皆口衔珠滴，珠翠云四十片，
                                大珠花、小珠花数如旧。三博，饰以金龙、翠云，皆垂珠滴。翠口圈一副，上饰珠宝钿花十二，翠钿如其数。
                                托里金口圈一副。珠翠面花五事。珠排环一对。”而出土实物与定制均不符。由此可知万历时冠服制度已有所变化。
                                1957年10月20日下午，北京明定陵地宫的最后一扇石门被开启，考古工作人员发现了静静摆在地宫里三具棺木，
                                分别属于万历皇帝、孝端皇后和后来被万历的孙子天启皇帝追封为皇太后的孝靖太后。其中万历和孝端的棺木保存较好，
                                孝靖的因为是迁葬来的，已腐朽不堪。经过清理，地宫里的29个随葬储物箱里共出土了2648件精美的文物，
                                包括纺织品、衣物、金器、银器、铜器、锡器、瓷器、琉璃器、玉器、石器、漆器、木器、首饰、宝石、珍珠、冠、带、佩饰、
                                钱币、武器等，其中大部分都堪称稀世之宝，全面直观地反映了明中后期高度发达的物质文化水平。特别是丝织工艺、
                                金属制作工艺等可谓是登峰造极，无与伦比。其中的4个储物箱内各有一个六角形的朱漆囊匣，匣内各装着1件凤冠，
                                出土时漆匣已朽，凤冠珠翠散乱，考古工作者根据原物修复成3龙2凤、12龙9凤、9龙9凤和6龙3凤的凤冠各一件，
                                其中这件属于孝端皇后的9龙9凤冠后入藏中国国家博物馆。根据《明史·舆服志》，
                                洪武三年定:“(皇后)受册、谒庙、朝会，服礼服。其冠圆匡，冒以翡翠，上饰九龙四凤，大花十二树，小花数如之。
                                两博十二钿。”永乐三年定制:“其冠饰翠龙九，金凤四，中一龙衔大珠一，上有翠盖，下垂珠结，余皆口衔珠滴，珠翠云四十片，
                                大珠花、小珠花数如旧。三博，饰以金龙、翠云，皆垂珠滴。翠口圈一副，上饰珠宝钿花十二，翠钿如其数。
                                托里金口圈一副。珠翠面花五事。珠排环一对。”而出土实物与定制均不符。由此可知万历时冠服制度已有所变化。
                                
                            </p>
                        </div>
                    </div>
                </div>
            </div>
            <!-- 相似推荐 -->
            <div class="flex flex-row gap-12 px-12">
                <div class="xsm:hidden md:sticky md:top-20 h-fit pt-12 pb-12 basis-1/6">
                    <img :style="{}" class="mb-6 h-full w-full max-h-75" src="https://gips3.baidu.com/it/u=113178756,797997158&fm=3039&app=3039&f=JPEG?w=1024&h=1024">
                    <div id="artwork-titile-sidebar" class="flex flex-col w-full max-w-[120rem] xl:mx-auto mb-5 md:mb-0">
                        <h3 class="custom-h3">佛教僧侣的法衣</h3>
                        <div>1643</div>
                        <div class="pt-3">中国 明朝</div>
                    </div>
                </div>
                <div id="see-also-container" class="basis-5/6">
                    <h3 class="custom-h3 border-b-2 border-black py-4">相似推荐</h3>
                    <div id="card-container" class="mt-4 grid gap-x-4 gap-y-6 lg:grid-cols-4 md:grid-cols-3 sm:grid-cols-2">
                         <card v-for="(item, index) in relatedArtworks" :key="index" :picUrl="item.imageUrl" :artworkTitle="item.name" :artworkMaterial="item.material" :id="item.id"></card>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

html body {
    margin: 0;
    padding: 0;
}

.header {
    height: 70px;
    width: 100%;
    background: white;
}

.grid-content {
    border-radius: 4px;
    min-height: 36px;
}

.controller-wrapper {
    opacity: 1;
    height: auto;
    padding: auto;
    background-color: rgb(220, 220, 220);
}

.details-container {
    background-color: white;
    padding-left: 50px;
    padding-right: 50px;
}

.custom-h3 {
    margin-top: 0;
    margin-bottom: 0;
    font-size: 28px;
    font-weight: 500;
}

#author-info, #title {
    padding-bottom: 10px;
}

.text-inline {
    margin-bottom: 5px;
}
</style>
