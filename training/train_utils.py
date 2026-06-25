import os

DATA_DIR = 'data'
DATA_FILE_NAME = 'car-details.csv'
DATA_FILE_PATH = os.path.join(DATA_DIR, DATA_FILE_NAME)    #TO READ DATA FROM THIS ADDRESS

APP_DIR = 'app'
MODEL_DIR_NAME = 'models'
MODEL_NAME = 'model.joblib'
MODEL_DIR = os.path.join(APP_DIR, MODEL_DIR_NAME)   #path of models folder
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_NAME)    # COMPLETE PATH OF OUR TRAINED MODEL
