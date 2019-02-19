import os
from PIL import Image, ImageOps
from flask import render_template, url_for, redirect
from app import app, db
from app.models import PhotoSelection

@app.route('/')
def index():
    photoSelection = PhotoSelection.query.first()
    return render_template('index.html', photo=photoSelection)

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/photo/<int:id>')
def select(id):
    p = PhotoSelection.query.first()
    p.photo = str(id) + '.jpg'
    db.session.commit()
    return redirect(url_for('admin'))