<template>
    <div id="single-display-area">
       <el-collapse v-model="activeNames" @change="handleChange">
           <el-collapse-item :title="`${item.standardName}    ${item.standardDescribe}`" :name="index" v-for="(item,index) in filterStandards" :key="index">
               <div class="single-details">
                   <div>
                       <span>{{item.businessSignals ? "买入" : "卖出"}}信号</span>
                       <span>{{`${item.investmentStandard.standardType ? "指数" : "基金"}类型    ${item.investmentStandard.standardObject.code}:${item.investmentStandard.standardObject.name}`}}</span>
                    </div>
                    <div>
                        <SingleIndexDetail :dataItem="item"></SingleIndexDetail>
                    </div>
                    <div class="sendMessage">
                        <div class="title">提示信息:</div>
                        <div class="content">{{item.sendMessage.content}}</div>
                    </div>
               </div>
           </el-collapse-item>
        </el-collapse> 
    </div>
</template>

<script>
import { mapGetters } from "vuex";
import SingleIndexDetail from "./single-index-detail.vue";

export default {
  name: "SingleDisplayArea",
  data() {
    return {
      activeNames: []
    };
  },
  computed: {
    ...mapGetters("standard", ["filterStandards"])
  },
  components: {
    SingleIndexDetail
  },
  methods: {
    handleChange(val) {
      this.$store.dispatch("standard/changePanelIndex", val);
    }
  }
};
</script>

<style>
#single-display-area .el-collapse-item__header {
  margin-top: 10px;
  background: rgba(255, 198, 102, 1);
  font-size: 20px;
  font-weight: bold;
  font-family: "宋体";
}
</style>


<style scoped>
.single-details {
  border: 1px solid #eee;
  border-radius: 2px;
  background: rgba(166, 212, 242, 0.2);
}
.single-details span {
  font-size: 22px;
  display: inline-block;
  font-famliy: "宋体";
  margin-top: 20px;
  background: rgba(64, 158, 255, 0.5);
  border-radius: 10px;
  border: 2px solid green;
  padding: 5px 20px;
  margin-bottom: 10px;
}
.sendMessage .title {
  text-align: left;
  font-size: 18px;
  margin-left: 10%;
  margin-top: 20px;
  background: rgba(0, 181, 66, 0.3);
  margin-right: 10%;
}
.sendMessage .content {
  padding-top: 10px;
  padding-bottom: 10px;
  font-size: 16px;
  margin-bottom: 30px;
  margin-left: 10%;
  margin-right: 10%;
  background: rgb(229, 229, 229);
  word-wrap: break-word;
}
</style>


