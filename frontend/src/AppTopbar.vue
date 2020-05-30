<template>
  <div class="layout-topbar">
    <b-button class="p-link layout-menu-button" id="toggler" @click="onMenuToggle">
      <span class="fa fa-bars" style="font-size:24px"></span>
    </b-button>
    <div class="layout-topbar-icons">
      <b-button class="p-link" id="switch" @click="logout">
        <span class="layout-topbar-item-text">Logout</span>
        <span class="layout-topbar-icon fa fa-fw fa-power-off" style="font-size:24px"></span>
      </b-button>
    </div>
  </div>
</template>

<script>
import Axios from "axios";
export default {
  data() {
    return {
    };
  },
  methods: {
    onMenuToggle(event) {
      this.$emit("menu-toggle", event);
    },

    logout: function(e) {
      e.preventDefault();
      const url = "http://localhost:5000/api/logout/access";
      const authUser = JSON.parse(window.localStorage.getItem("authUser"));
      const token = authUser.access_token;
      Axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;
      Axios.post(url, {
        headers: {
          "Content-Type": "application/json"
        }
      })
        .then(res => {
          console.log(res);
          this.$store.dispatch('clearAuthUser')
          window.localStorage.removeItem('authUser')
          window.localStorage.removeItem('id_text')
          this.$router.push("/");
        })
        .catch(err => {
          console.log("AXIOS ERROR: ", err);
        });
    }
  }
};
</script>
