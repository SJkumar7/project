from flask import Flask,render_template
app=Flask(__name__)

@app.route("/pha")

def pharmacy():
	return render_template("pharmacytable.html")

if __name__=='__main__':
	app.run(debug='true')  	