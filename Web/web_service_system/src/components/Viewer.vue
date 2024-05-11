<script>
    import OpenSeadragon from 'openseadragon';

    export default {
    mounted() {
        const viewer = OpenSeadragon({
            id: "openseadragon1",//标签id
            zoomInButton:   "zoom-in",
            zoomOutButton:  "zoom-out",
            fullPageButton: "expand",
            showNavigator: true, // 是否显示导航缩略图
            dragCursor: 'none',
            prefixUrl: "https://openseadragon.github.io/openseadragon/images/", //插件小图标
            tileSources : {
                type: "image",
                url: "https://www.chnmus.net/webfile/collection_img/_6666_/41000002_6666_A_1.JPG"
            }
        });
    }
    }
</script>

<template>
    <div>
        <div class="relative">
            <div id="openseadragon1" :style="{backgroundColor:'rgb(240, 240, 240)', width: '100%', height: 'calc(-9.2rem + 100dvh)', position: 'relative'}"></div>
        </div>
        <div class="controller-wrapper px-4 py-6 md:p-6 flex justify-between flex-col md:flex-row gap-4">
            <div class="flex flex-row items-center gap-2 order-2 md:gap-4 md:order-1">
                <div class="flex justify-between sm:justify-start w-full sm:w-auto gap-2 md:gap-4 sm:w-full md:w-full">
                    <button id="zoom-in" class="button text-xs flex items-center justify-center h-8 px-4 py-1 text-black">
                        放大
                        <ZoomIn style="width: 1em; height: 1em;" class="inline"/>
                    </button>
                    <button id="zoom-out" class="button text-xs flex items-center justify-center h-8 px-4 py-1">
                        缩小
                        <ZoomOut style="width: 1em; height: 1em;" class="inline"/>
                    </button>
                </div>
            </div>
            <div class="flex items-center gap-2 md:gap-4 order-1 md:order-2">
                <button id="expand" class="button text-xs flex items-center justify-center h-8 px-4 py-1">
                    展开
                    <FullScreen style="width: 1em; height: 1em;"  class="inline"/>
                </button>
            </div>
        </div>
    </div>
</template>

<style scoped>

.button {
    border-width: 2px;
    border-color: black;
    font-weight: 700;
}

.button:hover {
    border-color: #b64619d2;
    background-color: #b64619d2;
    color: white;
}

</style>