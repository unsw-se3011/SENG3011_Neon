# production stage
FROM swaggerapi/swagger-ui

ADD swagger.yaml /tmp/swagger.yaml
ENV SWAGGER_JSON=/tmp/swagger.yaml


ADD nginx.conf /etc/nginx/nginx.conf