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

@app.route('/ipcount')
def ipcount():
    return '12'

@app.route('/send_local_black_list')
def send_local_bl():
    bl_list = ["192.168.1.1", "192.168.1.2","192.168.1.3"]
    with open('./tmp/bl.txt', 'w+')as f:
        f.write("\n".join(bl_list))
    return 'oui'
    


if __name__ == '__main__':
    app.run()