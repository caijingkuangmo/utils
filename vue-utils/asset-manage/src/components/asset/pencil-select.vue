<template>
    <div id="pencil-select">
        <div id="pencil-icon">
            <i :class="{'el-icon-edit':isEdit == false, 'el-icon-check':isEdit==true}" @click="beginEdit"></i>
        </div>
        <el-select v-model="value" v-if="isEdit" placeholder="请选择" style="width:80%">
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
        <span v-else>{{value}}</span>

    </div>
</template>

<script>
/**
 * 组件间select值传递
 */
export default {
    name:"PencilSelect",
    data () {
        return {
            followOptions:[],
            isEdit:false,
            val: this.scp.row['monitorIndex'],
        }
    },
    created () {
        this.followOptions = this.$store.getters['asset/followOptions'];
    },
    props:['scp'],
    methods: {
        beginEdit(){
            if (this.isEdit) {
                console.log('发送修改数据');
            }
            this.isEdit = !this.isEdit;
        }
    },
    computed:{
        value:{
            get(){
                return this.val;
            },
            set(val){
                this.val = val;
            }
        }
    }
}
</script>

<style scoped>
#pencil-select{
    position: relative;
}
#pencil-icon{
    position: absolute;
    top:0;
    right: 0;
}
</style>


