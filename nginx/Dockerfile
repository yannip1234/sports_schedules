FROM nginx:1.21-alpine
RUN apk add --no-cache tzdata
ENV TZ America/New_York
RUN cp /usr/share/zoneinfo/$TZ /etc/localtime
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d