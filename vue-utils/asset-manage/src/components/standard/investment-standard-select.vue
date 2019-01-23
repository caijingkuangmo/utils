<template>
    <div>
        <div>
            <el-form ref="form" :model="form">
                <el-form-item label="投资标的">
                    <el-checkbox-group v-model="form.type">
                        <el-checkbox label="指数" name="type"></el-checkbox>
                        <el-checkbox label="基金" name="type"></el-checkbox>
                        <el-checkbox label="买入" name="type"></el-checkbox>
                        <el-checkbox label="卖出" name="type"></el-checkbox>
                    </el-checkbox-group>
                </el-form-item>
                <el-form-item v-if="standardDetailType == 'single'">
                    <el-button type="primary" icon="el-icon-search" @click="search"></el-button>
                    <el-button type="primary" icon="el-icon-delete" @click="del"></el-button>
                    <el-button type="primary" icon="el-icon-edit" @click="edit"></el-button>
                    <el-button type="primary" icon="el-icon-plus" @click="add"></el-button>
                </el-form-item>
                <el-form-item v-else-if="standardDetailType == 'composite'">
                    <el-button type="primary" icon="el-icon-search" @click="compositeSearch"></el-button>
                    <el-button type="primary" icon="el-icon-delete" @click="compositeDel"></el-button>
                    <el-button type="primary" icon="el-icon-edit" @click="compositeEdit"></el-button>
                    <el-button type="primary" icon="el-icon-plus" @click="compositeAdd"></el-button>
                </el-form-item>
            </el-form>
        </div>
        <div>
          <EditStandardDialog ref="dialog" v-if="standardDetailType == 'single'"></EditStandardDialog>
          <EditCompositeDialog ref="compositeDialog" v-else-if="standardDetailType == 'composite'"></EditCompositeDialog>
        </div>
    </div>
</template>

<script>
import { mapState, mapGetters } from "vuex";
import EditStandardDialog from "./edit-standard-dialog.vue";
import EditCompositeDialog from "./edit-composite-dialog.vue";

export default {
  name: "InvestmentStandardSelect",
  data() {
    return {
      form: {
        type: []
      }
    };
  },
  components: {
    EditStandardDialog,
    EditCompositeDialog
  },
  mounted() {
    this.form.type = this.investmentStandardTypes; //默认让所有标的勾上
  },
  methods: {
    search() {
      //获取勾选的types  修改vuex里types  面板里在getters里筛选
      this.$store.dispatch(
        "standard/changeInvestmentStandardTypes",
        this.form.type
      );
    },
    del() {
      //获取vuex里面板索引 删除state里 数据源的数据项，同时出发后端操作， 操作完成后 把面板索引修改成-1
      //加上二次确认
      let panelIndex = this.$store.getters["standard/panelIndex"];
      let singleStandards = this.$store.getters["standard/singleStandards"];
      if (panelIndex.length == 0) {
        this.$message({
          showClose: true,
          message: "请选择要删除的指标",
          type: "warning"
        });
      } else {
        var delItemId = [];
        panelIndex.forEach(index => {
          delItemId.push(singleStandards[index].standardId);
        });
        this.$confirm(`你确认要删除${delItemId}指标?`, "提示", {
          confirmButtonText: "确定",
          cancelButtonText: "取消",
          type: "warning"
        })
          .then(() => {
            delItemId.forEach(id => {
              singleStandards.splice(
                singleStandards.findIndex(item => item.standardId == id),
                1
              );
            });
            this.$message({
              type: "success",
              message: "删除成功"
            });
            this.$store.dispatch('standard/changePanelIndex',[])
          })
          .catch(() => {
            this.$message({
              type: "info",
              message: "已取消删除"
            });
          });
      }
    },
    edit() {
      //模态对话框弹出， 获取面板索引 并获取数据项赋值
      let panelIndex = this.$store.getters["standard/panelIndex"];
      if (panelIndex.length > 0) {
        this.$refs["dialog"].showDialog(true);
      } else {
        this.$message({
          type: "info",
          message: "编辑前请点选数据！"
        });
      }
    },
    add() {
      //模态对话框弹出
      this.$refs["dialog"].showDialog(false);
    },
    compositeSearch() {
      this.$store.dispatch("standard/changeInvestmentStandardTypes",this.form.type);
    },
    compositeDel() {
      let compositePanelIndex = this.$store.getters["standard/compositePanelIndex"];
      let compositeStandards = this.$store.getters["standard/compositeStandards"];
      if (compositePanelIndex.length == 0) {
        this.$message({
          showClose: true,
          message: "请选择要删除的指标",
          type: "warning"
        });
      } else {
        var delItemId = [];
        compositePanelIndex.forEach(index => {
          delItemId.push(compositeStandards[index].standardId);
        });
        this.$confirm(`你确认要删除${delItemId}指标?`, "提示", {
          confirmButtonText: "确定",
          cancelButtonText: "取消",
          type: "warning"
        })
          .then(() => {
            delItemId.forEach(id => {
              compositeStandards.splice(
                compositeStandards.findIndex(item => item.standardId == id),
                1
              );
            });
            this.$message({
              type: "success",
              message: "删除成功"
            });
            this.$store.dispatch('standard/changeCompositePanelIndex',[])
          })
          .catch(() => {
            this.$message({
              type: "info",
              message: "已取消删除"
            });
          });
      }
    },
    compositeEdit() {
      let compositePanelIndex = this.$store.getters["standard/compositePanelIndex"];
      if (compositePanelIndex.length > 0) {
        this.$refs["compositeDialog"].showDialog(true);
      } else {
        this.$message({
          type: "info",
          message: "编辑前请点选数据！"
        });
      }
    },
    compositeAdd() {
      this.$refs["compositeDialog"].showDialog(false);
    }
  },
  computed: {
    ...mapGetters("standard", ["investmentStandardTypes", "standardDetailType"])
  }
};
</script>

<style scoped>
.el-form {
  width: 500px;
}
.el-button {
  margin-left: 30px;
}
.el-form-item {
  display: inline;
}
</style>


