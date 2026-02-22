# Instagram Feed Ranking AI 🤖📱

This project simulates Instagram's feed ranking system using Machine Learning.

The model predicts user engagement probability and ranks posts accordingly.



## 📌 Project Overview

This AI system:

- Takes user interaction data
- Predicts engagement probability
- Ranks posts based on predicted score

It mimics how Instagram prioritizes posts in a feed.



## 🛠 Technologies Used

- Python
- Pandas
- Scikit-Learn
- Random Forest Classifier



## 📂 Project Structure

Instagram-Feed-Ranking-AI/
│
├── dataset.csv        # Training dataset
├── model.py           # Model training script
├── ranking.py         # Post ranking logic
├── requirements.txt   # Dependencies
└── README.md          # Project documentation


## ⚙️ Features Used for Ranking

- Likes
- Comments
- Time Spent on Post
- Recency

The model calculates an engagement probability score and sorts posts from highest to lowest relevance.


## ▶ How to Run the Project

1️⃣ Install dependencies:

pip install -r requirements.txt

2️⃣ Train the model:

python model.py

3️⃣ Rank new posts:

python ranking.py



## 🎯 Future Improvements

- Add Streamlit Web Interface
- Add Deep Learning Model
- Improve Dataset Size
- Deploy as Web Application



