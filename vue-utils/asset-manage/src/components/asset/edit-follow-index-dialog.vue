<template>
    <div id="edit-dialog">
        <el-dialog 
            title="编辑指标"
            :visible="dialogVisible"
            width="40%"
            :before-close="handleClose">
                <div id="dialog-content">
                    <div id="table-body">
                        <table border="1" bordercolor="black" style="border-collapse:collapse;width:100%;">
                            <tbody :model="monitorIndexs">
                                <tr v-for="(follow, index) in monitorIndexs" :key="index">
                                    <th width="10%">{{index+1}}</th>
                                    <td width="80%">
                                        <SelectTag :selectVal="follow.id" :index='index' @getSelectVal='getSelectVal'></SelectTag>
                                    </td>
                                    <td width="10%">
                                        <el-button type="primary" @click="deleteRow(index)">删除</el-button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <div id="add-button">
                        <el-button type="primary" @click="addRow">添加</el-button>
                    </div>
                </div>
                <div id="dialog-buttons">
                    <el-button @click="cancelDialog">取消</el-button>
                    <el-button @click="confirmDialog" type="primary">确认</el-button>
                </div>
        </el-dialog>
    </div>
</template>

<script>
import SelectTag from "./select-edit-tag.vue";

export default {
  name: "EditFollowIndexDialog",
  created() {
    //只要获取当前基金指标
  },
  data() {
    return {
      dialogVisible: false,
    };
  },
  methods: {
    deleteRow(index) {
      this.monitorIndexs.splice(index, 1);
    },
    addRow() {
      this.monitorIndexs.push({id:'',name:''});
    },
    showDialog() {
      this.dialogVisible = true;
    },
    cancelDialog() {
      this.dialogVisible = false;
    },
    confirmDialog() {
      this.dialogVisible = false;
      this.$store.dispatch("asset/changeMonitorIndexs", this.monitorIndexs); //发送还要个去空值操作
    },
    handleClose(done) {
      this.$confirm("确认关闭？")
        .then(_ => {
          done();
          this.dialogVisible = false;
        })
        .catch(_ => {});
    },
    getSelectVal(index, id, val) {
      this.monitorIndexs.splice(index,1,{id:id, name:val});
      // this.monitorIndexs[index] = val;
    }
  },
  computed: {
    monitorIndexs() {
      const holdDetails = this.$store.getters["asset/holdDetails"];
      const currentFundIndex = this.$store.getters["asset/currentFundIndex"];
      return holdDetails[currentFundIndex].details.monitorIndexs;;
    }
  },
  components: {
    SelectTag
  }
};
</script>

<style scoped>
#edit-dialog {
  text-align: center;
}
#add-button {
  text-align: right;
}
#dialog-buttons {
  margin-top: 20px;
}
</style>


