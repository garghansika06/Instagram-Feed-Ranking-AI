import pandas as pd
import joblib

# Load trained model
model = joblib.load("feed_model.pkl")

def rank_posts(new_posts):
    probabilities = model.predict_proba(new_posts)[:,1]
    new_posts['ranking_score'] = probabilities
    ranked = new_posts.sort_values(by='ranking_score', ascending=False)
    return ranked

# Simulated new posts
sample_posts = pd.DataFrame({
    'likes':[1,0,1,0],
    'comments':[0,1,1,0],
    'time_spent':[30,20,60,15],
    'recency':[1,3,0,4]
})

ranked_feed = rank_posts(sample_posts)
print(ranked_feed)