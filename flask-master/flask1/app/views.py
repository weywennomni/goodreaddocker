from app import app 

@app.route("/test1")
def index():
    return "I am test 1."
