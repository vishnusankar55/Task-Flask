from myapp.admin import admin_bp
import email
from django.forms import EmailField
from flask import Flask, render_template,url_for, redirect, jsonify, request, session
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired
from flask import current_app as app
from flask import render_template,request
from wtforms import StringField
from myapp import db

@admin_bp.route('/ad',methods=["POST","GET"])
def admin_reg():
    if request.method == "POST":
        name=request.form.get("name")
        email=request.form.get("email")
        phone=request.form.get("phone")
        admin = db.Admin()
        admin.name = name
        admin.email = email
        admin.phone = phone
        admin.save()
    return render_template("registeradmin.html")

@admin_bp.route('/viewad',methods=["POST","GET"])
def admin_view():
    res = db.Admin.objects()
    return render_template("viewadmin.html", res=res)