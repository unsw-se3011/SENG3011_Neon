# Design Detail

## API Module Development

### Web Server

We are decide to develop a WEB API using REST base communication and secure by HTTP via SSL (HTTPS).

### Designing the API

Design details discuss in our group meetings, and we are following these steps:

1. Discuss overall service structure thorugh building ER diagrams which allows everyone to have a good understanding of our project goal and theme
2. Identify the iteration pattern between server and client
3. Design how to decouple the data
4. List all the API endpoints needed and the parameters and data requirements for them
5. Decide what endpoints we need to include
6. Collect fake data to start scraping infomation off outbreaknewstoday.com

### Implementing API endpoints

The implementation steps are as follow:

1. Design the ER diagram
   - Deisgn be table structure
   - Design basic relationship between each model
   - Design which field will include
   - Design what table cotain which field
2. Map the ER diagram to models in Django
    - Map the relationship as Django relationships (one-to-many, many-to-many or even one-to-one)
    - Map the field as Django Model field in different type
3. Develop the Serializer and ViewSet class for the models
    - Map the Model's field to serializer's field
    - Define custom model serilizers
    - Define the create method in different model
    - Attach Serializer to ViewSet
4. Register ViewSet to route in Django
    - Map a ViewSet as an API-endpoint in Django
5. Testing our endpoint
    - Create REST-Client interative documents
    - Create Django's unit-test
6. Implement the swagger documentation
    - Install created app to Django
7. Include the filter Middleware to support Search and filter
    - Install the filter and search middleware
    - Define the model-field need to be search in each model in their own ViewSet
8. Testing filter functionality
    - Use REST Client to do some basic test

### Documentation

We plan to use these to document our API:

- ER diagram
- Readme in API module
- REST Clint's interactive API documents
- Swagger interactive documentation

### Testing

We plan to do these to help us test our backend API:

- We will build our endpoint test cases by Django Unit Test
- We will not only develop test cases for our internal method using unit tests as well as useing manual black-box testing to test our API from sample database to ensure the right output
- We will also implement the CI/CD pipeline to ensure the ordering of structured tests to be checked when publishing to our website

## Running our API in Web Service Mode

Web Services facilitate machine to machine communication.

While SOAP is an official protocol, REST is an architectural style; it lays down a set of guidelines to provide a RESTful web service, for example, stateless existence and the use of HTTP status codes.

Therefore, our agents follow a clear RESTful design because REST has a more flexible architecture which is reliable and secure.

The REST architecture allows API providers to deliver data in multiple formats like HTML and JSON.
Our memssage format is JSON because it is easily consumed by other applications. The lightweight and human-readable JSON format is ideal for data interchange over the internet.

## Passing Parameters to our API Module

We will use query string parameters to pass requests and we will inspect the URI query part to gain access to these parameter values. 

We did not choose to send parameters in the body of a POST request because when executing a POST request, the client is actually submitting a new document to the remote host. Since we do not need to submit new information to the server for searching articles, POST request is not that suitable in passing parameters to our API.

Users have to input 3 main information strings:

1. Period of interest (date format):

   - Start_date: yyyy-MM-ddTHH:mm:ss (not null)
   - End_date: yyyy-MM-ddTHH:mm:ss (not null)

2. Key_terms (string format):

   - Keyterm: xxx,yyy
     - Where xxx and yyy are the terms you want to search.
     - These terms can be empty
     - Our API is not case sensitive

3. Location (string format):

   - Location: xxx 
        - Where xxx is the place user is interested in - Our API will automatically find all the parent of that location.
        - E.g. If location=Kensington, our API will auto complete:
            - Suburb = Kensington
            - City = Sydney
            - State = NSW
            - Country = Australia  
        - E.g. If location= NSW, our API will auto complete:
            - State = NSW
            - Country = Australia
        - Hence our website will return all articles within NSW, including Kensington and Sydney.

## Collecting Results from Our API Module

### The Format of API Output

Our API follow the RESTful design.

#### HTTP Headers

To pass the JSON object as body, we set our `Content-Type` in HTTP header as `application/json`; such as

```
Content-Type: application/json
```

Also, at `options` filed, we are specified the action user can take by their permission.

```
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
```

If they are not logined, or the object doesn't have that action, they will be restrited in some actions.

```
Allow: GET, HEAD, OPTIONS
```

Also, we will use HTTP Status code to indicate the result of performed action

| HTTP Status Code |      Meaning |
| :--------------- | -----------: |
| 2xx              |      Success |
| 3xx              |  Redirection |
| 4xx              | Client Error |
| 5xx              | Server Error |

Further more, some status has extended meaning when we following RESTful design.

| HTTP Status Code |                                        Meaning |
| :--------------- | ---------------------------------------------: |
| 200              |                                        Success |
| 201              |                               Resource created |
| 203              |                          Credential is expired |
| 301              |                                 Delete success |
| 307              |                                    Redirection |
| 400              |                      Request is not sufficient |
| 401              |                            Authorized required |
| 403              |                                  Access Denied |
| 404              |                          Not Found error Error |
| 405              |                          Action is not allowed |
| 408              |                                 Action timeout |
| 500              | Some bugs is triggered during handling request |
| 501              |                      Action is not implemented |
| 503              |                                 Server is down |

#### Query String

This part is description about the information packed in the query string (URL) when usign `GET` HTTP method. Format are as follow:

| Field name | Format                                  |             Example |
| :--------- | --------------------------------------- | ------------------: |
| start_date | ISO-DateTime Format                     | 2015-10-01T08:45:10 |
| end_date   | ISO-DateTime Format                     | 2015-11-01T19:37:12 |
| keyterm    | String, with `,` or `<space>`as divider |        Anthrax,Zika |
| continent  | String                                  |             Oceania |
| country    | String                                  |           Australia |
| state      | String                                  |                 NSW |
| city       | String                                  |              Sydney |

(Currently, we design our location is as four hirachical level, store in backend.)  
We will join these parameter by HTTP standard. Hence, the sample request is:

```
http://projectneon.app/v0/reports/?start_date=2015-10-01T08:45:10&end_date=2015-11-01T19:37:12&keyterm=Anthrax,Zika&continent=Oceania&country=Australia&state=NSW&city=Sydney
```

## Challenges Addressed

1. Search in Location Hierarchy
   - Store each hierarchy of match location into backend as four fields in location table
   - When matching in NLPE, we match to its full hierarchy from a dataset  
2. The Perforamance issue in NLPE
   - We localise our computation request from NLPE
   - NLPE as another client to the backend
   - Use multi-processing to speed up NLPE
   - Use multi-threading to speed up the storing data in the backend
3. Multi-words Matching issue in NLPE
   - Remove tense before matching each word
   - Create a mapping from disease's logogram to its full name
4. Matching natural language date and time
   - Find as much as date and time as possible
   - If the year is not given, we must have the context of the published date
5. Duplicate data after scraping
   - Use URL as a key, filter out the request we have visited
6. Performance issue in API
   - Use PostgreSQL instead of SQLite
   - Pre-process as much as we can to the data source
   - Dockerlise all the services we provide
   - If we need to scale to multiple machines, we can deploy via Kubernetes
     - The consistency of the log file will not preserved when deploying via Kubernetes

## Implementation Language

**_Main OS_: Linux/Unix**  
_Comparison_: Linux/Unix VS Windows

- Linux/Unix can easily install packages via terminal whereas Windows you have to find a website to download.
- Linux/Unix supports many compiler languages and libraries required for developers

**_Frontend_: Vue, Vuetify**  
_Justification_: It delivers simple, attractive and responsive UI design. It is well built and has a flat learning curve.

_Comparison_: Vue VS React VS Angular

- Angular is a full framework and React more flexible because of setting independence. However, React involves more JavaScript than Vue.
- Vue has the cleanest framework and libraries; it helps to keep code efficient with the perfect balance of internal dependencies and flexibilities.
- React requires a lot of modern JavaScript knowledge that Vue does not.

_Language_: Vue, Javascript, CSS, HTML  
_Packages_: Moments, vue2-google-maps, axios, vuex, vue-router

**_Backend_: Django, Django-Rest**  
_Justification_: Commonly used framework that encourages rapid development and a clean design. It is also easier to stick with a familiar platform, Python. Django is a web browsable API, has authenticated policies, function-based views and extensive documentation.

_Comparison_: Django VS Flask

- Django provides a full-featured MVC Framework whereas Flask has a micro-framework, providing very little upfront.
- Django REST Framework includes flexible support for versioning.
- Flask does not have an excellent browsable API option, unlike Django.

_Language_: Python3  
_Packages_: Django-rest-cors, Django REST Swagger, django-rest-framework-jwt

**_Database_: PostgreSQL**  
_Justification_: It is the default database choice for Django. It is most advanced, SQL-compliant and open-source objective-RDBMS. PostgreSQL is suitable for storing a large amount of data.

_Comparison_: PostgreSQL VS MySQL VS SQLite

- PostgreSQL is not just a relational database management system, and it is also objective with support for nesting.
- PostgreSQL is better for reliability and data integrity to compare MySQL.
- SQLite does not support user management whereas PostgreSQL does.

_Language_: SQL (By ORM from Django)

**_NLP_: spaCy**  
_Justification_: Most commonly used NLP (Natural Language Processing) Packages. NLTK has tools for almost all NLP tasks.

_Comparison_: nltk VS spaCy

- NLTK has many algorithms for a problem to choose from (good for researchers), and it is harder for a developer to use, whereas spaCy only keep the best algorithm for a particular problem, so it is easier to find and use.
- NLTK is a string processing library (returns lists of strings) whereas spaCy uses object-oriented approach (returns document object whose words and sentences are objects themselves)
- NLTK is better for sentence tokenisation, but spaCy is a lot faster for word tokenisation and part-of-speech tagging

![nltk and spaCy Compare](img/time.PNG)
_Language_: Python3  
_Packages_: Response, Threading, json

**_Scraper_: Scrapy**  
_Justification_: Most commonly used scraper framework. Scrapy is an asynchronous framework.

_Comparison_: Scrapy VS Selenium

- Scraping is a lot faster in Scrapy than in Selenium.
- Scrapy consumes less memory and lowers CPU usage compared to Selenium.

_Language_: Python3  
_Packages_: lxml, cssselect, Response, json

## Development Environment

### General

We use VS Code as our main code editor. Because it includes many extensions that are developed by the community. It supports:

- Powerful linter in the main languages we use -- Vue(Javascript) and python3
- Good performance.
- REST Client for interactive documentation.
- Free to use.
- Cross-platform.

### Backend

We use virtual environment provided by python. It's a tool to isolated python environment. We also use a requirement list of the package we use to provide a unified development environment.

### REST Client Extension

This extension could provide us with a

- Interactive Documentation of backend API
- Easy to use and understand
- Basic testing cases
- See the interaction in real-time

### Frontend

We use yarn as our default package manager. It provides

- Easy to use command line interface.
- Quicker in solving dependencies.
- Default choice in nodejs community.

Also, we will use Vue-UI to help us in our development.

- Provide curtial infromation about compiled output
- User-friendly interface
- Package management tool remaps to Web-UI.

## Deploy Environment

We have purchased Vultr VPS to host all our frontend and backend server. Some advantages include:

- It is cheap
- It is like a real machine
- It can be built as a docker host
- It has ublic IP
- It has high availability

Also, we will use our home server to host the scrapy and NLPE. Because running these tasks are:

- Compute-intensive
- Time-consuming
- The internal code may change a lot
- Doesn't need to run in 24\*7

Furthermore, we will follow the tech trend of containerlize our service. Because DevOps is facing:

- Diverge environment between develop, testing and deploy environment.
- Diverge toolchain between frontend, backend, database and testing.
- Has a high potential to make mistakes during manual configuration.

By using Docker, we can:

- Provide a unified environment in all phases of development.
- Automate the process of setting up the virtual environment.
- Don't need to change the toolchain when facing a different situation.

## 2.Platform	Design
**Requirements	of	the	API	and	the	analytics	platform**

**Software	architecture**

**Additional information** <br>
Extra API usage: 
  - Google News API (as related news data source)
  - Team CSB (CDC based datasource)
  - Team PandeTrack (WHO based datasource)

Algorithms employed
