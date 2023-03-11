# build client frontend
FROM node:18.14.1-alpine as build-client-frontend-stage
WORKDIR /client_frontend
COPY /front/package*.json ./
RUN npm install
COPY /front/ /client_frontend/
RUN npm run build

# build admin frontend
FROM node:18.14.1-alpine as build-admin-frontend-stage
WORKDIR /admin_frontend
COPY /admin/package*.json ./
RUN npm install
COPY /admin/ /admin_frontend/
RUN npm run build

# production client frontend
FROM nginx:stable-alpine as production-stage
# Copy files for clinet frontend
COPY --from=build-client-frontend-stage /client_frontend/dist /usr/share/nginx/html
# Copy files for admin frontend
COPY --from=build-admin-frontend-stage /admin_frontend/dist /usr/share/nginx/html/admin
# Copy nginx configruations
COPY /nginx/default.conf /etc/nginx/conf.d/default.conf
# Create a directory for maintaing images
RUN mkdir -p /usr/share/nginx/images


CMD ["nginx", "-g", "daemon off;"]