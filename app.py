from flask import Flask, request, render_template  

app = Flask(__name__)


@app.route('/') # decorator
def index():
    return render_template("home.html")

'''
@app.route("/profile/<name>") # decorator
def profile(name):
    return render_template("profile.html", name=name)

@app.route('/becon', methods=['Get','Post']) 
def becon():
    if request.method=='POST':
        return 'Method Used: %s' % request.method
    else:
        return "Your are using Get"


@app.route('/') # decorator
def index():
    return 'This is the home page'


@app.route('/tuna')
def tina():
    return '<h2>I love tuna fish</h2>'

@app.route ('/profile/<username>')
def profile(username):
    return "<h2>Hey there   %s </h2>" %username


@app.route ('/post/<int:post_id>')
def post(post_id):
    return "<h2>Post ID is   %d </h2>" %post_id

'''


if __name__=="__main__":
    app.run(debug=True)