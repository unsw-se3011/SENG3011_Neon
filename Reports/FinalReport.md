# Final Report Summary

## Key benefits/achievements of the project

Throughout the history, public health are high concerns for health experts, researchers and governments.

Project Neon will track many disease reports from resource worldwide including OutbreaksNewsToday,  CDC, WHO, and Google News API, extract the important information through Scrapping and NLPE to provide advanced analysis presented in a user-friendly interface. 

By collecting a huge amount of data from the internet and extracting the summary report, we develop methods to track reports and estimate outbreaks and epidemics to capture global health hazards and help risk reduction. 

<br>
Our design separates the API into 3 parts.

Firstly, we use Scrapy to help us extract the data from the official website. In this part we also need additional management from this raw data such as mapping into the format we want as well as extract the useful information; hence we use Natural Language Parser Engine using NLPE. Through NLPE and Scrapy, we accomplished the extraction of raw data from websites as well as condense that raw data into only the necessary information to improve usability for our clients.

Further, we save these preprocess data into our database and waiting to be called. We decided to use mySQL as our database because it supports high volume of visits and provides huge storage space. Our database is here to achieve better reliability and efficienty through a huge amount of datasource, so that users always get the latest and greatest reports.

After we mapping all the data into the table of mySQL, we analyse the data in realtime analysis system in Python. Here, we produce estimation of outbreaks via infomation on the number of people infected, died, recovered, with new cases present. This will provide our users a very user firendly interface with visual representation of our efficient analysis which includes a colour intensity world map with the amount of people affected indicated, a monthly dot chart with our analysis results for given diseases, and also a weekly colomn graph showing the most recent reports on the disease.

Also, throughout our development, we used Docker, a continuous runtime environment system to ensure all parts of our system are functional and running without errors. This is to improve our websites' reliabability and usability as well as help us track the flow of our design.



## Team organisation and conclusion/appraisal of your work  

- Responsibilities/organization of the team
  - Ruofei.Huang  <br>
    Backend database developer and frontend implenmentation. Leader of our team. 
  - Xinze.Song  
    Design a simple backend frame and in charge of the NLPE calculation to extract texts from the targeted articles as well as outputing them to a json format file.
  - Ziqing.Yan  
  Testing both backend and frontend also provide advices about the UI design and implenmentation. Report writing and documentation.
  - Huiyue.Zhang  
  Report writing, provides advices throughout the project.

- How did the project go in your opinion  
  - Major achievements in project  
    - Development of an usable, reliable API by ourself.
    - Extract major information from website by Scrapy
    - Using NLPE to process the data from Scrapy
    - Using Vue to develop a website in a short time period
    - Format the data from other group's API hence it can use in our website
    - Using Swagger to document our API
    - Using Docker, Docker-compose and Kubernetes to standardize our runtime envrionement

  - Issues/problems encountered
    - Some report's main text still have unexpected characters and format
    - Some report's title missing number of affected people or disease name which makes the title not make sense
    - Could not reponse to the user input in report detail page.
    - The dot chart could not be presented in the first time of visit until it refresh the page
    - Could not use 'Get started' button to access search page
    - API returns data even have no parameters provided
    - API did not provide useful error message when it receive incorrect parameter

  - What kind of skills you wish you had before the workshop
    - Python Scrapy
    - Basic database development and management
    - CI/CD (continuous integration and continuous delivery)
    - Data anlayze algorithm
    - Natrual languague data extraction

  - Would you do it any differently now ?
    - Pay more resource on Natural Language part
    - Scrape more data source at the begining
    - Develop more algorithm on anlayze our data
    - Thinking more way to express our data
    - More detailed documentation on our API
    - More edge case testing of our backend
    - Focus more on deliverable rather than development build steps
