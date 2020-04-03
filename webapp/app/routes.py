from flask import render_template, url_for, flash, redirect, request
from flask import current_app as app
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bcrypt
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm
from app.models import User, Matches


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/project')
def project():
    return render_template('project.html', title='Project')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data.lower(), email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', 
                            form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f'Welcome back, {user.username}!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful. Please double check your credentials.', 'danger')
    return render_template('login.html', title='Login', 
                            form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account', methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        currentuser = User.query.filter_by(username = current_user.username).first() 
        if bcrypt.check_password_hash(currentuser.password, form.last_password.data): 
            current_user.email = form.email.data
            if form.new_password.data:
                current_user.password = bcrypt.generate_password_hash(form.new_password.data).decode('utf-8')
            db.session.commit()
            flash('Your account info has been updated!', 'success')
        else:
            flash('Double check your actual password, please.', 'danger')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.email.data = current_user.email
        form.new_password.data = current_user.password
    profile_image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    team_image_file = url_for('static', filename='team_logos/' + current_user.team_image_file)
    return render_template('account.html', title='My account',
                             profile_image_file=profile_image_file, team_image_file=team_image_file, form=form)

