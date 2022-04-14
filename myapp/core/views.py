from flask import render_template, request, Blueprint
from myapp.models import BlogPost
from myapp.models import Pet

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', blog_posts=blog_posts)

@core.route('/pets')
def pets():
    page = request.args.get('page', 1, type=int)
    pets = Pet.query.order_by(Pet.name.desc()).paginate(page=page, per_page=5)
    return render_template('pet_index.html', pets=pets)