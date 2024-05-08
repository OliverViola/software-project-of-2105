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
                url: "https://www.sxhm.com/Uploads/Picture/2021/11/11/s618c7eba48d28.png"
            }
        });
    }
    }
</script>

<template>
    <div>
        <div id="openseadragon1" style="width: 800px; height: 600px;"></div>
    </div>
</template>