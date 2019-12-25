#coding:utf-8
import json
import pyodbc
import base64
import hashlib
import encdec
import binascii

try:
  import cPickle as pickle
except ImportError:
  import pickle

class DataBase:
    def __init__(self):
       # 打开数据库连接
       self.db = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=127.0.0.1,1433;DATABASE=insuranceDB;UID=insdbmanager;PWD=123456')
       cursor = self.db.cursor()
       print '数据连接化成功'

    def checkExistID(self,id):
       try:
         cursor=self.db.cursor()
         sql = 'select username from userInfo where ID_N=\'{}\';'.format(id)
         #print sql
         cursor.execute(sql)
         ans = cursor.fetchall()
         cursor.close()
         if len(ans) != 0:
            return "用户已经存在"
         return 'pass'
       except:
            print '数据库操作失败'

    #检查保单号是否已经存在
    def checkBaodanNumber(self,baodan_number):
       try:
         cursor=self.db.cursor()
         sql = 'select baodan_number from insInfo where baodan_number=\'{}\';'.format(baodan_number)
         print sql
         cursor.execute(sql)
         ans = cursor.fetchall()
         #cursor.close()
         if len(ans) == 0:
            return True
         return False
       except:
            print '数据库操作失败'

    def getMD5(self,str):
       md = hashlib.md5()
       md.update(str.encode('utf8'))
       return md.hexdigest()

    def checkMiBao(self,username,mibao_q1,mibao_a1,mibao_q2,mibao_a2):
       if 1 == 1:
         cursor=self.db.cursor()
         sql = 'select username from userInfo where username=\'{}\' and mibao_q1=\'{}\' and mibao_a1=\'{}\' and mibao_q2=\'{}\' and mibao_a2=\'{}\';'.format(username,mibao_q1,mibao_a1,mibao_q2,mibao_a2)
         sql = unicode(sql)
         print sql
         cursor.execute(sql)
         ans = cursor.fetchall()
         cursor.close()
         if len(ans) == 0:
            return '密保错误'
         return 'pass'
       else:
            print '数据库操作失败'

    def checkLiPei(self,id,baodan_number):
       try:
         cursor=self.db.cursor()
         sql = 'select baodan_number from lipeiInfo where ID_N=\'{}\' and baodan_number=\'{}\';'.format(id,baodan_number)
         #print sql
         cursor.execute(sql)
         ans = cursor.fetchall()
         cursor.close()
         if len(ans) != 0:
            return "该保单已经理赔"
         return 'pass'
       except:
            print '数据库操作失败'


    #根据密保修改密码
    def updatePass1(self,json_data):
       dict_data = json.loads(json_data)
       username = dict_data['username'].encode('utf8')
       mibao_q1 = binascii.b2a_hex(encdec.des_encrypt(dict_data['mibao_q1'].encode('utf8')))
       mibao_a1 = binascii.b2a_hex(encdec.des_encrypt(dict_data['mibao_a1'].encode('utf8')))
       mibao_q2 = binascii.b2a_hex(encdec.des_encrypt(dict_data['mibao_q2'].encode('utf8')))
       mibao_a2 = binascii.b2a_hex(encdec.des_encrypt(dict_data['mibao_a2'].encode('utf8')))
       ck = self.checkMiBao(username,mibao_q1,mibao_a1,mibao_q2,mibao_a2)
       if ck != 'pass':
          return ck
       new_password = self.getMD5(dict_data['new_password'])
       try:
         cursor=self.db.cursor()
         sql = 'UPDATE userInfo SET password=\'{}\' WHERE username=\'{}\' and mibao_q1=\'{}\' and mibao_a1=\'{}\' and mibao_q2=\'{}\' and mibao_a2=\'{}\';'.format(new_password,username,mibao_q1,mibao_a1,mibao_q2,mibao_a2)
         print sql
         cursor.execute(sql)
         self.db.commit()
         cursor.close()
         print '数据更新成功!'
         return '更新成功'
       except:
         return '更新失败'

    #根据原密码，修改密码
    def updatePass0(self,username,password,json_data):
       dict_data = json.loads(json_data)
       password_ = self.getMD5(dict_data['password'])
       if password != password_:
          return '原密码错误!'
       new_password = self.getMD5(dict_data['new_password'])
       try:
         cursor=self.db.cursor()
         sql = 'UPDATE userInfo SET password=\'{}\' WHERE username=\'{}\' and password=\'{}\';'.format(new_password,username,password)
         print sql
         cursor.execute(sql)
         cursor.close()
         print '数据更新成功!'
         return '更新成功'
       except:
         #self.db.close()
         print '数据库更新失败'
         return '更新失败'

    def updateAcc(self,username,password,json_data):
       dict_data = json.loads(json_data)
       try:
         cursor=self.db.cursor()
         sql = 'exec updateAcc \'{}\',\'{}\',\'{}\',\'{}\',{},\'{}\',\'{}\''.format(username,password,dict_data['wechat'].encode('utf8'),dict_data['sex'].encode('utf8'),dict_data['age'].encode('utf8'),dict_data['birth'].encode('utf8'),dict_data['home_addr'].encode('utf8'))
         sql = unicode(sql)
         #print sql
         cursor.execute(sql)
         self.db.commit()
         cursor.close()
         #print '数据更新成功!'
         return u'更新成功'
       except:
         #self.db.close()
         #print '数据库更新失败'
         return u'更新失败'


    def insert(self,json_data):
       dict_data = json.loads(json_data)
       pstr = self.getMD5(dict_data['password'])
       mibao_q1 = binascii.b2a_hex(encdec.des_encrypt(dict_data['mibao_q1'].encode('utf8')))
       mibao_a1 = binascii.b2a_hex(encdec.des_encrypt(dict_data['mibao_a1'].encode('utf8')))
       mibao_q2 = binascii.b2a_hex(encdec.des_encrypt(dict_data['mibao_q2'].encode('utf8')))
       mibao_a2 = binascii.b2a_hex(encdec.des_encrypt(dict_data['mibao_a2'].encode('utf8')))

       try:
         #ck = self.checkExistUser(dict_data['username'].encode('utf8'))
         #print ck
         #if ck != 'pass':
            #return ck
         cursor=self.db.cursor()
         sql = "exec registerUser \'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\'".format(dict_data['username'],pstr,dict_data['name'],dict_data['ID'],dict_data['age'],dict_data['sex'],dict_data['birth'],dict_data['user_head'],dict_data['icon_head'],dict_data['home_addr'],dict_data['home_phone'],dict_data['mobphone'],dict_data['wechat'],mibao_q1,mibao_a1,mibao_q2,mibao_a2)
         #解决编码问题
         sql = unicode(sql)
         #print sql
         cursor.execute(sql)
         self.db.commit()
         cursor.close()
         print '数据插入成功!'
         return u'注册成功'
       except:
         #self.db.close()
         print '数据库插入失败'
         return u'注册失败'
    def insertBaodan(self,ID_N,baodan_number,baodan_data):
       #try:
         cursor=self.db.cursor()
         #print baodan_data
         bhash = hashlib.sha256(baodan_data.encode()).hexdigest()
         baodan_data = encdec.des_encrypt(baodan_data)
         #print 'before:',binascii.b2a_hex(baodan_data)
         sql = 'INSERT INTO insInfo (baodan_number,ID_N,baodan,bhash) VALUES (\'{}\',\'{}\',\'{}\',\'{}\');'.format(baodan_number,ID_N,binascii.b2a_hex(baodan_data),bhash)
         #print sql
         cursor.execute(sql)
         self.db.commit()
         cursor.close()
         print '保单数据插入成功!'
         return '投保成功'
       #except:
         #self.db.close()
         print '保单数据插入失败'
         return '投保失败'

    def insertLiPei(self,id,baodan_number,lipei_data):
       try:
         cursor=self.db.cursor()
         lipei_data = encdec.des_encrypt(lipei_data)
         sql = 'INSERT INTO lipeiInfo (ID_N,baodan_number,lipei,accepted) VALUES (\'{}\',\'{}\',\'{}\',\'{}\');'.format(id,baodan_number,binascii.b2a_hex(lipei_data),False)
         #print sql
         cursor.execute(sql)
         self.db.commit()
         cursor.close()
         print '理赔数据插入成功!'
         return '理赔成功'
       except:
         #self.db.close()
         print '理赔数据插入失败'
         return '理赔失败'

    def insertMgr(self,username,password):
       try:
         cursor=self.db.cursor()
         password = self.getMD5(password)
         sql = 'INSERT INTO mgrInfo (username,password) VALUES (\'{}\',\'{}\');'.format(username,password)
         #print sql
         cursor.execute(sql)
         self.db.commit()
         cursor.close()
         print '新增管理员成功!'
         return '新增管理员成功'
       except:
         #self.db.close()
         print '新增管理员失败'
         return '新增管理员失败'

    def insertBlackList(self,username):
       if 1 == 1:
         cursor=self.db.cursor()
         sql = 'INSERT INTO blackInfo (username) VALUES (\'{}\')'.format(username)
         #print sql
         cursor.execute(sql)
         self.db.commit()
         cursor.close()
         #print '新增黑名单成功!'
         return u'新增黑名单成功'
       else:
         #self.db.close()
         #print '新增黑名单失败'
         return u'新增黑名单失败'

    def removeBlackList(self,username):
       try:
         cursor=self.db.cursor()
         sql = 'DELETE FROM blackInfo WHERE username=\'{}\''.format(username)
         #print sql
         cursor.execute(sql)
         self.db.commit()
         cursor.close()
         #print '移出黑名单成功!'
         return u'移出黑名单成功'
       except:
         #self.db.close()
         #print '移出黑名单失败'
         return u'移出黑名单失败'


    def loginMgr(self,mgrname,password):
       cursor=self.db.cursor()
       cursor.execute('SELECT * FROM mgrInfo WHERE mgrname=\'{}\' and password=\'{}\';'.format(mgrname,password))
       nRet = cursor.fetchall()
       if len(nRet) == 0:
          return '登录失败'
       else:
          return 'success'

    def query(self,username,password):
       cursor=self.db.cursor()
       cursor.execute('select * from users_full_info WHERE username=\'{}\' and password=\'{}\';'.format(username,password))
       nRet = cursor.fetchall()
       if len(nRet) == 0:
          return '登录失败'
       else:
          pos = nRet[0]
          #print pos
          icon_p = pos[8]
          with open(icon_p,'rb') as f:
               icon_data = base64.b64encode(f.read())
          user_p = pos[7]
          with open(user_p,'rb') as f:
               user_icon_data = base64.b64encode(f.read())
          post_data = {
            "status":"success",
            "username":str(pos[0]).strip(),
            "name":str(pos[2]).strip(),
            "ID":str(pos[3]).strip(),
            "age":str(pos[4]).strip(),
            "sex":str(pos[5]).strip(),
            "birth":str(pos[6]).strip(),
            "user_head":user_icon_data,
            "icon_head":icon_data,
            "home_addr":str(pos[9]).strip(),
            "mobphone":str(pos[10]).strip(),
            "wechat":str(pos[11]).strip()
          }
          return post_data

    def getID(self,username,password):
       cursor=self.db.cursor()
       cursor.execute('SELECT ID_N FROM userInfo WHERE username=\'{}\' and password=\'{}\';'.format(username,password))
       nRet = cursor.fetchall()
       if len(nRet) == 0:
          return 'fail'
       else:
          pos = nRet[0]
          return pos[0]

    def getID2(self,username):
       cursor=self.db.cursor()
       cursor.execute('SELECT ID_N FROM userInfo WHERE username=\'{}\''.format(username))
       nRet = cursor.fetchall()
       if len(nRet) == 0:
          return 'fail'
       else:
          pos = nRet[0]
          return pos[0]


    #通过保单号获取身份证
    def getIDByBNum(self,bnum):
       cursor=self.db.cursor()
       cursor.execute('SELECT ID_N FROM insInfo WHERE baodan_number=\'{}\''.format(bnum))
       nRet = cursor.fetchall()
       if len(nRet) == 0:
          return 'fail'
       else:
          pos = nRet[0]
          return pos[0]

    def findNameByID(self,id):
       cursor=self.db.cursor()
       cursor.execute('SELECT name FROM userInfo WHERE ID_N=\'{}\' limit 0,1;'.format(id))
       nRet = cursor.fetchone()
       if nRet is None:
          cursor.close()
          return 'fail'
       else:
          name = nRet['name']
          self.db.use_result()
          cursor.close()
          return name

    def login(self,username,password):
       cursor=self.db.cursor()
       cursor.execute('SELECT username FROM userInfo WHERE username=\'{}\' and password=\'{}\';'.format(username,password))
       nRet = cursor.fetchall()
       if len(nRet) == 0:
          return '登录失败'
       return 'success'
    def isAdmin(self,username,password):
       cursor=self.db.cursor()
       cursor.execute('exec isAdmin \'{}\',\'{}\''.format(username,password))
       nRet = cursor.fetchall()
       if len(nRet) == 0:
          return False
       else:
          pos = nRet[0]
          if 'yes' in pos[0]:
             return True
          else:
             return False

    #受理保单
    def acceptBaodan(self,bnum):
       cursor=self.db.cursor()
       cursor.execute('UPDATE lipeiInfo set accepted = 1 where baodan_number = \'{}\''.format(bnum))
       cursor.commit()
       cursor.close()

    #查询未理赔的保单
    def queryBaodan0(self,id,page):
       '''condition = self.queryLiPeiNumber(id)
       if not isinstance(condition,list):
          condition = ''
       else:
          condition = ','.join(condition)'''
       cursor=self.db.cursor()
       sql = "exec unLInsInfo {},\'{}\'".format(page,id)
       print sql
       cursor.execute(sql)
       nRet = cursor.fetchall()
       if len(nRet) == 0:
          return '没有保单信息'
       else:
          pos = nRet[0]
          return pos[1]
    #查询所有用户所有的保单
    def queryBaodanAll(self,id,page):
       cursor=self.db.cursor()
       cursor.execute('SELECT baodan FROM insInfo WHERE ID_N=\'{}\' limit {},1;'.format(id,page))
       nRet = cursor.fetchall()
       if len(nRet) == 0:
          return '没有保单信息'
       else:
          pos = nRet[0]
          #print pos
          return pos['baodan']

    #查询某个人所有保单
    def queryBaodan(self,id,page):
       cursor=self.db.cursor()
       cursor.execute('SELECT baodan FROM insInfo WHERE ID_N=\'{}\' limit {},1;'.format(id,page))
       nRet = cursor.fetchall()
       if len(nRet) == 0:
          return '没有保单信息'
       else:
          pos = nRet[0]
          #print pos
          return pos['baodan']

    def queryBaodan1(self,id,baodan_num):
       cursor=self.db.cursor()
       cursor.execute('SELECT baodan FROM insInfo WHERE ID_N=\'{}\' and baodan_number=\'{}\';'.format(id,baodan_num))
       nRet = cursor.fetchall()
       if len(nRet) == 0:
          return '没有保单信息'
       else:
          pos = nRet[0]
          return pos[0]

    def queryLiPeiInfo(self,id,page):
       cursor=self.db.cursor()
       cursor.execute('exec getlipeiInfo {},\'{}\''.format(page,id))
       nRet = cursor.fetchall()
       if len(nRet) == 0:
          return '没有保单信息'
       else:
          pos = nRet[0]
          return pos[0]
    #根据保单号查询理赔情况
    def queryLiPeiInfo2(self,bnum):
       cursor=self.db.cursor()
       cursor.execute('exec getlipeiInfo2 \'{}\''.format(bnum))
       nRet = cursor.fetchall()
       if len(nRet) == 0:
          return '没有保单信息'
       else:
          pos = nRet[0]
          return pos[0]

    #查询所有的用户
    def queryUsers(self):
       cursor=self.db.cursor()
       cursor.execute('select * from users;')
       nRet = cursor.fetchall()
       if len(nRet) == 0:
          return '没有用户信息'
       else:
          return nRet

    #判断是否是黑名单
    def isBlack0(self,username):
       cursor=self.db.cursor()
       cursor.execute('select * from blackusers WHERE username=\'{}\';'.format(username))
       nRet = cursor.fetchall()
       if len(nRet) == 0:
          return False
       else:
          return True

    #判断是否是黑名单
    def isBlack(self,ID_N):
       cursor=self.db.cursor()
       cursor.execute('select * from blackusers WHERE ID_N=\'{}\';'.format(ID_N))
       nRet = cursor.fetchall()
       if len(nRet) == 0:
          return False
       else:
          return True

    #查询黑名单
    def queryBlackList(self):
       cursor=self.db.cursor()
       cursor.execute('select * from blackusers;')
       nRet = cursor.fetchall()
       if len(nRet) == 0:
          return '没有用户信息'
       else:
          return nRet

    #返回已经理赔了的保单号
    def queryLiPeiNumber(self,id):
       cursor=self.db.cursor()
       cursor.execute('SELECT baodan_number FROM lipeiInfo WHERE ID_N=\'{}\';'.format(id))
       nRet = cursor.fetchall()
       if len(nRet) == 0:
          return '没有保单信息'
       else:
          ans = []
          for pos in nRet:
              ans.append(pos['baodan_number'])
          ans = set(ans)
          new_list = [i for i in ans]
          return new_list

    def queryBaodanNumbers(self,id):
       cursor=self.db.cursor()
       cursor.execute('SELECT baodan_number FROM insInfo WHERE ID_N=\'{}\';'.format(id))
       nRet = cursor.fetchall()
       if len(nRet) == 0:
          return '没有保单信息'
       else:
          ans = []
          for pos in nRet:
             b_num = pos[0]
             ans.append(b_num)
          cursor.execute('SELECT baodan_number FROM lipeiInfo WHERE ID_N=\'{}\';'.format(id))
          nRet = cursor.fetchall()
          if len(nRet) != 0:
             for pos in nRet:
                b_num = pos[0]
                if b_num in ans:
                   ans.remove(b_num)
             if len(nRet) == 0:
                return '没有保单信息'
          return ans
    #查询所有用户所有的保单号码
    def getAllBaodanNumbers(self):
       cursor=self.db.cursor()
       cursor.execute('SELECT baodan_number FROM insInfo')
       nRet = cursor.fetchall()
       if len(nRet) == 0:
          return '没有保单信息'
       else:
         ans = []
         for pos in nRet:
             ans.append(pos[0])
         return ans
    #查询未受理的理赔保单
    def getAllBaodanNumbersToAccept(self):
       cursor=self.db.cursor()
       cursor.execute('SELECT baodan_number FROM lipeiInfo where accepted = 0')
       nRet = cursor.fetchall()
       if len(nRet) == 0:
          return '没有保单信息'
       else:
         ans = []
         for pos in nRet:
             ans.append(pos[0])
         return ans

    #查询已受理的理赔保单
    def getAllBaodanNumbersAccepted(self):
       cursor=self.db.cursor()
       cursor.execute('SELECT baodan_number FROM lipeiInfo where accepted = 1')
       nRet = cursor.fetchall()
       if len(nRet) == 0:
          return '没有保单信息'
       else:
         ans = []
         for pos in nRet:
             ans.append(pos[0])
         return ans

    def queryAllBaodanNumbers(self,id):
       cursor=self.db.cursor()
       cursor.execute('SELECT baodan_number FROM insInfo WHERE ID_N=\'{}\';'.format(id))
       nRet = cursor.fetchall()
       if len(nRet) == 0:
          return '没有保单信息'
       else:
         ans = ''
         for pos in nRet:
             line = pos[0] + '\n'
             ans += line
         return ans


    def findBaodanNumberByHash(self,mhash):
       cursor=self.db.cursor()
       cursor.execute('SELECT baodan_number FROM insInfo WHERE bhash=\'{}\';'.format(mhash))
       nRet = cursor.fetchall()
       if len(nRet) == 0:
          return '没有保单信息'
       else:
          cursor.close()
          pos = nRet[0]
          return pos['baodan_number']

    def getBaodanHashByNumber(self,baodan_number):
       cursor=self.db.cursor()
       cursor.execute('SELECT bhash FROM insInfo WHERE baodan_number=\'{}\';'.format(baodan_number))
       nRet = cursor.fetchall()
       if len(nRet) == 0:
          return '没有保单信息'
       else:
          pos = nRet[0]
          return pos[0]