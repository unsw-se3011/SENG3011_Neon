# Final Report Summary

## Key benefits/achievements of the project

Throughout the history, public health are high concerns for health experts, researchers and governments.

Project Neon will track many disease reports from resource worldwide including OutbreaksNewsToday,  CDC, WHO, and Google News API, extract the important information through Scrapping and NLPE to provide advanced analysis presented in a user-friendly interface. 

By collecting a huge amount of data from the internet and extracting the summary report, we develop methods to track reports and estimate outbreaks and epidemics to capture global health hazards and help risk reduction. 

<br>
Our design separates the API into 3 parts.

Firstly, we use Scrapy to help us extract the data from the official website. In this part we also need additional management from this raw data such as mapping into the format we want as well as extract the useful information; hence we use Natural Language Parser Engine using NLPE. Through NLPE and Scrapy, we accomplished the extraction of raw data from websites as well as condense that raw data into only the necessary information to improve usability for our clients.

Further, we save these pre-processd data into our database and waiting to be called. We decided to use mySQL as our database because it supports high volume of visits and provides huge storage space. Our database is here to achieve better reliability and efficiently through a huge amount of datasource, so that users always get the latest and greatest reports.

After we mapping all the data into the table of mySQL, we analyse the data in real-time analysis system in Python. Here, we produce estimation of outbreaks via information on the number of people infected, died, recovered, with new cases present. This will provide our users a very user friendly interface with visual representation of our efficient analysis which includes a colour intensity world map with the amount of people affected indicated, a monthly dot chart with our analysis results for given diseases, and also a weekly column graph showing the most recent reports on the disease.

Also, throughout our development, we used Docker, a continuous runtime environment system to ensure all parts of our system are functional and running without errors. This is to improve our websites' reliabability and usability as well as help us track the flow of our design.

In the part of website development, we use Vue to help us build up the frontend quickly.   

The component library of Vue provides a rich source of UI design. We import the Google charts to visualize our data. Also the Javascript based language helps we import our data into the website. 

## Team organisation and conclusion/appraisal of your work  

- **Responsibilities/organization of the team**
  - Ruofei.Huang  <br>
    Backend database developer and frontend implenmentation. Leader of our team. 
  - Xinze.Song  
    Design a simple backend frame and in charge of the NLPE calculation to extract texts from the targeted articles as well as outputing them to a json format file.
  - Ziqing.Yan  
  Testing both backend and frontend also provide advices about the UI design and implenmentation. Report writing and documentation.
  - Huiyue.Zhang  
  UI design planning, extracting data from PandeTrack API and format to fit our website. Report writing and documentation, D2&D4 Presentations and provides advices throughout the project.

- **How did the project go in your opinion**
  - Major achievements in project  
    - Development of an usable, reliable API by ourselves.
    - Extract majority of information from website by Scrapy
    - Using NLPE to process the data from Scrapy
    - Using Vue to develop a website in a short time period
    - Format the data from other group's API so that it can be uses in our website
    - Using Swagger to document our API
    - Using Docker, Docker-compose and Kubernetes to standardize our runtime environment

  - Issues/problems encountered
    - Some report's main text still had unexpected characters and format, meaning we still have improvement in our NLPE stage for data extraction. However, we did our best to achieve a reliable natural language data extraction given our allocated time.
    - Some report's title missing number of affected people or disease name which makes the title not make sense, again emphasising the report extraction correctness can improve.
    - Could not reponed to the user input in report detail page.
    - The dot chart could not be presented in the first time of visit until it refresh the page. This was fixed by analyzing our data in the backend instead of frontend.
    - API did not provide useful error message when it receive incorrect parameter, hence manual testing is very important in determining errors that occurred.

  - What kind of skills you wish you had before the workshop
    - Python Scrapy
    - Basic database development and management
    - CI/CD (continuous integration and continuous delivery)
    - Data analysis algorithm
    - Natrual languague data extraction

  - Would you do it any differently now?
    - Focus more on Scrapy and word processing
    - Scrape more data at the beginning of our project
    - Develop more algorithms to anlayze our data
    - Use multiple forms to present our data 
    - More detailed documentation on our API
    - Develop more cases for testing of our backend
    - Focus more on deliverable rather than development build steps
