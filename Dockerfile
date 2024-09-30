# Use an official Node.js image as a base
FROM node:18

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the Vue.js app for production
RUN npm run build

# Install a basic web server
RUN npm install -g serve

# Set the command to serve the app
CMD ["serve", "-s", "dist"]

# Expose port 5000 (or any port you prefer)
EXPOSE 5000
