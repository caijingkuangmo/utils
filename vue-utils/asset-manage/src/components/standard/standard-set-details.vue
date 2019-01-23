<template>
    <div id="standard-details">
        <el-container id="composite-standard-container" v-if="standardDetailType=='composite'">
            <el-header>
                <div class="composite-title">复合指标</div>
                <div class="investment-standard-select"><InvestmentStandardSelect></InvestmentStandardSelect></div>
            </el-header>
            <el-main>
                <CompositeDisplayArea></CompositeDisplayArea>
            </el-main>
        </el-container>
        <el-container id="single-standard-container" v-else>
            <el-header>
                <div class="single-title">单个指标</div>
                <div class="investment-standard-select"><InvestmentStandardSelect></InvestmentStandardSelect></div>
            </el-header>
            <el-main>
                <SingleDisplayArea></SingleDisplayArea>
            </el-main>
        </el-container>
    </div>
</template>

<script>
import {mapState, mapGetters} from 'vuex'
import InvestmentStandardSelect from './investment-standard-select.vue'
import SingleDisplayArea from './single-display-area.vue'
import CompositeDisplayArea from './composite-display-area.vue'

export default {
    name:"StandardSetDetails",
    data () {
        return {
            
        }
    },
    methods: {
        
    },
    components:{
        InvestmentStandardSelect,
        SingleDisplayArea,
        CompositeDisplayArea
    },
    computed: {
        standardDetailType(){
            return this.$store.getters['standard/standardDetailType']
        }
    }

}
</script>

<style scoped>
#standard-details{
    width: 100%;
}
.el-header {
  border: solid 1px #eee;
  text-align: left;
  line-height: 100px;
  height: 100px !important;
  position: relative;
}
.el-main {
  border: solid 1px #eee;
  text-align: center;
}
.single-title{
    font-size:24px;
    font-weight: bold;
    font-family: "宋体"
}
.composite-title{
    font-size:24px;
    font-weight: bold;
    font-family: "宋体"
}

.investment-standard-select{
    position: absolute;
    top:0;
    right: 0;
}
</style>


