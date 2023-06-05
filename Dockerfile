# Use an official Nginx image as the base
FROM nginx:latest

# Copy your application files into the container
COPY . /usr/share/nginx/html

# Expose the container's port
EXPOSE 80

# Start the Nginx server when the container starts
CMD ["nginx", "-g", "daemon off;"]
