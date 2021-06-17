import base64
import binascii
import gzip
from uuid import UUID

'''
c_ud uuid编码
c_gp gzip压缩
c_b4 base64编码
c_xs str异或
c_xb byte异或
c_r 反转
c_h hex编码
from_data 格式化payload
'''


def c_ud(content, *args):#uuid编码
    print("[*] 正在使用uuid进行编码")
    offset = 0
    out = ""
    while (offset < len(content)):
        countOfBytesToConvert = len(content[offset:])
        if countOfBytesToConvert < 16:
            ZerosToAdd = 16 - countOfBytesToConvert
            byteString = content[offset:] + (b'\x00' * ZerosToAdd)
            uuid = UUID(bytes_le=byteString)
        else:
            byteString = content[offset:offset + 16]
            uuid = UUID(bytes_le=byteString)
        offset += 16
        out += "{}".format(uuid)
    return out


def c_gp(content, *args):#gzip压缩
    print("[*] 正在使用gzip进行压缩")
    out = gzip.compress(content)
    return out


def c_b4(content, *args):#base64
    print("[*] 正在使用base64编码")
    out = base64.b64encode(content)
    return out


def c_xs(content, key, *args):#str异或
    print("[*] 正在使用XOR异或编码函数(str)")
    print("[*] xor key: %s" % key)
    out = ""
    for i in content:
        out += chr(ord(i) ^ key)
    return out


def c_xb(content, key, *args):#byte异或
    print("[*] 正在使用XOR异或编码函数(byte)")
    print("[*] xor key: %s" % key)
    out = b""
    for i in content:
        i = hex(i ^ key).replace("0x", "")
        if len(i) < 2:
            i = "0" + i
        out += bytes.fromhex(i)
    return out


def c_h(data, *args):#hex编码
    print("[*] 正在使用hex编码函数")
    out = binascii.b2a_hex(data)
    return out


def c_r(content, *args):#反转混淆
    print("[*] 正在使用反转混淆函数")
    out = content[::-1]
    return out


def from_data(content, *args):#格式化payload
    print("[*] 辅助函数：正在格式化文件中.......")
    out = ""
    for i in content:
        i = hex(i).replace("0x", "")
        if len(i) < 2:
            i = "0" + i
        out += "\\x" + i
    return out
