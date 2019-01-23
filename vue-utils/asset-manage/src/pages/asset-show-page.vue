<template>
    <div id="asset-show">
        <div id="asset-menu">
            <el-menu default-active="1"
            @open="handleOpen" 
            @close="handleClose"
            :collapse="isCollapse" style="width:95%;">
                <el-menu-item index="1" @click="showTotalAssetDetail">
                    <i class="el-icon-menu">总资产</i>
                    <span slot="title">总资产</span>
                </el-menu-item>
                <el-submenu index="2">
                    <template slot="title">
                        <i class="el-icon-goods">持仓明细</i>
                        <span slot="title">持仓明细</span>
                    </template>
                    <el-menu-item-group>
                        <el-menu-item :index="getMenuDetailIndex(2,index)" v-for="(fund, index) in holdDetails" :key="index" @click="showFundDetail(index)">{{fund.fundName}}</el-menu-item>
                    </el-menu-item-group>
                </el-submenu>
                <el-menu-item index="3" @click="showTradeDetail">
                    <i class="el-icon-document">交易流水明细</i>
                    <span slot="title">交易流水明细</span>
                </el-menu-item>
            </el-menu>
        </div>
        <div id="asset-content">
            <AssetShowDetail></AssetShowDetail>
        </div>
    </div>
</template>

<script>
import AssetShowDetail from "@/components/asset/asset-show-detail.vue";

export default {
  name: "AssetShowPage",
  data() {
    return {
      isCollapse: true,
      holdDetails: [],
      // currentFundIndex: 0
    };
  },
  created() {
    this.holdDetails = this.$store.getters["asset/holdDetails"];
    //   this.currentFundIndex = this.$store.getters['asset/currentFundIndex']
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    getMenuDetailIndex(menuIndex, index) {
      return `${menuIndex}-${index + 1}`;
    },
    showFundDetail(index) {
      this.$store.dispatch("asset/changeCurrentFundIndex", index);
      this.$store.dispatch("asset/changeAssetDetailType", "fund");
      this.$store.dispatch(
        "asset/changeFundName",
        this.holdDetails[index].fundCode
      );
      // this.currentFundIndex = this.$store.getters["asset/currentFundIndex"];
      // console.log(this.currentFundIndex);
    },
    showTradeDetail() {
      this.$store.dispatch("asset/changeAssetDetailType", "trade");
      this.$store.dispatch("asset/changeFundName", "00000");
    },
    showTotalAssetDetail(){
      this.$store.dispatch("asset/changeAssetDetailType", "total");
    }
  },
  components: {
    AssetShowDetail
  }
};
</script>

<style scoped>
#asset-show {
  font-size: 0;
}
#asset-menu {
  display: inline-block;
  font-size: 16px;
  width: 15%;
  vertical-align: top;
}
#asset-content {
  display: inline-block;
  font-size: 16px;
  width: 85%;
}
</style>


