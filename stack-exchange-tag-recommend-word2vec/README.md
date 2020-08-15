# Description

This **[mini webapp](https://tag-recommend.herokuapp.com/)** is an improvement on the **[previous web app](https://stack-exchange-tag-search.herokuapp.com/search)** which was designed to prompt a user to enter a keyword and get related tag recommendations. The tags are based on about 10000 documents fetched from Data Science site using Stack Exchange API. The improvement this time around is the addition a word2vec based machine learning algorithm which is found to provide some enhancements to the previously tested graph based brute-force method. Although both the methods were tested only on a limited data, there have been some significant observations that can be generalized. As an example, the following results were obtained as the term 'deep-learning' was searched for using both algorithms and on the Stack Exchange data science site.

In stack-exchange          |  Brute-force graph based                 |  Word2vec
:-------------------------:|:----------------------------------------:|:-------------------------:
![](https://github.com/nttek/urekaDataScience/blob/master/stack-exchange-tag-recommend-word2vec/ipynb/Data/stack-exchange3.png)  |  ![](https://github.com/nttek/urekaDataScience/blob/master/stack-exchange-tag-recommend-word2vec/ipynb/Data/graph2.png)  |  ![](https://github.com/nttek/urekaDataScience/blob/master/stack-exchange-tag-recommend-word2vec/ipynb/Data/word2vec2.png)


The findings above can be summarized as follows: 
1. Stack Exchange provides a brute-force based recommendation system. This was found to be evident even though limited data-set was used for creating the custom weighted-graph (only ten-thouthand documents).
2. Word2vec method returned much more insightful recommendations when compared to the graph algorithm very specific to the search term.
3. The graph algorithm was made to be more vocabulary rich by splitting hyphen separated words during the preprocessing . Whereas word2vec method didn't return results for some tag inquiries very close to what was given in the given documents (e.g. datascience).
4. Word2vec model changes in every new training although the training data was kept unchanged.

Next steps
* Train word2vec model on bigrams and phrases
