<template>
    <div id="display">
        <div v-if="dataItem.investmentStandard.indexType=='固定点'">
            <!-- <div>指数上涨到具体某个点</div> -->
            <div>
                {{dataItem.investmentStandard.standardObjectId}}上涨到{{dataItem.investmentStandard.targetValue}}
                {{dataItem.investmentStandard.unit}}
            </div>
        </div>
        <div v-else-if="dataItem.investmentStandard.indexType=='增长点'">
            <!-- <div>指数累计上涨多少点</div> -->
            <div>
                {{dataItem.investmentStandard.standardObjectId}}从{{dataItem.investmentStandard.time.startDate}}累计上涨{{dataItem.investmentStandard.targetValue}}
                {{dataItem.investmentStandard.unit}}
            </div>
        </div>
        <div v-else-if="dataItem.investmentStandard.indexType=='增长率'">
            <!-- <div>指数指定日期上涨百分之几</div> -->
            <div>
                {{dataItem.investmentStandard.standardObjectId}}从{{dataItem.investmentStandard.time.startDate}}累计上涨{{dataItem.investmentStandard.targetValue}}
                {{dataItem.investmentStandard.unit}}
            </div>
        </div>
        <div v-else-if="dataItem.investmentStandard.indexType=='指定时间增长率'">
            <!-- <div>基金指定日期上涨百分之几</div> -->
            <div>
                {{dataItem.investmentStandard.standardObjectId}}从{{dataItem.investmentStandard.time.startDate}}累计上涨{{dataItem.investmentStandard.targetValue}}
                {{dataItem.investmentStandard.unit}}
            </div>
        </div>
        <div v-else-if="dataItem.investmentStandard.indexType=='持仓增长率'">
            <!-- <div>基金涨幅达到多少</div> -->
            <div>
                {{dataItem.investmentStandard.standardObjectId}}从持仓开始累计上涨{{dataItem.investmentStandard.targetValue}}
                {{dataItem.investmentStandard.unit}}
            </div>
        </div>
        <div v-else-if="dataItem.investmentStandard.indexType=='累计天数'">
            <!-- <div>累计上涨天数</div> -->
            <div>
                {{dataItem.investmentStandard.standardObjectId}}累计上涨时间达{{dataItem.investmentStandard.targetValue}}
                {{dataItem.investmentStandard.unit}}
            </div>
        </div>
        <div v-else-if="dataItem.investmentStandard.indexType=='阶级持仓增长率'">
            <!-- <div>阶段监控基金持仓以来收益率</div> -->
            <div v-for="(rankItem,index) in dataItem.investmentStandard.rank.rankMap" :key="index">
                {{rankItem.tm}}{{dataItem.investmentStandard.timeUnit}}内累计上涨达{{rankItem.val}}{{dataItem.investmentStandard.unit}}
            </div>
            <div>
                往后每个{{dataItem.investmentStandard.timeUnit}}内累计上涨到{{dataItem.investmentStandard.rank.every}}{{dataItem.investmentStandard.unit}}
            </div>

        </div>
        <div v-else-if="dataItem.investmentStandard.indexType=='阶级固定点'">
            <!-- <div>阶段监控固定点数</div> -->
            <div v-for="(rankItem,index) in dataItem.investmentStandard.rank.rankMap" :key="index">
                {{rankItem.tm}}{{dataItem.investmentStandard.timeUnit}}内上涨到固定点{{rankItem.val}}{{dataItem.investmentStandard.unit}}
            </div>
        </div>
        <div v-else-if="dataItem.investmentStandard.indexType=='阶级增长点'">
            <!-- <div>阶段监控指定时间的点数变化到固定点数</div> -->
            <div v-for="(rankItem,index) in dataItem.investmentStandard.rank.rankMap" :key="index">
                从{{dataItem.investmentStandard.time.startDate}}{{rankItem.tm}}{{dataItem.investmentStandard.timeUnit}}内累计上涨达{{rankItem.val}}{{dataItem.investmentStandard.unit}}
            </div>
            <div>
                往后每个{{dataItem.investmentStandard.timeUnit}}内累计上涨到{{dataItem.investmentStandard.rank.every}}{{dataItem.investmentStandard.unit}}
            </div> 
        </div>
    </div>
</template>

<script>
export default {
  name: "SingleIndexDetail",
  data() {
    return {};
  },
  methods: {},
  props: ["dataItem"]
};
</script>

<style scoped>
#display div {
  margin-top: 7px;
  font-size: 18px;
  font-family: "微软雅黑";
  font-weight: 300;
  font-style: oblique;
}
#display div div{
  border-top: 1px solid gray;
  border-bottom: 1px solid gray;
  margin-left: 10%;
  margin-right: 10%;
}
</style>


