from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def home():
    return render_template('index.html')

@public.route('/login',methods=['post','get'])
def login():
    if 'submit' in request.form:
        uname=request.form['username']
        pasw =request.form['password']
        q="select * from login where username='%s' and password='%s'"%(uname,pasw)
        res=select(q)
        if res:
            session['login_id']=res[0]["login_id"]
            if res[0]['usertype'] == "admin":               
                return redirect(url_for("admin.adminhome"))
            if res[0]['usertype'] == "govtstaff":               
                return redirect(url_for("gov.govhome"))
            if res[0]['usertype'] == "shop":
                r="select * from shop where login_id='%s'"%(session['login_id']) 
                res1=select(r)
                if res1:
                    session['shop_id']=res1[0]['shop_id']          
                return redirect(url_for("shop.shophome"))
            if res[0]['usertype'] == "user":
                r="select * from users where login_id='%s'"%(session['login_id']) 
                res1=select(r)
                if res1:
                    session['uid']=res1[0]['user_id']          
                return redirect(url_for("api.userhome"))
    return render_template("login.html")

@public.route('/shop_keeper_reg',methods=['get','post'])
def shop_keeper_reg():
    if 'submit' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        shop=request.form['shop']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        uname=request.form['uname']
        pwd=request.form['pwd']
        u="insert into login values(null,'%s','%s','shop')"%(uname,pwd)
        log=insert(u)

        r="insert into shop values(null,'%s','%s','%s','%s','%s','%s','%s')"%(log,fname,lname,shop,place,phone,email)
        insert(r)
    return render_template("shop_reg.html")


@public.route('/sign_up',methods=['post','GET'])
def sign_up():
    data={}
    if 'submit' in request.form:
        ee1=request.form['ee1']
        ee2=request.form['ee2']
        ee3=request.form['ee3']
        ee4=request.form['ee4']
        ee5=request.form['ee5']
        ee6=request.form['ee6']
        ee7=request.form['ee7']
        ee8=request.form['ee8']
        ee9=request.form['ee9']
        ee10=request.form['ee10']
        ee11=request.form['ee11']
        ee12=request.form['ee12']
        jk="insert into login values(null,'%s','%s','user')"%(ee11,ee12)
        gh=insert(jk)
        op="insert into users values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(gh,ee1,ee2,ee3,ee4,ee5,ee6,ee7,ee8,ee9,ee10)
        res=insert(op)
        return redirect(url_for('public.login'))
    return render_template('sign_up.html',data=data)
