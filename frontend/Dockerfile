# Use an official Node.js runtime as the base image
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and yarn.lock files to the container
COPY package.json yarn.lock ./

# Install project dependencies
RUN yarn install

# Copy the entire project directory to the container
COPY . .

# Build the project
RUN yarn build

EXPOSE 3000 

# Define the command to start the container
CMD ["yarn", "dev", "--host", "0.0.0.0"]