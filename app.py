from flask import Flask, request,make_response,jsonify,redirect,url_for
from flask import render_template
from flask_bootstrap import Bootstrap
from faker import Faker
fake=Faker()
app = Flask(__name__)
bootstrap=Bootstrap(app)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
@app.route('/hello')
def hello():
    name = request.args.get('name', 'Flask') # 获取查询参数name的值
    return '<h1>Hello, %s!<h1>' % name # 插入到返回值中
@app.route('/goback/<int:year>')
def go_back(year):
    return '<p>Welcome to %d!</p>' % (2018 - year)
@app.route('/foo')
def foo():
    return jsonify(name='Grey Li', gender='male')
@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name', name)
    return response
@app.route('/watchlist')
def watchlist():
    return render_template('newhtml.html', user=user, movies=movies)
@app.route('/blog')
def blog():
    return render_template('nbase.html', name="lijinze")
@app.route('/css')
def css():
    return render_template('mycss.css')
@app.route('/login')
def login():
    return render_template('login.html')



user = {
'username': 'Grey Li',
'bio': 'A boy who loves movies and music.',
}
movies = [
{'name': 'My Neighbor Totoro', 'year': '1988'},
{'name': 'Three Colours trilogy', 'year': '1993'},
{'name': 'Forrest Gump', 'year': '1994'},
{'name': 'Perfect Blue', 'year': '1997'},
{'name': 'The Matrix', 'year': '1999'},
{'name': 'Memento', 'year': '2000'},
{'name': 'The Bucket list', 'year': '2007'},
{'name': 'Black Swan', 'year': '2010'},
{'name': 'Gone Girl', 'year': '2014'},
{'name': 'CoCo', 'year': '2017'},
]