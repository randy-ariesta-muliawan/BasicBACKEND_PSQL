from flask import Flask, render_template

app = Flask(__name__)


@app.route("/about")
def about():

	return render_template("about.html")

@app.route("/contact")
def contact():

	return render_template("contact.html")


@app.route("/instagram")
def instagram():

	return render_template("instagram.html")


if __name__ == '__main__':
	app.run(debug=True)