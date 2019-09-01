from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Comments
from flaskblog.models import Post
from flaskblog.comments.forms import CommentsForm


comments = Blueprint('comments', __name__)


@comments.route("/new_comment", methods=['GET', 'POST'])
@login_required
def new_comment():
    form = CommentsForm()
    if form.validate_on_submit():
        post = Post.query.get(1)
        comment = Comments(title=form.title.data, author= current_user, post=post)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('new_comment.html', title='New comment',
                           form=form, legend='New Comment')

