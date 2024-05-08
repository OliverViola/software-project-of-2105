<template>
    <div id = "body">
        <div class = "header">Header</div>
        <div id = "main">
            <!-- flex布局details and picture -->
            <el-row>
                <el-col :xs="24" :sm="24" :md="14" :lg="14" :xl="14" class="pink-col">
                    <div class="grid-content ep-bg-purple" />
                </el-col>
                <el-col :xs="24" :sm="24" :md="10" :lg="10" :xl="10" class="details-container">
                    <div class="navigator"></div>

                    <!-- <el-card style="max-width: 480px" shadow="never">
                        <p v-for="o in 4" :key="o" class="text item">{{ 'List item ' + o }}</p>
                    </el-card> -->

                    <div id="title">
                        <h3 class="custom-h3" >佛教僧侣的法衣（袈裟）</h3>
                        <div :style = "{ fontSize: '16px' }">1643</div>
                    </div>
                    <div>
                        <div  class="grid grid-cols-1 pb-4 gap-2 mt-2">
                            <h3 class="custom-h3">中国 明朝</h3>
                            <div>(1368-1644)</div>
                            <div>丝绸和金线；刺绣</div>
                        </div>
                    </div>
                </el-col>
            </el-row>
            <!-- grid布局，猜你喜欢 -->
            <div></div>
        </div>
        <div id = "footer"></div>
    </div>
</template>

<style>
html body {
    margin: 0;
    padding: 0;
}

.header {
    height: 89px;
    width: 100%;
}
.el-row {
    margin-bottom: 5px;
}
.el-col {
    /* border-radius: 4px; */
}

.grid-content {
    border-radius: 4px;
    min-height: 36px;
}

.pink-col {
    background-color: rgb(240, 240, 240);
}

.details-container {
    background-color: white;
    padding-left: 50px;
    padding-right: 50px;
}

.custom-h3 {
    margin-top: 0;
    margin-bottom: 5px;
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
