FROM node:18.14.1-alpine as builder
WORKDIR /admin_dashboard
COPY /package*.json /admin_dashboard/
RUN npm install
COPY . /admin_dashboard/
RUN npm run build

# production client frontend
FROM nginx:stable-alpine as production-stage
# Copy files for admin frontend
COPY --from=builder /admin_dashboard/dist /usr/share/nginx/admin_dashboard
COPY build/default.conf /etc/nginx/conf.d/nginx.conf

EXPOSE 8001
CMD ["nginx", "-g", "daemon off;"]