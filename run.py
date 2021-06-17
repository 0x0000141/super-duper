from core import functions as modules
from argparse import ArgumentParser, FileType
import random

def main(src,dst,func,key):
    if not key:
        key = random.randint(1,200)
    content = src.read()
    out = getattr(modules,func)(content,key)
    print("[*] payload length: %s " % len(out))
    if isinstance(out,str):
        with open(dst,"w+") as file:
            file.write(out)
    elif isinstance(out,bytes):
        with open(dst,"wb+") as file:
            file.write(out)


if __name__ == '__main__':
    parser = ArgumentParser(prog="run",description="payload混淆处理 \t > Author: Dmagic Email：weedssec@gmail.com")
    parser.add_argument("-s",'--src',help="需要处理的文件",type=FileType('rb'),required=True)
    parser.add_argument('-d', '--dst', help='处理完成输出的文件名', type=str, required=True)
    parser.add_argument('-f', '--func', help='需要使用处理的func', type=str, required=True)
    parser.add_argument('-k', '--key', help='指定XOR异或混淆的Key 默认随机生成', type=int, required=False)
    args = parser.parse_args()
    main(src=args.src,dst=args.dst,func=args.func,key=args.key)
    print("[+] 处理完成")
