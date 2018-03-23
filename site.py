from flask import Flask,render_template,request
import os
import json as JSON
import pandas as pd

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

@app.route('/update_whitelist', methods=['GET'])
def update_whitelist():
    oui = open('./tmp/nginx.conf').readlines()
    oui_render = reduce( lambda x ,y : x + y , oui)
    return render_template('form-editor.html', placeholder = oui_render)

@app.route('/update_whitelist', methods=['POST'])
def update_whitelist_post():
    with open('./tmp/nginx.conf', 'w') as f:
        f.write(request.form['conf'])

    return render_template('form-editor.html', placeholder = request.form['conf'])

@app.route('/see_basic_logs')
def render_logs():
    with open('./tmp/nginx.log', 'r') as f:
        lines = f.readlines()
        lines = map(lambda x : {'message' : x, 'level' : x[x.find("[")+1:x.find("]")]}, lines)
        return render_template('ui-alert.html', messages = lines)

@app.route('/see_access_logs')
def render_access_logs():
    with open('./tmp/nginx.access.log', 'r') as f:
        lines = f.readlines()
        lines = map(lambda x : {'message' : x[x.find("-"):len(x) -1], 'ip' : x[0:x.find("-")]}, lines)
        return_dict = {}
        for elem in lines:
            if return_dict.has_key(elem['ip']):
                return_dict[elem['ip']] = return_dict[elem['ip']] + elem.message
            else:
                return_dict[elem['ip']] = elem.message

        return render_template('ui-alert.html', messages = lines)



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