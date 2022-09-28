# 自定义课表接口

本程序允许您自行编写接口，以便适配其他学校的课表

要自定义接口，您需要实现一个类，其结构如下：  

```py
class CustomApi:
    def requirements():
        # ...

    def fetch(args):
        # ...
```

类中的函数均应为`static`函数

## `CustomApi`

### `requirements`

参数：无  
返回：`list[str]`

该函数返回所有需要向用户读取的数据的键，在稍后的`fetch`函数中，用户的输入会与这里的键对应  

例如：  

```py
def requirements():
    return ['link', 'year']
```

### `fetch`

参数：`dict`(见上)  
返回：`list[dict]`(见下)

该函数用于获取并解析数据，返回值中的每一项都应具有以下键值：

| Key | Type | Descr. |
| :-: | :-: | :-: |
| `name` | `str` | 课程名称 |
| `teacher` | `str` | 教师姓名 |
| `location` | `str` | 上课地点 |
| `weeks` | `list[int]` | 需要上这一门课的所有周，每一周对应一个元素 |
| `weekday_order` | `int` | 这一门课位于周几 |
| `class_order` | `int` | 第几节课 |
| `time` | `dict` | 上课时间，见下 |
| `time['from']` | `tuple[int, int]` | 课程起始时间，\[0\]为小时，\[1\]为分钟 |
| `time['to']` | `tuple[int, int]` | 课程结束时间，\[0\]为小时，\[1\]为分钟 |

## 修改程序

要使`main.py`调用您自行编写的接口，只需在其中引用您的`.py`文件并将其中的`fjnu_api.FJNUApi`替换为您的接口的类名即可