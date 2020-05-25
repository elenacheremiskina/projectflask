<template>
  <div :class="containerClass" @click="onWrapperClick">
    <AppTopBar
      @menu-toggle="onMenuToggle"
      v-if="userStore.authUser !== null && userStore.authUser.access_token"
    />
    <transition name="layout-sidebar" id="layout-menuu">
      <div
        :class="sidebarClass"
        @click="onSidebarClick"
        v-show="isSidebarVisible()"
        v-if="userStore.authUser !== null && userStore.authUser.access_token"
      >
        <div class="layout-logo">
          <router-link to="/"></router-link>
        </div>
        <AppMenu :model="menu" @menuitem-click="onMenuItemClick" />
      </div>
    </transition>
    <div class="layout-main">
      <router-view />
    </div>
  </div>
</template>

<script>
import AppTopBar from "./AppTopbar.vue";
import AppMenu from "./AppMenu.vue";
import { mapState } from "vuex";

export default {
  data() {
    return {
      user: null,
      layoutMode: "static",
      layoutColorMode: "dark",
      staticMenuInactive: false,
      overlayMenuActive: false,
      mobileMenuActive: false,
      menu: [
        { label: "Главная", icon: "fas fa-fw fa-home", to: "/dashboard" },
        {
          label: "Частотный анализ",
          icon: "fa fa-fw fa-chart-bar",
          to: "/sample"
        },
        {
          label: "Синтаксический анализ",
          icon: "fa fa-fw fa-edit",
          to: "/syntax"
        },
        {
          label: "Семантический анализ",
          icon: "fa fa-fw fa-list",
          to: "/semantic"
        },
        { label: "Отчет", icon: "fa fa-fw fa-file", to: "/report" },
        { label: "Справка", icon: "fa fa-fw fa-question-circle", to: "/help" }
      ]
    };
  },
  watch: {
    $route() {
      this.menuActive = false;
      this.$toast.removeAllGroups();
    }
  },
  methods: {
    onWrapperClick() {
      if (!this.menuClick) {
        this.overlayMenuActive = false;
        this.mobileMenuActive = false;
      }

      this.menuClick = false;
    },
    onMenuToggle() {
      this.menuClick = true;

      if (this.isDesktop()) {
        if (this.layoutMode === "overlay") {
          this.overlayMenuActive = !this.overlayMenuActive;
        } else if (this.layoutMode === "static") {
          this.staticMenuInactive = !this.staticMenuInactive;
        }
      } else {
        this.mobileMenuActive = !this.mobileMenuActive;
      }

      event.preventDefault();
    },
    onSidebarClick() {
      this.menuClick = true;
    },
    onMenuItemClick(event) {
      if (event.item && !event.item.items) {
        this.overlayMenuActive = false;
        this.mobileMenuActive = false;
      }
    },
    addClass(element, className) {
      if (element.classList) {
        element.classList.add(className);
      } else {
        element.className += " " + className;
      }
    },
    removeClass(element, className) {
      if (element.classList) {
        element.classList.remove(className);
      } else {
        element.className = element.className.replace(
          new RegExp(
            "(^|\\b)" + className.split(" ").join("|") + "(\\b|$)",
            "gi"
          ),
          " "
        );
      }
    },
    isDesktop() {
      return window.innerWidth > 1024;
    },
    isSidebarVisible() {
      if (this.isDesktop()) {
        if (this.layoutMode === "static") {
          return !this.staticMenuInactive;
        } else if (this.layoutMode === "overlay") {
          return this.overlayMenuActive;
        } else {
          return true;
        }
      } else {
        return true;
      }
    }
  },
  computed: {
    ...mapState({
      userStore: state => state.userStore
    }),
    containerClass() {
      return [
        "layout-wrapper",
        {
          "layout-overlay": this.layoutMode === "overlay",
          "layout-static": this.layoutMode === "static",
          "layout-static-sidebar-inactive":
            this.staticMenuInactive && this.layoutMode === "static",
          "layout-overlay-sidebar-active":
            this.overlayMenuActive && this.layoutMode === "overlay",
          "layout-mobile-sidebar-active": this.mobileMenuActive
        }
      ];
    },
    sidebarClass() {
      return [
        "layout-sidebar",
        {
          "layout-sidebar-dark": this.layoutColorMode === "dark"
        }
      ];
    }
  },
  created() {
    const userObj = JSON.parse(window.localStorage.getItem("authUser"));
    this.$store.dispatch("setUserObject", userObj);
  },
  beforeUpdate() {
    if (this.mobileMenuActive) {
      this.addClass(document.body, "body-overflow-hidden");
    } else {
      this.removeClass(document.body, "body-overflow-hidden");
    }
  },
  components: {
    AppTopBar: AppTopBar,
    AppMenu: AppMenu
  }
};
</script>

<style lang="scss">
@import "./App.scss";
</style>
