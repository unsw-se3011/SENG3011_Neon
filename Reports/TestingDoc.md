# Test Documentation
Project Neon have been working hard to ensure that our API is not only functional, but will also provide accurate and efficient data. 


**< describe the testing processes used in the development of API,  referring to the data and scripts included in Phase_1 folder. >**


## Testing Tools and Process:

**Black-box testing**: <br>
Swagger (used for testing) <br>
1.	A list of test cases and their expected results were documented and the request URL were passed into Swagger
2.	Tests included checking the status, the body and the content type of the response

Initially, the test cases only contained correct input. Then we added tests for incorrect output to check error handling of the API.

Limitation: 
- Multiple requests at the same time is not supported<br>
- Testing results could not be stored<br>
- Test case are not easy to change

**White-box testing**: <br>

Django Unit testing (used for testing) <br>
1.	API module was broken down and major methods are testing by individual unit tests through Django unit test.

Limitation: 
- Multiple requests at the same time is not supported<br>
- Testing results could not be stored<br>


**Performance testing**: <br>

JMeter (used for testing) <br>
1.  API functions could be tested by defining different test cases 
2.  By runing the test project, all the test cases that has been define will request the API 
3.  By changing the Thread Group the tests will be run in different time for example it can simulate that we have 5 users request for the same time and the defined test cases will be run in 5 times each
4.  All the test result and responses will be stored in Results Tree for checking 

Limitation: 
- Random input data for group testing is not supported


Shell Script (used for testing) <br>
1. By pre-define format text file, running different requests for curl in the shell script
2. Compute the average response time and by curl the output of returns 

Limitation :
- Input data is not easy to change



## Overview of Test Cases, Test Data and Test API results: <EXAMPLE from test data>

**Test Data:**


**Tests for Correctness:**

Black-box Testing:
```
Query:

start_date=2018-03-31T01:56:55
end_date=2019-03-31T01:56:55
location=Australia
key_term=Anthrax,Zika
```
_Results:_  Code 200 OK, returns list of results within the date range, location including areas specified as Sydney, and include all keyterms.

```
Query:

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
Query:

start_date=2018-03-31T01:56:55
end_date=2018-03-30T01:56:55
location=
key_term=
```
_Results:_  Code 400 Bad Request, with response: "date": "Start date must be earlier than end date."
```
Query:

start_date=2018-03-31
end_date=2019-03-31
location=Australia
key_term=Anthrax,Zika
```
_Results:_  Code 500 Internal Server Error, with response: "not supported between instances of 'NoneType' and 'NoneType'"


White-box Testing:
## < ADD INFO >
Test for Performance:<br>
Shell script tesing:
-   Testing average time for requesting, by record the time for each response in 10 times and expected the average time will not longer than 1s for all test cases
![10 times testing](img/test1.PNG)
-   Regular testing for each endpoint, by record the detail of response time inclding time_total, throughput, handshake, transmit. Each endpoint will be requested only single time, also the expected for total time will not longer than 1s for all test cases
![all testing](img/test2-1.PNG)
![all testing](img/test2-2.PNG)

JMeter testing:
-   Testing for 10 users are requesting for our API at the same time expect the responses are stable for all requests.
![input](img/j-2.PNG)
![output](img/j-1.PNG)

## < Describe the output of testing and what actions you took to improve the test results. >

Overall, the ouput of black-box testing had no major problems. One improvement for future deliverables is to develop better scrapping system so more reports are returned responding to a query.