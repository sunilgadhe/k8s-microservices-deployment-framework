#Build Stage
FROM nginx:latest as build 
WORKDIR /usr/share/nginx/html 
COPY src/ .

#Final Stage
FROM nginx:alpine
COPY --from=build /usr/share/nginx/html /usr/share/nginx/html

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]



