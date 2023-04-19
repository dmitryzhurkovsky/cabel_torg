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
    meta: {name: 'Вход'},
    beforeEnter: guest,
    component: () =>
      import("../views/Auth/Login.vue")
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
    meta: {name: 'Кабельторг'},
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
    meta: {name: 'Каталог'}, 
    props: true,
    component: () =>
        import("../views/Catalog.vue")
  },
  {
    path: '/category/:id',
    name: 'Category',
    meta: {name: 'Категория'}, 
    // props: (route) => ({ query: route.query }),
    props: true,
    component: () =>
        import("../views/Catalog.vue")
  },
  {
    path: '/user-cab',
    name: 'user-cab',
    beforeEnter: auth,
    meta: {name: 'Личный кабинет'},
    component: () =>
        import("../views/Personal/user_cab.vue")
  },
  {
    path: '/cart',
    name: 'cart',
    meta: {name: 'Корзина'},
    component: () =>
        import("../views/Personal/cart.vue")
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
        import("../views/How_to_works.vue")
  },
  {
    path: '/warranty',
    name: 'warranty',
    meta: {name: 'Гарантийное обслуживание'},
    component: () =>
        import("../views/Warranties.vue")
  },
  {
    path: '/shipping',
    name: 'shipping',
    meta: {name: 'Оплата и доставка'},
    component: () =>
        import("../views/Shipping.vue")
  },
  {
    path: '/card_product/:id',
    name: 'Card_product',
    meta: {name: 'Карточка товара'},
    props: true,
    component: () =>
        import("../views/Card_product_grid.vue")
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
  {
    path: '/new/:id',
    name: 'New',
    meta: {name: 'Новость'},
    props: true,
    component: () =>
        import("../views/OneNew.vue")
  },
  {
    path: "/:catch(.*)",
    redirect: '/404',
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
