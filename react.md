新的管理后台打算使用react来做
这里会记录react的相关坑，当然会使用程序的框架，初步已经定为ant disgin减少设计成本

## 几个概念
 - models 从后台来看就是一个数据模型，在react也是代表这数据类型，其中定义了数据的来源，和数据的存储
 - routes 定义了数据与view绑定的关系
 - view 由于进行了各种封装，反倒是view在显示中显得不那么重要了。

通过state来获取各种数据，或许还是挺方便的。
根据state不同来选择不同的状态 直接在虚拟的dom中编写逻辑即可