Recommendations POC
==============================

Summary
==============================
This Analysis is aimed to get comfortable with Python module Surprise for 
generating recommendations.

Dataset
==============================
This project will use the `ratings.csv` dataset available 
[here](https://www.kaggle.com/rounakbanik/the-movies-dataset/data)

This dataset is comma delimited.  It has has 26024289 observations.

Columns
------------------------------
* userId
* movieId
* rating
* timestamp

Analysis Performed
==============================
Built a recommender using `surprise` including looking at grid search and predicting to 10
recommendations for a user.

Future Work
==============================
I'm confused on how to do bulk top 10 per user and had to do 1 function call for every 
pair of user and movie.

Look at using cosine and other similarity metrics built into surprise.
