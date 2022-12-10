### This will probably become a function with (social_network, stock) as inputs to evaluate the social sentiment
### of a specific stock in the specified social network.

from transformers import AutoTokenizer, AutoModelForSequenceClassification
from nlp_functions import preprocessing, get_sentiment
import os

# import time
# start_time = time.time()

# Load model and tokenizer
# path = os.path.normpath(os.getcwd() + '/NLP_model')
path = 'cardiffnlp/twitter-roberta-base-sentiment'    # To load it directly from the source
model = AutoModelForSequenceClassification.from_pretrained(path)
tokenizer = AutoTokenizer.from_pretrained(path)

### To be replaced with a function to retrieve tweets/reddit posts about a specific stock...
texts = ["test for a very good positive example", 
"this one is not likely to work very well",
"i'm not really sure about this one, time will tell",
"just a random useless one to see what happens"]

# Preprocessing
texts_processed = [preprocessing(text) for text in texts]

# Get sentiment
sentiment = [get_sentiment(text, model, tokenizer) for text in texts_processed]

print(sentiment)
# print(f"Execution time: {time.time()-start_time}")



