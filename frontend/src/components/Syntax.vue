<template>
  <div class="p-grid p-fluid">
    <div class="p-col-12">
      <div>
        <b-card title="В разработке">
          <div class="form-group">
            <!-- <label for="exampleFormControlTextarea1">Example textarea</label> -->
            <textarea class="form-control" id="exampleFormControlTextarea1" rows="10"></textarea>
          </div>
          <!-- <script ssrc="C:\Users\lenovo\Desktop\Project\Projects\node_modules\conllu\browser.js"></script> -->
        </b-card>
      </div>
    </div>
  </div>
</template>

<script>
import conllu from "conllu"
import fs from "fs"
import Conllu from "conllu-brat"
export default {
  data() {
    return {
      file: null,
      text: "",
      type: ""
    };
  },
    created() {
    Conllu('C:/Users/lenovo/Desktop/kk.conllu')
  },
  methods: {
    upload: function(e) {
      e.preventDefault();
      // var data = new FormData();
      // data.append("file", document.getElementById("file").files[0]);
      // console.log(document.getElementById("file").files[0]);
      // const authUser = JSON.parse(window.localStorage.getItem("authUser"));
      Conllu.parse('C:/Users/lenovo/Desktop/kk.conllu')

      // const token = authUser.access_token;
    }
  },
};
// Conllu.parse('C:/Users/lenovo/Desktop/kk.conllu')
// // Counllu
// // var conllu = require("conllu")
// // var fs = require("fs")
// // // Conllu.
// var c = new conllu.Conllu()
// c.serial = fs.readFileSync('C:/Users/lenovo/Desktop/kk.conllu','utf8')
// window.conllu
</script>

<style scoped>
</style>
