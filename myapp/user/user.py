from myapp.user import user_bp
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

@user_bp.route('/userr',methods=["POST","GET"])
def user_reg():
    if request.method == "POST":
        name=request.form.get("name")
        email=request.form.get("email")
        phone=request.form.get("phone")
        user = db.User()
        user.name = name
        user.email = email
        user.phone = phone
        user.save()
    return render_template("userregister.html")

@user_bp.route('/viewu',methods=["POST","GET"])
def user_view():
    res = db.User.objects()
    return render_template("viewuser.html", res=res)