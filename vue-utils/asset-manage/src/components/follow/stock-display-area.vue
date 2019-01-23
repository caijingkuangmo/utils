<template>
    <div id="stock-display-area">
        <span v-if="notShow">当前无数据，请点选</span>
        <el-container v-else>
            <el-header>
                <span class="stock-name">{{currentIndex.name}}</span>
                <span class="stock-code">{{currentIndex.code}}</span>
            </el-header>
            <el-main>
              <div>
                <span class="stock-number">当前点数(净值): {{currentIndex.number}}</span>
                <span class="stock-rate">涨跌幅: {{currentIndex.rate}}</span>
                <span class="stock-date">时间: {{currentIndex.date}}</span>
              </div>
              <div v-if="indexName == 'jijin'" class="stock-lately">
                <div class="stock-lately-select">
                  请选择：
                    <el-select v-model="lastly">
                        <el-option v-for="item in options" 
                        :key="item.value"
                        :value="item.value"
                        :label="item.label"></el-option>
                    </el-select>
                </div>
                <div>
                  <span class="stock-lately-rate">累计涨跌幅: {{currentIndex.lately[this.lastly].rate}}</span>
                </div>

            </div>
            <div v-else-if="indexName == 'zhishu'" class="stock-lately">
                <div class="stock-lately-select">
                  请选择：
                    <el-select v-model="lastly">
                        <el-option v-for="item in options" 
                        :key="item.value"
                        :value="item.value"
                        :label="item.label"></el-option>
                    </el-select>
                </div>
                <div>
                  <div>
                    <span class="stock-lately-rate">累计涨跌幅: {{currentIndex.lately[this.lastly].rate}}</span>
                    <span class="stock-lately-maxRiseDays">最大连涨天数: {{currentIndex.lately[this.lastly].maxRiseDays}}</span>
                    <span class="stock-lately-maxDropDays">最大连跌天数: {{currentIndex.lately[this.lastly].maxDropDays}}</span>
                  </div>
                  <div>
                    <span class="stock-lately-maxSpot">最低点: {{currentIndex.lately[this.lastly].maxSpot.num}} 时间为: {{currentIndex.lately[this.lastly].maxSpot.date}}</span>
                    <span class="stock-lately-minSpot">最高点: {{currentIndex.lately[this.lastly].minSpot.num}} 时间为: {{currentIndex.lately[this.lastly].minSpot.date}}</span>
                  </div>
                </div>
            </div>
            </el-main>
        </el-container>
    </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "StockDisplayArea",
  props: ["selectVal"],
  data() {
    return {
      lastly: "最近一周",
      options: [
        {
          value: "最近一周",
          label: "最近一周"
        },
        {
          value: "最近一月",
          label: "最近一月"
        },
        {
          value: "最近一年",
          label: "最近一年"
        }
      ]
    };
  },
  methods: {},
  computed: {
    notShow() {
      return this.selectVal.length == 2 ? false : true;
    },
    indexName() {
      if (this.selectVal.length == 2) {
        return this.selectVal[0];
      } else {
        return "other";
      }
    },
    currentIndex() {
      let ret = {};
      this.$store.getters["follow/stocks"][this.selectVal[0]].forEach(item => {
        if (item.id == this.selectVal[1]) {
          ret = item;
        }
      });
      return ret;
    },
    ...mapGetters("follow", ["stocks"])
  }
};
</script>

<style scoped>
.el-header {
  background: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 60px;
}
.el-main {
  background: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 150px;
}

#stock-display-area .stock-name {
  font-size: 24px;
  font-weight: 900;
  font-family: "微软雅黑";
}

#stock-display-area .stock-code {
  font-size: 18px;
  margin-left: 30px;
}
#stock-display-area .stock-number {
  font-size: 22px;
  font-weight: bold;
}
.el-main span {
  font-size: 18px;
  font-family: "仿宋";
  font-weight: bold;
  margin-left: 30px;
}
.el-main div {
  margin-top: -60px;
  text-align: left;
}

.stock-lately div {
  margin-top: -90px;
}
.stock-lately-select {
  margin-left: 30px;
}
</style>


