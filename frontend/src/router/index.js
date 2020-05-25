import Vue from "vue";
import Router from "vue-router";
import Dashboard from "../components/Dashboard.vue";
import SampleDemo from "../components/SampleDemo.vue";
import Syntax from "../components/Syntax.vue";
import Semantic from "../components/Semantic.vue";
import Report from "../components/Report.vue";
import Help from "../components/Help.vue";
import Login from "../components/Auth/Login.vue";
import Registration from "../components/Auth/Registration.vue";

Vue.use(Router);

let router = new Router({
  mode: "history",
  routes: [
    {
      path: "/dashboard",
      name: "dashboard",
      component: Dashboard,
      meta: {
        requireAuth: true,
      },
    },
    {
      path: "/sample",
      name: "sample",
      component: SampleDemo,
      meta: {
        requireAuth: true,
      },
    },
    {
      path: "/Syntax",
      name: "syntax",
      component: Syntax,
      meta: {
        requireAuth: true,
      },
    },
    {
      path: "/semantic",
      name: "semantic",
      component: Semantic,
      meta: {
        requireAuth: true,
      },
    },
    {
      path: "/report",
      name: "report",
      component: Report,
      meta: {
        requireAuth: true,
      },
    },
    {
      path: "/help",
      name: "help",
      component: Help,
      meta: {
        requireAuth: true,
      },
    },
    {
      path: "/",
      name: "login",
      component: Login,
      meta: {
        guest: true,
      },
    },
    {
      path: "/registration",
      name: "registration",
      component: Registration,
      meta: {
        guest: true,
      },
    },
  ],
  scrollBehavior() {
    return { x: 0, y: 0 };
  },
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requireAuth)) {
    if (localStorage.getItem("authUser") == null) {
      next({
        path: "/",
        params: { nextUrl: to.fullPath },
      });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
