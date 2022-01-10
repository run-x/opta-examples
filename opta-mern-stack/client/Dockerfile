FROM node:latest
RUN echo "test"
RUN mkdir /app
COPY package.json /app
WORKDIR /app
RUN npm install
COPY . .
CMD ["npm", "start"]

