from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello():
    html_str="""
    <!DOCTYPE html>
 <html lang="kr">
 <head>
 <meta charset="UTF-8">
 <title>Flask Home Page</title>
 </head>
 <body>
 <form method="GET" action="/gugudan">
 <h2>구구단 출력하기</h2>
 <label>단 :
 <input type="text" name="dan">
 </label>
 <button type="submit">출력</button>
 </form>
 </body>
 </html>"""
    return html_str


@app.route("/hello/<name>")
def say_hello(name):
    return f"안녕하세요. {escape(name)}님."

@app.route("/dan/<dan>")
def gugudan_html(dan):
    html_str=""
    for i in range(1,10):
        html_str += f"{dan} X {i} = {int(dan)*i}<br>"
    return html_str

@app.route("/gugudan/")
def gugudan_html_dan():
    dan = request.args.get("dan")
    html_str=""
    for i in range(1,10):
        html_str += f"{dan} X {i} = <strong>{int(dan)*i}</strong><br>"
    return html_str

app.run(debug=True)
