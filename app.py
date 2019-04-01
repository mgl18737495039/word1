from flask import *
import datetime

from orm import mange
import datetime


app = Flask(__name__)
app.send_file_max_age_default = datetime.timedelta(seconds=1)

@app.route('/',methods=["GET","POST"])
def hello_world():
    user =request.cookies.get("id")
    if user :
        username=mange.checkUserId(user)
        username=username[0][0]

    else:
        username=None

    result = mange.checkUserAllText()

    return render_template("index.html",username=username,result=result)

@app.route('/login',methods=["GET","POST"])
def login():
    print("*******************")
    if request.method == "GET":

        return render_template("login.html")
    elif request.method=="POST":
        username=request.form['username']
        pwd =request.form['pwd']
        reluat=mange.checkUser(username,pwd)
        print(reluat)
        if reluat:
            res =make_response(redirect("/xiangmu"))
            res.set_cookie('id',str(reluat.id),expires=datetime.datetime.now() +datetime.timedelta(days=7))

            return res
        else:

            return render_template("login.html",reluat=reluat)

@app.route("/tuichu")
def tuichu():
    res=make_response(redirect('/'))
    res.delete_cookie("id")
    return  res
@app.route('/xiangmu')
def xiangmu():
    user=request.cookies.get("id")
    resault=mange.checkUserText(user)


    return render_template("xiangmu.html",resault=resault)
if __name__ == '__main__':
    app.run(debug=True)
@app.route('/xq',methods=['GET'])
def xq():
    name=request.args.get('name')
    result=mange.checkText(name)

    return render_template('xq.html',result=result[0])
@app.route("/zhuce",methods=["GET","POST"])
def zhuce():
    if request.method=='GET':
        return render_template('zhuce.html')
    elif request.method =='POST':
        username=request.form['username']
        pwd=request.form['pwd']
        email=request.form['email']
        #存入数据库
        mange.insertUser(username,pwd,email)
        return render_template('login.html')
@app.route('/addtext',methods=["GET","POST"])
def addtext():
    if request.method=='GET':
        return render_template('addtext.html')
    elif request.method == 'POST':
        text=request.form["text"]
        textname=request.form["textname"]
        user=request.cookies.get("id")
        mange.inserttext(textname,text,user)
        return redirect('/xiangmu')
@app.route('/del',methods=["GET"])
def dele():
    nametext=request.args.get('name')
    print(nametext)
    mange.dele(nametext)
    return redirect('/xiangmu')
@app.route('/xiugai',methods=["GET","POST"])
def updataText():
    nametext = request.args.get('name')

    result=mange.checkTextU(nametext)
    print(result.textname)
    print(result.text)

    return render_template("xiugai.html",name=result.textname,text=result.text,nametext=nametext)
@app.route('/xiugai2',methods=['POST'])
def updataText2():
    nametext=request.args.get('name')
    textname=request.form['textname']
    text=request.form['text']
    e=mange.updataTxet(textname,text,nametext)
    print(e)
    return redirect('/xiangmu')