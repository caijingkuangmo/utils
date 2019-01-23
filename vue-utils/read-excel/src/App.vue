<template>
  <div id="app">
    测试excel读取
    https://blog.csdn.net/liyi_mowu/article/details/84768140
    <input type="file" ref="upload" accept=".xls,.xlsx" class="outputlist_upload">
  </div>
</template>

<script>
import XLSX from "xlsx";
export default {
  name: "app",
  data() {
    return {
      outputs: []
    };
  },
  mounted() {
    this.$refs.upload.addEventListener("change", e => {
      //绑定监听表格导入事件
      this.readExcel(e);
    });
  },
  methods: {
    readExcel(e) {
      //表格导入
      var that = this;
      const files = e.target.files;
      console.log(files);
      if (files.length <= 0) {
        //如果没有文件名
        return false;
      } else if (!/\.(xls|xlsx)$/.test(files[0].name.toLowerCase())) {
        this.$Message.error("上传格式不正确，请上传xls或者xlsx格式");
        return false;
      }

      const fileReader = new FileReader();
      fileReader.onload = ev => {
        try {
          const data = ev.target.result;
          const workbook = XLSX.read(data, {
            type: "binary"
          });
          const wsname = workbook.SheetNames[0]; //取第一张表
          const ws = XLSX.utils.sheet_to_json(workbook.Sheets[wsname]); //生成json表格内容
          console.log(ws);
          that.outputs = []; //清空接收数据
          //编辑数据
          for (var i = 0; i < ws.length; i++) {
            var sheetData = {
              address: ws[i].addr,
              value: ws[i].value
            };
            that.outputs.push(sheetData);
          }
          this.$refs.upload.value = "";
        } catch (e) {
          return false;
        }
      };
      fileReader.readAsBinaryString(files[0]);
    }
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
