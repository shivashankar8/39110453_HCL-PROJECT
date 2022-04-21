from flask import Flask, render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    
    return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)    
import pickle
model=pickle.load(open('./airpollution.pkl','rb'))
app=Flask(__name__)
@app.route('/')
def loadPage():
    return render_template('index.html')
@app.route('/predict',methods=["POST"])
def predict():
    a=float(request.form["SO2"])
    b=float(request.form["NO2"])
    c=float(request.form["RSPM"])
    d=float(request.form["SPM"])
    
    

    res=model.predict([[a,b,c,d]])
    return render_template('index.html',z=res[0])
if __name__=="__main__":
    app.run(debug=True)