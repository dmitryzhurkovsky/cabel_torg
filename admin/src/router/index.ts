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
    // {
    //   path: '/radiobutton',
    //   name: 'Radiobutton',
    //   component: Radiobutton
    // },
    // {
    //   path: '/progress',
    //   name: 'Progress',
    //   component: Progress
    // },
    // {
    //   path: '/input',
    //   name: 'Input',
    //   component: Input
    // },
    // {
    //   path: '/tabs',
    //   name: 'Tabs',
    //   component: Tabs
    // },
    // {
    //   path: '/table',
    //   name: 'Table',
    //   component: Table
    // },
  ]
})

export { router };