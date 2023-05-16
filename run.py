import pymysql
from bottle import Bottle, request, response, template
import random
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from email.header import Header
import threading

# 全局设置
# 注释后带*为需要修改或必填
# 注释后带^的为可修改
# 其余不建议修改
e_add = "smtp.example.com" # 邮箱SMTP服务器地址*
e_a = 465 # 邮箱SMTP服务器SSL端口
e_user = "xxx@example.com" # 邮箱账号*
e_pass = "AaBbCc123" # 邮箱登录授权码(SMTP密码)*
e_xuser = "抗原检测结果通知" # 显示的发件人名称^
e_sub = "抗原检测结果报告" # 邮件标题^
e_body = "请在47-48行继续修改" # 邮件内容，不熟悉HTML语言不建议修改（重要）！
web = "https://example.com/" # 本网站主页*
po = 8080 # 网站运行端口，若服务器未安装任何环境，建议使用80端口，其他非80端口见nginx的代理功能^
d_add = "127.0.0.1" # mysql数据库地址*
d_po = 3306 # mysql数据库端口*
d_user = "root" # mysql数据库用户名*
d_pass = "password" # mysql数据库密码*
d_base = "chaxun" # mysql数据库名*
houtai = "/backend" # 后台地址^
bian = 'utf-8' # 编码格式
#————————————下方内容不建议修改——————————

app = Bottle()

# 邮件设置
con = smtplib.SMTP_SSL(e_add,e_a)

from_addr = e_user
subject = e_sub

def sende(em,code):
    con.login(e_user,e_pass)
    msg = MIMEMultipart()
    subject = Header(e_sub, bian).encode() 
    msg['Subject'] = subject
    msg['From'] = e_xuser + ' <' + e_user + '>'
    msg['To'] = em
    content = '''
    <center><h1>抗原检测结果报告</h1>
    <p>尊敬的'''+em+''',您的抗原检测结果已出，请访问<a herf="'''+ web + '''">'''+ web + '''</a>查询结果</p>您的唯一查询码为：'''+code+'''</center>
    '''
    html = MIMEText(content, 'html', bian) 
    msg.attach(html)
    # 发送邮件
    con.sendmail(e_user, em, msg.as_string()) 
    con.quit()


def connect_db():
    return pymysql.connect(
        host=d_add,
        user=d_user,
        password=d_pass,
        database=d_base
    )

@app.route("/main.js")
def js():
    return template("main.js")

@app.route("/")
def index():
    return template("frontend.html")

@app.route(houtai)
def backend():
    return template("backend.html")

@app.route("/upload", method="POST")
def upload():
    email = request.forms.get("email")
    text=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    num=["1","2","3","4","5","6","7","8","9","0"]
    a=13
    jihuo=""
    for i in range(a):
        r=random.randint(0, 1)
        r1=text[random.randint(0, 25)]
        r2=num[random.randint(0,9)]
        if r==0:
            jihuo=jihuo+r1
        else:
            jihuo=jihuo+r2
    result = request.forms.get("result")
    query_code = jihuo
    if query_code and result:
        try:
            with connect_db() as conn:
                with conn.cursor() as cursor:
                    sql = "INSERT INTO results (query_code, result) VALUES (%s, %s)"
                    cursor.execute(sql, (query_code, result))
                conn.commit()
            thread = threading.Thread(target=sende,kwargs={'em': email, 'code': jihuo})
            thread.start()            
            return {"status": "success", "se":jihuo}
        except pymysql.IntegrityError:
            response.status = 400
            return {"status": "error", "message": "Duplicate query code"}
    response.status = 400
    return {"status": "error", "message": "Missing query code or result"}

@app.route("/search", method="POST")
def search():
    query_code = request.forms.get("query_code")

    if query_code:
        with connect_db() as conn:
            with conn.cursor() as cursor:
                sql = "SELECT result FROM results WHERE query_code = %s"
                cursor.execute(sql, (query_code,))
                result = cursor.fetchone()

        if result:
            return {"status": "success", "result": result[0]}
        else:
            return {"status": "not_found"}

    return {"status": "error", "message": "Missing query code"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=po)