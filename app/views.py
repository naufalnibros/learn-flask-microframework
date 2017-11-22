# from app import app
#
# @app.route('/')
# @app.route('/index')
# def index():
#     user = {"nickname": "NAUFALIS"}
#     return \
#         """
#         <html>
#             <head>
#                 <title>MY MICROBLOG</title>
#             </head>
#             <body>
#                 <h1> HALLO MY NAME """+ user["nickname"] +"""</h1>
#             </body>
#         </html>
#         """

# from flask import render_template
# from app import app
#
# @app.route('/')
# @app.route('/index')
# def index():
#     user = {"nickname" : "NAUFALIS"}
#     post = [
#         {
#             "author" : {"nickname": "Saslis"},
#             "body" : "HAI salam kenal~"
#         },
#         {
#             "author" : {"nickname": "Naudal"},
#             "body" : "Salam kenal juga~"
#         }
#     ]
#     return render_template("index.html", title="Gombes", user=user, post=post)

from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {"nickname" : "NAUFALIS"}
    post = [
        {
            "author" : {"nickname": "Saslis"},
            "body" : "HAI salam kenal~"
        },
        {
            "author" : {"nickname": "Naudal"},
            "body" : "Salam kenal juga~"
        }
    ]
    return render_template("index.html", title="Gombes", user=user, post=post)

# Function Example 1
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     return render_template("login.html", title="Sign In", form=form)

# function Example 2
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("login requested for openId '%s', remember me %s" %
            (form.openid.data, str (form.remember_me.data)))
        return redirect("/index")
    return render_template("login.html", title="Sign In", form=form, providers=app.config["OPENID_PROVIDERS"])
