from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

# Конфигурација за база на податоци (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registrations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

# Модел за регистрација
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    ime_tura = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Registration {self.first_name} {self.last_name}>'

# Креирање на базата и табелите ако не постојат
with app.app_context():
    db.create_all()

# Почетна страница
@app.route('/')
def index():
    return render_template('index.html')

# Рута за процесирање на формата за пријава
@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone = request.form['phone']
    ime_tura = request.form['ime_tura']
    
    try:
        # Зачувување во базата на податоци
        new_registration = Registration(first_name=first_name, last_name=last_name, email=email, phone=phone, ime_tura=ime_tura)
        db.session.add(new_registration)
        db.session.commit()
        print("Регистрацијата е успешно зачувана во базата.")
        return f"Фала, {first_name} {last_name}, за вашата регистрација! Ќе ве контактираме на {email}."
    except Exception as e:
        db.session.rollback()
        print(f"Грешка при зачувување на регистрацијата: {e}")
        return f"Грешка при зачувување на регистрацијата: {e}"

# Рута за прикажување на сите пријавени учесници
@app.route('/registrations')
def show_registrations():
    registrations = Registration.query.all()
    return render_template('registrations.html', registrations=registrations)

# Рута за логирање
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']
        if password == 'jocotoursstruga2000':
            session['admin'] = True
            return redirect(url_for('admin_panel'))
        else:
            return 'Невалидна лозинка!'
    return render_template('login.html')

# Заштитена рута за административниот панел
@app.route('/admin')
def admin_panel():
    if not session.get('admin'):  
        return redirect(url_for('login'))  
    registrations = Registration.query.all()
    return render_template('admin_panel.html', registrations=registrations)

# Рута за бришење на запис
@app.route('/delete/<int:id>')
def delete_registration(id):
    registration = Registration.query.get(id)
    if registration:
        db.session.delete(registration)
        db.session.commit()
    return redirect(url_for('admin_panel'))

# Рута за одјава
@app.route('/logout')
def logout():
    session.pop('admin', None)  
    return redirect(url_for('login'))

# Рута за страната соопштение
@app.route('/soop')
def soop():
    return render_template('soop.html')

# Рута за страната галерија
@app.route('/gallery')
def gallery():
    return render_template('galerija.html')

if __name__ == '__main__':
    app.run(host='192.168.1.6', port=5000, debug=True)


