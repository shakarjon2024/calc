from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calc():
    result = None 

    if request.method  == "POST":
        a = int(request.form.get('a'))
        b = int(request.form.get('b'))
        result = a + b 

    return render_template("calc.html", result=result)



if __name__ == '__main__':
    app.run(debug=True)
