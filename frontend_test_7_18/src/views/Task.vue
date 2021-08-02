<template>
  <div>
    <v-data-table :headers="headers" :items="desserts"  :items-per-page="5" class="elevation-1">
     <template v-slot:item.actions="{ item }">
      <v-btn  color="green" class="mr-2" @click="checkReport(item)"> 查看报告 </v-btn>
      <v-btn  @click="deleteItem(item)"> 删除报告 </v-btn>
     </template>
    </v-data-table>
  </div>
</template>
<script>
export default {
  created() {
        this.initialize();
    // this.$api.task.getTaskData('').then(res=>{
    //         console.log(res)
    //     })
  },
  methods: {
      // initialize(){
      //   this.$api.task.getTaskData().then(res=>{
      //           console.log(res)
      //       })
      // }
    initialize() {
      // let post_data = {
      // }
      this.$api.task.getTaskData().then(res=>{
              this.desserts=res.data.msg.data
          })
    },

    checkReport(item) {
      console.log(item)
      window.open(item.report)
    },
    
  },

  data() {
    return {
      headers: [
        {
          text: "任务ID",
          align: "start",
          sortable: false,
          value: "id",
        },
        { text: "任务描述", value: "remark" },
        { text: "创建时间", value: "create_at", sortable: false },
        { text: "Actions", value: "actions"},
      ],
      desserts: [
        
      ],
    };
  },
};
</script>