import { createRouter, createWebHistory } from 'vue-router'

const guest = (to, from, next) => {
  if (!localStorage.getItem("authToken")) {
    return next();
  } else {
    return next("/");
  }
};
const auth = (to, from, next) => {
  if (localStorage.getItem("authToken")) {
    return next();
  } else {
    return next("/login");
  }
};

const routes = [
  {
    path: "/login",
    name: "Login",
    beforeEnter: guest,
    component: () =>
      import(/* webpackChunkName: "login" */ "../views/Auth/Login.vue")
  },
  {
    path: "/register",
    name: "Register",
    beforeEnter: guest,
    component: () =>
      import(/* webpackChunkName: "register" */ "../views/Auth/Register.vue")
  },
  {
    path: "/verify/:hash",
    name: "Verify",
    beforeEnter: auth,
    props: true,
    component: () =>
      import(/* webpackChunkName: "verify" */ "../views/Auth/Verify.vue")
  },
  {
    path: "/offer",
    name: "Offer",
    component: () =>
        import("../views/Offer.vue")
  },
  {
    path: '/',
    name: 'Main',
    component: () =>
      import("../views/Main.vue")
  },
  {
    path: '/about',
    name: 'About',
    component: () =>
        import("../views/About.vue")
  },
  {
    path: '/wholesale',
    name: 'Wholesale',
    component: () =>
        import("../views/Wholesale.vue")
  },,
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
