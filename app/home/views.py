from . import home

@home.route("/home")
def index():
    return "Home page"