from sqlalchemy.orm import sessionmaker
from utils.data import engine, Contact

# Crear una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

@session.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    return render_template('index.html', contacts=data)


@session.route('/add', methods=['POST'])
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


@session.route('/edit/<id>')
def edit(id):
    cur = mysql.connection.cursor()
    cur.execute(f'SELECT * FROM contacts WHERE id = {id}')
    data = cur.fetchall()
    return render_template('edit.html', contact=data[0])


@session.route('/update/<id>', methods=['POST'])
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


@session.route('/delete/<string:id>')
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute(f'DELETE FROM contacts WHERE id = {id}')
    mysql.connection.commit()
    flash('Contact deleted successfully')
    return redirect(url_for('index'))
