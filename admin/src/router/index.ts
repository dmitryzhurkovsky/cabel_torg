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
      component: () => import('@/views/Articles.vue')
    },
    {
      beforeEnter: auth,
      path: '/banners',
      name: 'Banners',
      component: () => import('@/views/Banners.vue')
    },
    {
      beforeEnter: auth,
      path: '/call_requests',
      name: 'Calls',
      component: () => import('@/views/CallRequests.vue')
    },
    {
      beforeEnter: auth,
      path: '/feedback_requests',
      name: 'Feedback',
      component: () => import('@/views/FeedbackRequests.vue')
    },
    {
      beforeEnter: auth,
      path: '/discount',
      name: 'Discount',
      component: () => import('@/views/Discount.vue')
    },
    {
      beforeEnter: auth,
      path: '/settings',
      name: 'Settings',
      component: () => import('@/views/Settings.vue')
    },
    {
      beforeEnter: auth,
      path: '/stocks',
      name: 'Stocks',
      component: () => import('@/views/Stocks.vue')
    },
    {
      beforeEnter: auth,
      path: '/users',
      name: 'Users',
      component: () => import('@/views/Users.vue')
    },
    {
      beforeEnter: auth,
      path: '/price',
      name: 'Price',
      component: () => import('@/views/Price.vue')
    },
  ]
})

export { router };