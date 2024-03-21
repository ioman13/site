from flask import Flask, url_for, request, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello'


@app.route('/')
@app.route('/index')
def index():
    title = 'title'
    return render_template('i.html', title=title)


@app.route("/training/<prof>")
@app.route("/<prof>")
def p(prof):
    title = "professia"
    return render_template('h.html', title=title, t=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
