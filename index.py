from flask import Flask,request,render_template

app = Flask(__name__)

data = []

@app.route("/",methods = ['GET','POST'])
def index():
    if request.form == 'GET':
        input = request.form.get('search')
        print(input)
    else:
        pass
    return render_template('index.html')

@app.route("/search")
def result():
    return render_template('results.html')



app.run(debug=True)

