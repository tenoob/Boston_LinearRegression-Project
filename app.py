from flask import Flask, render_template, request
import pickle
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/result', methods=['POST'])  # This will be called from UI
def prediction():
    if (request.method=='POST'):
        num1=float(request.form['LSTAT'])
        num2 = float(request.form['RM'])
        model = pickle.load(open("linearregression.pkl",'rb'))
        result = model.predict([[num1,num2]])
        return render_template('results.html',result=round(result[0],2))

if __name__ == '__main__':
    app.run(debug=True)
