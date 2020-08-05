# Description

This **[mini webapp](https://stack-exchange-tag-search.herokuapp.com/search)** is designed to prompt a user to enter a keyword and get related tag recommendations. In order to do so, the app does three distinct steps:

1. It fetches about 10000 records of related tags in JSON using the Stack Exchange API.
2. A weighted graph is then generated from the saved records.
3. When a request is made with a specific keyword, a set of related tags are returned using a simple Brute Force Algorithm according to the weighted graph.

The app has two pages. 

[Home page](https://github.com/nttek/urekaDataScience/blob/master/stack-exchange-tag-search/App%20screenshots/Home%20page.png)

[Results page](https://github.com/nttek/urekaDataScience/blob/master/stack-exchange-tag-search/App%20screenshots/Results%20page.png)

Future improvements

- Implementation of a database feature to enable efficient management of large sets of records.
- Introducing new Machine Learning algorithms to enhance results.
- Additionally some parts of the code will be revised and made more readable along the process
