<template>
    <div>
        <div>
            <el-form>
                <el-form-item label="请选择指标对象">
                    <el-cascader
                        :options="selectOptions"
                        change-on-select
                        :value="selectVal"
                        @change="changeSelectVal">
                    </el-cascader>
                    <span class="buttons">
                        <el-button type="primary" icon="el-icon-plus" @click="add"></el-button>
                        <el-button type="primary" icon="el-icon-delete" @click="del"></el-button>
                    </span>
                </el-form-item>
            </el-form>
        </div>
        <div>
            <StockDisplayArea :selectVal="selectVal"></StockDisplayArea>
        </div>
        <AddIndexDialog ref='dialog'></AddIndexDialog>
    </div>
</template>

<script>
/**
 * 监控哪些内容，怎么监控
 * 1.怎么监控：前期不支持灵活，统一网站，去东方财富上爬取，配置里只需要：
 *   两个：提供代号，指定类型（指数还是基金）
 *
 * 2.监控哪些内容
 *  指数：  名称，代号，多少点，时间  涨跌幅   最近一周，最近一月，最近一年   累计涨跌幅  最大连涨天数 最大连跌天数 最低点(时间)  最高点（时间）  后面可加极端涨跌幅天（比如3% 5%）
 *  基金：  名称，代号，基金净值，时间 涨跌幅  最近一周，最近一月，最近一年   累计涨跌幅
 */
import StockDisplayArea from "@/components/follow/stock-display-area.vue";
import AddIndexDialog from "@/components/follow/add-index-dialog.vue"
import {mapGetters} from 'vuex'

export default {
  name: "StockFollowPage",
  data() {
    return {
      selectVal: [],
    };
  },
  computed:{
    ...mapGetters('follow',['selectOptions','stocks'])
  },
  methods: {
    changeSelectVal(value) {
      this.selectVal = value;
    },
    add() {
      this.$refs.dialog.showDialog();
    },
    del() {
      //获取选中值  this.selectVal 进行删除
      if (this.selectVal.length != 2) {
        this.$message({
          showClose: true,
          message: "请选择要删除的具体指标",
          type: "warning"
        });
      } else {
        var delIndex;
        var delIndexName;
        this.stocks[this.selectVal[0]].forEach((item,index) => {
          if (item.id == this.selectVal[1]) {
            delIndex = index;
            delIndexName = item.name;
          }
        })
        this.$confirm(`你确认要删除[${delIndexName}]指标?`, "提示", {
          confirmButtonText: "确定",
          cancelButtonText: "取消",
          type: "warning"
        })
          .then(() => {
            this.$store.dispatch('follow/delStock', {indexType:this.selectVal[0], index:delIndex});
            this.selectVal = [];
            this.$message({
              type: "success",
              message: "删除成功"
            });
          })
          .catch(() => {
            this.$message({
              type: "info",
              message: "已取消删除"
            });
          });
      }
    },
  },
  components: {
    StockDisplayArea,
    AddIndexDialog
  }
};
</script>

<style scoped>
.buttons{
  margin-left:80px;
}
</style>


