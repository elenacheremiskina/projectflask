<template>
  <div class="p-grid p-fluid">
    <div class="p-col-12 p-lg-8">
      <div>
        <b-card title="Частотный анализ" v-if="loaded">
          <div class="chart-block">
            <reactive-bar-chart :chart-data="datacollection"></reactive-bar-chart>
          </div>
        </b-card>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ReactiveBarChart from "@/components/ReactiveBarChart";

export default {
  components: { ReactiveBarChart },
  data() {
    return {
      expense: null,
      date: null,
      expenseamount: null,
      datacollection: null,
      loaded: false
    };
  },
  created() {
    this.fillData();
  },
  mounted() {
    this.fillData();
  },
  methods: {
    fillData() {
      this.loaded = false;
      const authUser = JSON.parse(window.localStorage.getItem("authUser"));
      const token = authUser.access_token;
      axios
        .get("http://localhost:5000/api/text/" + localStorage.getItem("id_text"), {
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json"
        }
      }) 
        .then(response => {
          let results = response.data;
          this.date = response.data.text;
          let expenseresult = results.count;
          this.expense = expenseresult;
          this.datacollection = {
            labels: this.date,
            datasets: [
              {
                label: "Количество слов",
                backgroundColor: "grey",
                data: this.expense
              }
            ]
          };
          this.loaded = true;
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style></style>
