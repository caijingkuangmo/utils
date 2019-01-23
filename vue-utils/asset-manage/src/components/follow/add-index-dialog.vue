<template>
    <div>
        <el-dialog
            title='添加指标'
            width="50%"
            :visible="visible"
            :before-close="handleClose">
            <el-form ref="form" :model="form" label-width="80px">
                <el-form-item label="指标代号" prop="number">
                    <el-input v-model="form.number"></el-input>
                </el-form-item>
                <el-form-item label="指标类型" prop="type">
                    <el-switch
                        v-model="form.type"
                        active-text="指数"
                        inactive-text="基金">
                    </el-switch>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
                <el-button @click="cancelDialog">取消</el-button>
                <el-button @click="confirmDialog">确认</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
export default {
  name: "AddIndexDialog",
  data() {
    return {
      form: {
        number: "",
        type: true
      },
      visible: false
    };
  },
  watch: {
    visible(newValue) {
        if(!newValue) {this.$refs['form'].resetFields();}
    }
  },
  methods: {
    cancelDialog() {
      this.visible = false;
    },
    confirmDialog() {
      this.visible = false;
      this.$store.dispatch("follow/changeStocks", this.form);
      //直接更新后端和vuex，不用上传到父组件
    },
    showDialog() {
      this.visible = true;
    },
    handleClose(done) {
      this.$confirm("确认关闭？")
        .then(_ => {
          this.visible = false;
          done();
        })
        .catch(_ => {});
    }
  }
};
</script>

<style scoped>
</style>


