from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from grocery_app.models import GroceryStore, GroceryItem

# from grocery_app.auth.forms import SignUpForm, LoginForm

from grocery_app.extensions import app, db, bcrypt

auth = Blueprint("auth", __name__)
