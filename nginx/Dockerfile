# build fronend
FROM node:18.12.1-alpine as build-stage
WORKDIR /frontend
COPY /front/package*.json ./
RUN npm install
COPY /front/ /frontend/
RUN npm run build

# production
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /frontend/dist /usr/share/nginx/html
COPY /nginx/default.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]