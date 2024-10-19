from flask import Flask, render_template
import pandas as pd
App = Flask(__name__)

@App.route('/')
def home():
    return render_template('index.html', title='Home', css = 'index')

@App.route('/home')
def index():
    return render_template('index.html', title='Home', css = 'index')

@App.route('/careers')
def careers():
    education_df = pd.read_csv("education.csv")
    education_list = education_df.to_dict(orient='records')
    for i, row in education_df.iterrows():
        print(i, row)
    careers_df = pd.read_csv("careers.csv")
    careers_list = careers_df.to_dict(orient='records')
    for i, row in careers_df.iterrows():
        print(i, row)

    return render_template('careers.html', title='Careers', css = 'careers', education=education_list, careers=careers_list)

@App.route('/contact')
def contact():
    return render_template('email.html', title='Contact' , css = 'contact')

if __name__ == '__main__':
    App.run(debug=True)