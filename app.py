from flask import flash,Flask,render_template,redirect,url_for,jsonify,request,session,abort
import mysql.connector
from datetime import datetime,timedelta
from datetime import date
from flask_session import Session
from otp import genotp
from sdmail import sendmail
from tokenreset import token
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

app=Flask(__name__)
app.secret_key='A@Bullela@_3'
app.config["SESSION_TYPE"]="filesystem"
db=os.environ['RDS_DB_NAME']
user=os.environ['RDS_USERNAME']
password=os.environ['RDS_PASSWORD']
host=os.environ['RDS_HOSTNAME']
port=os.environ['RDS_PORT']

mydb=mysql.connector.connect(host=host,user=user,password=password,db=db,port=port)
with mysql.connector.connect(host=host,user=user,password=password,db=db,port=port) as conn:
    cursor=conn.cursor()
    cursor.execute("create table if not exists users(id varchar(50) NOT NULL,name varchar(150) DEFAULT NULL, email varchar(200) DEFAULT NULL,mobile_no varchar(10) DEFAULT NULL, password varchar(20)DEFAULT NULL,target bigint DEFAULT 0,consumed bigint DEFAULT 0,workouttarget bigint DEFAULT 0,workoutconsumed bigint DEFAULT 0,PRIMARY KEY (id))")
    cursor.execute("create table if not exists items(item varchar(30) NOT NULL,category varchar(50) DEFAULT NULL,carbohydrates float DEFAULT NULL, fats float DEFAULT NULL,protein float DEFAULT NULL,fiber float DEFAULT NULL,calorie float DEFAULT NULL,PRIMARY KEY (item))")
    cursor.execute("CREATE TABLE salary (salary decimal(5,2)DEFAULT NULL)")
    cursor.execute("CREATE TABLE workout(workout varchar(150) DEFAULT NULL,time int DEFAULT NULL,callories int DEFAULT NULL)")
    cursor.execute("CREATE TABLE callorie_track (item varchar(100) DEFAULT NULL,category varchar(80) DEFAULT NULL,quantity bigint DEFAULT NULL,id varchar(50) DEFAULT NULL,carbohydrates decimal(7,2) DEFAULT NULL,fats decimal(7,2) DEFAULT NULL,protein decimal(7,2) DEFAULT NULL,fiber decimal(7,2) DEFAULT NULL,callories bigint DEFAULT NULL,date date DEFAULT NULL,KEY id (id),CONSTRAINT callorie_track_ibfk_1 FOREIGN KEY (id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE)")
    cursor.execute("CREATE TABLE workout_track (workout varchar(50) DEFAULT NULL,time int DEFAULT NULL,id varchar(50) DEFAULT NULL,callories bigint DEFAULT NULL,date date DEFAULT NULL,KEY id (id),CONSTRAINT workout_track_ibfk_1 FOREIGN KEY (id) REFERENCES users (id) ON DELETE CASCADE ON UPDATE CASCADE)")
    

Session(app)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/homepage/<id1>',methods=['GET','POST'])
def homepage(id1):
    if session.get('user'):
        cursor=mydb.cursor(buffered=True)
        cursor.execute('select target from users where id=%s',[id1])
        target=cursor.fetchone()[0]
        cursor.execute('select consumed from users where id=%s',[id1])
        consumed=cursor.fetchone()[0]
        cursor.execute('select workouttarget from users where id=%s',[id1])
        worktarget=cursor.fetchone()[0]
        cursor.execute('select workoutconsumed from users where id=%s',[id1])
        workconsumed=cursor.fetchone()[0]
        current_date=date.today()
        current_date=f"{current_date.year}-{current_date.month}-{current_date.day}"
        today_date=datetime.strptime(current_date,'%Y-%m-%d')
        date_today=datetime.strftime(today_date,'%Y-%m-%d')
        seven_back=date.today()-timedelta(days=7)
        seven_days_back=datetime.strftime(seven_back,'%Y-%m-%d')
        cursor.execute('select item,category,sum(quantity),sum(carbohydrates),sum(fats),sum(protein),sum(fiber),sum(callories) from callorie_track where id=%s and date=%s group by item order by category asc',[id1,date_today])
        day_report=cursor.fetchall()
        cursor.execute('select item,category,sum(quantity),sum(carbohydrates),sum(fats),sum(protein),sum(fiber),sum(callories) from callorie_track where id=%s and date>=%s group by item order by category asc',[id1,seven_days_back])
        sevendays_report=cursor.fetchall()
        cursor.execute('select workout,sum(time),sum(callories) from workout_track where id=%s and date=%s group by workout',[session.get('user'),date_today])
        day_report_w=cursor.fetchall()
        cursor.execute('select workout,sum(time),sum(callories) from workout_track where id=%s and date>=%s group by workout',[session.get('user'),seven_days_back])
        sevendays_report_w=cursor.fetchall()
        cursor.close()
        if request.method=='POST':
            if 'target' in [i for i in request.form]:
                target=request.form['target']
                cursor=mydb.cursor(buffered=True)
                cursor.execute('update users set target=%s where id=%s',[target,id1])
                mydb.commit()
                cursor.close()
            if 'worktarget' in [i for i in request.form]:
                worktarget=request.form['worktarget']
                cursor=mydb.cursor(buffered=True)
                cursor.execute('update users set workouttarget=%s where id=%s',[worktarget,id1])
                mydb.commit()
                cursor.close()
            return render_template('profile.html',target=target,id1=id1,consumed=consumed,worktarget=worktarget,workconsumed=workconsumed,day_report=day_report,sevendays_report=sevendays_report,day_report_w=day_report_w,sevendays_report_w=sevendays_report_w)
        return render_template('profile.html',target=target,id1=id1,consumed=consumed,worktarget=worktarget,workconsumed=workconsumed,day_report=day_report,sevendays_report=sevendays_report,day_report_w=day_report_w,sevendays_report_w=sevendays_report_w)
    return redirect(url_for('login'))
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        id1=request.form['id']
        cursor=mydb.cursor(buffered=True)
        cursor.execute('SELECT ID from users')
        users=cursor.fetchall()
        cursor.close()
        if (id1,) in users:
            flash('User Id already Exists')
            return render_template('registration.html')
        name=request.form['name']
        email=request.form['email']
        number=request.form['number']
        password=request.form['password']
        otp=genotp()
        subject='Thanks for registering'
        body = 'your one time password is- '+otp
        sendmail(email,subject,body)
        return render_template('otp.html',otp=otp,id1=id1,name=name,email=email,number=number,password=password)
    return render_template('registration.html')

@app.route('/otp/<otp>/<id1>/<name>/<email>/<number>/<password>',methods=['POST','GET'])
def getotp(otp,id1,name,email,number,password):
    if request.method == 'POST':
        OTP=request.form['otp']
        if otp == OTP:
            cursor=mydb.cursor(buffered=True) 
            cursor.execute('INSERT INTO users (id,name,email,mobile_no,password) values(%s,%s,%s,%s,%s)',[id1,name,email,number,password])
            mydb.commit()
            cursor.close()
            flash('Details registered successfully')
            return redirect(url_for('login'))
        else:
            flash('wrong OTP')

    return render_template('otp.html',otp=otp,id1=id1,name=name,email=email,number=number,password=password)

@app.route('/forgotpassword',methods=('GET', 'POST'))
def forgotpassword():
    if request.method=='POST':
        id1 = request.form['id']
        cursor=mydb.cursor(buffered=True)
        cursor.execute('select id from users') 
        deta=cursor.fetchall()
        if (id1,) in deta:
            cursor.execute('select email from users where id=%s',[id1])
            data=cursor.fetchone()[0]
            cursor.close()
            subject=f'Reset Password for {data}'
            body=f'Reset the passwword using-\{request.host+url_for("resetpwd",token=token(id1,300))}'
            sendmail(data,subject,body)
            flash('Reset link sent to your registered mail id')
            return redirect(url_for('login'))
        else:
            flash('user does not exits')
    return render_template('forgot.html')

@app.route('/resetpwd/<token>',methods=('GET', 'POST'))
def resetpwd(token):
    try:
        s=Serializer(app.config['SECRET_KEY'])
        id1=s.loads(token)['user']
        if request.method=='POST':
            npwd = request.form['npassword']
            cpwd = request.form['cpassword']
            if npwd == cpwd:
                cursor=mydb.cursor(buffered=True)
                cursor.execute('update users set password=%s where id=%s',[npwd,id1])
                mydb.commit()
                cursor.close()
                return 'Password reset Successfull'
            else:
                return 'Password does not matched try again'
        return render_template('newpassword.html')
    except Exception as e:
        abort(410,description='reset link expired')

@app.route('/login',methods=['GET','POST'])
def login():
    if session.get('user'):
        return redirect(url_for('homepage',id1=session['user']))
    if request.method=="POST":
        user=request.form['user']
        cursor=mydb.cursor(buffered=True)
        cursor.execute('SELECT id from users')
        users=cursor.fetchall()            
        password=request.form['password']
        cursor.execute('select password from users where id=%s',[user])
        data=cursor.fetchone()
        cursor.close() 
        if (user,) in users:
            if password==data[0]:
                session['user']=user
                return redirect(url_for('homepage',id1=user))
            else:
                flash('Invalid Password')
                return render_template('login.html')
        else:
            flash('Invalid user id')
            return render_template('login.html')      
    return render_template('login.html')
@app.route('/addfood',methods=['GET','POST'])
def addfood():
    if session.get('user'):
        cursor=mydb.cursor(buffered=True)
        today=date.today()
        current_date=datetime.strptime(f'{str(today.year)}-{str(today.month)}-{str(today.day)}','%Y-%m-%d')
        cursor.execute('SELECT item from items order by category asc')
        items=cursor.fetchall()
        cursor.execute('SELECT target from users where id=%s',[session.get('user')])
        target=int(cursor.fetchone()[0])
        current_date=date.today()
        current_date=f"{current_date.year}-{current_date.month}-{current_date.day}"
        today_date=datetime.strptime(current_date,'%Y-%m-%d')
        date_today=datetime.strftime(today_date,'%Y-%m-%d')
        cursor.execute('select item,category,sum(quantity),sum(carbohydrates),sum(fats),sum(protein),sum(fiber),sum(callories) from callorie_track where id=%s and date=%s group by item',[session.get('user'),date_today])
        day_report=cursor.fetchall()
        cursor.close()
        if target==0:
            flash('Set the target first!')
            return render_template('addfood.html',id1=session['user'],items=items)
        if request.method=="POST":
            cursor=mydb.cursor(buffered=True)
            item=request.form['item']
            category=request.form['category']
            quantity=int(request.form['quantity'])
            cursor.execute('SELECT carbohydrates,fats,protein,fiber,calorie from items where item=%s',[item])
            cal_data=cursor.fetchone()
            carbohydrates=round(quantity*(cal_data[0]/100),2)
            fats=round(quantity*(cal_data[1]/100),2)
            protein=round(quantity*(cal_data[2]/100),2)
            fiber=round(quantity*(cal_data[3]/100),2)
            calories=round(quantity*(cal_data[4]/100),2)
            cursor.execute('SELECT consumed from users where id=%s',[session.get('user')])
            consumed=round(float(cursor.fetchone()[0]),2)+calories
            cursor.execute('update users set consumed=%s where id=%s',[consumed,session.get('user')])
            cursor.execute('insert into callorie_track (id,item,category,quantity,carbohydrates,fats,protein,fiber,callories,date) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',[session.get('user'),item,category,quantity,carbohydrates,fats,protein,fiber,calories,current_date])
            mydb.commit()
            cursor.execute('select item,category,sum(quantity),sum(carbohydrates),sum(fats),sum(protein),sum(fiber),sum(callories) from callorie_track where id=%s and date=%s group by item',[session.get('user'),date_today])
            day_report=cursor.fetchall()
            cursor.close()
            return render_template('addfood.html',id1=session['user'],items=items,day_report=day_report)
        return render_template('addfood.html',id1=session['user'],items=items,day_report=day_report)
    return redirect(url_for('login'))
@app.route('/addworkout',methods=['GET','POST'])
def addwork():
    if session.get('user'):
        cursor=mydb.cursor(buffered=True)
        today=date.today()
        current_date=datetime.strptime(f'{str(today.year)}-{str(today.month)}-{str(today.day)}','%Y-%m-%d')
        cursor.execute('SELECT workout from workout')
        workouts=cursor.fetchall()
        cursor.execute('SELECT workouttarget from users where id=%s',[session.get('user')])
        workouttarget=int(cursor.fetchone()[0])
        current_date=date.today()
        current_date=f"{current_date.year}-{current_date.month}-{current_date.day}"
        today_date=datetime.strptime(current_date,'%Y-%m-%d')
        date_today=datetime.strftime(today_date,'%Y-%m-%d')
        cursor.execute('select workout,sum(time),sum(callories) from workout_track where id=%s and date=%s group by workout',[session.get('user'),date_today])
        day_report=cursor.fetchall()
        cursor.close()
        if workouttarget==0:
            flash('Set the target first!')
            return render_template('addworkout.html',id1=session['user'],workouts=workouts)
        if request.method=="POST":
            cursor=mydb.cursor(buffered=True)
            time=float(request.form['time'])
            category=request.form['category']
            cursor.execute('SELECT time,callories from workout where workout=%s',[category])
            cal_data=cursor.fetchone()
            calories=round(time*(cal_data[1]/cal_data[0]),2)
            cursor.execute('SELECT workoutconsumed from users where id=%s',[session.get('user')])
            consumed=round(float(cursor.fetchone()[0]),2)+calories
            cursor.execute('update users set workoutconsumed=%s where id=%s',[consumed,session.get('user')])
            cursor.execute('insert into workout_track (workout,time,id,callories,date) values(%s,%s,%s,%s,%s)',[category,time,session.get('user'),calories,current_date])
            mydb.commit()
            cursor.execute('select workout,sum(time),sum(callories) from workout_track where id=%s and date=%s group by workout',[session.get('user'),date_today])
            day_report=cursor.fetchall()
            cursor.close()
            return render_template('addworkout.html',id1=session['user'],workouts=workouts,day_report=day_report)
        return render_template('addworkout.html',id1=session['user'],workouts=workouts,day_report=day_report)
    return redirect(url_for('login'))
@app.route('/logout')
def logout():
    session['user']=None
    return redirect(url_for('home'))
@app.route('/view')
def view():
    return render_template('details.html')
app.run(debug=True,use_reloader=True)
