export default defineNuxtRouteMiddleware((to, from) => {
  const originalFullPath = to.fullPath;
  const indexOfQuestionMark = originalFullPath.indexOf('?');

  const pathPart = indexOfQuestionMark !== -1
    ? originalFullPath.substring(0, indexOfQuestionMark)
    : originalFullPath;

  const queryPart = indexOfQuestionMark !== -1
    ? originalFullPath.substring(indexOfQuestionMark)
    : '';

  // Normalize path:
  let normalizedPath = pathPart.toLowerCase();
  if (normalizedPath.startsWith('www.')) {
    normalizedPath = normalizedPath.slice(4);
  }

  // Убираем дублирующиеся слеши
  normalizedPath = normalizedPath.replace(/\/{2,}/g, '/');

  // Убираем конечный слеш (кроме "/")
  if (normalizedPath.length > 1 && normalizedPath.endsWith('/')) {
    normalizedPath = normalizedPath.slice(0, -1);
  }

  const rebuiltFullPath = normalizedPath + queryPart;

  if (originalFullPath !== rebuiltFullPath) {
    return navigateTo(rebuiltFullPath, { redirectCode: 301 });
  }
});
