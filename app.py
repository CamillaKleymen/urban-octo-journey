from flask import Flask
app = Flask(__name__)
from users import user_bp
app = Flask(__name__)
app.config["CSRF_ENABLED"] = True
app.config["SECRET_KEY"] = "DFgES_541454@k&DfsKdf4442"
app.register_blueprint(user_bp)

@app.route("/")
def home():
    user_link = "<a href='/user/'>Users</a><br>"
    return user_link

app.run(debug=True)