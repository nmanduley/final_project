import os
import cv2
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Layer, Conv2D, Dense, MaxPooling2D, Input, Flatten
import tensorflow as tf
import streamlit_authenticator as stauth
import requests


# Custom L1 distance layer
class L1Dist(Layer):
    def __init__(self, **kwargs):
        super().__init__()
    
    def call(self, input_embedding, validation_embedding):         # Input/anchor and pos/neg data
        return tf.math.abs(input_embedding - validation_embedding)


# Load model
def load_facial_recognition_model():
    model_path = os.path.join('facial_recognition', 'siamese_model.h5')
    model = tf.keras.models.load_model(model_path, compile=False,
        custom_objects={'L1Dist':L1Dist, 'BinaryCrossentropy':tf.losses.BinaryCrossentropy})
    return model


# Load verification images
def verify(model, detection_threshold, verification_threshold):
    results = []
    for image in os.listdir(os.path.join('facial_recognition', 'app_data', 'verification_images')):
        input_img = preprocess_image(os.path.join('facial_recognition', 'app_data', 'input_images', 'input_image.jpg'))
        validation_img = preprocess_image(os.path.join('facial_recognition', 'app_data', 'verification_images', image))
        prediction = model.predict(list(np.expand_dims([input_img, validation_img], axis=1)))
        results.append(prediction)

    detection = np.sum(np.array(results) > detection_threshold)
    verification = detection / len(os.listdir(os.path.join('facial_recognition', 'app_data', 'verification_images')))
    verified = verification > verification_threshold

    return results, verified


# Scale and resize
def preprocess_image(file_path):
    """Receives a path to an img and returns a 100x100p normalized image"""
    # Read image
    raw_img = tf.io.read_file(file_path)
    # Load image
    img = tf.io.decode_jpeg(raw_img)
    # Preprocessing
    img = tf.image.resize(img, (100,100))
    # Normalizing
    img = img/255.0
    return img


# Cut picture frame to 250x250p
def cut_frame(frame):
    dim = 250
    x_offset = 250
    y_offset = 150
    frame = frame[y_offset:y_offset+dim, x_offset:x_offset+dim, :]
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return frame


# Build train and test partition
def preprocess_twin(input_img, validation_img, label) -> tuple:
    '''Receives input and validation image with the corresponding label and returns
    a tuple containing the preprocessed input and validation image, as well as the label'''
    return (preprocess_image(input_img), preprocess_image(validation_img), label)


# Create authenticator object
def create_authenticator(api_key):
    # test_name = ["Nicolas", "admin"]
    # test_username = ["nmanduley", "admin"]
    # test_pass = ["123456", "123456"]
    # hashed_password = stauth.Hasher(test_pass).generate()
    # authenticator = stauth.Authenticate(test_name, test_username, hashed_password,
    # 'NM_final_project', 'cookie_key', cookie_expiry_days=30)

    # API connection
    api_url = 'http://127.0.0.1:8000'
    names_json = requests.get(f"{api_url}/first_names").json()
    all_names = [c["first_name"] for c in names_json]
    usernames_json = requests.get(f"{api_url}/users").json()
    all_usernames = [c["username"] for c in usernames_json]
    pass_json = requests.get(f"{api_url}/hashes/{api_key}").json()
    all_passwords = [c["password"] for c in pass_json]
    # Create authenticator object
    authenticator = stauth.Authenticate(all_names, all_usernames, all_passwords,\
    'NM_final_project', 'abcde', cookie_expiry_days=30)

    return authenticator


# Get authentication status prompt for display
def get_auth_prompt(verified):
    successful_prompt = '<p style="font-family:sans-serif; color:Green; font-size: 38px;">Authentication successful!</p>'
    failed_prompt = '<p style="font-family:sans-serif;color:Red; font-size: 38px;">Authentication failed</p>'
    return successful_prompt if verified else failed_prompt