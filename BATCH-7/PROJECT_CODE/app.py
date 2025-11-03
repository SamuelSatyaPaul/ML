from flask import Flask, render_template, request, flash, redirect
import pickle
import numpy as np
from PIL import Image

app = Flask(__name__)

def predict(values, dic):
    
    if len(values) == 24:
        model = pickle.load(open('model.pkl','rb'))
        
        pre=model.predict([values])[0]
        print(pre)
        return pre
    
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/kidney", methods=['GET', 'POST'])
def kidneyPage():
    return render_template('kidney.html')


@app.route("/predict", methods = ['POST', 'GET'])
def predictPage():
    try:
        if request.method == 'POST':
            to_predict_dict = request.form.to_dict()
            to_predict_list = list(map(float, list(to_predict_dict.values())))
            for v in to_predict_list:
                print(type(v))
            pred = predict(to_predict_list, to_predict_dict)
            print(pred)
    except Exception as e:
        print(e)
        message = "Please enter valid Data"
        return render_template("home.html", message = message)

    return render_template('predict.html', pred = pred)


if __name__ == '__main__':
	app.run(debug = True)