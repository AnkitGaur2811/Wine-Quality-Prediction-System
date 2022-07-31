# Now making Webapp for the project using some new things i have Learnt 
# Flask -> for backend
# HTML,CSS, Jinja -> for frontend 
# Heroku -> for deployment (if possible)
# ------------------------------importing all the libs and function needed------------------------
from email import message
from flask import Flask,render_template,request,redirect,url_for
from forms import wine_q # these imports sre from forms.py
import pickle
import numpy as np

# ------------------------------Loading the model to the webapp ---------------------------
Model = pickle.load(open("Wine_quality_pred.pkl","rb"))

# Creating Flask App
app = Flask(__name__)
app.config['SECRET_KEY']="Or@nge01@nk!t001"
# -------------------------------- Routes -----------------------------------------------
@app.route("/")
def home():
    """This function is the fuction which will show how the application renders to user"""
    return render_template("home.html")

@app.route("/about")
def about():
    """ This function renders the about section of the webapp"""
    return render_template("about.html")

@app.route("/predict",methods=["POST","GET"])
def winepred():
    """This is the main function which renders the form for prediction"""
    if request.method == "POST":
        # print(request)
        # print(request.form)
        feature=[x for x in request.form.values()]
        # print(feature)
        features=feature[1:]
        # print(features)
        feature_final=np.array(features).reshape(1,-1)
        print(feature_final)
        prediction=Model.predict(feature_final)
        if prediction=="good":
            return redirect(url_for('results', pred="g",name=feature[0]))
        else:
            return redirect(url_for('results', pred="b",name=feature[0]))    
    return render_template("prediction.html")

@app.route("/predict/res/<name>/<pred>")
def results(pred,name):
    """This route will render the result of the predictions to user"""
    return render_template("result.html",pred=pred,name=name)


# ----------------------------------- Main code ---------------------------------------
if __name__ =="__main__":
    Port = 80
    app.run(debug = True, port = Port)