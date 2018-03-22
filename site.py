from flask import Flask,render_template,request
import os

root_dir = os.path.dirname(os.getcwd())

app = Flask(__name__,static_url_path=root_dir)


@app.route('/index.html')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index1.html')
def analytics():
    return render_template('index1.html')

if __name__ == '__main__':
    app.run()