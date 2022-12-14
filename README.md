# FJNU-ics

**福建师范大学课表自动生成工具，可显示上课地点，教师名称等信息，支持一键导入，兼容各种日历APP**

- 如果你是重庆邮电大学学生，请访问 [CQUPT-ics](https://github.com/qwqVictor/CQUPT-ics) 项目，可自动生成学生课表。

- 如果你不是上述两所大学的学生，请访问 [python-ical-timetable](https://github.com/junyilou/python-ical-timetable) 项目，可手动生成学生课表。也可参照下文来编写您的自定义接口。

![](/doc/images/preview.png)

# 功能

- 为你的课表生成跨平台可通用的`.ics`日历文件。可一键导入手机，平板电脑，笔记本电脑等移动设备，便于随时随地进行查看。

- 仅需提供课表查询页面链接即可生成，方便快捷。


# 使用

## 准备工作

- 本代码需使用 **Python 3** 运行，建议 Python 版本在 3.7 以上。
- 本代码使用了`browsercookie`读取浏览器的Cookies数据，请确保您的浏览器在其支持范围以内(推荐Google Chrome，Edge，Firefox等主流浏览器)

关于 Python 3 的具体配置方法请见[教程](/doc/python_configuration.md)

## 生成ics文件

1. 在项目目录中运行`pip install -r requirements.txt`

2. 在浏览器（建议使用 Chrome 等主流浏览器）中登录[FJNU教务系统](https://jwglxt.fjnu.edu.cn/jwglxt/xtgl/login_slogin.html)并打开课表查询页面，复制课表查询页面的链接

3. 在项目目录中运行`python main.py`

4. 在`Link`行粘贴刚刚复制的链接并回车

5. 在`Year`行输入要查询的学年(例如`2022-2023`则输入`2022`)并回车

6. 在`Semester`行输入要查询的学期(`1`、`2`或`3`)并回车

7. 此时目录中将会生成`output.ics`，该文件即为生成的ics文件

## 导入日历

### 微软日历

单击生成的`output.ics`，选择最上方「添加到日历」即可

### Android 手机日历

用QQ，微信等常用聊天软件将 ics 文件传至 Android 设备，之后在「打开方式」中选择「日历」，根据系统提示导入即可

### iOS 日历

iOS 日历导入方式较为繁琐，本人曾使用两种方式成功导入，供参考。

#### 方法1：使用NodeJS

1. 安装 [NodeJS](https://nodejs.org)

2. 在任一目录下运行`npm install http-server --global`

3. 在`output.ics`文件所在目录运行`http-server`

4. 使用Safari浏览器打开终端中显示的网址，通常形式为`http://*.*.*.*:*`，其中`*`为通配符

5. 在页面中找到`.ics`文件，点击打开，并根据系统提示导入日历

#### 方法2：使用文件传输网址

以[奶牛快传](https://cowtransfer.com/)为例。

1. 将 ics 文件传至奶牛快传。

2. 此时奶牛快传将会给出文件链接和提取码，点击「Copy both」进行复制，并通过QQ，微信等社交软件传至 iOS 设备。

3. 将文件链接复制到 Safari 浏览器中，输入提取码，点击「下载」。

4. 此时系统会自动弹出日程，单击右上角「添加全部」。

5. **这点十分重要！！！** 请点击右下角「添加日历」，输入日历名称并选中，之后点击「完成」。

**不要**直接点击完成，否则万一出错删除会非常麻烦。


# 其他问题

## 关于仓山校区

~~由于制作人之一为旗山校区学生，故代码中课程时间均采用旗山校区作息时间。~~

~~若你来自仓山校区，请将`main.py`中的`class time`替换为以下内容~~

```python
class_time = [None, (8, 00), (8, 55), (10, 00), (10, 55), (14, 0), (14, 55), 
	(15, 50), (16, 45), (18, 30), (19, 25), (20, 20), (21, 15)]
```

Update: 开发者在课表后端返回数据中发现了指示校区的部分，现已实现根据校区的不同自动调整时间

## 关于不同学期

本项目于 2022 年 9 月 26 日上传，故默认适配学期为 2022-2023 上半学期。

若想要在其他学期使用，请打开`main.py`，将`current_time`一行中最后的数字改为当前学期第一周周一的日期，格式为`(年, 月, 日)`

## 关于其他学校

见[自定义接口](/doc/custom_interface.md)

# 隐私政策与保护

程序运行过程中，需要收集您在`jwglxt.fjnu.edu.cn`域下的cookies以模拟用户登录并获取请求结果  
我们保证您的cookies只会用于ics文件的生成  
我们只保证本repo中的文件遵守上述规则，若您得到的文件并非与本repo完全一致，则需您自行承担可能的风险与后果  
使用此程序即代表您了解并同意以上条件  



# 联系我们

- 直接提交issue
- telegram：[@MoveToEx](https://t.me/MoveToEx)，[@Album.](https://t.me/album921)



