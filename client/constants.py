import urllib2

#domain = 'zhaohai.oicp.io'
#port = 56690
domain = "127.0.0.1"
port = "5000"

host = 'http://{}:{}'.format(domain,port)
gk_url = host + '/gk'
upload_url = host + '/upload'
login_url = host + '/login'
regacc_url = host + '/regacc'
updateacc_url = host + '/updateAcc'
updatepass0_url = host + '/updatePass0'
updatepass1_url = host + '/updatePass1'
mine_url = host + '/mine'
get_info_url = host + '/getInfo'
getInsForm_url = host + '/getInsForm'
showInsForm = host + '/showInsForm'
loadShowInsForm = host + '/loadingHtml?html=showInsForm'
loginout_url = host + '/loginout'
view_all_baodan_url = host + '/view_all_baodan'
baodan_to_acc_url = host + '/view_baodan_to_accept'
user_url = host + '/view_users'
black_url = host + '/view_blacks'
lipei_url = host + '/insLiPei'
lipei_his_url = host + '/view_baodan_accepted'
lipei_his_2_url = host + '/loadingHtml?html=showLiPeiHis'

def loginout(opener):
    req = urllib2.Request(
        url=loginout_url)
    ans = opener.open(req).read()
    print 'loginout:' + ans

def judge_pure_english(keyword):
    return all(ord(c) < 128 for c in keyword)


def judge_pure_digit(keyword):
    return all((ord(c) >= ord('0') and ord(c) <= ord('9')) for c in keyword)


def judge_id(id_n):
    a = (len(id_n) == 18)
    b = True
    for c in id_n:
        o = ord(c)
        if not ((o >= ord('0') and o <= ord('9')) or c == 'x' or c == 'X'):
            b = False
            break
    return a and b
