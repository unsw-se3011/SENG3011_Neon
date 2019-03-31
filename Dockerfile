# FROM node:8 AS frontend-build
# WORKDIR /app/
# ADD frontend/ /app/
# RUN npm install 
# RUN npm run build 

# production stage
FROM nginx:stable-alpine as production-stage
# COPY --from=frontend-build /app/dist /usr/share/nginx/html
ADD PHASE_1/API_SourceCode/static /usr/share/nginx/html/static
# copy the server config to direct the dynamic reponse to 
# python backend 
COPY PHASE_1/nginx/default.conf /etc/nginx/conf.d/default.conf 

RUN mkdir -p /usr/share/nginx/html/log/
RUN touch /usr/share/nginx/html/log/access_log.txt

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]