FROM node:18.14.1-alpine as builder
WORKDIR /artefacts
COPY /package*.json ./
RUN npm install
COPY . /artefacts/
RUN npm run build

FROM node:18.14.1-alpine
WORKDIR /client_frontend

ENV PORT 800

COPY --from=builder /artefacts  /client_frontend/

CMD [ "node", ".output/server/index.mjs" ]
