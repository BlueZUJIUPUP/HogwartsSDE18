<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="desserts"
      :items-per-page="5"
      class="elevation-1"
    >
    
     <template v-slot:item.actions="{ item }">
      <v-btn  color="green" class="mr-2" @click="editItem(item)"> 查看报告 </v-btn>
      <v-btn  @click="deleteItem(item)"> 删除报告 </v-btn>
     </template>
    </v-data-table>
  </div>
</template>
<script>
export default {
  data() {
    return {
      headers: [
        {
          text: "任务ID",
          align: "start",
          sortable: false,
          value: "taskid",
        },
        { text: "任务描述", value: "remark" },
        { text: "Actions", value: "actions", sortable: false },
      ],
      desserts: [
        {
          taskid: "Frozen Yogurt",
          remark: 159,
        },
        {
          taskid: "Frozen Yogurt",
          remark: 159,
        },
      ],
    };
  },
};
</script>