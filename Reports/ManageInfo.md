# Management Information

## Work Breakdown Structure

![Work Break Down Structure](img/wbs.png)

## Critical Path Method

### Dependency Graph

![Dependency Graph](img/dependency.png)

### Critical Path

![Critical Path](img/critical_path.png)

### Assigned Responsibility (Iter. 1)

| Name         | Responsibility                                                                                                                                                 |
| :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Huiyue ZHANG | Team Management>Product Owner> Design Planning>Report Witing{Epic Story, User Story, Use Cases, Deisgn features}                                               |
| Ruofei HUANG | Manager>GitHub>\*, Documents>Deliverable>{Management Information, Design Detail}, Management>Planning>{WBS, Critical Path},Scraper>Scrapy>\*(Fail to Complete) |
| Xinze SONG   | Backend>RESTful Endpoint>\*, Documents>Communicating>API Documents                                                                                             |
| Ziqing YAN   | Frontend>Normal INterface>\*                                                                                                                                   |

### Assigned Responsibility (Iter. 2)

| Name         | Responsibility                                                            |
| :----------- | :------------------------------------------------------------------------ |
| Huiyue ZHANG | Documents>Deliverable>Design Detail                                       |
| Ruofei HUANG | Documents>Deliverable>Management Information                              |
| Xinze SONG   | Data Extraction>NLPE>\*                                                   |
| Ziqing YAN   | Frontend>Normal INterface>\*, Documents>Deliverable>Testing Documentation |

### Assigned Responsibility (Iter. 3)

| Name         | Responsibility                                         |
| :----------- | :----------------------------------------------------- |
| Huiyue ZHANG |                                                        |
| Ruofei HUANG | Data Extraction>OAU>\*                                 |
| Xinze SONG   | Data Extraction>NLPE>\*                                |
| Ziqing YAN   | Frontend>Normal INterface>\*,Frontend>Map Interface>\* |

## Iteration Plan

| Iterations         | Detail                                                                           |
| :----------------- | :------------------------------------------------------------------------------- |
| 1. Week 1 - Week 3 | Backend APIs, Most frontend pages, Scraper and NLPE for one API                  |
| 2. Week 3 - Week 5 | Backend tests and admin site, attach frontend and backend, Map apis, Evolve NLPE |
| 3. Week 5 - Week 7 | Second API and NLPE, frontend testing, frontend style correction.                |
| 4. Week 7 - Week 9 | Prepare for presentation, final touches.                                         |

## Software Help Manage Team

<!-- Need to expand the details and how we will use it. -->

### GitHub/ Repo Project

Github is commonly use and be assigned as a repo manage platform by this course. Also the Project feature in the GitHub repo is a replacement of Trello. It's easy to use and we don't need to sign in to another website to manage the repository.

### WeChat

Since all of teamates are Chinese, we are using WeChat for all day. So the message in WeChat won't be missed by our teamates.

### Google Doc

Google Doc allow us to edit a same time. It's very suitable for us to work together about same documents and share the information about this project.

## Backlog for Daily Progress Checking

| Iterations | Detail                                                                                                                                                         |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Feb 19     | Setting up Messenger group, github, webcms; research for API; found new teammate                                                                               |
| Feb 20     | Decision of api, work distribution, mentoring time; start of User Story and Entity Relationship Diagram, Github, documenting.                                  |
| Feb 21     | Decision of meeting time                                                                                                                                       |
| Feb 22     | Finish up User Story, setting up new tasks.                                                                                                                    |
| Feb 25~26  | Inreamental progress, scraped ProMed’s metadata, data model, vue pages.                                                                                        |
| Feb 27     | Group Meeting and mentoring session, scrape all the data from Outbreak news today, front-end progress is checked, backen has a hard time to set up those APIs. |
| Feb 28     | Some backend endpoint is setted up, learning nltk for data extraction.                                                                                         |
| Mar 1      | Modify repo structure for D1, backend enpoint rush                                                                                                             |
| Mar 2      | Developing Endpoint                                                                                                                                            |
| Mar 3      | Documentation of Deliverable 1, Iris is back! Working on the backen endpoint                                                                                   |
| Mar 4      | Incremental improvement in API! Map interface in frontend. Acceptance Criteria in User Story and some Use case                                                 |
| Mar 5      | Critical Path                                                                                                                                                  |
| Meeting    | Talking about management issues, purpose of website, what's the whole sites structure, problems with current version of document.                              |
| Mar 6      | Basic version of backend is complete. Handover to Iris and Jeana to write document. Itios to write the NLPE. Merge branch for iteration 1.                     |
| Mar 7      | Incremental progress of deliverable 1 document                                                                                                                 |
| Mar 7      | Design documentation.                                                                                                                                          |
| Mar 11     | Another version of Design documentation.                                                                                                                       |
| Mar 13     | Actual start of iteration 2, assigned works to frontend, CICD, NLPE .                                                                                          |
| Mar 15     | Login in frontend, Some parser by Spacy, buy a domain and server for this project, dockerlise our backend.                                                     |
| Mar 18     | Increamental inproment in atural language parser, deploy backend by docker-compose.                                                                            |
| Mar 20     | Swich back to nltk for parser, three parser is set up, k8s delopment file is done, improment in frontend.                                                      |
| Mar 21     | Searching and filtering in backend.                                                                                                                            |
| Mar 23     | Refined Design document and some discussion, some parser is finished.                                                                                          |
| Mar 24     | Design documentation, location filter support, comments on the current parser.                                                                                 |
| Mar 25     | Replace old swagger engine, debug the swagger doucment, d2 document, finalise the design document.                                                             |
| Mar 27     | Swagger need imporvement, reduce the enpoint in the document and add expect value. Need to impove the NLPE for more parser. Need to add a img url for article. |
| Mar 27     | Swagger document start to redo. Location logic need to modify. Teststing document and log file clarifications. Search component in frontend.                   |
| Mar 29     | Expose log file, add img url in backend. Half way of the swagger documents.                                                                                    |
| Mar 31     | Merge the nlpe into master. Swagger document and server is setted up. Tweaked the location filter.                                                             |
| Apr 1      | Refactor part of nlpe code, create a JSON client for parser, import data to server, deploy on server.                                                          |
| Apr 2      | Quick fix on sender and bugs on backend.                                                                                                                       |
| Apr 3      | Bugs on the backend, need more detail on the architecture.                                                                                                     |
| Apr 3      | Frontend release plan, next week's meeting's plan, some unclear about demenstration, imporve disease parser in nlpe, backend quickfix.                         |
| Apr 5      | Merge the improvement of NLPE                                                                                                                                  |
| Apr 6      | Releasing the frontend, improvement on the json client for NLPE.                                                                                               |
| Apr 7      | Frontend improment, demonstration's documents.                                                                                                                 |
| Apr 8      | Frontend progress is behind, restart a branch to do it.                                                                                                        |
| Apr 13-21    | Based on the feedback of the first presentation we added more features such as map and dot chart also changed some UI design of our website.                                    |
|Apr 22 Meeting | For the new functions we do some testing and found out the bugs. Also we decided to add the BookMark function to our website. Finally we do some preparation for the presentation. |
| Apr 23    | Add the BookMark feature and fix the bugs that has been found. Prepare for the final presentation.                                |
| Apr 24   | Concluded the whole project and the presentation. Wrote the final report.                          |
| Apr 29    | Finished our final report |


## Summary of Poject Management
Overall, we divided the entire project into several parts which are the frontend, backend, scraper, management, documentation, and data extraction. Also, we subdivided what we needed to do in each part, and set a time we expected to finish the task for each part. Meanwhile, the actual time taken to complete each part were constantly updated. Tasks for each member were distributed according to their personal strength in order to improve productivity. Each team member would first mark the their given tasks in yellow and then mark them in green after they completed the tasks. Although all the work we planned were carried out in the way we want, unfortunately due to time, some of our parts were not fully implemented as we expected. Besides, we used Wechat to communicate with each other since everyone of us have a Wechat account. Wechat made it faster and easier to communicate and make improvement for our project as well as acting the role as a online log book which records all the work we done everyday so that everyone of us were on the same page to ensure the effectiveness and efficiency of our work.
