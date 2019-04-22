FROM node:10 AS frontend-build
WORKDIR /app/
ADD PHASE_2/Application_SourceCode/ /app/
RUN yarn install 
RUN yarn build 

# production stage
FROM nginx:stable-alpine as production-stage
# copy the frontend build 
COPY --from=frontend-build /app/dist /usr/share/nginx/html
ADD PHASE_1/API_SourceCode/static /usr/share/nginx/html/static
# copy the server config to direct the dynamic reponse to 

# proxy file for navigave between backend endpoint
COPY PHASE_1/nginx/default.conf /etc/nginx/conf.d/default.conf 
# overwrite the log formate
COPY PHASE_1/nginx/nginx.conf /etc/nginx/nginx.conf 

RUN mkdir -p /usr/share/nginx/html/log/
RUN touch /usr/share/nginx/html/log/access_log.txt

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]