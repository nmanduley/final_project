from scipy.special import softmax
import numpy as np

def preprocessing(text):
    '''Preprocess a text to split it into separate words.
    If a link is detected, it is replaced by the string 'http'.
    If a user mention is detected (@username), it is replaced by the string '@user'
    '''
    text_words = []
    for word in text.split(' '):
        if word.startswith('@') and len(word)>1:
            word = '@user'
        elif word.startswith('http'):
            word = 'http'
        text_words.append(word)
    return ' '.join(text_words)


def get_sentiment(text, model, tokenizer):
    '''Function that receives a preprocessed text, a model and a tokenizer and returns 
    the overall sentiment as Negative, Neutral or Positive.
    '''
    labels = ['Negative', 'Neutral', 'Positive']
    
    encoded_tweet = tokenizer(text, return_tensors='pt')
    output = model(**encoded_tweet)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    index = np.argmax(scores)
    return labels[index]