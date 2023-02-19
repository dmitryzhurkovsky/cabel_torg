import {createRouter, createWebHistory, NavigationGuard} from 'vue-router'

const guest: NavigationGuard = (to, from, next) => {
  if (!localStorage.getItem("authToken")) {
    return next();
  } else {
    return next("/");
  }
};

const auth: NavigationGuard = (to, from, next) => {
  if (localStorage.getItem("authToken")) {
    return next();
  } else {
    return next("/login");
  }
};

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      beforeEnter: auth,
      path: '/',
      name: 'Index',
      component: () => import('@/views/Index.vue')
    },
    {
      beforeEnter: guest,
      path: '/login',
      name: 'Login',
      component: () => import('@/views/Login.vue')
    },
    {
      beforeEnter: auth,
      path: '/partners',
      name: 'Partners',
      component: () => import('@/views/Partners.vue')
    },
    {
      beforeEnter: auth,
      path: '/delivery_types',
      name: 'DeliveryTypes',
      component: () => import('@/views/DeliveryTypes.vue')
    },
    {
      beforeEnter: auth,
      path: '/articles',
      name: 'Articles',
      component: () => import('@/views/Articless.vue')
    },
  ]
})

export { router };