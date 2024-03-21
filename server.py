from flask import Flask, url_for, request, render_template
from data import db_session
from data.users import User, Jobs


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello'


@app.route("/")
def index():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    users = session.query(User).all()
    names = {name.id: (name.surname, name.name) for name in users}
    return render_template("index.html", jobs=jobs, names=names)


def main():
    db_session.global_init("db/mars_explorer.db")
    app.run()


if __name__ == '__main__':
    main()
