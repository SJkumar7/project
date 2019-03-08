from flask import Flask,render_template
app=Flask(__name__)

@app.route("/stu")

def student():
	return render_template("studentmedissue.html")

if __name__=='__main__':
	app.run(debug='true')  	