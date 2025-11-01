# app.py
# from flask import Flask, request, flash, redirect, url_for, render_template
# from flask_migrate import Migrate
# from models import db, AdminUser
# from config import Config
# from werkzeug.security import generate_password_hash

# from routes.cars import cars_bp
# from routes.users import users_bp

# app = Flask(__name__)
# app.config.from_object(Config)
# app.secret_key = 'your_secret_key_here'  # Add this for flash messages

# db.init_app(app)
# Migrate(app, db)

# Register blueprints
# app.register_blueprint(cars_bp)
# app.register_blueprint(users_bp)

# @app.route('/')
# def home():
#     return render_template('base.html')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         email = request.form['email']
#         username = request.form['username']
#         password = request.form['password']
        
#         # Hash password
#         hashed = generate_password_hash(password)
        
#         try:
#             new_admin = AdminUser(
#                 email=email,
#                 username=username,
#                 password_hash=hashed
#             )
#             db.session.add(new_admin)
#             db.session.commit()
#             flash('Admin registered successfully!', 'success')
#             return redirect(url_for('login'))
#         except Exception as e:
#             db.session.rollback()
#             flash('Username or email already exists', 'error')
    
#     return render_template('register.html')

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/dashboard')
def dashboard():
    return render_template('users/dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)