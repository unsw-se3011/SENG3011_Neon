# Project Neon

Project Project Using:  
Frontend:
[Vue](https://cn.vuejs.org/v2/guide/),
[Vuex](https://vuex.vuejs.org/guide/),
[Vuetify](https://vuetifyjs.com/en/getting-started/quick-start),
[Vue-router](https://router.vuejs.org/),
[Axios](https://cn.vuejs.org/v2/cookbook/using-axios-to-consume-apis.html)  
Backend:
[Django](https://docs.djangoproject.com/en/2.1/),
[PostgreSQL](https://www.postgresql.org/),
[Django-Rest-Framework](http://www.django-rest-framework.org/tutorial/quickstart/),
[django-rest-framework-jwt](https://github.com/GetBlimp/django-rest-framework-jwt)  
Web Crawler:
[Scrapy](http://doc.scrapy.org/en/latest/intro/tutorial.html)  
DevOps:
[Docker](https://www.docker.com/),
[Docker-Compose](https://docs.docker.com/compose/),
[Django-test](https://docs.djangoproject.com/en/2.1/topics/testing/overview/)

## Getting involve

### Set Your Working Branch

```bash
# create to your branch and working there
$ git checkout -b YOUR_BRANCH_NAME

# when you finshish, push the commits
$ git add && git commmit && git push
# IF you are push this branch FIRST TIME, you may use this line
$ git push --set-upstream origin YOUR_BRANCH_NAME
```

## Docker Environment

First, we need to install:
[Docker Community Edition](https://docs.docker.com/install/#releases)
and
[Docker Compose](https://docs.docker.com/compose/install/#install-compose)

### Deploy Environment (temporary)

```bash 
# start the deploy env 
docker-compose up 
# end it ( otherwise it will keep running in background)
docker-compose down 

# kill it to rebuild 
docker-compose down --rmi all

```


## APIs Documents

The api document is in [api.http](./api.http); You need to run it via [vscode Rest Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)

You can install it via this command in vscode command panel (Ctrl + Shift + P):

```bash
ext install humao.rest-client
```

## URLs

| URL                                                                                            | Detail               |
| :--------------------------------------------------------------------------------------------- | :------------------- |
| [http://neon.whiteboard.house:8000/](http://neon.whiteboard.house:8000/)                       | Home Page (frontend) |
| [http://neon.whiteboard.house:8000/v0/](http://neon.whiteboard.house:8000/v0/)                 | Api Root             |
| [http://neon.whiteboard.house:8000/v0/swagger/](http://neon.whiteboard.house:8000/v0/swagger/) | Swagger Documents    |
| [http://neon.whiteboard.house:8000/admin/](http://neon.whiteboard.house:8000/admin/)           | Django admin         |

## For D2 Justification

The generated swagger is incorrect in some cases such as the `POST` method for `report` and `report_event` classes. The lecturer said we can use another API document for D2. You can directly hit the API Root specified above. The query string parameter is handle in the filtets section in the supported pages.

Also, we are mainly using [REST Client in vscode](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) for the cases that not fit in both auto-generated documentation. Such as creating `report` and `report_event`.  
The document file is in: [PHASE_1/API_Documentation/api.http](PHASE_1/API_Documentation/api.http)

![create report](img/report.png)

You can copy the body of the report example an paste into `swagger` or `django rest documentation` and try it out, that will do too.

![swagger creation](img/swagger.png)