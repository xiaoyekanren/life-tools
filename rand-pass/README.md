
## generate_password.py
生成密码

### 使用方式
```shell
generate_password.py [para1] [para2]
# 可选参数1: 密码长度， 7~ +∞
# 可选参数2: 取3或4，取3密码不包含字符，默认取4
```
### 生成exe
```shell
pyinstaller -F generate_password.py -i img\vip.ico
```