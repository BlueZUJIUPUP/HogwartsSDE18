<template>
  <v-data-table
    v-model="selected"
    :single-select="singleSelect"
    item-key="id"
    show-select
    :headers="headers"
    :items="desserts"
    sort-by="id"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title> 测试用例</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-spacer></v-spacer>
        <!-- <v-btn color="green" @click="getCaseList()">测试接口</v-btn> -->
        <v-btn color="green" dark class="mb-2" @click="executeCase()"
          >执行用例</v-btn
        >
        <v-dialog v-model="dialog" max-width="500px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">
              新建用例
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="editedItem.id"
                      label="用例ID"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="editedItem.nodeID"
                      label="nodeID"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field
                      v-model="editedItem.remark"
                      label="备注"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="close"> Cancel </v-btn>
              <v-btn color="blue darken-1" text @click="save"> Save </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="text-h5"
              >Are you sure you want to delete this item?</v-card-title
            >
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete"
                >Cancel</v-btn
              >
              <v-btn color="blue darken-1" text @click="deleteItemConfirm"
                >OK</v-btn
              >
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:item.actions="{ item }">
      <v-icon small class="mr-2" @click="editItem(item)"> mdi-pencil </v-icon>
      <v-icon small @click="deleteItem(item)"> mdi-delete </v-icon>
    </template>
  </v-data-table>
</template>


<script>
export default {
  data: () => ({
    oldid: "",
    singleSelect: false,
    selected: [],
    dialog: false,
    dialogDelete: false,
    headers: [
      {
        text: "用例ID",
        align: "start",
        sortable: false,
        value: "id",
      },
      { text: "nodeID", value: "nodeID" },
      { text: "用例备注", value: "remark" },
      { text: "Actions", value: "actions", sortable: false },
    ],
    desserts: [],
    editedIndex: -1,
    editedItem: {
      id: "",
      nodeID: "",
      remark: "",
    },
    defaultItem: {
      id: "",
      nodeID: 0,
      remark: 0,
    },
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "新建用例" : "编辑用例";
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
  },

  created() {
    this.initialize();
  },
  //   updated () {
  //     this.initialize();
  //     },

  methods: {
    initialize() {
      let post_data = {};
      this.$api.cases.getCaseList(post_data).then((res) => {
        // console.log(res)
        // // this.toast res.data.message
        // console.log(res.data.msg.data)
        this.desserts = res.data.msg.data;
      });
    },

    editItem(item) {
      this.editedIndex = this.desserts.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
      //获取旧的用例id
      this.oldid = this.editedItem.id;
      // console.log(this.oldid)
    },

    deleteItem(item) {
      this.editedIndex = this.desserts.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      //删除用例的OK
      //   this.desserts.splice(this.editedIndex, 1);
      console.log(this.editedItem);
      let post_data = { id: this.editedItem.id };
      console.log(post_data);
      this.$api.cases.deleteCase(post_data).then((res) => {
        console.log(res);
        // // this.toast res.data.message
        // console.log(res.data.msg.data)
        // this.desserts=res.data.msg.data
        this.initialize();
      });
      this.closeDelete();
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    save() {
      if (this.editedIndex > -1) {
        //   console.log("this.editedIndex > -1")
        // Object.assign(this.desserts[this.editedIndex], this.editedItem);
        // 编辑用例的save
        let oldid = this.oldid;
        // console.log(oldid)
        let post_data = {
          oldData: {
            id: oldid,
          },
          newData: {
            id: this.editedItem.id,
            nodeID: this.editedItem.nodeID,
            remark: this.editedItem.remark,
          },
        };
        console.log(post_data);
        this.$api.cases.updateCase(post_data).then((res) => {
          console.log(res);
          // this.toast res.data.message
          // console.log(res.data.msg.data)
          // this.desserts=res.data.msg.data
          this.initialize();
        });
      } else {
        // this.desserts.push(this.editedItem);
        // console.log("this.editedIndex < -1")
        // 新建用例的save
        let post_data = {
          id: this.editedItem.id,
          nodeID: this.editedItem.nodeID,
          remark: this.editedItem.remark,
        };
        this.$api.cases.createCase(post_data).then((res) => {
          console.log(res);
          // this.toast res.data.message
          // console.log(res.data.msg.data)
          // this.desserts=res.data.msg.data
          this.initialize();
        });
      }
      this.close();
    },
    executeCase() {
      // console.log("执行用例")
      console.log(this.selected);
      this.$api.task.addTask(this.selected).then((res) => {
        console.log(res);
        if (res.data.error === 0) {
          alert("用例执行成功，请到测试任务页面进行查看");
        } else {
          alert("用例未执行成功，请检查日志信息");
        }
      });
    },
  },
};
</script>

<style scoped>
</style>