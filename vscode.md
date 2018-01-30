# 使用vscode

## pycharm
个人更多的是使用pycharm，当然对于一个穷人来说正版还是挺贵的，所以就一直修改系统时间来获得长时间的试用，当然现在这个路子不灵了。

## 替代品vim
很早之前和在服务器之间使用的就是vim，当然配置文件还是用雨神的配置文件，普通编辑修改一下绰绰有余，但是编辑项目稍微上一点规模个人就有点吃力了，当然linux下有不错的gui也可以使用pycharm。最后还是投靠了 vscode的怀抱。

## 插件安装
插件安装非常简单，当然配置好之后使用git 的gist同步配置还是非常方便的。
个人使用习惯不同可能配置起来不太一样。

## 使用体验
已经使用vscode 开发了一整个项目了，目前没有任何不适应，只是format 的时候遇到了一点麻烦，而且pep8有设置的问题，当然现在 结合flak8之后，无论是提示还是自动的格式化都很方便。

## 最重要的插件配置
由于使用了 sync 同步settings 所以基本上也没什么好记住什么需要特别的配置。只是如果auth不可以的时候，应该查看是否有权限访问gist，由于设置了读取为public，但是上传插件的时候，就会出现插件地址不同的地方。
```
windows 下设置token
%APPDATA%\Code\User\syncLocalSettings.json.
mac下设置token
Mac, $HOME/Library/Application Support/Code/User/syncLocalSettings.json.
linux 下设置token
~/.config/Code/User/settings.json. 
```
除此意外也就没什么需要注意的了。gist 在git 上需要代理才可以上去。