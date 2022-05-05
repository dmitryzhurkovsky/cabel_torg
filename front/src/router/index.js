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
  },
  {
    path: '/404',
    name: '404',
    component: () =>
        import("../views/404.vue")
  },
  {
    path: '/how_to_work',
    name: 'how_to_work',
    component: () =>
        import("../views/how_to_work.vue")
  },
  {
    path: '/warranty',
    name: 'warranty',
    component: () =>
        import("../views/warranty.vue")
  },
  {
    path: '/shipping',
    name: 'Shipping',
    component: () =>
        import("../views/Shipping.vue")
  },
  {
    path: '/card_product_grid',
    name: 'Card_product_grid',
    component: () =>
        import("../views/Card_product_grid.vue")
  },
  {
    path: '/card_product',
    name: 'Card_product',
    component: () =>
        import("../views/Card_product.vue")
  },
  {
    path: '/contacts',
    name: 'Contacts',
    component: () =>
        import("../views/Contacts.vue")
  },
  {
    path: '/news',
    name: 'News',
    component: () =>
        import("../views/News.vue")
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
