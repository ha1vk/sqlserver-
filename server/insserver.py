#coding:utf-8
from flask import Flask, request,Response,render_template,redirect,url_for,send_file,make_response
import os
import sys
import database
import socket
import constants
import encdec
import base64
import json
import random
from datetime import datetime,timedelta

reload(sys) 
sys.setdefaultencoding('utf8')

#os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

#创建flask对象
app = Flask(__name__)

#创建数据库对象
db = database.DataBase()

#返回秘钥给客户端
@app.route('/gk', methods=['GET'])
def gk():
    return constants.gk,200

#注册账户
@app.route('/upload', methods=['POST'])
def upload():
    values = request.get_json()

    data = values.get('icon_data')
    id_n = values.get('id_n')
    type = values.get('type')
    action = values.get('action')
    #print data
    if data is None or id_n is None or type is None:
        return "Error: 数据格式错误", 400
    if action is None and db.checkExistID(id_n) != 'pass':
        return "Error:身份证用户已经存在",200
    data = base64.b64decode(data)
    path = 'icons/' + id_n +'_' + type + '.jpg'
    with open(path,'wb') as f:
        f.write(data)
    return '上传成功',200

#登录账户
@app.route('/login', methods=['POST'])
def login():
    values = request.get_json()
    username = values.get('username')
    password = values.get('password')
    type = values.get('type')
    if username is None or password is None:
        return "Error: 未收到数据", 400
    if type == 'mgr':
        ans = db.loginMgr(username,password)
    else:
        ans = db.login(username,password)
    if 'success' == ans:
        response = Response('success')
        expires = datetime.now() + timedelta(hours=8)
        response.set_cookie('username',username,expires=expires)
        response.set_cookie('ps',password,expires=expires)
        return response
    else:
        return ans,200

#登录账户
@app.route('/loginout', methods=['GET'])
def loginout():
    response = make_response('注销')
    response.delete_cookie('username')
    response.delete_cookie('ps')
    return response

@app.route('/getInfo', methods=['GET'])
def getInfo():
    username = request.cookies.get('username')
    password = request.cookies.get('ps')
    if username is None or password is None:
        return "还未登录", 400
    ans = db.query(username,password)
    if isinstance(ans,dict):
        ans = json.dumps(ans,indent=4)
    return ans,200


@app.route('/jquery.form.js', methods=['GET'])
def jqueryF():
    return send_file('templates/jQuery.Form.js')

@app.route('/jquery.processing.plugin.js', methods=['GET'])
def jqueryP():
    return send_file('templates/jquery.processing.plugin.js')

@app.route('/unknown.jpg', methods=['GET'])
def unknown():
    return send_file('templates/unknown.jpg')

@app.route('/loading.gif', methods=['GET'])
def loadingGif():
    return send_file('templates/loading.gif')

@app.route('/loading2.gif', methods=['GET'])
def loadingGif2():
    return send_file('templates/loading2.gif')

@app.route('/loading3.gif', methods=['GET'])
def loadingGif3():
    return send_file('templates/loading3.gif')

#注册账户
@app.route('/regacc', methods=['POST'])
def regacc():
    values = request.get_json()
    data = values.get('userData')
    if data is None:
        return "Error: 未收到数据", 400
    print('已经收到用户的数据')
    data = encdec.des_descrypt(data)
    print(data)
    #db.insert(data)
    return db.insert(data),200

#更新账户
@app.route('/updateAcc', methods=['POST'])
def updateAcc():
    username = request.cookies.get('username')
    password = request.cookies.get('ps')
    if username is None or password is None:
        return "还未登录", 400
    values = request.get_json()
    data = values.get('userData')
    if data is None:
        return "Error: 未收到数据", 400
    print('已经收到用户的数据')
    data = encdec.des_descrypt(data)
    print(data)
    return db.updateAcc(username,password,data),200

#更新密码
@app.route('/updatePass0', methods=['POST'])
def updatePass0():
    username = request.cookies.get('username')
    password = request.cookies.get('ps')
    if username is None or password is None:
        return "还未登录", 400
    values = request.get_json()
    data = values.get('userData')
    if data is None:
        return "Error: 未收到数据", 400
    print('已经收到用户的数据')
    data = encdec.des_descrypt(data)
    print(data)
    return db.updatePass0(username,password,data),200


#更新密码
@app.route('/updatePass1', methods=['POST'])
def updatePass1():
    values = request.get_json()
    data = values.get('userData')
    if data is None:
        return "Error: 未收到数据", 400
    print('已经收到用户的数据')
    data = encdec.des_descrypt(data)
    print(data)
    return db.updatePass1(data),200

#返回保单填写表
@app.route('/getInsForm', methods=['GET'])
def getInsForm():
    username = request.cookies.get('username')
    password = request.cookies.get('ps')
    if username is None or password is None:
        return "还未登录", 400
    t = datetime.now()
    s = str(t.year) + str(t.month) + str(t.day) + str(t.hour) + str(t.minute) + str(t.second)
    baodan_number = s + str(random.randint(1, 5000))
    while not db.checkBaodanNumber(baodan_number):
        baodan_number = s + str(random.randint(1, 5000))

    return render_template('InsurancePolicy.html',baodan_number=baodan_number,curY=str(t.year) + ' ',curM=str(t.month) + '  ',curD=str(t.day) + '  ',tarY=str(t.year + 1) + '  ',tarM=str(t.month) + '  ',tarD = str(t.day) + '  ',Insurer='link4  ',InsurerAddr='HUSE  ',InsurerZip='000000  ',InsurerTel='123456987  ',InsurerFax='10-123456987  ')

@app.route('/submitInsForm', methods=['POST'])
def submitInsForm():
    username = request.cookies.get('username')
    password = request.cookies.get('ps')
    if username is None or password is None:
        return "还未登录", 400
    if db.isBlack0(username):
        return "黑名单用户，无法投保!",400

    form = request.form
    baodan_data = json.dumps(form,sort_keys=True)
    id = db.getID(username,password)
    if id == 'fail':
        return id,400
    ans = db.insertBaodan(id,form['baodan_number'],baodan_data)
    return redirect(url_for('showInsForm'))

@app.route('/submitLiPeiForm', methods=['POST'])
def submitLiPeiForm():
    username = request.cookies.get('username')
    password = request.cookies.get('ps')
    if username is None or password is None:
        return "还未登录", 400
    if db.isBlack0(username):
        return "黑名单用户，无法理赔!",400
    form = request.form
    baodan_number = form['baodan_number']

    lipei_data = json.dumps(form,sort_keys=True)
    print lipei_data
    id = db.getID(username,password)
    if id == 'fail':
        return id,400
    ans = db.insertLiPei(id,baodan_number,lipei_data)

    return '理赔申请已提交，等待受理',200


@app.route('/showInsForm', methods=['GET'])
def showInsForm():
    page = request.args.get('page')
    if page is None:
       page = 0
    nextpage = int(page) + 1
    prevpage = int(page) -1
    username = request.cookies.get('username')
    password = request.cookies.get('ps')
    if username is None or password is None:
        return render_template('unknown.html',prevpage=-1,Text="还未登录")
    id = db.getID(username,password)
    if id == 'fail':
        return id,400
    ans = db.queryBaodan0(id,page)
    if ans == '没有保单信息':
        return  render_template('unknown.html',prevpage=prevpage,m_html="showInsForm",Text=ans)
    #print encdec.des_descrypt(ans)
    baodan = json.loads(encdec.des_descrypt(ans))
    #print baodan
    return render_template('ReadInsurancePolicy.html',prevpage=prevpage,nextpage=nextpage,baodan_number=baodan[u'baodan_number'].decode('utf8'),baodan_id=baodan[u'baodan_id'].decode('utf8'),baodan_id2=baodan[u'baodan_id2'].decode('utf8'),baodan_id3=baodan[u'baodan_id3'].decode('utf8'),baodan_id4=baodan[u'baodan_id4'].decode('utf8'),baodan_id5=baodan[u'baodan_id5'].decode('utf8'),baodan_id6=baodan[u'baodan_id6'].decode('utf8'),baodan_id7=baodan[u'baodan_id7'].decode('utf8'),baodan_id8=baodan[u'baodan_id8'].decode('utf8'),baodan_id9=baodan[u'baodan_id9'].decode('utf8'),baodan_id10=baodan[u'baodan_id10'].decode('utf8'),baodan_id11=baodan[u'baodan_id11'].decode('utf8'),baodan_id12=baodan[u'baodan_id12'].decode('utf8'),baodan_id13=baodan[u'baodan_id13'].decode('utf8'),baodan_id14=baodan[u'baodan_id14'].decode('utf8'),baodan_id15=baodan[u'baodan_id15'].decode('utf8'),baodan_id16=baodan[u'baodan_id16'].decode('utf8'),baodan_id17=baodan[u'baodan_id17'].decode('utf8'),baodan_id18=baodan[u'baodan_id18'].decode('utf8'),baodan_id19=baodan[u'baodan_id19'].decode('utf8'),baodan_id20=baodan[u'baodan_id20'].decode('utf8'),baodan_id21=baodan[u'baodan_id21'].decode('utf8'),baodan_id22=baodan[u'baodan_id22'].decode('utf8'),baodan_id23=baodan[u'baodan_id23'].decode('utf8'),baodan_id24=baodan[u'baodan_id24'].decode('utf8'),baodan_id25=baodan[u'baodan_id25'].decode('utf8'),baodan_id26=baodan[u'baodan_id26'].decode('utf8'),baodan_id27=baodan[u'baodan_id27'].decode('utf8'),baodan_id28=baodan[u'baodan_id28'].decode('utf8'),baodan_id29=baodan[u'baodan_id29'].decode('utf8'),baodan_id30=baodan[u'baodan_id30'].decode('utf8'),baodan_id31=baodan[u'baodan_id31'].decode('utf8'),baodan_id32=baodan[u'baodan_id32'].decode('utf8'),baodan_id33=baodan[u'baodan_id33'].decode('utf8'),baodan_id34=baodan[u'baodan_id34'].decode('utf8'),baodan_id35=baodan[u'baodan_id35'].decode('utf8'),baodan_id36=baodan[u'baodan_id36'].decode('utf8'),baodan_id37=baodan[u'baodan_id37'].decode('utf8'),baodan_id38=baodan[u'baodan_id38'].decode('utf8'),baodan_id39=baodan[u'baodan_id39'].decode('utf8'),baodan_id40=baodan[u'baodan_id40'].decode('utf8'),baodan_id41=baodan[u'baodan_id41'].decode('utf8'),baodan_id42=baodan[u'baodan_id42'].decode('utf8'),baodan_id43=baodan[u'baodan_id43'].decode('utf8'),baodan_id44=baodan[u'baodan_id44'].decode('utf8'),baodan_id45=baodan[u'baodan_id45'].decode('utf8'),baodan_id46=baodan[u'baodan_id46'].decode('utf8'),baodan_id47=baodan[u'baodan_id47'].decode('utf8'),baodan_id48=baodan[u'baodan_id48'].decode('utf8'),baodan_id49=baodan[u'baodan_id49'].decode('utf8'),baodan_id50=baodan[u'baodan_id50'].decode('utf8'),baodan_id51=baodan[u'baodan_id51'].decode('utf8'),baodan_id52=baodan[u'baodan_id52'].decode('utf8'),baodan_id53=baodan[u'baodan_id53'].decode('utf8'),baodan_id54=baodan[u'baodan_id54'].decode('utf8'),baodan_id55=baodan[u'baodan_id55'].decode('utf8'),baodan_id56=baodan[u'baodan_id56'].decode('utf8'),baodan_id57=baodan[u'baodan_id57'].decode('utf8'),baodan_id58=baodan[u'baodan_id58'].decode('utf8'),baodan_id59=baodan[u'baodan_id59'].decode('utf8'))

@app.route('/loadLiPeiForm', methods=['POST'])
def loadLiPeiForm():
    username = request.cookies.get('username')
    password = request.cookies.get('ps')
    if username is None or password is None:
        return render_template('unknown.html',prevpage=-1,Text="还未登录")
    values = request.get_json()
    baodan_numb = values.get('baodan_numb')
    id = db.getID(username,password)
    if id == 'fail':
        return id,400
    ck = db.checkLiPei(id,baodan_numb)
    if ck != 'pass':
        return render_template('unknown.html',prevpage=-1,Text="该保单已经理赔，请选择其他保单")
    ans = db.queryBaodan1(id,baodan_numb)
    if ans == '没有保单信息':
        return  render_template('unknown.html',prevpage=-1,Text=ans)
    baodan = json.loads(encdec.des_descrypt(ans))
    return render_template('LiPeiForm.html',**baodan)

@app.route('/insLiPei', methods=['GET'])
def insLiPei():
    username = request.cookies.get('username')
    password = request.cookies.get('ps')
    if username is None or password is None:
        return render_template('unknown.html',prevpage=-1,Text="还未登录")
    id = db.getID(username,password)
    if id == 'fail':
        return id,400
    ans = db.queryBaodanNumbers(id)
    if ans == '没有保单信息':
        return  render_template('unknown.html',prevpage=-1,Text=ans)
    ans.sort()
    context = {
      "baodans":ans
    }
    return render_template('LiPei.html',**context)


@app.route('/view_users', methods=['GET'])
def viewUsers():
    username = request.cookies.get('username')
    password = request.cookies.get('ps')
    if username is None or password is None:
        return render_template('unknown.html',prevpage=-1,Text="还未登录")
    users = db.queryUsers()
    if '没有' in users:
        return render_template('unknown.html',prevpage=-1,Text=users)
    context = {
      "users":users,
      "len":len(users)
    }
    return render_template('user_viewer.html',**context)

#查看所有的保单
@app.route('/view_all_baodan', methods=['GET'])
def viewAllBaodans():
    username = request.cookies.get('username')
    password = request.cookies.get('ps')
    if not db.isAdmin(username,password):
       return render_template('unknown.html',prevpage=-1,Text="请不要越界")
    ans = db.getAllBaodanNumbers()
    if ans == '没有保单信息':
        return  render_template('unknown.html',prevpage=-1,Text=ans)
    ans.sort()
    context = {
      "mode":"viewAll",
      "baodans":ans
    }
    return render_template('viewAllBaoDan.html',**context)

#通过保单号加载保单(只读)
@app.route('/load_next_baodan', methods=['POST'])
def loadBaoDanByNum():
    values = request.get_json()
    num = values.get('baodan_numb')
    #prev = values.get('prev')
    #next = values.get('next')
    prev = next = -1;
    if num is None:
       return render_template('unknown.html',prevpage=-1,Text="参数错误")
    username = request.cookies.get('username')
    password = request.cookies.get('ps')
    if not db.isAdmin(username,password):
       return render_template('unknown.html',prevpage=-1,Text="请不要越界")
    id = db.getIDByBNum(num);
    if id == 'fail':
        return id,400
    #这张保单已经理赔
    if db.checkLiPei(id,num) != 'pass':
       ans = db.queryLiPeiInfo2(num)
       if ans == '没有保单信息':
           return  render_template('unknown.html',prevpage=-1,m_html="showLiPeiHis",Text=ans)
       ans = json.loads(encdec.des_descrypt(ans))

       baodan = db.queryBaodan1(id,num)
       baodan = json.loads(encdec.des_descrypt(baodan))
       context = ans.update(baodan)
       return render_template('ReadLiPeiInfo.html',prevpage=prev,nextpage=next,**ans)
    #未理赔保单
    else:
       ans = db.queryBaodan1(id,num)
       if ans == '没有保单信息':
           return  render_template('unknown.html',prevpage=-1,m_html="showInsForm",Text=ans)
       #print encdec.des_descrypt(ans)
       baodan = json.loads(encdec.des_descrypt(ans))
       #print baodan
       return render_template('ReadInsurancePolicy.html',prevpage=prev,nextpage=next,baodan_number=baodan[u'baodan_number'].decode('utf8'),baodan_id=baodan[u'baodan_id'].decode('utf8'),baodan_id2=baodan[u'baodan_id2'].decode('utf8'),baodan_id3=baodan[u'baodan_id3'].decode('utf8'),baodan_id4=baodan[u'baodan_id4'].decode('utf8'),baodan_id5=baodan[u'baodan_id5'].decode('utf8'),baodan_id6=baodan[u'baodan_id6'].decode('utf8'),baodan_id7=baodan[u'baodan_id7'].decode('utf8'),baodan_id8=baodan[u'baodan_id8'].decode('utf8'),baodan_id9=baodan[u'baodan_id9'].decode('utf8'),baodan_id10=baodan[u'baodan_id10'].decode('utf8'),baodan_id11=baodan[u'baodan_id11'].decode('utf8'),baodan_id12=baodan[u'baodan_id12'].decode('utf8'),baodan_id13=baodan[u'baodan_id13'].decode('utf8'),baodan_id14=baodan[u'baodan_id14'].decode('utf8'),baodan_id15=baodan[u'baodan_id15'].decode('utf8'),baodan_id16=baodan[u'baodan_id16'].decode('utf8'),baodan_id17=baodan[u'baodan_id17'].decode('utf8'),baodan_id18=baodan[u'baodan_id18'].decode('utf8'),baodan_id19=baodan[u'baodan_id19'].decode('utf8'),baodan_id20=baodan[u'baodan_id20'].decode('utf8'),baodan_id21=baodan[u'baodan_id21'].decode('utf8'),baodan_id22=baodan[u'baodan_id22'].decode('utf8'),baodan_id23=baodan[u'baodan_id23'].decode('utf8'),baodan_id24=baodan[u'baodan_id24'].decode('utf8'),baodan_id25=baodan[u'baodan_id25'].decode('utf8'),baodan_id26=baodan[u'baodan_id26'].decode('utf8'),baodan_id27=baodan[u'baodan_id27'].decode('utf8'),baodan_id28=baodan[u'baodan_id28'].decode('utf8'),baodan_id29=baodan[u'baodan_id29'].decode('utf8'),baodan_id30=baodan[u'baodan_id30'].decode('utf8'),baodan_id31=baodan[u'baodan_id31'].decode('utf8'),baodan_id32=baodan[u'baodan_id32'].decode('utf8'),baodan_id33=baodan[u'baodan_id33'].decode('utf8'),baodan_id34=baodan[u'baodan_id34'].decode('utf8'),baodan_id35=baodan[u'baodan_id35'].decode('utf8'),baodan_id36=baodan[u'baodan_id36'].decode('utf8'),baodan_id37=baodan[u'baodan_id37'].decode('utf8'),baodan_id38=baodan[u'baodan_id38'].decode('utf8'),baodan_id39=baodan[u'baodan_id39'].decode('utf8'),baodan_id40=baodan[u'baodan_id40'].decode('utf8'),baodan_id41=baodan[u'baodan_id41'].decode('utf8'),baodan_id42=baodan[u'baodan_id42'].decode('utf8'),baodan_id43=baodan[u'baodan_id43'].decode('utf8'),baodan_id44=baodan[u'baodan_id44'].decode('utf8'),baodan_id45=baodan[u'baodan_id45'].decode('utf8'),baodan_id46=baodan[u'baodan_id46'].decode('utf8'),baodan_id47=baodan[u'baodan_id47'].decode('utf8'),baodan_id48=baodan[u'baodan_id48'].decode('utf8'),baodan_id49=baodan[u'baodan_id49'].decode('utf8'),baodan_id50=baodan[u'baodan_id50'].decode('utf8'),baodan_id51=baodan[u'baodan_id51'].decode('utf8'),baodan_id52=baodan[u'baodan_id52'].decode('utf8'),baodan_id53=baodan[u'baodan_id53'].decode('utf8'),baodan_id54=baodan[u'baodan_id54'].decode('utf8'),baodan_id55=baodan[u'baodan_id55'].decode('utf8'),baodan_id56=baodan[u'baodan_id56'].decode('utf8'),baodan_id57=baodan[u'baodan_id57'].decode('utf8'),baodan_id58=baodan[u'baodan_id58'].decode('utf8'),baodan_id59=baodan[u'baodan_id59'].decode('utf8'))

#加载待受理的保单
@app.route('/load_baodan_toaccept', methods=['POST'])
def loadBaoDanToAccept():
    values = request.get_json()
    num = values.get('baodan_numb')
    if num is None:
       return render_template('unknown.html',prevpage=-1,Text="参数错误")
    username = request.cookies.get('username')
    password = request.cookies.get('ps')
    if not db.isAdmin(username,password):
       return render_template('unknown.html',prevpage=-1,Text="请不要越界")
    id = db.getIDByBNum(num);
    if id == 'fail':
        return id,400
    #这张保单已经理赔
    if db.checkLiPei(id,num) != 'pass':
       ans = db.queryLiPeiInfo2(num)
       if ans == '没有保单信息':
           return  render_template('unknown.html',prevpage=-1,m_html="showLiPeiHis",Text=ans)
       ans = json.loads(encdec.des_descrypt(ans))

       baodan = db.queryBaodan1(id,num)
       baodan = json.loads(encdec.des_descrypt(baodan))
       context = ans.update(baodan)
       return render_template('ToAcceptLiPeiInfo.html',**ans)
    #未理赔保单
    else:
       return  render_template('unknown.html',prevpage=-1,m_html="showInsForm",Text='没有保单信息')

#查看待受理的保单
@app.route('/view_baodan_to_accept', methods=['GET'])
def viewBaodansToAccept():
    username = request.cookies.get('username')
    password = request.cookies.get('ps')
    if not db.isAdmin(username,password):
       return render_template('unknown.html',prevpage=-1,Text="请不要越界")
    ans = db.getAllBaodanNumbersToAccept()
    if ans == '没有保单信息':
        return  render_template('unknown.html',prevpage=-1,Text=ans)
    ans.sort()
    context = {
       "mode":"viewToAccept",
      "baodans":ans
    }
    return render_template('viewAllBaoDan.html',**context)

#受理保单
@app.route('/accept_baodan', methods=['GET'])
def acceptBaoDan():
    username = request.cookies.get('username')
    password = request.cookies.get('ps')
    if not db.isAdmin(username,password):
       return render_template('unknown.html',prevpage=-1,Text="请不要越界")
    bnum = request.args.get('baodan_num')
    if bnum is None:
       return render_template('unknown.html',prevpage=-1,Text="参数错误")
    ans = db.acceptBaodan(bnum)
    return redirect(url_for('viewBaodansToAccept'))

#查看已受理的保单
@app.route('/view_baodan_accepted', methods=['GET'])
def viewBaodansAccepted():
    username = request.cookies.get('username')
    password = request.cookies.get('ps')
    if not db.isAdmin(username,password):
       return render_template('unknown.html',prevpage=-1,Text="请不要越界")
    ans = db.getAllBaodanNumbersAccepted()
    if ans == '没有保单信息':
        return  render_template('unknown.html',prevpage=-1,Text=ans)
    ans.sort()
    context = {
       "mode":"viewAccepted",
      "baodans":ans
    }
    return render_template('viewAllBaoDan.html',**context)

#加载已受理的保单
@app.route('/load_baodan_accepted', methods=['POST'])
def loadBaoDanAccepted():
    values = request.get_json()
    num = values.get('baodan_numb')
    if num is None:
       return render_template('unknown.html',prevpage=-1,Text="参数错误")
    username = request.cookies.get('username')
    password = request.cookies.get('ps')
    if not db.isAdmin(username,password):
       return render_template('unknown.html',prevpage=-1,Text="请不要越界")
    id = db.getIDByBNum(num);
    if id == 'fail':
        return id,400
    ans = db.queryLiPeiInfo2(num)
    if ans == '没有保单信息':
        return  render_template('unknown.html',prevpage=-1,m_html="showLiPeiHis",Text=ans)
    ans = json.loads(encdec.des_descrypt(ans))

    baodan = db.queryBaodan1(id,num)
    baodan = json.loads(encdec.des_descrypt(baodan))
    context = ans.update(baodan)
    return render_template('ReadLiPeiInfo.html',**ans)

@app.route('/view_blacks', methods=['GET'])
def viewBlacks():
    username = request.cookies.get('username')
    password = request.cookies.get('ps')
    if username is None or password is None:
        return render_template('unknown.html',prevpage=-1,Text="还未登录")
    users = db.queryBlackList()
    if '没有' in users:
        return render_template('unknown.html',prevpage=-1,Text=users)
    context = {
      "users":users,
      "len":len(users)
    }
    return render_template('black_viewer.html',**context)

@app.route('/removeBlackList', methods=['POST'])
def removeBlackList():
    username = request.cookies.get('username')
    password = request.cookies.get('ps')
    if username is None or password is None:
        return "还未登录",400
    values = request.get_json()
    username = values.get('username')
    if username is None:
        return "Error: 未收到数据", 400
    ans = db.removeBlackList(username)
    if '成功' in ans:
        return ans,200
    else:
        return ans,400


@app.route('/addBlackList', methods=['POST'])
def addBlackList():
    username = request.cookies.get('username')
    password = request.cookies.get('ps')
    if username is None or password is None:
        return "还未登录",400
    values = request.get_json()
    username = values.get('username')
    if username is None:
        return "Error: 未收到数据", 400
    ans = db.insertBlackList(username)
    if u'成功' in ans:
        return ans,200
    else:
        return ans,400

@app.route('/judge_users', methods=['GET'])
def judgeUsers():
    username = request.cookies.get('username')
    password = request.cookies.get('ps')
    if username is None or password is None:
        return render_template('unknown.html',prevpage=-1,Text="还未登录")
    ID_N = request.args.get('ID_N')
    if ID_N is None:
        return '参数错误',200
    if db.isBlack(ID_N):
        return '黑名单用户',200
    else:
        return '正常用户',200

#某用户名下的保单
@app.route('/owned_baodan', methods=['GET'])
def ownedBaodan():
    username = request.cookies.get('username')
    password = request.cookies.get('ps')
    if username is None or password is None:
        return "还未登录",400
    username = request.args.get('username')
    id = db.getID2(username)
    if id == 'fail':
        return id,400
    ans = db.queryAllBaodanNumbers(id)
    return ans,200


@app.route('/loadingHtml', methods=['GET'])
def loadingHtml():
    m_html = request.args.get('html')
    page = request.args.get('page')
    if m_html is None:
        return render_template('unknown.html',prevpage=-1,Text="参数不对")
    if page is None:
       page = 0
    return render_template('loadingHtml.html',m_html=m_html,page=page)

@app.route('/showLiPeiHis', methods=['GET'])
def showLiPeiHis():
    page = request.args.get('page')
    if page is None:
       page = 0
    nextpage = int(page) + 1
    prevpage = int(page) -1
    username = request.cookies.get('username')
    password = request.cookies.get('ps')
    if username is None or password is None:
        return render_template('unknown.html',prevpage=-1,Text="还未登录")
    id = db.getID(username,password)
    if id == 'fail':
        return id,400
    ans = db.queryLiPeiInfo(id,page)
    if ans == '没有保单信息':
        return  render_template('unknown.html',prevpage=prevpage,m_html="showLiPeiHis",Text=ans)
    ans = json.loads(encdec.des_descrypt(ans))
    baodan_number = ans['baodan_number']
    id = db.getID(username,password)
    if id == 'fail':
        return id,400
    baodan = db.queryBaodan1(id,baodan_number)
    baodan = json.loads(encdec.des_descrypt(baodan))
    context = ans.update(baodan)
    return render_template('ReadLiPeiInfo.html',prevpage=prevpage,nextpage=nextpage,**ans)

@app.route('/test', methods=['GET'])
def test():
    return 'ok',200

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    constants.myaddr = 'Addr:{}:{}'.format(ip,port)
    print constants.myaddr
    app.run(host='0.0.0.0', port=port,threaded=True)
