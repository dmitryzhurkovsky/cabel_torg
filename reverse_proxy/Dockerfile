FROM nginx:stable-alpine as production-stage
COPY /reverse_proxy/prod.conf /etc/nginx/conf.d/prod.conf
CMD ["nginx", "-g", "daemon off;"]