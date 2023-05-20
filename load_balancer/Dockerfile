FROM nginx:stable-alpine as production-stage
COPY /load_balancer/default.conf /etc/nginx/conf.d/default.conf
CMD ["nginx", "-g", "daemon off;"]