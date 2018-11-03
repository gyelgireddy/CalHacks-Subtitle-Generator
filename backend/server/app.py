from flask import Flask , request, render_template

app = Flask(__name__)




@app.route('/')
@app.route('/<user>')
def index(user=None):
    return render_template("user.html", user=user)
    #return 'Method used: %s' % request.method


@app.route('/lmao', methods = ['GET','POST'])
def nerd():
    if request.method == 'Post':
        return "You are using POST"
    return 'You are using GET'


@app.route('/profile/<username>')
def profile(username):
    return render_template("profile.html", name=username)



@app.route('/post/<int:id>')
def post(id):
    return "Post Id: %s" % id


if __name__  == "__main__":
    app.run(debug=True)