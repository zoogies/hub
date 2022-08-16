FROM node:lts-alpine

WORKDIR /

COPY . ./
# RUN cd src/portfolio && yarn install
# RUN cd src/portfolio && yarn build

# RUN npm install --global serve

# CMD ["serve","-s","src/portfolio/build"]