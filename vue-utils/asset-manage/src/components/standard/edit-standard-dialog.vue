<template>
    <div id="edit-standard-dialog">
        <el-dialog
            :title="dialogTitle"
            :visible="visible"
            width="70%"
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
                                <el-switch v-model="form.investmentStandard.standardType" 
                                    active-text="指数"
                                    active-color="#13ce66"
                                    inactive-text="基金"
                                    inactive-color="#ff4949"></el-switch>
                            </el-form-item>
                        </el-form>
                        <el-form ref="form" :model="form" label-width="100px" v-else-if="activeStep==1">
                            <el-form-item label="监控对象">
                                <el-select v-model="form.investmentStandard.standardObject.code" placeholder="请选择监控对象">
                                    <el-option :label="name" v-for="(name,code) in monitorObjSelect" :key="code" :value="code"></el-option>
                                </el-select>
                            </el-form-item>
                            <el-form-item label="监控方式">
                                <el-radio-group v-model="selectIndexType">
                                    <el-radio v-for="(obj,stock) in indexTypes" :key="stock" :label="stock"></el-radio>
                                </el-radio-group>
                            </el-form-item>
                            <el-form-item label="起始时间" v-if="indexTypes[selectIndexType].needStartTime">
                                <el-date-picker type="date" placeholder="选择日期" v-model="form.investmentStandard.time.startDate"></el-date-picker>
                            </el-form-item>
                            <el-form-item label="时间单位" v-if="indexTypes[selectIndexType].needTimeUnit">
                              <el-select v-model="form.investmentStandard.timeUnit">
                                <el-option label="月" value="月"></el-option>
                                <el-option label="周" value="周"></el-option>
                                <el-option label="日" value="日"></el-option>
                              </el-select>
                            </el-form-item>
                            <el-form-item label="设定目标">
                              <StandardTable v-if="indexTypes[selectIndexType].edit.isTable" :unit="form.investmentStandard.unit" :timeUnit="form.investmentStandard.timeUnit" 
                                :rank="form.investmentStandard.rank.rankMap" @getRank="getRank"></StandardTable>
                              <div v-else>
                                <el-input v-model="form.investmentStandard.targetValue" style="width:220px;"></el-input>
                                {{form.investmentStandard.unit}}
                                <span v-if="selectIndexType == '累计天数'">{{form.investmentStandard.timeUnit}}</span>
                              </div>
                            </el-form-item>
                            <el-form-item label="单位目标" v-if="indexTypes[selectIndexType].edit.isTable && indexTypes[selectIndexType].edit.hasEvery">
                              <el-input v-model="form.investmentStandard.rank.every" style="width:220px;"></el-input>
                              {{form.investmentStandard.unit}}{{form.investmentStandard.timeUnit ? `/${form.investmentStandard.timeUnit}` : ""}}
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
import config from "@/config/config.js";
import StandardTable from "./standard-table.vue";
import moment from "moment";

export default {
  name: "EditStandardDialog",
  data() {
    return {
      visible: false,
      activeStep: 0,
      config,
      confirmButtonText: "下一步",
      selectIndexType2: "",
      dialogTitle: "添加",
      form2: {
        standardName: "",
        standardDescribe: "",
        businessSignals: true,
        sendMessage: {
          title: "",
          content: ""
        },
        investmentStandard: {
          standardType: true,
          standardObject: {
            code: "",
            name: ""
          },
          indexType: "",
          timeUnit: "",
          unit: "",
          time: {
            startDate: moment()
          },
          rank: {
            rankMap: [
              {
                id: 1,
                tm: "",
                val: ""
              }
            ],
            every: ""
          },
          targetValue: ""
        }
      },
      form: {}
    };
  },
  created() {
    this.form = this.form2;
  },
  methods: {
    cancelDialog() {
      this.visible = false;
      this.activeStep = 0;
      this.confirmButtonText = "下一步";
      this.form = this.form2;
    },
    showDialog(isEdit) {
      this.visible = true;
      if (isEdit) {
        this.dialogTitle = "编辑";
        let singleStandards = this.$store.getters["standard/singleStandards"];
        this.form =
          singleStandards[this.$store.getters["standard/panelIndex"][0]];
        this.selectIndexType2 = this.form.investmentStandard.indexType;
      } else {
        (this.dialogTitle = "添加"), (this.form = this.form2);
      }
    },
    confirmDialog() {
      this.activeStep++;
      if (this.activeStep == 2) {
        this.confirmButtonText = "确认";
        this.form.investmentStandard.standardObject.name = this.monitorObjSelect[
          this.form.investmentStandard.standardObject.code
        ];
        this.form.investmentStandard.indexType = this.selectIndexType2;
      } else if (this.activeStep > 2) {
        this.visible = false;
        this.activeStep = this.activeStep - 3;
        this.confirmButtonText = "下一步";
        this.form.investmentStandard.indexType = this.selectIndexType;
        this.form = this.form2;
      }
    },
    closeDialog() {
      this.visible = false;
      this.confirmButtonText = "下一步";
      this.activeStep = 0;
      this.form = this.form2;
    },
    getRank(rank) {
      this.form.investmentStandard.rank.rankMap = rank;
    }
  },
  computed: {
    monitorObjSelect() {
      if (this.form.investmentStandard.standardType) {
        return this.monitorIndexMap["指数"];
      } else {
        return this.monitorIndexMap["基金"];
      }
    },
    indexTypes() {
      if (this.form.investmentStandard.standardType) {
        return this.config.StockMarketIndexTypes;
      } else {
        return this.config.fundIndexTypes;
      }
    },
    selectIndexType: {
      get() {
        if (this.form.investmentStandard.standardType) {
          this.selectIndexType2 = this.selectIndexType2 && Object.keys(this.indexTypes).includes(this.selectIndexType2)
            ? this.selectIndexType2
            : "固定点";
        } else {
          this.selectIndexType2 = this.selectIndexType2 && Object.keys(this.indexTypes).includes(this.selectIndexType2)
            ? this.selectIndexType2
            : "持仓增长率";
        };
        this.form.investmentStandard.unit = this.indexTypes[
          this.selectIndexType2
        ].unit;
        return this.selectIndexType2;
      },
      set(val) {
        this.selectIndexType2 = val;
      }
    },
    ...mapGetters("standard", ["monitorIndexMap"])
  },
  components: {
    StandardTable
  }
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


