#coding:utf-8
from pyDes import des, CBC, PAD_PKCS5
import binascii
import constants


def des_encrypt(s):
    """
    DES 加密
    :param s: 原始字符串
    :return: 加密后字符串，16进制
    """
    iv = constants.gk
    k = des(iv, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return en

def des_descrypt(s):
    """
    DES 解密
    :param s: 加密后的字符串，16进制
    :return:  解密后的字符串
    """
    iv = constants.gk
    k = des(iv, CBC, iv, pad=None, padmode=PAD_PKCS5)
    #print binascii.b2a_hex(s)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    print de
    return de
