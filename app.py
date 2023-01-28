from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# MySQL connection
app = Flask(__name__)
app.config['MYSQL_HOST'] = ' mysql-flask-app-container'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)

# Settings
app.secret_key = 'mysecretkey'


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    return render_template('index.html', contacts=data)


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        print(f'fullname: {fullname}; phone: {phone}; email: {email}\n')
        cur = mysql.connection.cursor()
        cur.execute(f'INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)',
                    (fullname, phone, email))
        mysql.connection.commit()
        flash('Contact added successfully')
        return redirect(url_for('index'))


@app.route('/edit/<id>')
def edit(id):
    cur = mysql.connection.cursor()
    cur.execute(f'SELECT * FROM contacts WHERE id = {id}')
    data = cur.fetchall()
    return render_template('edit.html', contact=data[0])


@app.route('/update/<id>', methods=['POST'])
def update(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email: str = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE contacts \n"
                    "        SET fullname = %s, \n"
                    "            phone = %s, \n"
                    "            email = %s \n"
                    "            WHERE id = %s",
                    (fullname, phone, email, id))
        mysql.connection.commit()
        flash('Contact update successfully')
        return redirect(url_for('index'))


@app.route('/delete/<string:id>')
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute(f'DELETE FROM contacts WHERE id = {id}')
    mysql.connection.commit()
    flash('Contact deleted successfully')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
