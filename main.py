from flask import Flask,render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail,Message
from datetime import datetime
import json
import os
from werkzeug.utils import secure_filename
import math

app = Flask(__name__)

with open("configure.json","r") as c:
    params = json.load(c)["params"]

app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = params["gmail_user"],
	MAIL_PASSWORD = params["gmail_password"]
	)
mail = Mail(app)

app.config['SECRET_KEY'] = 'some secret string here'

app.config['UPLOAD_FOLDER']= params["upload_loacation"]

local_server = True
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)

class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25) , nullable= False)
    email = db.Column(db.String(25) , nullable= False)
    msg = db.Column(db.String(200) , nullable= False)
    date = db.Column(db.String(12) , nullable= False)

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25) , nullable= False)
    content = db.Column(db.String(400) , nullable= False)
    author = db.Column(db.String(25) , nullable= False)
    date = db.Column(db.String(12) , nullable= False)
    image = db.Column(db.String(20) , nullable= True)
    slug = db.Column(db.String(20) , nullable= False)




@app.route('/',methods=['GET'])
def home():
    
    posts = Posts.query.filter_by().all()
    last = math.ceil(len(posts)/int(params["no_of_posts"]))

    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page=1
    page = int(page)
    posts = posts[(page-1)*int(params["no_of_posts"]) : (page-1)*int(params["no_of_posts"])+int(params["no_of_posts"])]

    # pagination logic
    if(page==1):
        prev = "#"
        next = "/?page=" + str(page+1)
    elif(page==last):
        prev = "/?page=" + str(page-1)
        next =  "#"
    else:
        prev = "/?page=" + str(page-1)
        next = "/?page=" + str(page+1)

    return render_template("home.html", param=params, posts=posts, prev=prev, next=next)


@app.route("/post/<string:slug>",methods=['GET'])
def post_page(slug):
    post = Posts.query.filter_by(slug=slug).first()
    if post:
        return render_template("post.html", param=params,post=post)


@app.route("/about")
def about():
    return render_template("about.html", param=params)


@app.route("/contact",methods = ['POST', 'GET'])
def contacts():
    if (request.method == "POST"):
        name = request.form.get("name")
        email = request.form.get("email")
        msg = request.form.get("msg")
        entry = Contact(name=name, email=email, msg=msg, date=datetime.now())
        db.session.add(entry)
        db.session.commit()

        mail.send_message("New message from "+name,
		sender=email,
		recipients=[params["gmail_user"]],
        body = msg + name )
    return render_template("contact.html", param=params)


@app.route("/dashboard",methods=['GET','POST'])
def dashboard():
    if('user' in session and session['user']==params["admin_user"]):
        post = Posts.query.filter_by().all()
        return render_template("dashboard.html", param=params, posts= post)
    if request.method=='POST':
        # redirect to admin panel
        uname = request.form.get("username")
        passw = request.form.get("userpass")
        if (uname == params["admin_user"]) and (passw == params["admin_password"]):
            # set session variable
            session["user"] = uname
            post = Posts.query.filter_by().all()
            return render_template("dashboard.html",param=params, posts = post)
        else:
            return  uname + passw
    return render_template("login.html", param=params)


@app.route("/edit/<string:sno>",methods=['GET','POST'])
def edit(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            ftitle = request.form.get("title")
            fcontent = request.form.get("content")
            fauthor = request.form.get("author")
            fimg_src = request.form.get("img_src")
            fslug = request.form.get("slug")
            fdate = datetime.now()

            if sno=='0':
                post = Posts(title=ftitle, content=fcontent, author=fauthor, image=fimg_src, slug=fslug, date=fdate)
                db.session.add(post)
                db.session.commit()
            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title = ftitle
                post.content = fcontent
                post.author = fauthor
                post.image = fimg_src
                post.slug = fslug
                post.date = fdate
                db.session.commit()
                return redirect('/edit/'+sno)
        post = Posts.query.filter_by(sno=sno).first()
        return render_template('edit.html', param=params, post=post, sno=sno)
    return render_template("login.html", param=params)


@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')


@app.route("/delete/<string:sno>",methods=['GET','POST'])
def delete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')


@app.route("/uploader",methods=['POST'])
def uploader():
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method=='POST':
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return 'Uploaded successfully'

app.run(debug=True)