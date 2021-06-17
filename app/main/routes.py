from re import I
import requests
from flask import render_template, request, redirect
from flask import current_app, url_for
from flask_login import login_user, login_required, logout_user
from google.oauth2 import id_token
from google.auth.transport import requests
from ..models import User, TotalCounts
from . import bp
from .forms import CounterForm
from . import utils


@bp.route("/", methods=['GET', 'POST'])
def index():
    tot_count = TotalCounts.query.get(1)
    if request.method == 'POST':
        form = CounterForm()
        if request.args.get('locale') == 'hi':
            if form.validate_on_submit():
                utils.add_data_to_db(form.data)
                return redirect(url_for("main.index", locale='hi'))
            return render_template("index_hi.html", form=form, counts=tot_count)
        else:
            if form.validate_on_submit():
                utils.add_data_to_db(form.data) 
                # return render_template("index.html", form=form, counts=tot_count)
                return redirect(url_for("main.index"))
            return render_template("index.html", form=form, counts=tot_count)
    elif request.method == 'GET':
        form = CounterForm()
        if request.args.get('locale') == 'hi':
            return render_template("index_hi.html", form = form, counts=tot_count)
        else:
            return render_template("index.html", form=form, counts=tot_count)




@bp.route("/login", methods=["GET", "POST"])
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

    token = request.form.get('credential')
    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), current_app.config["GOOGLE_CLIENT_ID"])

        # ID token is valid. Get the user's Google Account ID from the decoded token.
        userid = idinfo['sub']
    except ValueError as e:
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



@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@bp.route("/faq")
def faq():
    return render_template("faq.html")
