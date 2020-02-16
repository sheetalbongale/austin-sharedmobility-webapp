from flask import Flask, render_template
from plot import plot

app = Flask(__name__)


@app.route("/")
def render_plot():
    return render_template("index.html", plot_data=plot())


if __name__ == "__main__":
    app.run(debug=True)
