FROM node:15

WORKDIR /app

# Install Angular (will not change)
RUN npm install -g @angular/cli @angular-devkit/build-angular 

# Updates packages
COPY package*.json /app/
RUN npm install
