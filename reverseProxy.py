from flask import Flask,render_template,request
import os
import json as JSON
import mysql.connector 

application = Flask(__name__)

config_path = '/etc/BDD/config.json'
f = open(config_path, 'r')
config_params = JSON.load(f)
host = config_params['host']
user = config_params['user']
mdp = config_params['mdp']
database = config_params['db']

conn = mysql.connector.connect(host=host,user=user,password=mdp, database=database)



@application.route('/index.html')
@application.route('/')
def index():
    return render_template('index.html')

@application.route('/index1.html')
def analytics():
    return render_template('index1.html')

@application.route('/ipcount')
def ipcount():
    return '12'

@application.route('/send_local_black_list')
def send_local_bl():
    cursor = conn.cursor()
    with open('/etc/csf/csf.deny', 'r')as f:
        ip = f.readlines()
        for entry in ip:
            cursor.execute('INSERT INTO ThreatList values("'+ entry + '", NOW(), 1) ON DUPLICATE KEY UPDATE `Count` = `Count` +1;')
    conn.commit()
    return 'ok'

@application.route('/get_commune_black_list')    
def get_commune_black_list():
    curs = conn.cursor()
    curs.execute('SELECT Ip from BlackList')
    row = [item[0].decode("utf-8") for item in curs.fetchall()]
    with open('/etc/csf/csf.deny', 'w+')as f:
        f.writelines(row)
    conn.commit()
    return 'BlackList synchronized'

@application.route('/update_config', methods=['GET'])
def update_whitelist():
    oui = open('./tmp/nginx.conf').readlines()
    oui_render = reduce( lambda x ,y : x + y , oui)
    return render_template('form-editor.html', placeholder = oui_render)

@application.route('/update_config', methods=['POST'])
def update_whitelist_post():
    with open('/etc/csf/csf.conf', 'w') as f:
        f.write(request.form['conf'])

    return render_template('form-editor.html', placeholder = request.form['conf'])

@application.route('/see_basic_logs')
def render_logs():

    with open('/var/log/nginx/error.log', 'r') as f:x
        lines = f.readlines()
        lines = map(lambda x : {'message' : x, 'level' : x[x.find("[")+1:x.find("]")]}, lines)
        return render_template('ui-alert.html', messages = lines)

@application.route('/see_access_logs')
def render_access_logs():
    with open('/var/log/nginx/acess.log', 'r') as f:
        lines = f.readlines()
        lines = map(lambda x : {'message' : x[x.find("-"):len(x) -1], 'ip' : x[0:x.find("-")]}, lines)
        return_dict = {}
        for elem in lines:
            if return_dict.has_key(elem['ip']):
                return_dict[elem['ip']].applicationend(elem['message'])
            else:
                return_dict[elem['ip']] = [elem['message']]

        return render_template('ui-alert.html', messages = lines)

@application.route('/csf_config')
def render_csf_config():
    return 'TODO'





@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@application.errorhandler(400)
def page_not_found(e):
    return render_template('400.html'), 400

@application.errorhandler(403)
def page_not_found(e):
    return render_template('403.html'), 403

@application.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

@application.errorhandler(503)
def page_not_found(e):
    return render_template('503.html'), 503

if __name__ == '__main__':
    application.run(host='0.0.0.0')