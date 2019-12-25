--创建数据库
create database insuranceDB

use insuranceDB

--创建实名信息表
create table realInfo(
ID_N	Char(20),--身份证
name	Char(20),--姓名
age	Int,--年龄
sex	Char(5),--性别
birth	date,--生日
icon_head	Char(100),--身份证照片
home_addr	Char(50),--家庭地址
primary key(ID_N)
)

--创建用户信息表
create table userInfo(
username	Char(20),--用户名
ID_N	Char(20),--身份证
password	Char(64),--密码
user_head	Char(100),--头像
mobphone	Char(20),--手机号
wechat	Char(20),--微信
mibao_q1	Char(100),--密保问题1
mibao_a1	Char(100),--密保答案1
mibao_q2	Char(100),--密保问题2
mibao_a2	Char(100),--密保答案2
primary key(username),
foreign key(ID_N) references realInfo
)

--创建保单信息表
create table insInfo(
baodan_number	Char(20),--保单号
ID_N	Char(20),--身份证
baodan	image,--完整的保单数据
bhash	Char(64),--保单的hash值(用于校验保单是否被人为修改)
primary key(baodan_number),
foreign key(ID_N) references realInfo
)

--创建管理员信息表
create table mgrInfo(
mgrname	Char(20),--用户名
password	Char(64),--密码
primary key(mgrname)
)

--创建理赔信息表
create table lipeiInfo(
ID_N	Char(20),--身份证
baodan_number	Char(20),--保单号
lipei	Image,--完整的理赔信息表数据
accepted	Bit,--是否已受理
primary key(baodan_number),
foreign key(baodan_number) references insInfo,
foreign key(ID_N) references realInfo
)

--创建黑名单信息表
create table blackInfo(
username	Char(20), --用户名
primary key(username),
foreign key(username) references userInfo
)

--提前设置几个管理员，密码123456
--使用md5存储密码，加强安全性
insert into mgrInfo values('sea','e10adc3949ba59abbe56e057f20f883e')
insert into mgrInfo values('hai','e10adc3949ba59abbe56e057f20f883e')
insert into mgrInfo values('root','e10adc3949ba59abbe56e057f20f883e')

go
--创建查询用户信息的视图
create view users as
select username,name,userInfo.ID_N
from userInfo,realInfo 
where userInfo.ID_N = realInfo.ID_N
go
--查询用户信息
select * from users

--创建查询黑名单用户信息的视图
create view blackusers as
--在视图中再调用视图^_^
select users.username,name,ID_N from users,blackInfo
where users.username = blackInfo.username
go

--查询黑名单用户
select * from blackusers

--创建查询用户完整信息的视图
create view users_full_info as
select username,password,name,userInfo.ID_N,age,sex,birth,user_head,icon_head,home_addr,mobphone,wechat
from userInfo,realInfo 
where userInfo.ID_N = realInfo.ID_N
go

--查询用户完整的信息
select * from users_full_info

--drop procedure registerUser
--创建用于注册用户信息的存储过程
create procedure registerUser
@username CHAR(20),
@password CHAR(64),
@name CHAR(20),
@ID_N CHAR(20),
@age INT,
@sex CHAR(5),
@birth date,
@user_head CHAR(100),
@icon_head CHAR(100),
@home_addr CHAR(50),
@home_phone CHAR(20),
@mobphone CHAR(20),
@wechat CHAR(20),
@mibao_q1 CHAR(100),
@mibao_a1 CHAR(100),
@mibao_q2 CHAR(100),
@mibao_a2 CHAR(100)
as
begin
if Exists(select username from userInfo where username = @username)
begin
RAISERROR('错误，用户名已经存在',16,1)
end
else
begin
--注意插入顺序，由于主外键的约数，插入顺序很重要
--向实名信息表插入信息
insert into realInfo values(@ID_N,@name,@age,@sex,@birth,@icon_head,@home_addr)
--向基本信息表插入信息
insert into userInfo values(@username,@ID_N,@password,@user_head,@mobphone,@wechat,@mibao_q1,@mibao_a1,@mibao_q2,@mibao_a2)
end
end
go

--delete from userInfo
--delete from realInfo

--测试注册的存储过程
exec registerUser 'root','e10adc3949ba59abbe56e057f20f883e','zhaohai','510623200002278308','20','男','2000/1/1','icons/510623200002278318_user.jpg','icons/510623200002278318_id.jpg','11','111','11','11','b292994bd34cfa75ae5cecf221389de4','a71f2864552a30b2','dc1131e265da80a078b6f8561c64010d6df68f857cc7c700','8f7d25a6e27c96ec'

--创建查询未理赔的保单的存储过程
create procedure unLInsInfo
@limit int,
@ID_N CHAR(20)
as
begin
SELECT TOP 2 baodan_number,baodan 
FROM insInfo 
WHERE ID_N=@ID_N and baodan_number not in (SELECT baodan_number FROM lipeiInfo WHERE ID_N = @ID_N) and baodan_number not in (
select top (@limit) baodan_number from insInfo WHERE ID_N=@ID_N and baodan_number not in (SELECT baodan_number FROM lipeiInfo WHERE ID_N = @ID_N))
end
go

--drop procedure unLInsInfo

--创建查询理赔的存储过程
create procedure getlipeiInfo
@limit int,
@ID_N CHAR(20)
as
begin
SELECT TOP 2 baodan_number,lipei
FROM lipeiInfo 
WHERE ID_N=@ID_N and baodan_number not in (
select top (@limit) baodan_number from lipeiInfo)
end
go
--根据保单号查询理赔情况
create procedure getlipeiInfo2
@baodan_number CHAR(20)
as
begin
select lipei
from lipeiInfo
where baodan_number = @baodan_number
end
go

--drop procedure getlipeiInfo
exec unLInsInfo 0,'510623200002278318  '

exec unLInsInfo 1,'510623200002278318  '

exec getlipeiInfo 0,'510623200002278318'

--delete from lipeiInfo
--delete from insInfo

--创建根据用户名，获取所有保单号的视图
create view getbaodan_num_by_username as
select username,password,name,userInfo.ID_N,age,sex,birth,user_head,icon_head,home_addr,mobphone,wechat
from userInfo,realInfo 
where userInfo.ID_N = realInfo.ID_N
go

--INSERT INTO blackInfo (username) VALUES ('aa')

select * from users_full_info

--创建存储过程，用于检验是否是管理员
create procedure isAdmin
@username CHAR(20),
@password CHAR(64)
as
begin
if Exists(select * from mgrInfo where mgrname = @username and password = @password)
select 'yes'
else
select 'no'
end
go


--测试是否是管理员
exec isAdmin 'root','e10adc3949ba59abbe56e057f20f883e'

--查询未理赔的保单号
SELECT baodan_number FROM lipeiInfo where accepted = 0

--创建存储过程，用于更新用户信息
create procedure updateAcc
@username CHAR(20),
@password CHAR(64),
@wechat CHAR(20),
@sex CHAR(5),
@age int,
@birth date,
@home_addr CHAR(50)
as
begin
UPDATE userInfo set wechat = @wechat where username = @username and password = @password
UPDATE realInfo set sex = @sex,age = @age,birth = @birth,home_addr = @home_addr
end
go

