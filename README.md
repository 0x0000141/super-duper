# super-duper

## 简介

项目地址：https://github.com/magisec/super-duper

使用混淆与加密规避查杀，基于Python3开发，无任何依赖。

## 可用函数

可用混淆函数列表：

- c_ud uuid编码
- c_gp gzip压缩
- c_b4 base64编码
- c_xs str异或
- c_xb byte异或
- c_r 反转
- c_h hex编码
- from_data 格式化payload

## 使用帮助

查看帮助

```
python3 run.py --help
```

![image-20210617210956069](https://gitee.com/magisec/images/raw/master/image-20210617210956069.png)



## 使用方法

使用gzip压缩

```
python3 run.py -s mimi.raw -d gzip_mimi.raw -f c_gp
```

![image-20210617211052589](https://gitee.com/magisec/images/raw/master/image-20210617211052589.png)

使用base64编码

```
python3 run.py -s mimi.raw -d base64_mimi.raw -f c_b4
```

![image-20210617211217838](https://gitee.com/magisec/images/raw/master/image-20210617211217838.png)

### vt查杀

mimi.txt（混淆前）

![image-20210530193400861](https://gitee.com/magisec/images/raw/master/image-20210530193400861.png)

mimi.raw （混淆后）

![image-20210530193431499](https://gitee.com/magisec/images/raw/master/image-20210530193431499.png)
