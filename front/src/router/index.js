import { createRouter, createWebHistory } from 'vue-router'

const guest = (to, from, next) => {
  // console.log('TO', to , 'From', from, 'Next', next);
  if (!localStorage.getItem("authToken")) {
    // console.log('asasdasd');
    return next();
  } else {
    // console.log('//////');
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
      import("../views/Auth/Login.vue")
  },
  {
    path: "/register",
    name: "Register",
    beforeEnter: guest,
    component: () =>
      import("../views/Auth/Register.vue")
  },
  {
    path: "/verify/:hash",
    name: "Verify",
    beforeEnter: auth,
    props: true,
    component: () =>
      import("../views/Auth/Verify.vue")
  },
  {
    path: "/offer",
    name: "Offer",
    meta: {name: 'Публичная оферта'},
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
    meta: {name: 'О компании'},
    component: () =>
        import("../views/About.vue")
  },
  {
    path: '/catalog',
    name: 'Catalog',
    component: () =>
        import("../views/Catalog.vue")
  },
  {
    path: '/user-cab',
    name: 'user-cab',
    meta: {name: 'Личный кабинет'},
    component: () =>
        import("../views/Personal/user_cab.vue")
  },
  {
    path: '/cart',
    name: 'cart',
    component: () =>
        import("../views/Personal/cart.vue")
  },

  {
    path: '/user-cab-set',
    name: 'user-cab-set',
    component: () =>
        import("../views/Personal/user_cab-set.vue")
  },
  {
    path: '/wholesale',
    name: 'Wholesale',
    meta: {name: 'Оптовым клиентам'},
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
    meta: {name: 'Как оформить заказ'},
    component: () =>
        import("../views/How_to_work.vue")
  },
  {
    path: '/warranty',
    name: 'warranty',
    meta: {name: 'Гарантийное обслуживание'},
    component: () =>
        import("../views/Warranty.vue")
  },
  {
    path: '/shipping',
    name: 'shipping',
    meta: {name: 'Оплата и доставка'},
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
    meta: {name: 'Контактная информация'},
    name: 'Contacts',
    component: () =>
        import("../views/Contacts.vue")
  },
  {
    path: '/news',
    name: 'News',
    meta: {name: 'Новости'},
    component: () =>
        import("../views/News.vue")
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
