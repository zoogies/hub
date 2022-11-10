FROM node:lts-alpine

WORKDIR /src/frontend

COPY . .
RUN yarn install
RUN yarn build

CMD ["node","build/index.js"]