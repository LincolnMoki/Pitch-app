from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Pitch,Comment
from .. import db,photos
from .forms import UpdateProfile,PitchForm,CommentForm
from flask_login import login_required,current_user
import datetime

# Views
@main.route('/')
def index():

    business = Pitch.get_pitches('business')
    product = Pitch.get_pitches('product')
    sport = Pitch.get_pitches('sport')


    return render_template('index.html', business = business, product = product, sport = sport)


@main.route('/posts')
@login_required
def posts():
    posts = Post.query.all()
    likes = Upvote.query.all()
    user = current_user
    return render_template('pitch_display.html', posts=posts, likes=likes, user=user)



@main.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user._get_current_object().id
        post_obj = Post(post=post, title=title, category=category, user_id=user_id)
        post_obj.save()
        return redirect(url_for('main.index'))
    return render_template('pitch.html', form=form)
