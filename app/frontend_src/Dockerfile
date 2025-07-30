# Build Stage
FROM nginx:latest as build 
WORKDIR /usr/share/nginx/html 
COPY . /usr/share/nginx/html

# Final Stage
FROM nginx:alpine
COPY --from=build /usr/share/nginx/html /usr/share/nginx/html

RUN chmod +x /usr/share/nginx/html/entrypoint.sh
ENTRYPOINT ["/usr/share/nginx/html/entrypoint.sh"]

