from flask import render_template, flash, url_for, redirect, session, request, g
from app import app
from models import Post, User
from decorators import login_required
from forms import PostForm, EditForm

from google.appengine.api import users
from google.appengine.ext import db


@app.before_request
def before_request():
    g.user = users.get_current_user()

@app.route('/' , methods = ['GET', 'POST'])
def redirect_to_home():
    return redirect(url_for('list_posts'))

@app.route('/posts' , methods = ['GET', 'POST'])
def list_posts():
    posts = Post.all().order('-when')
    return render_template('list_posts.html', posts=posts, users=users)

@app.route('/posts/new', methods = ['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title = form.title.data,
                    content = form.content.data,
                    image = form.image.data,
                    author = users.get_current_user())
        post.put()
        flash('Post saved on database.')
        return redirect(url_for('list_posts'))
    return render_template('new_post.html', form=form, users=users)

@app.route('/user/', methods = ['GET', 'POST'])
def user():
    user = 'test2@example.com'
    if user == None:
        flash('User ' + nickname + ' not found.')
        return redirect(url_for('index'))
    posts = Post.gql('WHERE author = :1', user)
    return render_template('user.html', user = user, posts = posts, users = users)

@app.route('/edit', methods = ['GET', 'POST'])
@login_required
def edit_user():
    form = EditForm()
    if form.validate_on_submit():
        user = User(id = users.get_current_user().user_id(),
                    nickname = form.nickname.data,
                    email = form.email.data,
                    role = "USER",
                    about_me = form.about_me.data)
        user.put()
        flash('Saved')
        return redirect(url_for('edit_user'))
    else:
        form.nickname.data = g.user.nickname()
        form.email.data = g.user.email()
        form.about_me = g.user.about_me()
    return render_template('edit_user.html', form=form, users=users)

