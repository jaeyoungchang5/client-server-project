# Paradigms Final Project (Client Server Project): Web Startup
Our project analyzes police recruitment data based on ethnicity. The data source comes from the South Bend Data Portal, as we are looking into the South Bend Police Department.

## Group Members
- JaeYoung Chang (jchang5)
- Maggie Farrell (mfarre22)

## Server Side Functionality
The API functions developed for this project are GET_ETHNICITY, GET_TEST, GET_TESTS, GET_ETHNICTIES, PUT_RESULT, POST_RESULT, and DELETE_RESULT. 
- The GET functions are used to make get requests and retrieve various data based on a test or ethnicity. 
- PUT_RESULT will update a specific test result for a particular ethnicity
- POST_RESULT will increment the respective data for the particular ethnicity. 
- DELETE_RESULT will then delete a specific candidate's entire application data.

These functions can be used to not only discover trends across tests for a single ethnicity or to see how different ethnicities tend to perform in each test, but they can also be used to compare two ethnicities side by side and analyze their tests.

The full table with JSON specification can be found at this link: https://docs.google.com/document/d/1WCu4kMQ5VM_V39WjOPwB4ynSFCJYEurm2YRx8M5SLmU/edit

## Testing
The test file for this project can be executed by running the command 'python3 test_api.py'.

## Complexity
The project consists of 1 server, 2 libraries (one for retrieving recruitment data and one for user account information), 3 controllers (one for each library and one for resetting the data), and 1 client. The client in this case can be viewed in a browser using html and javascript. The main page of the webpage displays some initial data on test results by ethnicity. There are also several tabs at the top of the page, where the user can view more information about the project, add their own recruitment data, or login to their personal account. The scale of the project is broadended to many interpretations of the SBPD ethnicity data, so the user can view the data based on different variables and analyze trends that are revealed by this layout.

