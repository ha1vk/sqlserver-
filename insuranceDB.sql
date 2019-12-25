--�������ݿ�
create database insuranceDB

use insuranceDB

--����ʵ����Ϣ��
create table realInfo(
ID_N	Char(20),--���֤
name	Char(20),--����
age	Int,--����
sex	Char(5),--�Ա�
birth	date,--����
icon_head	Char(100),--���֤��Ƭ
home_addr	Char(50),--��ͥ��ַ
primary key(ID_N)
)

--�����û���Ϣ��
create table userInfo(
username	Char(20),--�û���
ID_N	Char(20),--���֤
password	Char(64),--����
user_head	Char(100),--ͷ��
mobphone	Char(20),--�ֻ���
wechat	Char(20),--΢��
mibao_q1	Char(100),--�ܱ�����1
mibao_a1	Char(100),--�ܱ���1
mibao_q2	Char(100),--�ܱ�����2
mibao_a2	Char(100),--�ܱ���2
primary key(username),
foreign key(ID_N) references realInfo
)

--����������Ϣ��
create table insInfo(
baodan_number	Char(20),--������
ID_N	Char(20),--���֤
baodan	image,--�����ı�������
bhash	Char(64),--������hashֵ(����У�鱣���Ƿ���Ϊ�޸�)
primary key(baodan_number),
foreign key(ID_N) references realInfo
)

--��������Ա��Ϣ��
create table mgrInfo(
mgrname	Char(20),--�û���
password	Char(64),--����
primary key(mgrname)
)

--����������Ϣ��
create table lipeiInfo(
ID_N	Char(20),--���֤
baodan_number	Char(20),--������
lipei	Image,--������������Ϣ������
accepted	Bit,--�Ƿ�������
primary key(baodan_number),
foreign key(baodan_number) references insInfo,
foreign key(ID_N) references realInfo
)

--������������Ϣ��
create table blackInfo(
username	Char(20), --�û���
primary key(username),
foreign key(username) references userInfo
)

--��ǰ���ü�������Ա������123456
--ʹ��md5�洢���룬��ǿ��ȫ��
insert into mgrInfo values('sea','e10adc3949ba59abbe56e057f20f883e')
insert into mgrInfo values('hai','e10adc3949ba59abbe56e057f20f883e')
insert into mgrInfo values('root','e10adc3949ba59abbe56e057f20f883e')

go
--������ѯ�û���Ϣ����ͼ
create view users as
select username,name,userInfo.ID_N
from userInfo,realInfo 
where userInfo.ID_N = realInfo.ID_N
go
--��ѯ�û���Ϣ
select * from users

--������ѯ�������û���Ϣ����ͼ
create view blackusers as
--����ͼ���ٵ�����ͼ^_^
select users.username,name,ID_N from users,blackInfo
where users.username = blackInfo.username
go

--��ѯ�������û�
select * from blackusers

--������ѯ�û�������Ϣ����ͼ
create view users_full_info as
select username,password,name,userInfo.ID_N,age,sex,birth,user_head,icon_head,home_addr,mobphone,wechat
from userInfo,realInfo 
where userInfo.ID_N = realInfo.ID_N
go

--��ѯ�û���������Ϣ
select * from users_full_info

--drop procedure registerUser
--��������ע���û���Ϣ�Ĵ洢����
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
RAISERROR('�����û����Ѿ�����',16,1)
end
else
begin
--ע�����˳�������������Լ��������˳�����Ҫ
--��ʵ����Ϣ�������Ϣ
insert into realInfo values(@ID_N,@name,@age,@sex,@birth,@icon_head,@home_addr)
--�������Ϣ�������Ϣ
insert into userInfo values(@username,@ID_N,@password,@user_head,@mobphone,@wechat,@mibao_q1,@mibao_a1,@mibao_q2,@mibao_a2)
end
end
go

--delete from userInfo
--delete from realInfo

--����ע��Ĵ洢����
exec registerUser 'root','e10adc3949ba59abbe56e057f20f883e','zhaohai','510623200002278308','20','��','2000/1/1','icons/510623200002278318_user.jpg','icons/510623200002278318_id.jpg','11','111','11','11','b292994bd34cfa75ae5cecf221389de4','a71f2864552a30b2','dc1131e265da80a078b6f8561c64010d6df68f857cc7c700','8f7d25a6e27c96ec'

--������ѯδ����ı����Ĵ洢����
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

--������ѯ����Ĵ洢����
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
--���ݱ����Ų�ѯ�������
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

--���������û�������ȡ���б����ŵ���ͼ
create view getbaodan_num_by_username as
select username,password,name,userInfo.ID_N,age,sex,birth,user_head,icon_head,home_addr,mobphone,wechat
from userInfo,realInfo 
where userInfo.ID_N = realInfo.ID_N
go

--INSERT INTO blackInfo (username) VALUES ('aa')

select * from users_full_info

--�����洢���̣����ڼ����Ƿ��ǹ���Ա
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


--�����Ƿ��ǹ���Ա
exec isAdmin 'root','e10adc3949ba59abbe56e057f20f883e'

--��ѯδ����ı�����
SELECT baodan_number FROM lipeiInfo where accepted = 0

--�����洢���̣����ڸ����û���Ϣ
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

