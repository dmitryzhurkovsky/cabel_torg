FROM nginx:stable-alpine as production-stage
COPY /reverse_proxy/default.conf /etc/nginx/conf.d/default.conf
CMD ["nginx", "-g", "daemon off;"]