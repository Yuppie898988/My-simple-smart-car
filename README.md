# 基于语音控制的室外多场景导航车
这款导航车可以根据使用者发出的语音指令获得目标地址，并向目标地址导航、快递或闪送等服务，并且具有成本低廉，导航精确，操控便捷的优点。具体实现功能如下：
1.   通过语音识别和关键词提取处理，将使用者对多功能导航车发出的语音指令进行信息处理；
2.   通过GPS模块获取起始地址经纬度，并且在线获取目标地址经纬度，然后规划合适的行进路线；
3.   通过L298N驱动模块对多功能导航车进行控制，使其按照规划的路线行进。

# 技术架构
* 基于华为云一句话识别与定制语音合成实现语音交互
* 利用Python结合正则表达式对用户指令进行信息提取
* 通过ATGM332D定位模块与高德地图API实现实时地址经纬度获取，路线规划

# 环境依赖
本项目代码在树梅派4B官方系统Raspberry Pi OS上运行，需提前安装以下库：
* re
* os
* csv
* time
* json
* serial
* gpiozero
* requests
* 华为云语音交互服务的python SDK
  * 此SDK需要用到setuptools，requests与websocket-client库
  * SDK下载链接为：https://sis-sdk-repository.obs.cn-north-1.myhuaweicloud.com/python/huaweicloud-python-sdk-sis-1.3.0.tar.gz

# 自定义目的地
若地点偏僻无法在线搜索目的地，可导入目的地数据集（csv格式，第一列为目的地名称，第二列为经度，第三列为维度）

如：8单元，117.237657,39.174227

导航时只需说出：“我要去8单元“即可

若选择导入数据集模式需要将path_planning.py中的第32行search(des_name)改为为offline(des_name)
