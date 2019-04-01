# Test Documentation
Project Neon have been working hard to ensure that our API is not only functional, but will also provide accurate and efficient data. 


**< describe the testing processes used in the development of API,  referring to the data and scripts included in Phase_1 folder. >**


## Testing Environment:

Black-Box testing: Swagger 
- Swagger helps developers design, build, document, and test RESTful Web services. It queries different parameters effectively and provide flexibility when testing response types, URL requests. 
- A limitation is that Swagger does not save requests to a history which means previous tests cannot be found unless documented by individuals.
- When requests are passed into Swagger, it will return whether the querie passed or failed extracting the JSON response.


**Testing Tool & their limitations:**
1.	Jmeter (Performance testing)
2.	Swagger (black box testing)
3.	Django Unit testing (white box testing)


## Testing Process:

**Black-box testing**:
1.	A list of test cases and their expected results were documented. and the request URL were passed into Swagger
2.	Tests included checking the status, the body and the content type of the response as well as a check for the correctness of results returned from the query.

Initially, the test cases only contained correct input. Then we added tests for incorrect output to check error handling of the API.

**White-box testing**:
1.	API module was broken down and major methods are testing by individual unit tests through Django unit test.

**Performance testing**:


## Overview of Test Cases, Test Data and Test API results: <EXAMPLE from test data>

**Test Data:**


**Tests for Correctness:**

Black-box Testing:
```
start_date=2018-03-31T01:56:55
end_date=2019-03-31T01:56:55
location=Australia
key_term=Anthrax,Zika
```
_Results:_  Code 200 OK, returns list of results within the date range, location including areas specified as Sydney, and include all keyterms.

```
start_date=2018-03-31T01:56:55
end_date=2019-03-31T01:56:55
location=
key_term=
```
_Results:_  Code 200 OK, returns list of results within the date range, and order reports worldwide by newest date.



White-box Testing:
## < ADD INFO >


**Test for Incorrectness and Errors:**

Black-box Testing:

```
start_date=2018-03-31T01:56:55
end_date=2018-03-30T01:56:55
location=
key_term=
```
_Results:_  Code 400 Bad Request, with response: "date": "Start date must be earlier than end date."
```
start_date=2018-03-31
end_date=2019-03-31
location=Australia
key_term=Anthrax,Zika
```
_Results:_  Code 500 Internal Server Error, with response: "not supported between instances of 'NoneType' and 'NoneType'"


White-box Testing:
## < ADD INFO >


**Test for Performance:**
< ADD INFO >


## < Describe the output of testing and what actions you took to improve the test results. >


Overall, the ouput of black-box testing had no major problems. One improvement for future deliverables is to develop better scrapping system so more reports are returned responding to a query.

for white box testing.....


for performance.......