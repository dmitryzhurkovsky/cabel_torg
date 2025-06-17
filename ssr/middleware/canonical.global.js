export default defineNuxtRouteMiddleware((to, from) => {
  const originalFullPath = to.fullPath;
  const indexOfQuestionMark = originalFullPath.indexOf('?');

  const router = useRouter();

  console.log('canonical to: ', to.path, ' from: ', from.path);
  // console.log('canonical to', router);
  
  let rebuildedTarget = to.path.toLowerCase();

  const queryPart = indexOfQuestionMark !== -1
    ? originalFullPath.substring(indexOfQuestionMark)
    : '';

  // console.log('query: ', queryPart);
  
  if (to.path) {
    // console.log('start: ', rebuildedTarget);
    if (rebuildedTarget.startsWith('www.')) {
      rebuildedTarget = rebuildedTarget.slice(4);
    }
    // console.log('after www slice: ', rebuildedTarget);
    rebuildedTarget = rebuildedTarget.replace(/\/{2,}/g, '/');
    // console.log('after /// slice: ', rebuildedTarget);
    if (rebuildedTarget.endsWith('/') && to.path !== '/') rebuildedTarget = rebuildedTarget.slice(0, -1)
    // console.log('after last / slice: ', rebuildedTarget);
  }
  if (to.path !== rebuildedTarget) {
    if (queryPart.length) rebuildedTarget = rebuildedTarget + queryPart;
    console.log('Redirect is needed to: ', rebuildedTarget);

    console.log('Redirecting from middlware...');
    if (process.server) {
      console.log('From server');
      return navigateTo(rebuildedTarget, { redirectCode: 301 });
    } else {
      console.log('From client');
      router.push(rebuildedTarget, { redirectCode: 301 });
    }
  } else {
    console.log('Not needed redirect!!!');
    return 
  }
});
