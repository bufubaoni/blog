# jupyter 
## install
 - pip install jupyter
## run
 - jupyter notebook
会自动为你打开一个网页，使用token访问
## config
如果需要设置那么需要 

 - jupyter notebook --generate-config

生成配置文件

针对自定义配置其实可以配置到 
 - ~/.jupyter/jupyter_notebook_config.json
其中配置和json格式相同，运行配置password之后就会出现此文件，当然可以自己生成。
## 添加新的notebook
按照以上方法那么安装的只有一个notebook，就是python2的运行环境，(如果默认pip为pip3那么就只有一个python3的notebook)
如果需要添加3的运行环境按照以下步骤
1.  python3 安装jupyter `pip3 install jupyter`
2.  启用python3的kernel `ipython3 kernelspec install-self`
3.  打开jupyter的主页，然后即可看到拥有 python3 的notebook类型
---
设置
jupyter notebook --generate-config 生成配置文件
jupyter notebook --ip=0.0.0.0 --no-browser --allow-root
---
注：
如果本机有两个jupyter 那么两个会互相影响，如果当前的起不来那么
使用 `lsof -i tcp:8888`(查看当前占用端口的进程)来查看进程，然后`kill -9 <pid>`关闭此进程即可