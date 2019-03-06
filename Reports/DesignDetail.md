# Design Details - Initial documentation


Describe how	you	intend	 to	develop	 the	API	module	and	provide the	ability	 to	run	it	in	Web	
service	mode


## Developing API module
___
### Design
- **Scraping:**  we scraped all of our data and extract the main content from htmp, then push them all to our backend via multiple http request. our own developed Natural Lange Parser Engine (NLPE) will wake up and using a distributed iterator to extract one by one. NLPE will have another http request to backend to created report and report event if the article is parsed. 
- **Backend:** 

- **Frontend:** our user can use our frontend to view all our data in backend via RESTful APIs. In the fronend, to show the map and location of a ourtbreak, we will use Google Maps APIs.

### Development


### Document


### Testing




## Linking API to Web service mode
___




## Passing Parameters and Collecting Results


**Input Parameters for API：**
-


**Period of Interst:**
- time periods cannot be empty
- end_date must be later than start_date
```json
TimePeriod{
    start_date:  <yyyy-MM-ddTHH:mm:ss>,
    end_date:    <yyyy-MM-ddTHH:mm:ss>
};

```

**Keywords:**
- Keywords are not case sensitive
- List of key terms are seperated y a comma

```sql
Keywords{
    keywords    String
};
```

**Location:**
- Search disease reports by a location name e.g. city, country, state


```sql
location{
    location    String
};
```
Our API will filter the disease reports according to the time period



**END**
-
___



![Architecture Design](img/Architecture.png)

## How we develop our API module?

Because we decouple all our module by using JSON and Http Request. We seperate each module easily, which allow us can have different develop cycle.

From the frist stage, we scraped all of our data and extract the main content from htmp, then push them all to our backend via multiple http request. 

Secondly, our own developed Natural Lange Parser Engine (NLPE) will wake up and using a distributed iterator to extract one by one. NLPE will have another http request to backend to created report and report event if the article is parsed. 

Thirdly, our user can use our frontend to view all our data in backend via RESTful APIs. In the fronend, to show the map and location of a ourtbreak, we will use Google Maps APIs.

Sidenote:

- NLPE also will call the Google Map API while parsing the article.
- Scraper and NLPE will wake up once a day to perform data collection and do parsing daily.

## How parameters passed to our module?

API examples:




## Developement Platform (Technical Stack)

**Main OS: Linux/Unix**  
Reason: Commonly used by developers

**Frontend: Vue, Vuetify**  
Reason: To deliver simple and responsive UI design  
Language: Vue, Javascript, CSS, HTML  
Packages: Moments, vue2-google-maps, axios, vuex, vue-router

**Backend: Django, Django-Rest**  
Reason: Commonly used framework that encourages rapid development and a clean design  
Language: Python3  
Packages: Django-rest-cors, Django REST Swagger, django-rest-framework-jwt

**Database: PostgreSQL**  
Reason: Suitable to store large amount of data  
Language: SQL (By ORM from Django)

**NLP: nltk-all**  
Reason: Most commonly used NLP (Natural Language Procesing) Packages  
Language: Python3  
Packages: Response, Threading, json

**Scraper: Scrapy**  
Reason: Most commonly used scraper framework  
Language: Python3  
Packages: lxml, cssselect, Response, json
