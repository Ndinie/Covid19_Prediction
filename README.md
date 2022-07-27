# Project Title
Prediction model on COVID19 cases

## Project Description
The year 2020 was a catastrophic year for humanity. Pneumonia of unknown aetiology was first reported in December 2019.
Since then, COVID-19 spread to the whole world and became a global pandemic. 
More than 200 countries were affected due to pandemic and many countries were trying to save precious lives of their people 
by imposing travel restrictions, quarantines, social distances, event postponements and lockdowns to prevent the spread of the virus. 

However, due to lackadaisical attitude, efforts attempted by the governments were jeopardised, thus, predisposing to the wide spread of virus and lost of lives.
The scientists believed that the absence of AI assisted automated tracking and predicting system is the cause of the wide spread of COVID-19 pandemic. Hence,
the scientist proposed the usage of deep learning model to predict the daily COVID cases to determine if travel bans should be imposed or rescinded.

## How to Install and Run the Project
This project can be run via [Google Colab](https://colab.research.google.com/?utm_source=scs-index) by creating a new notebook or just download the [Covid19_Prediction_main](https://github.com/Ndinie/Covid19_Prediction/blob/main/covid19_prediction_main.py) to test it out!

Google Colab also provide us with free GPU where all you neeed to do is change the runtime type to 'GPU'.
Plus Colab does not need any additional modules installation.

# How to use the project
You need to ensure that when you load the dataset, it links directly to the correct path which is here [cases_malaysia.csv](https://github.com/MoH-Malaysia/covid19-public/blob/main/epidemic/cases_malaysia.csv)

Don't forget to upload [covid19_prediction_module.py](https://github.com/Ndinie/Covid19_Prediction/blob/main/covid19_prediction_module.py) inside Covid19_Prediction_main.py so that you could run it smoothly.

Then after that you can proceed as usual. You can also check each of sections inside **Covid19_Prediction_main.py** 
to analyze how the flow of training the dataset is.

Below is the Architecture of the model that you can acquired under model development.

![model](https://github.com/Ndinie/Covid19_Prediction/blob/main/static/model.png)

The result from this model that we can achieved is as shown below:

![actual-vs-predicted-graph](https://github.com/Ndinie/Covid19_Prediction/blob/main/static/actual-vs-predicted-graph.png)

## Credits
Greatest appreciation to [MoH-Malaysia](https://github.com/MoH-Malaysia/covid19-public) for providing this dataset.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)

 
