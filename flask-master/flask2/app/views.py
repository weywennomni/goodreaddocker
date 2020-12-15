from app import app 

@app.route("/test2")
def index():
    return "This is the test 2 page"
