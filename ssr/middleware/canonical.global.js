export default defineNuxtRouteMiddleware((to, from) => {
  const originalFullPath = to.fullPath;
  const indexOfQuestionMark = originalFullPath.indexOf('?');

  console.log('canonical to: ', to.path, ' from: ', from.path);
  let rebuildedTarget = to.path.toLowerCase();

  const queryPart = indexOfQuestionMark !== -1
    ? originalFullPath.substring(indexOfQuestionMark)
    : '';

  // console.log('query: ', paramsStr);
  
  if (to.path) {
    if (rebuildedTarget.startsWith('www.')) {
      rebuildedTarget = rebuildedTarget.slice(4);
    }
    rebuildedTarget = rebuildedTarget.replace(/\/{2,}/g, '/');
    if (rebuildedTarget.endsWith('/') && to.path !== '/') rebuildedTarget = rebuildedTarget.slice(0, -1)
  }
  if (to.path !== rebuildedTarget) {
    if (paramsStr.length) rebuildedTarget = rebuildedTarget + paramsStr;
    console.log('Redirect is needed to: ', rebuildedTarget);
    return navigateTo(rebuildedTarget, { redirectCode: 301 });
  }
});
