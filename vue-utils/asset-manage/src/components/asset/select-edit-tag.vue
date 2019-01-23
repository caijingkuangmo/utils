<template>
    <div id="follow-select">
        <el-select v-model="selectValue" placeholder="请选择" style="width:100%" @change="sendSelectVal">
            <el-option-group
                v-for="group in followOptions"
                :key="group.label"
                :label="group.label">
                    <el-option
                        v-for="item in group.options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value"></el-option>
            </el-option-group>
        </el-select>
    </div>
</template>

<script>
/**
 * 1.select组件向上传值
 * 2.值与标签对应问题  ---存在报错
 */

export default {
  name: "SelectEditTag",
  data() {
    return {
      // selectVal:"2",
      followOptions: [],
      selectValue: this.selectVal
    };
  },
  created() {
    this.followOptions = this.$store.getters["asset/followOptions"];
  },
  methods: {
    sendSelectVal() {
      this.followOptions.forEach(indexItem => {
        indexItem.options.forEach(item => {
          if (item.value == this.selectValue) {
            this.$emit(
              "getSelectVal",
              this.index,
              this.selectValue,
              item.label
            );
            return;
          }
        });
      });
    }
  },
  props: ["selectVal", "index"]
};
</script>

<style scoped>
</style>


