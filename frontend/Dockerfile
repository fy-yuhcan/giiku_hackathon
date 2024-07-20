FROM node:20

WORKDIR /app

COPY package*.json ./

ENV NODE_OPTIONS=--openssl-legacy-provider

CMD ["npm", "run", "dev"]
