from flask import Flask,render_template,request
import requests
import json
app=Flask(__name__)

@app.route("/")
def home() :
	return render_template("index2.html")



@app.route("/login")
def login() :
	return render_template("login.html")

@app.route("/mg",methods=['POST','GET'])
def inseret():
	if request.method=='POST':
		result=request.form
		x1=json.dumps(result)
		print(x1)
		url=' https://287c848jxj.execute-api.us-east-1.amazonaws.com/dev'
		headers={"content-type":"application/json"}
		r=requests.post(url,data=x1,headers=headers)
		return HttpResponse 'data posted successfully'

if __name__=="__main__":
    app.run(debug='true')	














