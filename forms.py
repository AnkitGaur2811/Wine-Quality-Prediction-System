# Importing Flask's form modules to make the forms
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,DecimalField
from wtforms.validators import InputRequired,Length

# ----------------- class for form ------------
class wine_q(FlaskForm):
    fixed_acidity = DecimalField("Fixed acidity: ", validators=[InputRequired()])
    volatile_acidity = DecimalField("Volatile acidity: ", validators=[InputRequired()])
    citric_acid = DecimalField("Citric acid: ", validators=[InputRequired()])
    residual_sugar = DecimalField("Residual sugar: ", validators=[InputRequired()])
    chlorides = DecimalField("Chlorides: ", validators=[InputRequired()])
    free_sulfur_dioxide = DecimalField("Free sulfur dioxide: ", validators=[InputRequired()])
    total_sulfur_dioxide = DecimalField("Total sulfur dioxide: ", validators=[InputRequired()])
    density = DecimalField("Density: ", validators=[InputRequired()])
    pH = DecimalField("pH: ", validators=[InputRequired()])
    sulphates = DecimalField("Sulphates: ", validators=[InputRequired()])
    alcohol = DecimalField("Alcohol: ", validators=[InputRequired()])
    submit = SubmitField('Predict Now')
