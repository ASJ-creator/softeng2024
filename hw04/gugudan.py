from flask import Flask, request
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def home():
    html_str = '''
<!DOCTYPE html>
<html lang="kr">
<head>
    <meta charset="UTF-8">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js">
    </script>
</head>
<body>
    <form id="form_id" action="javascript:post_query()">   
            <input type="text" name="dan" value=7>
        <button type="submit">Go</button>
    </form>
<div id = "results"></div>
    <script>
    function post_query() {
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/gugudan/",
            data: $("#form_id").serialize(),
            success: update_result,
            dataType: "html"
        });
    }
    function update_result(data) {
        $("#results").html(data);
    }
    </script>
</body>
</html>'''
    return html_str

@app.route('/<name>')
#def hello(name):
    return f'Hello, {escape(name)}!'

@app.route("/dan/<dan>")
def gugudan_html(dan):
    html_str=""
    for i in range(1,10):
        html_str += f"{dan} X {i} = {int(dan)*i}<br>"
    return html_str


@app.route('/gugudan/')
def gugudan():
    dan = request.args.get("dan","2")
    html_str = ""
    for i in range(1, 10):
        html_str += f"{dan} X {i} = <strong>{int(dan) * i}</strong><br>"
    return html_str




app.run(debug=True)
