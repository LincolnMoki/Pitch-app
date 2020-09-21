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


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    pitches_count = Pitch.count_pitches(uname)
    user_joined = user.date_joined.strftime('%b %d, %Y')

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,pitches = pitches_count,date = user_joined)

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
