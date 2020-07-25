from flask import Flask,session,redirect,url_for,flash
from  flask import  render_template
from  flask import request
from wl  import crawl
import f1
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm                        #引入FlaskForm类，作为自定义Form类的基类
from wtforms import StringField,SubmitField,SelectMultipleField,SelectField         #StringField对应HTML中type="text"的<input>元素，SubmitField对应type='submit'的<input>元素
from wtforms.validators import Required    
class NameForm(FlaskForm):
    name = StringField('What is your name?',validators=[Required()])
    language = SelectMultipleField(u'性别',choices=[('先生','male'),('女士','female')])
    degree= SelectField(u'学历',choices=[('大专','大专'),('本科','本科')])
    submit = SubmitField('Submit')

a=crawl()
app = Flask(__name__)
bootstrap=Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'    
@app.route('/')
def index():
    return  render_template(
    'main.html',
    the_title="my world",
    the_word=a.chase())
@app.route('/f1',methods=['GET','POST'])
def function1():
    return  render_template(
    'function1.html',
    the_title="FUNCTION 1",
    ans="?")
@app.route('/result',methods=['GET','POST'])
def function11():
    n=request.form['a']
    nn=request.form['b']
    ans=int(n)+int(nn)
    return  render_template(
    'function1.html',
    the_title="FUNCTION 1",
    ans=ans)
@app.route('/<name>')
def test(name):
    return name
@app.route("/f2",methods=['GET','POST'])
def f2():
    name = None
    form = NameForm()
    oldname=session.get('name')
    language=session.get('language')
    flash("last man is %s"%oldname)
    if form.validate_on_submit():                            #返回True
        session['name'] = form.name.data 
        session['language'] = form.language.data
        session['degree'] = form.degree.data                             #执行 
        return redirect(url_for('f2'))                                    #执行
    return render_template('f2.html',name=session.get('name'),language=session.get('language')[0],degree=session.get('degree'),form=form)
if __name__ == '__main__':
    app.debug = True # 设置调试模式，生产模式的时候要关掉debug
    app.run()