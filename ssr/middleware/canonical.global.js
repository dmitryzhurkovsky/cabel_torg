export default defineNuxtRouteMiddleware((to, from) => {

  // console.log('canonical to: ', to.path, ' from: ', from.path);
  let rebuildedTarget = to.path.toLowerCase();

  const originalString = to.fullPath;
  const indexOfQuestionMark = originalString.indexOf('?');
  
  const paramsStr = indexOfQuestionMark !== -1 
      ? originalString.substring(indexOfQuestionMark) 
      : '';

  // console.log('query: ', paramsStr);
  
  if (to.path) {
    if (rebuildedTarget.startsWith('www.')) {
      rebuildedTarget = rebuildedTarget.slice(4);
    }
    rebuildedTarget = rebuildedTarget.replace(/\/{2,}/g, '/');
    if (rebuildedTarget.endsWith('/')) rebuildedTarget = rebuildedTarget.slice(0, -1)
  }
  if (to.path !== rebuildedTarget) {
    if (paramsStr.length) rebuildedTarget = rebuildedTarget + paramsStr;
    // console.log('Redirect is needed to: ', rebuildedTarget);
    return navigateTo(rebuildedTarget, { redirectCode: 301 });
  }
});
