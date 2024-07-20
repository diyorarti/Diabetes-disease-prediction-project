from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from ML.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

@app.route('/',methods=['GET']) 
def homePage():
    return render_template("index.html")

@app.route('/train', methods=["GET"])
def training():
      os.system("python main.py")
      return "Training Successful!" 


@app.route('/predict',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            HighBP =float(request.form['HighBP'])
            HighChol =float(request.form['HighChol'])
            CholCheck =float(request.form['CholCheck'])
            BMI =float(request.form['BMI'])
            Smoker =float(request.form['Smoker'])
            Stroke =float(request.form['Stroke'])
            HeartDiseaseorAttack =float(request.form['HeartDiseaseorAttack'])
            PhysActivity =float(request.form['PhysActivity'])
            Fruits =float(request.form['Fruits'])
            Veggies =float(request.form['Veggies'])
            HvyAlcoholConsump =float(request.form['HvyAlcoholConsump'])
            AnyHealthcare =float(request.form['AnyHealthcare'])
            NoDocbcCost =float(request.form['NoDocbcCost'])
            GenHlth =float(request.form['GenHlth'])
            MentHlth =float(request.form['MentHlth'])
            PhysHlth =float(request.form['PhysHlth'])
            DiffWalk =float(request.form['DifWalk'])
            Sex =float(request.form['Sex'])
            Age =float(request.form['Age'])
            Education =float(request.form['Education'])
            Income = float(request.form['Income'])
       
         
            data = [HighBP, HighChol, CholCheck, BMI,Smoker, Stroke, HeartDiseaseorAttack, PhysActivity, Fruits, Veggies, HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age, Education, Income]
            data = np.array(data).reshape(1, 11)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')

if __name__ == "__main__":
	app.run(host="0.0.0.0", port = 8080)