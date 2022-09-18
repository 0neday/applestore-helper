## Apple 商店助手

### 功能特性
1. 无限循环监听。异步循环监听
2. 自定义监听时间。修改脚本中的 `await asyncio.sleep(3)`
3. 钉钉机器人消息推送。
### 注意事项
需要先在手机 `Apple Store` 商店里下单，填写好个人信息（身份证后4位，姓名，手机号），支付方式。
当有钉钉提醒时，点击零售店选择取货时间。

<div align=center><img src="https://s2.loli.net/2022/09/18/MRVreyO5TvF738g.png" width="300 "></div>


### 获取零售店代码和机型代码
在 `apple` 购买选购界面，`chrome` 浏览器右键检查，切换到 `network` 选项。在选购界面按照提示勾选 `pro，promax`，存储大小等。在 `network` 下找到 `fulfillment-messages`开头的链接，切换到 `payload` 选项, 找到 `store` 和 `parts.0` ，对应替换脚本中的 `storeCode` 和 `model`。

![chrome_inspect.png](https://s2.loli.net/2022/09/18/d7rwEemWx4IRAVO.png)

### 获取钉钉机器人`accesskey`

按照官方文档，[钉钉开放平台文档，自定义机器人接入](https://open.dingtalk.com/document/robots/custom-robot-access)

替换脚本中的 `token`

### 运行
安装 [Python](https://www.python.org/downloads/) 环境。
```
python 14pro.py 
```
<img src="https://s2.loli.net/2022/09/18/yBTMvWgd8cekH7o.png" width="300 ">

### 下一步实现
全流程自动下单。

### Credits, thanks for help
[Apple Store iPhone预约助手](https://github.com/hteen/apple-store-helper) @hteen

### license MIT


### 如果觉得有用，打赏一颗糖果，谢谢！

<img src='https://s2.loli.net/2022/09/18/cdTKyJMD9mo7g4t.jpg' width='300px'/>


