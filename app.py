from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import pickle
import os
from wsgiref import simple_server
from Raw_Data_Formater import Raw_Data_Formater
from Data_Validator import data_validator
from Preprocessing.preprocessing import Preprocessor
from Log_writer.logger import App_Logger

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

log_writer = App_Logger()

app = Flask(__name__)
CORS(app)


@app.route('/', methods=["GET"])
@cross_origin()
def homePage():
    log_writer.log("Entered Home Page"+"\n\n\n")
    return render_template("index.html")


@app.route('/Prediction', methods=["GET", "POST"])
@cross_origin()
def  index():
    try:
        if request.method == 'POST':
            data = Raw_Data_Formater.data_formater()
            data = data.format_data()
            log_writer.log("Data Aggregation and Formatting Completed Successfully")

            validator = data_validator.Validator()
            validator.validate(data)
            log_writer.log("Data Validation Completed Successfully")

            preprocessor=Preprocessor()
            data=preprocessor.preprocess(data)
            log_writer.log("Preprocessing and Transformation of Data Completed Successfully")

            model = pickle.load(open('xgboost.pickle', 'rb'))
            log_writer.log("XGBoost Model Loaded successfully")
            pred = model.predict(data)
            log_writer.log("Prediction for the given data created successfully "+"\n\n\n")

            return render_template("results.html", prediction=pred[0])

    except Exception as e:
        return print(e)

port = int(os.getenv("PORT",5001))

if __name__ == "__main__":
    host = '0.0.0.0'
    app.run(debug=True)
    httpd = simple_server.make_server(host, port, app)
    print("Serving on %s %d" % (host, port))
    httpd.serve_forever()
