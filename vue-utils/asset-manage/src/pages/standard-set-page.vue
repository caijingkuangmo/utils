<template>
    <div id="standard-set">
        <div id="standard-menu">
            <el-menu default-active="1"
                style="width:95%;">
                    <el-menu-item index="1">
                        <i class="el-icon-tickets" @click="showCompositeStandard">复合指标</i>
                    </el-menu-item>
                    <el-menu-item index="2" @click="showSingleStandard">
                        <i class="el-icon-document">单个指标</i>
                    </el-menu-item>
            </el-menu>
        </div>
        <div id="standard-content">
            <StandardSetDetails></StandardSetDetails>
        </div>
    </div>
</template>

<script>
/**
 * 两个指标设定
 * 1.复合指标   必须依赖单个指标
 *      主要提供一些嵌套逻辑关系，与 或
 * 2.单个指标
 *      进仓指标和清仓指标吗
 *      就要涉及时间（月 周 日）分持仓时间（基金标的），累计涨跌时间（基金，指数标的）   监控哪个指数  盈亏率（基金标的）  
 *      指数点数或指数涨跌幅（指数标的） 短信与提示信息
 * 
 * 建议：清仓指标简单直接  进仓指标可以复杂多个 （保守原则）
 * 
 *  起止计算时间--确认
 * 1） 恒生上涨或下跌到某个点 开始买入或卖出 1000元
 * 2） 恒生上涨或下跌多大幅度（多少个点） 买入或卖出500  需要起止时间
 * 3） 恒生累计下跌5天（同时下跌多少幅度或多少点） 买入  需要起止时间
 *      
 *      基金标的原则（不建议监控基金净值，持仓成本--拆分、折算 会影响分析，建议监控盈亏率  从资金的有效性来看，收益率需兼顾持仓时间）
 * 4） 基金 累计下跌 5% 买入500  需要起止时间
 * 5） 基金 {3月:5%，6月：7%，9月：9%， 12月：12%} 
 *          或 每月1% 每年12% 空档期多少个月   可以合起来，空档期可以在字典里设，不设置字典，设置每月效果
 *          
 *          纯增长率出仓 20%
 * 
 */
import StandardSetDetails from '@/components/standard/standard-set-details.vue'

export default {
    name:"StandardSetPage",
    data () {
        return {
            
        }
    },
    methods: {
        showCompositeStandard(){
            this.$store.dispatch('standard/changeStandardDetailType', 'composite')
        },
        showSingleStandard(){
            this.$store.dispatch('standard/changeStandardDetailType', 'single');
        }

    },
    components:{
        StandardSetDetails
    }
}
</script>

 <style scoped>
 #standard-set{
     font-size: 0;
 }
 #standard-menu{
     display: inline-block;
     font-size: 16px;
     width: 15%;
     vertical-align: top;
 }
 #standard-content{
     display: inline-block;
     font-size: 16px;
     width: 85%; 
 }
 </style>
 

