# super-duper

## 简介

项目地址：https://github.com/magisec/super-duper

使用混淆与加密规避查杀，基于Python3开发，无任何依赖。

## 混淆函数

可用混淆函数列表：

- Confuse_uuid 使用uuid加密
- Confuse_xor_str 对str进行xor混淆
- Confuse_xor_file 对byte进行xor混淆
- Confuse_gzip_xor 使用gzip压缩数据 > Xor异或混淆 适用于体积较大的工具，效果相当不错。
- Confuse_uuid_xor_gzip_hex 使用uuid加密 > xor异或 > gzip压缩 > hex 进行混淆，效果很好，付出代价同样大，更适用于小体积的shellcode。

## 使用帮助

查看帮助

```
python confuse_tools.py --help
```

![image-20210530191719614](https://gitee.com/magisec/images/raw/master/image-20210530194450066.png)

调用Confuse_gzip_xor对mimikatz进行混淆

```
python confuse_tools.py -s mimi.txt -d mimi.raw -f Confuse_gzip_xor
```

![image-20210530193157125](https://gitee.com/magisec/images/raw/master/image-20210530193157125.png)

我们可以获取到随机生成的xor_key。这个key，请自行解密。
## 2021.5.31更新
支持自定义密钥，默认随机生成。
```
python confuse_tools.py -s mimi.txt -d mimi.raw -f Confuse_gzip_xor -k 70
```

### vt查杀

mimi.txt（混淆前）

![image-20210530193400861](https://gitee.com/magisec/images/raw/master/image-20210530193400861.png)

mimi.raw （混淆后）

![image-20210530193431499](https://gitee.com/magisec/images/raw/master/image-20210530193431499.png)

