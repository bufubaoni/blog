# linux 服务器制作ssh登陆证书
## 一般过程
在服务器查看
```bash
/etc/ssh/sshd_config # centos系统存放设置
AuthorizedKeysFile	.ssh/authorized_keys # 存放公钥文件
# 然后将自己的.ssh/id_rsa.pub文件内容写入 .ssh/authorized_keys 如果有多用户就添加多行
# 最后使用 ssh username@xxx.xxx.xxx.xxx 登陆服务器
```
可以配置多用户登陆

## 阿里云处理过程
在控制台中生成密钥对，阿里云会将私钥 以 xxx.pem 形式下载到本地（只能下载一次）
然后在控制台中重启服务器（在terminal中重启无效），
阿里云会将公钥写入 服务器 .ssh/authorized_keys 文件

虽然这样方便了key文件传播，但是缺增加了追溯的难度