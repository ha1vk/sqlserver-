#coding:utf-8
import urllib2

from pyDes import des, CBC, PAD_PKCS5
import binascii
import constants


def des_encrypt(s):
    """
    DES 加密
    :param s: 原始字符串
    :return: 加密后字符串，16进制
    """
    req = urllib2.Request(
        url=constants.gk_url)
    iv = urllib2.urlopen(req).read()
    print(iv)
    k = des(iv, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s.encode('utf8'), padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)

def des_descrypt(s):
    """
    DES 解密
    :param s: 加密后的字符串，16进制
    :return:  解密后的字符串
    """
    req = urllib2.Request(
        url=constants.gk_url)
    iv = urllib2.urlopen(req).read()
    k = des(iv, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de