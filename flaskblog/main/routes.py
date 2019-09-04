from flask import render_template, request, Blueprint
from flaskblog.models import Post, User

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    page2 = request.args.get('page2', 1, type=int)
    page3 = request.args.get('page3', 1, type=int)

    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=4)
    users = User.query.paginate(page=page2)

    return render_template('home.html', posts=posts, users=users)


@main.route("/about")
def about():
    return render_template('about.html', title='About')