from flask import Flask,render_template,request
import os
import json as JSON

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
        f.write("\n".join(bl_list, "\n"))
    return 'oui'

@app.route('/get_commune_black_list')    
def get_commune_black_list():
    with open('./tmp/commune_bl.json', 'r') as json_data:
        commun_bl = JSON.load(json_data)
    return "\n".join(commun_bl['blIP'])

@app.route('/update_whitelist')
def update_whitelist():
    oui = open('./tmp/nginx.conf').readlines()
    oui_render = reduce( lambda x ,y : x + y , oui)
    return render_template('form-editor.html', placeholder = oui_render)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(400)
def page_not_found(e):
    return render_template('400.html'), 400

@app.errorhandler(403)
def page_not_found(e):
    return render_template('403.html'), 403

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

@app.errorhandler(503)
def page_not_found(e):
    return render_template('503.html'), 503

if __name__ == '__main__':
    app.run()