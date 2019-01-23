<template>
    <div id="composite-display-area">
       <el-collapse v-model="activeNames" @change="handleChange">
           <el-collapse-item :title="`${item.standardName}    ${item.standardDescribe}`" :name="index" v-for="(item,index) in filterCompositeStandards" :key="index">
               <div class="composite-details">
                   <div>
                       <span>{{item.businessSignals ? "买入" : "卖出"}}信号</span>
                       <span>{{`${item.standardType ? "指数" : "基金"}类型    ${item.standardObject.code}:${item.standardObject.name}`}}</span>
                    </div>
                    <div class="logical-relation">
                      <div class="condition" v-if="item.logicalRelation.relation">有指标成立触发</div>
                      <div class="condition" v-else>指标同时成立触发</div>
                      <div v-for="(selItem, index) in selectIndexs(item)" :key="index">
                        <span>{{selItem.label}}</span><span>{{selItem.desc}}</span>
                      </div>
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

export default {
  name: "CompositeDisplayArea",
  data() {
    return {
      activeNames: []
    };
  },
  computed: {
    ...mapGetters("standard", ["filterCompositeStandards"]),
    ...mapGetters("asset", ["followOptions"])
  },
  components: {},
  methods: {
    handleChange(val) {
      this.$store.dispatch("standard/changeCompositePanelIndex", val);
    },
    selectIndexs(item) {
      var sel = [];
      this.followOptions.forEach(indexItem => {
        indexItem.options.forEach(optionItem => {
          if (item.logicalRelation.indexs.includes(optionItem.value)) {
            sel.push(optionItem);
          }
        });
      });
      return sel;
    }
  }
};
</script>

<style>
#composite-display-area .el-collapse-item__header {
  margin-top: 10px;
  background: rgba(255, 198, 102, 1);
  font-size: 20px;
  font-weight: bold;
  font-family: "宋体";
}
</style>


<style scoped>
.composite-details {
  margin-top: 20px;
  border: 1px solid #eee;
  border-radius: 2px;
  background: rgba(166, 212, 242, 0.2);
  margin-left: 10%;
  margin-right: 10%;
  margin-left:5px;
  margin-right:5px;
}
.composite-details span {
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
.logical-relation {
  text-align: left;
}
.condition {
  background: rgba(206, 130, 72, 0.3);
  font-size: 20px;
  font-weight: 900;
  font-family: "仿宋";
  padding-left: 30px;
}
.logical-relation span {
  font-size: 18px;
  background: rgba(140, 220, 254, 0.5);
  border: 0px;
  margin-top: 15px;
  margin-left: 30px;
}
.sendMessage .title {
  text-align: left;
  font-size: 18px;
  margin-top: 10px;
  background: rgba(0, 181, 66, 0.3);
  padding-left: 30px;
}
.sendMessage .content {
  padding-top: 10px;
  padding-bottom: 10px;
  font-size: 16px;
  margin-bottom: 30px;
  background: rgb(229, 229, 229);
  word-wrap: break-word;
}
</style>


