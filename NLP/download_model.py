# To be executed once only, to download and save the model from the original source to the specified path
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os

# Load model and tokenizer
roberta = 'cardiffnlp/twitter-roberta-base-sentiment'   # From https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment
model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)

# Save model
path = os.path.join(os.getcwd(), 'NLP_model')
model.save_pretrained(path)
tokenizer.save_pretrained(path)