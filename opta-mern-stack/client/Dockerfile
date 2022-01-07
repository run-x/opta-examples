FROM node:latest
RUN echo "test"
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
CMD ["npm", "start"]

