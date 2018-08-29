from yourapplication import app

@app.route('/')
def index():
    return 'Hello World!'


@app.route("/blog")
def blog():
    return "This is the blog page"
