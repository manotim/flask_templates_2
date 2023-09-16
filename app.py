from flask import Flask, render_template, request, redirect
from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY']='mikemanotinyambega'

@app.route('/')
def home():
    return 'Hello World'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/blog')
def blog():
    posts = [
        {'title':'Semen Retention Miracle', 'author':'Paul Mason'},
        {'title': 'Radical Protection', 'author':'Dr. Morris'}
    ]
    return render_template('blog.html', author='Mike', sunny=False, posts=posts)

@app.route('/blog_post/<blog_id>')
def blog_post(blog_id):
    return f"You are viewing Blog Post {blog_id}"

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result=result)
    return render_template('signup.html', form=form)

if __name__ == '__main__':
    app.run()