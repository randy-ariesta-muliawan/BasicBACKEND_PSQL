from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():

	return render_template("search.html")


@app.route("/search")
def search():

	query = request.args.get("query")
	return redirect("https://www.google.com/search?q="+query)


if __name__ == '__main__':
	app.run(debug=True)