// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import Vuelidate from "vuelidate";
import store from "./store";

import Chart from "primevue/chart";
import Editor from "primevue/editor";
import Menu from "primevue/menu";
import Panel from "primevue/panel";
import Sidebar from "primevue/sidebar";
import Toast from "primevue/toast";
import ToastService from "primevue/toastservice";

import { BButton } from "bootstrap-vue";
import { BCard } from "bootstrap-vue";
import { BFormFile } from "bootstrap-vue";
import { BForm } from "bootstrap-vue";
Vue.component("b-form", BForm);
import { BFormInput } from "bootstrap-vue";
Vue.component("b-form-input", BFormInput);
import { BInputGroup } from "bootstrap-vue";
Vue.component("b-input-group", BInputGroup);
import { BFormText } from "bootstrap-vue";
Vue.component("b-form-text", BFormText);
import { BFormGroup } from "bootstrap-vue";
Vue.component("b-form-group", BFormGroup);

import { library } from "@fortawesome/fontawesome-svg-core";
import { faHome, faSignOutAlt } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

library.add(faHome, faSignOutAlt);

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import "@fortawesome/fontawesome-free/css/all.css";
import "@fortawesome/fontawesome-free/js/all.js";

import "primevue/resources/themes/nova-dark/theme.css";
import "primevue/resources/primevue.min.css";
import "primeflex/primeflex.css";
import "prismjs/themes/prism-coy.css";
import "./assets/layout/layout.scss";

Vue.use(Vuelidate);
Vue.use(ToastService);
Vue.config.productionTip = false;
Vue.component("b-button", BButton);
Vue.component("font-awesome-icon", FontAwesomeIcon);
Vue.component("b-card", BCard);
Vue.component("b-form-file", BFormFile);
Vue.component("Toast", Toast);
Vue.component("Chart", Chart);
Vue.component("Editor", Editor);
Vue.component("Menu", Menu);
Vue.component("Panel", Panel);
Vue.component("Sidebar", Sidebar);

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
