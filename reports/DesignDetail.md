# Design Details - Initial documentation

![Architecture Design](img/Architecture.png)

## How we develop our API module?

Because we decouple all our module by using JSON and Http Request. We seperate each module easily, which allow us can have different develop cycle.

From the frist stage, we scraped all of our data and extract the main content from htmp, then push them all to our backend via multiple http request. Secondly, our own developed Natural Lange Parser Engine (NLPE) will wake up and using a distributed iterator to extract one by one. NLPE will have another http request to backend to created report and report event if the article is parsed. Thirdly, our user can use our frontend to view all our data in backend via RESTful APIs. In the fronend, to show the map and location of a ourtbreak, we will use Google Maps APIs.

Sidenote:

- NLPE also will call the Google Map API while parsing the article.
- Scraper and NLPE will wake up once a day to perform data collection and do parsing daily.

## How parameters passed to our module?

API examples:


## Developement Platform (Technical Stack)

**Main OS:** Linux/Unix *commonly used by developers*

**Frontend:** Vue, Vuetify *used to deliver simple and creative UI design*
Language: Vue, Javascript, CSS, HTML  
Packages: Moments, vue2-google-maps, axios, vuex, vue-router

**Backend:** Django, Django-Rest *commonly used framework that encourages rapid development and a clean design*
Language: Python3  
Packages: Django-rest-cors, Django REST Swagger,django-rest-framework-jwt

**Database:** PostgreSQL *used to manage the database system for our users*
Language: SQL (By ORM from Django)

**NLP:** nltk-all *used to analyze large amounts of natural language data*
Language: Python3  
Packages: Response, Threading, json

**Scraper:** Scrapy *used to frequently gather data from the main data source, Outbreak News Today*
Language: Python3  
Packages: lxml, cssselect, Response, json
