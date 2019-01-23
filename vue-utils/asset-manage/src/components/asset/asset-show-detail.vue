<template>
    <div id="asset-detail">
        <el-container id="fund-detail-container" v-if="assetDetailType==='fund'">
            <el-header id="pane-header">
                <div>
                    <span class="header-name">{{fund.fundName}}</span>
                    <span class="header-code">{{fund.fundCode}}</span>
                </div>
                <div class="search-button">
                    <el-button type="success" icon="el-icon-search" @click="viewFundDetails">查看基金明细</el-button>
                </div>
            </el-header>
            <el-main id="pane-body">
                <div><span>实时金额:  {{fund.details.realTimeAmount}}元</span><span>进仓金额:  {{fund.details.intoWarehouseAmount}}元</span></div>
                <div><span>盈亏金额:  {{fund.details.profitAndLossAmount}}元</span><span>盈亏比:  {{fund.details.profitAndLossRatio}}%</span></div>
                <div><span>持仓时间:  {{fund.details.HoldingTime}}/月</span></div>
                <div>
                    <div class="follow-index">
                        <div v-for="(v,k) in fund.details.monitorIndexs" :key="k">
                            <span>编号: {{k+1}}</span><span>跟踪指标: {{v.name}}</span>
                        </div>
                        <div class="follow-index-edit-button">
                            <el-button icon="el-icon-edit" type="success" @click="showEditDialog">编辑</el-button>
                        </div>
                    </div>
                </div>
            </el-main>
             <FollowDialog ref="followDialog"></FollowDialog>
        </el-container>
        <el-container id="trade-detail-container" v-else-if="assetDetailType==='trade'">
          <el-header id="trade-header">
            <div id="trade-title">交易明细</div>
            <div id="trade-fund-select">
              <span>基金选择：</span>
              <el-select v-model="tradeSelVal" placeholder="请选择" @change="changeFundName">
                <el-option label="总资产" value="00000">
                </el-option>
                <el-option
                  v-for="item in holdDetails"
                  :key="item.fundCode"
                  :label="item.fundName"
                  :value="item.fundCode">
                </el-option>
              </el-select>
            </div>
          </el-header>
          <el-main>
            <TradeTable></TradeTable>
          </el-main>
        </el-container>
        <el-container id="total-asset-detail-container" v-else-if="assetDetailType==='total'">
            <el-header id='total-header'>
              <div id="total-title">总资产</div>
            </el-header>
            <el-main>
              <div class="total-item-father">
                <div class="total-item">总资产额: {{totalAsset.totalNum}}</div>
                <div class="total-item">
                  <div>盈亏额: {{totalAsset.profitAndLossAmount}}</div>
                  <div>盈亏比: {{totalAsset.profitAndLossRatio}}%</div>
                </div>
                <div class="total-item">持仓时间: {{totalAsset.HoldingTime}}</div>
              </div>
              <div>
                <el-table :data="holdDetails">
                  <el-table-column prop="fundName" label="基金名称" align="center" width="250"></el-table-column>
                  <el-table-column prop="fundCode" label="基金代号" align="center" width="150"></el-table-column>
                  <el-table-column prop="details.realTimeAmount" label="实时金额" align="center" width="150"></el-table-column>
                  <el-table-column prop="details.profitAndLossAmount" label="盈亏额" align="center" width="150"></el-table-column>
                  <el-table-column prop="details.profitAndLossRatio" label="盈亏比" align="center" width="150"></el-table-column>
                  <el-table-column prop="details.HoldingTime" label="持仓时间" align="center" width="150"></el-table-column>
                  <el-table-column label="操作" align="center" width="150">
                    <template slot-scope="scope">
                      <el-button type="primary" @click="enterFundDetailPage(scope.$index, scope.row)">详情</el-button>
                    </template>
                  </el-table-column>
                </el-table>
              </div>
            </el-main>
        </el-container>
    </div>
</template>

<script>
/**
 *
 */
import { mapState, mapGetters } from "vuex";
import FollowDialog from "./edit-follow-index-dialog.vue";
import TradeTable from "./trade-table.vue";

export default {
  name: "AssetShowDetail",
  data() {
    return {
      baseValue: this.$store.state.asset.holdDetails,
      holdDetails: this.$store.getters["asset/holdDetails"]
      // tradeSelectVal: "00000"
    };
  },
  watch: {
    baseValue(newValue, oldValue) {
      console.log(newValue, oldValue);
    }
  },
  created() {
    // console.log(mapGetters);
    // this.holdDetails = this.$store.getters["asset/holdDetails"];
    // this.tradeSelVal = this.$store.getters["asset/tradeSelectVal"];
    // this.currentFundIndex = this.$store.getters["asset/currentFundIndex"];//计算属性渲染时是否自动触发，那是不是就不需要这里创建时触发了？
    // this.currentFund = this.holdDetails[this.currentFundIndex];
  },
  methods: {
    viewFundDetails() {
      this.$store.dispatch("asset/changeAssetDetailType", "trade");
      // this.tradeSelVal = this.$store.getters['asset/tradeSelectVal'];
    },
    showEditDialog() {
      this.$refs.followDialog.showDialog();
    },
    changeFundName() {
      // this.$store.dispatch("asset/changeFundName", this.tradeSelVal);
    },
    enterFundDetailPage(index, row) {
      this.$store.dispatch("asset/changeCurrentFundIndex", index);
      this.$store.dispatch("asset/changeAssetDetailType", "fund");
      this.$store.dispatch(
        "asset/changeFundName",
        this.holdDetails[index].fundCode
      );
    }
  },
  components: {
    FollowDialog,
    TradeTable
  },
  computed: {
    fund() {
      return this.holdDetails[this.$store.state.asset.currentFundIndex];
    },
    ...mapGetters("asset", {
      assetDetailType: "assetDetailType",
      tradeSelectVal: "tradeSelectVal",
      totalAsset: "totalAsset"
    }),
    tradeSelVal: {
      get() {
        return this.$store.getters["asset/tradeSelectVal"];
      },
      set(val) {
        this.$store.dispatch("asset/changeFundName", val);
      }
    }
  }
};
</script>

<style scoped>
#asset-detail {
  width: 100%;
}

.el-header {
  border: solid 1px #eee;
  text-align: center;
  line-height: 60px;
}
.el-main {
  border: solid 1px #eee;
  text-align: center;
}
#pane-header {
  position: relative;
}
.search-button {
  position: absolute;
  top: 0px;
  right: 70px;
}

.header-name {
  font-size: 30px;
  font-weight: bold;
  font-family: "微软雅黑";
}
.header-code {
  vertical-align: bottom;
  margin: 20px;
  font-size: 20px;
}

#pane-body {
  text-align: left;
}

#pane-body span {
  margin: 50px;
  font-size: 18px;
}
#pane-body > div {
  padding: 20px;
  border-top: solid #eee 1px;
  border-bottom: solid #eee 1px;
}
.follow-index {
  font-size: 16px;
  color: gray;
  font-style: oblique;
  border-top: solid #eee 1px;
  border-bottom: solid #eee 1px;
}
.follow-index > div {
  padding: 10px;
}
.follow-index-edit-button {
  text-align: right;
  margin-right: 50px;
}

#trade-title {
  font-size: 30px;
  font-weight: bold;
}

#trade-header {
  position: relative;
}
#trade-fund-select {
  font-size: 16px;
  position: absolute;
  top: 0;
  right: 8%;
}

#total-title {
  font-size: 30px;
  font-weight: bold;
}

.total-item-father {
  height: 120px;
  line-height: 50px;
  margin-bottom: 30px;
  border-bottom: solid 1px #eee;
}

.total-item {
  display: inline-block;
  vertical-align: middle;
  width: 30%;
  font-size: 20px;
  font-weight: 500px;
}
</style>


