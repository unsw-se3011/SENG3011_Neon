# Test Documentation
Project Neon have been working hard to ensure that our API is not only functional, but will also provide accurate and efficient data. 


**< describe the testing processes used in the development of API,  referring to the data and scripts included in Phase_1 folder. >**


## Testing Environment:
**Testing Tool & their limitations:**
1.	Jmeter (Performance testing)
2.	Postman (black box testing)
3.	Django Unit testing (white box testing)


## Testing Process:

**Black-box testing**:
1.	A list of test cases and their expected results were documented. and the request URL were passed into Swagger?
2.	Tests included checking the status, the body and the content type of the response

Initially, the test cases only contained correct input. Then we added tests for incorrect output to check error handling of the API.

**White-box testing**:
1.	API module was broken down and major methods are testing by individual unit tests through Django unit test.

**Performance testing**:


## Overview of Test Cases, Test Data and Test API results: <EXAMPLE from test data>


1.Tests for Correctness:
-	Location = Kensington 
-	Location = Sydney
-	Location = Australia 

2.Test for Incorrectness and Errors:
-	different status codes




3.Test for Performance:



## < Describe the output of testing and what actions you took to improve the test results. >