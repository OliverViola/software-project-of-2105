<script>
    import OpenSeadragon from 'openseadragon';

    export default {
    mounted() {
        const viewer = OpenSeadragon({
            id: "openseadragon1",//标签id
            showNavigator: true, // 是否显示导航缩略图
            prefixUrl: "https://openseadragon.github.io/openseadragon/images/", //插件小图标
            tileSources : {
                type: "image",
                // crossOriginPolicy: 'Anonymous',
                // ajaxWithCredentials: false,
                // url: "https://www.sxhm.com/Uploads/Picture/2021/11/11/s618c7eba48d28.png"
                url: "https://gips3.baidu.com/it/u=113178756,797997158&fm=3039&app=3039&f=JPEG?w=1024&h=1024"
            }
        });
    }
    }
</script>

<template>
    <div id="openseadragon1" :style="{backgroundColor:'rgb(240, 240, 240)', width: '100%', height: 'calc(-12.5rem + 100dvh)', position: 'relative'}"></div>
</template>