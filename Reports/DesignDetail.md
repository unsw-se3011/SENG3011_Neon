# Design Detail

## API Module Development

### Design

Design details will be discuss in our group meetings, we will follow these steps:

1. Disscuss Overall Service Structure
2. Identify the iteration pattern between server and client
3. Collect all the information need to be included in endpoints
4. Design how to decouple the data
5. Deside what endpoints we need to include

### Implementation

The implementation steps are as follow:

1. Design the ER diagrame
2. Map the ER diagrame to models in django
3. Develop the Serializer and ViewSet class for the models
4. Register ViewSet to route in Django
5. Testing our endpoint
6. Implement the swagger documentation
7. Include the filter Middleware to support Search and filter
8. Testing filter functionality

### Documentation

We will try to uses these to document our api:

- ER diagrame
- Readme in API module
- REST Clint's interative API documents
- Swagger interative documentation

### Testing

We will try to do these to help us test our backend API:

- REST Client's interative API documents
- Develop our enpoint test cases by Django Unit Test
- Develop test cases for our internal method by using Django Unit Test

## Running Our API in Web Service Mode

We want to build a reliable and secure API module and our agent will follow the RESTful design to communicate.

### The Architectural Model

We will use the [Service Oriented Architecture](https://www.w3.org/TR/ws-arch/#service_oriented_architecture) in Web Services and Arichitecural Style.

- Agent
  - Requester Agent:
    - Signle page web app
    - Natual Language Process Engine
    - Outbreak Aggreagation Unit
  - Provider Agent:
    - Django Backend
- Person or Organization
  - Own by team Neon
- Action
  - Create, Update and Delete on resources
  - Read and Search on Resources
  - Comment on Resource
  - Register account
  - Authenticate
- Policy
  - Only Administrator can perform Create, Update and Delete on resources
  - Anyone can Read and Search on Resources
  - Registered user can Comment on Resource
  - Anyone can Register
  - Registered user can authenticate
- Goal State
  - Resources are correctly managed by Administrator
  - Registered User can comment on Resource
  - User can register
  - Registered user can be authenticated
- Service Role
  - Researcher
  - Admin
  - Natural Language Process Unit (Machine)
  - Outbreak Aggregation Unit (Machine)
- Message
  - Resources
  - Authenticate Information
  - Comments
- Service Interface
  - Web Interface
    - REST Endpoints
    - Swagger Documents
    - JSON Web Token Endpoint
  - Service Semantics
    - RESTful Design
    - JWT Authentication
- Service Task
  - Admin login and manage Resources
  - Registered user login and comments on Resources
  - User and registered user read resources
  - Unregistered user to register and login

## Passing Parameters to Our API Module

## Collecting Results from Our API Module

## Implementation Language

## Development Environment

## Deploy Environement
