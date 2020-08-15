# Description

This **[mini webapp](https://tag-recommend.herokuapp.com/)** is an improvement on the **[previous web app](https://stack-exchange-tag-search.herokuapp.com/search)** which was designed to prompt a user to enter a keyword and get related tag recommendations. The tags are based on about 10000 documents fetched from Data Science site using Stack Exchange API. The improvement this time around is the addition a word2vec based machine learning algorithm which is found to provide some enhancements to the previously used brute-force method. Although both the methods were tested only on a limited data, there have been some significant observations that can be generalized.

The findings include 
1. Stack Exchange provides a brute-force based recommendation system. This was found to be evident even though limited data-set was used for creating the custom weighted-graph (only ten-thouthand documents).
2. Word2vec method returned much more insightful recommendations when compared to the graph algorithm very specific to the search term.
3. The graph algorithm was made to be more vocabulary rich by splitting hyphen separated words during the preprocessing . Whereas word2vec method didn't return results for some tag inquiries very close to what was given in the given documents (e.g. datascience).
4. Word2vec model changes in every new training although the training data was kept unchanged.

The above mentioned findings can be shown in the following tag recommendation results. The term 'deep-learning' were used on both methods and on the Stack Exchange web search.



Next steps
* Train word2vec model on bigrams and phrases