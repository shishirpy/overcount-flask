import json
import pprint
from re import I
import requests
from flask import render_template, request, redirect
from flask import current_app, url_for
from flask_login import login_user, current_user
from google.oauth2 import id_token
from google.auth.transport import requests
from .. import db
from ..models import Count, User
from . import bp
from .forms import CounterForm
from . import utils


@bp.route("/", methods=['GET', 'POST'])
def index():
    if current_user.is_anonymous:
        print("CURRENT USER NONE")
    else:
        print("CURRENT USER", current_user.email)
    if request.method == 'POST':
        form = CounterForm()
        print(form.data)
        if request.args.get('locale') == 'hi':
            if form.validate_on_submit():
                # count = Count(author_id
                utils.add_data_to_db(form.data)
            return render_template("index_hi.html", form = form)
        else:
            if form.validate_on_submit():
                utils.add_data_to_db(form.data) 
                return render_template("index.html", form=form)
            return render_template("index.html", form=form)
    elif request.method == 'GET':
        print("POSTR BODY")
        print(request.data)
        form = CounterForm()
        return render_template("index.html", form=form)


@bp.route("/login")
def login():
    # Find out what URL to hit for Google login
    google_provider_cfg = utils.get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = current_app.oauth_client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email"],
    )
    
    print(request_uri)
    return redirect(request_uri)


@bp.route("/login/callback", methods=["POST"])
def callback():
    csrf_token_cookie = request.cookies.get('g_csrf_token')
    if not csrf_token_cookie:
        print("COOKIEE MISSING")
    csrf_token_body = request.form.get('g_csrf_token')
    if not csrf_token_body:
        print("BODY TOKEN MISSING")

    print("TOKENS", csrf_token_cookie, csrf_token_body)
    print("==" * 20)
    

    token = request.form.get('credential')
    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), current_app.config["GOOGLE_CLIENT_ID"])

        # ID token is valid. Get the user's Google Account ID from the decoded token.
        userid = idinfo['sub']
    except ValueError:
        # Invalid token
        pass

    #try:
    usr = User.query.get(userid)
    if not usr:
        new_user = User(id=userid, email=idinfo['email'])
        utils.add_user_to_db(new_user)
        print("ADDED NEW USER,", new_user)
        login_user(new_user)
    else:
        login_user(usr)
    return redirect(url_for('main.index'))
    
