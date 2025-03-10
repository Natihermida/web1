from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    return 'Username: ' + username + ' Password: ' + password
    #una vez el loggin es correcto redireciono a admin.html
    if(username == 'admin' and password == 'admin'):
        return redirect(url_for('admin'))

@app.route('/admin', methods=['GET'])
def admin():
    return render_template('admin/admin.html')

if __name__ == '__main__':
    app.run(debug=True, port=80)
    