# build
FROM node:lts-alpine as build-stage
WORKDIR /frontend
COPY package*.json ./
RUN npm install
COPY . /frontend/
RUN npm run build

# production
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /frontend/dist /usr/share/nginx/html
COPY --from=build-stage /frontend/build/nginx/default.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]