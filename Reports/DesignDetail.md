# Design Details - Initial documentation

## Developing API module

(This is for just backend module, I'm not quite sure that the API module is just backend, or all the module we include in the system.)

We designed the ER diagrame base on the requirement list. Then we create the models of it. The models in Django ORM will map to the database schema. Then we base on the model develop our serializers and viewsets. In this stage, we tests our API at first time. Then we overwrite the function in viewsets and serilaizer we can support the relationships definded in the databse. Then we can test it again in the enpoints. In this stage, we include some basic doucments. We can wrap our output and the input JSON together to the enpoint we want to meet the requirements. Then we finish up the documents. Finally, we tweak our endpoind by adding the search functionlaity and the filter keyword in our enpoint by configure our filter backends. Tweak the permission by adding the permission setting or even write our own permission controll classes. Also add this final piece of software.

Firstly,we intend to choose the combination of Python and Django to build up the API server.Both of them provide rich resources and functions for programming and web server development and make the coding become easier.

Then,based on the requirement an API must have basic methods such as GET, POST, PUT and DELETE to allow website could get the information correctly. Since the API server provides these methods we should use in every object, we separate the API for 5 sections by classify its URL.

Based on the functionality,’users’ is for user register and login request which provides authentication for users as well as the management of users.‘Reports’ which provides an interface for getting the whole report contains layout of an outbreak news.’Reports events’ which relays on report provides an interface for getting the detailed information about the report.’Articles’ are the original resources that we scrap from the official outbreak websites provides and interface for getting the completed article which users might need to use.’Location’ provides the function of finding all related reports that happened on a specific area.

After we have a structure of API,we need to consider about the data of API.By the suggestion of specification,we intend to use a scraper to gather data frequently. Python scrapy library will be our choice.We are preferring run this service in daily.Since we already choose reliable and official API it will help us to filter some articles we do not need it.These data will be analysed and defined as outbreak by our server and breakdown into a report object stored in our database.

Finally,we will document the API as a readable,user friendly website form.As specification suggestion we will use swagger to document our API. It will develop a clear guide for further website request.It should show all the methods we have,what parameters that function needs,what is the response of the API and what the response indicates also gives example of how to use each function.

### Design

- **Scraping:** we scraped all of our data and extract the main content from htmp, then push them all to our backend via multiple http request. our own developed Natural Lange Parser Engine (NLPE) will wake up and using a distributed iterator to extract one by one. NLPE will have another http request to backend to created report and report event if the article is parsed.
- **Backend:**

- **Frontend:** our user can use our frontend to view all our data in backend via RESTful APIs. In the fronend, to show the map and location of a ourtbreak, we will use Google Maps APIs.

### Development

### Document

### Testing

## Frontend

Base on the doucments provided in the backend phase, we first connect our frontend and backend via some dummy components. In this phase we don't chase on the visual effect and design rules. Then we know what's the difficulties on representing the data in the backend. We can have some draft on how we representing our data, what's component we will use. Then after design, we can directly code it since vuetify have many good qulity and easy to use components which can save our time by skipping the Hi-fi phase. In this stage we might meet some model need to have difficult frontend logic to show it properly, we will introduce some unittest in our fontend to help our developments. After this, we have a pretty and workable frontend web app. Then, we can final tweak our frontend by tweaking colors, adding adpation code for mobile phone and add responsive style to properly display our component on small devices. Finally, we will test our fontend together, find some bugs or make some suggestion to improve our frontend. And we code it for our suggestion from our teammates.

## Scraper

First, we create a new spider for our new datasorce. Then, we test it and scrape some example page from it. In here we divide it into two part. One is for parse the index page which include the links to all the article we want to scrape from. So we parse the index page for the links. Then we can develop our main parse code for the parser of main article. We need to locate the main text document elements. Then we remove the content we don't want such as advertisements, scripts, link to non-article content. Then we wrap all the inforamtion in to Item class we for this website. Use Item pipline and store them as a JSON Lines file. Finally, we use our JSON Lines file and a simple scipt to store our scrapted articles into our backend.

## NLPE/ OAU (Outbreak Aggregation Unit)

We devlop our simple script to interact to our own backend. Then we use our NLP package to tokenise a article, chunking it. Then we apply our code for data extration such as date, disease, syndrome, effect type and so on. We wrap our data into report and some report events in it. In OAU, we instead of extrating data, we develop our geological fence and time fence to detect the outrbeaks then we wrap those reports into a outbreak object. Then we use a small script to store it back to our frontend.

## Linking API to Web service mode

# Passing Parameters and Collecting Results

**Input Parameters for API:**

_Period of Interst:_

- time periods cannot be empty
- end_date must be later than start_date

```sql
TimePeriod{
    start_date:  <yyyy-MM-ddTHH:mm:ss>,
    end_date:    <yyyy-MM-ddTHH:mm:ss>
};

```

_Keywords:_

- Keywords are not case sensitive
- List of key terms are seperated y a comma

```sql
Keywords{
    keywords:    <string>
};
```

_Location:_

- Search disease reports by a location name e.g. city, country, state

```sql
location{
    location:    <string>
};
```

**Collecting results:**
Our API will filter the disease reports according to the time period

**Output from API:**

GET\
PUT\
POST\
DELETE

## Developement Platform (Technical Stack)

**_Main OS_: Linux/Unix**  
_Justification_: It is commonly used by developers

_Comparison_: Linux/Unix VS Windows

- Linux/Unix are able to easily install packages via terminal whereas Windows you have to find a website to download.

**_Frontend_: Vue, Vuetify**  
_Justification_: It delivers simple, attractive and responsive UI design. It is well built and has easy architecture.

_Comparison_: Vue VS React VS Angular

- React is usually used for building mobile apps.
- Angular is a full framework and React is more flexible because of set independence. However, React involves more JavaScript than Vue.
- Vue has the cleanest framework and libraries; it helps to keep code efficient with the perfect balance of internal dependencies and flexibilities.

_Language_: Vue, Javascript, CSS, HTML  
_Packages_: Moments, vue2-google-maps, axios, vuex, vue-router

**_Backend_: Django, Django-Rest**  
_Justification_: Commonly used framework that encourages rapid development and a clean design. It is also easier to stick with a familiar platform, Python. Django is a web browsable API, has authenticated policies, function-based views and extensive documentation.

_Comparison_: Django VS Flask

- Django provides a full-featured MVC Framework whereas Flask has a micro-framework, providing very little upfront.
- Django REST Framework includes flexible support for versioning.
- Flask does not have a good browsable API option, unlike Django.

_Language_: Python3  
_Packages_: Django-rest-cors, Django REST Swagger, django-rest-framework-jwt

**_Database_: PostgreSQL**  
_Justification_: It is the default database choice for Django. It is most advanced, SQL-compliant and open-source objective-RDBMS. PostgreSQL is suitable for storing large amount of data.

_Comparison_: PostgreSQL VS MySQL VS SQLite

- PostgreSQL is not just a relational database management system, it is also objective with support for nesting.
- PostgreSQL is better for reliability and data integrity whereas MySQL handles less reliability.
- SQLite does not support user management whereas PostgreSQL does.

_Language_: SQL (By ORM from Django)

**_NLP_: nltk-all**  
_Justification_: Most commonly used NLP (Natural Language Procesing) Packages. NLTK has tools for almost all NLP tasks.

_Comparison_: nltk VS spaCy

- TBA

_Language_: Python3  
_Packages_: Response, Threading, json

**_Scraper_: Scrapy**  
_Justification_: Most commonly used scraper framework. Scrapy is an asynchronous framework

_Comparison_: Scrapy VS Selenium

- Scraping is a lot faster in Scrapy than in Selenium.
- Scrapy consumes less memory and lower CPU usage compared to Selenium.

_Language_: Python3  
_Packages_: lxml, cssselect, Response, json

## **END**

---

![Architecture Design](img/Architecture.png)

## How we develop our API module?

Because we decouple all our module by using JSON and Http Request. We seperate each module easily, which allow us can have different develop cycle.

From the frist stage, we scraped all of our data and extract the main content from htmp, then push them all to our backend via multiple http request.

Secondly, our own developed Natural Lange Parser Engine (NLPE) will wake up and using a distributed iterator to extract one by one. NLPE will have another http request to backend to created report and report event if the article is parsed.

Thirdly, our user can use our frontend to view all our data in backend via RESTful APIs. In the fronend, to show the map and location of a ourtbreak, we will use Google Maps APIs.

Sidenote:

- NLPE also will call the Google Map API while parsing the article.
- Scraper and NLPE will wake up once a day to perform data collection and do parsing daily.
