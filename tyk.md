# tyk
安装了一天的 tyk 终于到一个阶段了，
现在可以 为其添加一个api ，但是没有对api进行权限和 rate limiting 之类的控制
需要安装 redis，mongodb，tyk-gateway, tyk-dashboard

tyk 的操作方式比较奇怪，每一个需要为其分配权限，而不是添加插件进行控制。