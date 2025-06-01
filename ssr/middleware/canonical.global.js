export default defineNuxtRouteMiddleware((to, from) => {

  console.log('canonical to: ', to.fullPath, ' from: ', from.fullPath);
  let rebuildedTarget = to.fullPath.toLowerCase();
  if (to.fullPath) {
    if (rebuildedTarget.startsWith('www.')) {
      rebuildedTarget = rebuildedTarget.slice(4);
    }
    rebuildedTarget = rebuildedTarget.replace(/\/{2,}/g, '/');
    if (rebuildedTarget.endsWith('/')) rebuildedTarget = rebuildedTarget.slice(0, -1)
  }
  if (to.fullPath !== rebuildedTarget) {
    console.log('Redirect is needed to: ', rebuildedTarget);
    return navigateTo(rebuildedTarget, { redirectCode: 301 });
  }
});
