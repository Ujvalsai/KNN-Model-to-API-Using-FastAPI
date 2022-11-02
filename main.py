# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:36:54 2022

@author: vujvalsai
"""
from IrisData import Iris
import uvicorn
from fastapi import FastAPI
import pickle

import nest_asyncio
nest_asyncio.apply()

app = FastAPI()


@app.get('/')
def get_index():
    return {'Hello, Welcome to FastAPI'}

@app.get('/name')
def get_name(name:str):
    return{'Hello : ', name}

@app.post("/predict")
def get_data(data:Iris):

    
    data = data.dict()
    
    SpecalLength = data['SpecalLength']
    SepalWidth = data['SepalWidth']
    PetalLength = data['PetalLength'] 
    PetalWidth = data['PetalWidth']
    
    model = pickle.load(open(r'C:\Users\vujvalsai\.spyder-py3\FastAPI\KnnModelFastAPI\knnModelTest1.pkl','rb'))
    predict = model.predict([[SpecalLength, SepalWidth, PetalLength, PetalWidth]])
    
    predict = predict[0]
    
    if(predict == 0):
        return{'The flower is Setosa'}
    elif(predict == 1):
        return{'The flower is Versicolor'}
    elif(predict == 2):
        return{'The flower is Virginica'}
    else:
        return{'Invalid Inputs'}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
