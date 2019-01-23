<template>
    <div id="trade-table">
        <el-table
            :data="filterTradeRecords"
            border
            style="width:100%"
            :default-sort="{prop:'date', order:'descending'}"
            :row-class-name="tableRowClassName">
                <el-table-column
                    prop="date"
                    label="日期"
                    sortable
                    :filters="[{text:'2016-02-01',value:'2016-05-01'},{text:'2017-04-01',value:'2017-04-01'}]"
                    :filter-method="filterHandler"
                    width="120">
                </el-table-column>
                <el-table-column
                    prop="fundName"
                    label="基金名称"
                    sortable
                    width="240">
                </el-table-column>
                <el-table-column
                    prop="realTimeAmount"
                    label="实时金额"
                    sortable
                    width="110">
                </el-table-column>
                <el-table-column
                    prop="intoWarehouseAmount"
                    label="进仓金额"
                    sortable
                    width="110">
                </el-table-column>
                <el-table-column
                    prop="profitAndLossAmount"
                    label="盈亏金额"
                    sortable
                    width="110">
                </el-table-column>
                <el-table-column
                    prop="profitAndLossRatio"
                    label="盈亏比"
                    sortable
                    width="100">
                </el-table-column>
                <el-table-column
                    prop="HoldingTime"
                    label="持仓时间"
                    sortable
                    width="110">
                </el-table-column>
                <el-table-column
                    prop="monitorIndex"
                    label="监控指标"
                    sortable
                    :sort-method="monitorIndexSort"
                    width="240">
                        <template slot-scope="scope">
                            <PencilSelect :scp="scope"></PencilSelect>
                        </template>
                </el-table-column>
        </el-table>
    </div>
</template>

<script>
/**
 * 
 */
import { mapState, mapGetters } from "vuex";
import PencilSelect from './pencil-select.vue'

export default {
  name: "TradeTable",
  data () {
      return {

      }
  },
  computed: mapGetters("asset", ["filterTradeRecords"]),
  methods: {
    tableRowClassName({ row, rowIndex }) {
      if (rowIndex === 1) {
        return "warning-row";
      } else if (rowIndex === 3) {
        return "success-row";
      }
      return "";
    },
    monitorIndexSort(a, b) {
      console.log(a, b);
      alert("你需要编写排序");
    },
    filterHandler(value, row, column) {
      console.log("filterHanler-->", value);
      const property = column["property"];
      return row[property] === value;
    }
  },
  components:{
      PencilSelect
  }
};
</script>
<style>
#trade-table .cell {
  text-align: center;
}
.el-table .warning-row {
  background: oldlace;
}
.el-table .success-row {
  background: #f0f9eb;
}
</style>

<style scoped>
</style>


