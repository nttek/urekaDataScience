# Description

This **[mini webapp](https://tag-recommend.herokuapp.com/)** is an improvement on the **[previous web app](https://stack-exchange-tag-search.herokuapp.com/search)** which was designed to prompt a user to enter a keyword and get related tag recommendations. The tags are based on about 10000 documents fetched from Data Science site using Stack Exchange API. The improvement this time around is the addition a word2vec based machine learning algorithm which is found to provide some enhancements to the previously used brute-force method.


The findings include 
1. Stack-exchange provides a brute-force based recommendation system. This was found to be evident even though limited data-set was used for creating the custom weighted-graph (only ten-thouthand documents).

2. Word2vec method returned much more insightful when compared to the graph algorithm even beyond expectations.

3. Both the used methods work only on the limited data used.

4. The graph algorithm was made to be more vocabulary rich by splitting hyphen separated words during the preprocessing . Whereas word2vec method didn't return results for some tag inquiries very close to what was given in the given documents (e.g. datascience).

5. Word2vec model changes in every new training although the training data was kept unchanged.
