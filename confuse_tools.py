from core import functions as modules
from argparse import ArgumentParser, FileType
import random

def main(src,dst,func):
    key = random.randint(1,200)
    content = src.read()
    out = getattr(modules,func)(content,key)
    if isinstance(out,str):
        with open(dst,"w+") as file:
            file.write(out)
    elif isinstance(out,bytes):
        with open(dst,"wb+") as file:
            file.write(out)
    print("[*] xor key: %s" % key)

if __name__ == '__main__':
    parser = ArgumentParser(prog="confuse tools",description="payload混淆规避 \t > Author: 想念烟雨 Email：weedssec@gmail.com")
    parser.add_argument("-s",'--src',help="需要混淆的文件",type=FileType('rb'),required=True)
    parser.add_argument('-d', '--dst', help='混淆完成输出的文件名', type=str, required=True)
    parser.add_argument('-f', '--func', help='需要使用混淆的func', type=str, required=True)
    args = parser.parse_args()
    main(src=args.src,dst=args.dst,func=args.func)
    print("[+] 混淆完成")
