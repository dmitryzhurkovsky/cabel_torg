export default defineNuxtRouteMiddleware((to, from) => {
  const token = useCookie('authToken');
  
  if (!token.value && to.path !== '/login') {
    return navigateTo('/login');
  }
  if (token.value && to.path === '/login') {
    return navigateTo('/user_profile');
  }
  return true;
});
