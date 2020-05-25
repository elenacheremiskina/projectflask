<template>
  <div
    class="layout-menu-container"
    id="layout-menu-container"
    v-if="userStore.authUser !== null && userStore.authUser.access_token"
  >
    <AppSubmenu :items="model" class="layout-menu" :root="true" @menuitem-click="onMenuItemClick" />
  </div>
</template>

<script>
import AppSubmenu from "./AppSubmenu";
import { mapState } from "vuex";
export default {
  computed: {
    ...mapState({
      userStore: state => state.userStore
    })
  },
  props: {
    model: Array
  },
  methods: {
    onMenuItemClick(event) {
      this.$emit("menuitem-click", event);
    }
  },
  components: {
    AppSubmenu: AppSubmenu
  }
};
</script>

<style scoped>
</style>
