# AISA (<u>AI</u> <u>S</u>tocks <u>A</u>nalyzer)

## Final Project: Bootcamp Big Data and Machine Learning (BDML) - CORE Code School
### Author: Nicolas Manduley

## General Description
A tool to assist in the analysis of the stock market making use of:
- Facial recognition to register a new user (and maybe also log-in)
- AI models to forecast tendencies in the stock market using Yahoo Finance
- Natural Language Processing (NLP) to evaluate social sentiment (Twitter, Reddit...) for specific assets
- An organized and up-to-date list of institutional investors from the SEC platform
- A streamlit dashboard to generate and visualize the graphics, tables, etc. to assist the analysis
- Others?

## Instructions
1. To clone this repository, execute `git clone git@github.com:nmanduley/final_project.git`
2. Install requirements by executing `pip install -r requirements.txt`
3. ?
4. NLP Model

By default, the Roberta NLP model is loaded from the original source (https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment).

Alternatively, for better performance, the model can be downloaded and executed from the hard drive.

To download the model, execute the file '*download_model.py*'. The script will create a new folder named "NLP_model" in the current working directory, where the model will be downloaded.

To load the model from the local directory, open (**insert .py script where the models are loaded; currently eval_social_sentiment.py**) and:
- Comment the line `path = 'cardiffnlp/twitter-roberta-base-sentiment' `
- Uncomment the line `path = os.path.normpath(os.getcwd() + '/NLP_model')`

Section's To-Do:
- [ ] README: Specify/update the python script where the models will be loaded (parentheses above)
- [ ] Maybe make a config.py (or other name) file to specify a variable with values, e.g. 'local' and 'remote', to switch between the NLP model loading methods 
- [ ] Write function to collect tweets, reddit posts and/or other data to evaluate social sentiment
- [ ] Convert *eval_social_sentiment.py* into a function with (social_network, stock_name) as inputs





