<template>
<div id="standard-table">
    <div id="edit-table-body">
        <table border="1" bordercolor="black" style="border-collapse:collapse;width:220px;">
        <thead>
            <tr>
            <th>时长{{timeUnit ? `(${timeUnit})` : ''}}</th>
            <th>增长值({{unit}})</th>
            <th>操作</th>
            </tr>
        </thead>
        <tbody :model="rank">
            <tr v-for="(rankItem,index) in rank" :key="index">
            <td width="80px"><el-input v-model="rankItem.tm" @blur="sendRank"></el-input></td>
            <td width="80px"><el-input v-model="rankItem.val" @blur="sendRank"></el-input></td>
            <td width="55px"><el-button type="primary" icon="el-icon-minus" @click="deleteRow(rankItem.id)"></el-button></td>
            </tr>
        </tbody>
        </table>
    </div>
    <div id="add-button">
        <el-button type="primary" icon="el-icon-plus" @click="addRow"></el-button>
    </div>
</div>
</template>

<script>
export default {
  name: "StandardTable",
  methods: {
    deleteRow(id) {
      this.rank.splice(
        this.rank.findIndex(item => {
          return item.id == id;
        }),
        1
      );
    },
    addRow() {
      this.rank.push({
        id: this.rank.length > 0 ? this.rank[this.rank.length - 1].id + 1 : 1,
        tm: "",
        val: ""
      });
    },
    sendRank(){
       this.$emit('getRank', this.rank); 
    }
  },
  data() {
    return {};
  },
  props: ["rank","timeUnit","unit"],
};
</script>

<style scoped>
#add-button{
  margin-left:162px;
}
</style>


