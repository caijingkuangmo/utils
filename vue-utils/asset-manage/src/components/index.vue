<template>
   <div id="index-tab">
       <el-tabs type="border-card">
           <el-tab-pane label="资产状况">
               <AssetPage></AssetPage>
           </el-tab-pane>
            <el-tab-pane label="指标设定">
                <StandardPage></StandardPage>
            </el-tab-pane>
            <el-tab-pane label="指数跟踪">
                <StockFollowPage></StockFollowPage>
            </el-tab-pane>
       </el-tabs>
    </div> 
</template>

<script>
import AssetPage from "@/pages/asset-show-page.vue"
import StandardPage from "@/pages/standard-set-page.vue"
import StockFollowPage from "@/pages/stock-follow-page.vue"

export default {
    name:"index",
    data () {
        return {
            
        }
    },
    methods: {
        
    },
    components: {
        AssetPage,
        StandardPage,
        StockFollowPage
    }
}
</script>

<style scoped>

</style>


