<template>
  <div class="p-grid p-fluid">
    <div class="p-col-12 p-lg-8">
      <div>
        <b-card title="Частотный анализ">
          <Chart type="bar" :data="barData" />
        </b-card>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      barData: {
        labels: [
          "Зима",
          "Осень",
          "Весна",
          "Лето",
          "Декабрь",
          "Сентябрь",
          "Март",
          "Июнь",
        ],
        datasets: [
          {
            label: "Количество слов",
            backgroundColor: "#2f4860",
            data: [65, 59, 76, 83, 56, 60, 54, 70],
          },
        ],
      },
    };
  },
};
</script>

<style></style>
