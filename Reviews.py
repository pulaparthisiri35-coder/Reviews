import nltk
from textblob import TextBlob
import re

# 1. Sample Dataset (Tweets/Reviews)
data = [
    "I absolutely love this new phone! The camera is amazing. 😍",
    "This was the worst experience ever. I want a refund.",
    "The service was okay, nothing special but not bad either.",
    "I'm so frustrated with the constant lagging. Avoid this app!",
    "Great quality and fast shipping. Highly recommend!",
    "The food was cold and the waiter was rude."
]

# 2. NLP Cleaning Function
def clean_text(text):
    # Remove special characters, numbers, and links
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert to lowercase
    text = text.lower().strip()
    return text

# 3. Process and Classify
print(f"{'Original Review':<55} | {'Sentiment'}")
print("-" * 70)

for review in data:
    cleaned = clean_text(review)
    
    # Using TextBlob to get sentiment polarity
    # Polarity is a float between -1.0 (Negative) and 1.0 (Positive)
    analysis = TextBlob(cleaned)
    
    if analysis.sentiment.polarity > 0:
        sentiment = "Positive ✅"
    elif analysis.sentiment.polarity < 0:
        sentiment = "Negative ❌"
    else:
        sentiment = "Neutral 😐"
        
    print(f"{review[:54]:<55} | {sentiment}")
  output:
Original Review                                         | Sentiment
----------------------------------------------------------------------
I absolutely love this new phone! The camera is amazing | Positive ✅
This was the worst experience ever. I want a refund.    | Negative ❌
The service was okay, nothing special but not bad either| Positive ✅
I'm so frustrated with the constant lagging. Avoid this | Negative ❌
Great quality and fast shipping. Highly recommend!      | Positive ✅
The food was cold and the waiter was rude.              | Negative ❌
