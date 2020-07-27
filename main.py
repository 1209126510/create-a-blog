from flask import Flask
from flask_bootstrap import Bootstrap
from  flask import  render_template
app = Flask(__name__)
bootstrap=Bootstrap(app)
@app.route('/')
def index():
      return  render_template('base.html')
if __name__ == '__main__':
    app.debug = True # 设置调试模式，生产模式的时候要关掉debug
    app.run()

