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

## APIs Documents

The api document is in [api.http](./api.http); You need to run it via [vscode Rest Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)

You can install it via this command in vscode command panel (Ctrl + Shift + P):

```bash
ext install humao.rest-client
```

## URLs

| URL                                                        | Detail              |
| :--------------------------------------------------------- | :------------------ |
| [http://localhost:8080/](http://localhost:8080/)           | Home Page (Backend) |
| [http://localhost:8000/admin](http://localhost:8000/admin) | Django admin        |
