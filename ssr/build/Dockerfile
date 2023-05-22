FROM node:18.14.1-alpine as builder
WORKDIR /artefacts
COPY /package*.json ./
RUN npm install
COPY . /artefacts/
RUN npm run build

FROM node:18.14.1-alpine
WORKDIR /frontend

COPY --from=builder /artefacts  /frontend/

ENV PORT 8002
CMD [ "node", ".output/server/index.mjs" ]
