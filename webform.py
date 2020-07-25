from flask_wtf import FlaskForm                        #引入FlaskForm类，作为自定义Form类的基类
from wtforms import StringField,SubmitField           #StringField对应HTML中type="text"的<input>元素，SubmitField对应type='submit'的<input>元素
from wtforms.validators import Required                #引入验证函数
 
class NameForm(FlaskForm):
    name = StringField('What is your name?',validators=[Required()])
    submit = SubmitField('Submit')