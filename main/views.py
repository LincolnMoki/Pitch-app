from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from . import main
from .forms import PostForm, CommentForm, UpdateProfile
from ..models import Post, Comment, User, Upvote, Downvote
from .. import db 



@main.route('/')
def index():
    posts = Post.query.all()
    product = Post.query.filter_by(category='product').all()
    idea = Post.query.filter_by(category='idea').all()
    business = Post.query.filter_by(category='Business').all()
    return render_template('index.html', business=business, product=product, idea=idea, posts=posts)

