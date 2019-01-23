<template>
    <div id="edit-standard-dialog">
        <el-dialog
            :title="dialogTitle"
            :visible="visible"
            width="50%"
            @close="closeDialog"
            center>
                <div>
                  <div class="standard-set-step">
                    <el-steps :active="activeStep" finish-status="success" simple style="height:30px;">
                      <el-step title="设置标题"></el-step>
                      <el-step title="设置指标"></el-step>
                      <el-step title="设置信息"></el-step>
                    </el-steps>
                  </div>
                  <div class="fill-form">
                        <el-form ref="form" :model="form" label-width="100px" v-if="activeStep==0">
                            <el-form-item label="指标名称">
                                <el-input v-model="form.standardName"></el-input>
                            </el-form-item>
                            <el-form-item label="指标描述">
                                <el-input type="textarea" v-model="form.standardDescribe"></el-input>
                            </el-form-item>
                            <el-form-item label="信号类型">
                                <el-switch v-model="form.businessSignals" active-text="买入" inactive-text="卖出"></el-switch>
                            </el-form-item>
                            <el-form-item label="监控类型">
                                <el-switch v-model="form.standardType" 
                                    active-text="指数"
                                    active-color="#13ce66"
                                    inactive-text="基金"
                                    inactive-color="#ff4949"></el-switch>
                            </el-form-item>
                        </el-form>
                        <el-form ref="form" :model="form" label-width="100px;" v-else-if="activeStep==1">
                            <el-form-item label="监控对象">
                                <el-select v-model="form.standardObject.code" placeholder="请选择监控对象">
                                    <el-option :label="name" v-for="(name,code) in monitorObjSelect" :key="code" :value="code"></el-option>
                                </el-select>
                            </el-form-item>
                            <el-form-item label="逻辑关系">
                              <el-switch v-model="form.logicalRelation.relation"
                                active-text="与" inactive-text="或"
                                active-color="#13ce66" inactive-color="#ff4949">
                              </el-switch>
                            </el-form-item>
                            <el-form-item label="点选指标">
                              <el-transfer
                                filterable
                                :filter-method="filterMethod"
                                :titles="['source','target']"
                                v-model="selectIndexs"
                                @change="handleChange"
                                :data="data2"></el-transfer>
                            </el-form-item>
                        </el-form>
                        <el-form ref="form" :model="form" label-width="100px" v-else-if="activeStep==2">
                            <el-form-item label="邮件标题">
                                <el-input v-model="form.sendMessage.title"></el-input>
                            </el-form-item>
                            <el-form-item label="邮件内容">
                                <el-input type="textarea" v-model="form.sendMessage.content"></el-input>
                            </el-form-item>
                        </el-form>
                  </div>
                </div>
                <span slot="footer" class="dialog-footer">
                    <el-button @click="cancelDialog">取消</el-button>
                    <el-button type="primary" @click="confirmDialog">{{confirmButtonText}}</el-button>
                </span>
        </el-dialog>
    </div>
</template>
<script>
import { mapGetters } from "vuex";

export default {
  name: "EditStandardDialog",
  data() {
    return {
      visible: false,
      activeStep: 0,
      confirmButtonText: "下一步",
      dialogTitle: "添加",
      selectIndexs: [],
      form2: {
        standardName: "",
        standardDescribe: "",
        sendMessage: {
          title: "",
          content: ""
        },
        businessSignals: true,
        standardType: true,
        standardObject: {
          code: "",
          name: ""
        },
        logicalRelation: {
          relation: true,
          indexs: []
        }
      },
      form: {}
    };
  },
  created() {
    this.form = this.form2;
    this.selectIndexs = [];
  },
  methods: {
    cancelDialog() {
      this.visible = false;
      this.activeStep = 0;
      this.form = this.form2;
      this.confirmButtonText = "下一步";
      this.selectIndexs = [];
    },
    showDialog(isEdit) {
      this.visible = true;
      if (isEdit) {
        this.dialogTitle = "编辑";
        let compositeStandards = this.$store.getters[
          "standard/compositeStandards"
        ];
        this.form =
          compositeStandards[
            this.$store.getters["standard/compositePanelIndex"][0]
          ];
        this.selectIndexs = this.form.logicalRelation.indexs;
      } else {
        (this.dialogTitle = "添加"),
          (this.form = this.form2),
          (this.selectIndexs = []);
      }
    },
    confirmDialog() {
      this.activeStep++;
      if (this.activeStep == 2) {
        this.confirmButtonText = "确认";
        this.form.standardObject.name = this.monitorObjSelect[
          this.form.standardObject.code
        ];
        this.form.logicalRelation.indexs = this.selectIndexs;
      } else if (this.activeStep > 2) {
        this.visible = false;
        this.activeStep = 0;
        this.confirmButtonText = "下一步";

        //触发发送数据动作

        this.form = this.form2;
        this.selectIndexs = [];

      }
    },
    closeDialog() {
      this.visible = false;
      this.confirmButtonText = "下一步";
      this.activeStep = 0;
      this.form = this.form2;
      this.selectIndexs = [];
    },
    filterMethod(query, item) {
      return item.label.indexOf(query) > -1;
    },
    handleChange(value, direction, movedKeys) {
      console.log(value, direction, movedKeys);
      console.log(this.value2);
    }
  },
  computed: {
    monitorObjSelect() {
      if (this.form.standardType) {
        return this.monitorIndexMap["指数"];
      } else {
        return this.monitorIndexMap["基金"];
      }
    },
    data2() {
      const data = [];
      this.followOptions.forEach((indexItem, index) => {
        indexItem.options.forEach(item => {
          data.push({
            label: `${item.label} ${indexItem.label}`,
            key: item.value
          });
        });
      });
      return data;
    },
    ...mapGetters("standard", ["monitorIndexMap"]),
    ...mapGetters("asset", ["followOptions"])
  },
  components: {}
};
</script>

<style>
#edit-standard-dialog .el-step__icon {
  vertical-align: middle;
}
#edit-standard-dialog .el-dialog__title {
  font-size: 20px;
  font-weight: bold;
  font-family: "宋体";
}
</style>

<style scoped>
.standard-set-step {
  margin-top: -60px;
}
.fill-form {
  margin-top: 20px;
}
</style>


