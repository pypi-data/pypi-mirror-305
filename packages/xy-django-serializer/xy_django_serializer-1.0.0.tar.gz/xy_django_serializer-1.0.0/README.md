<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:23
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:51:38
 * @FilePath: /xy_django_serializer/README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_django_serializer

- [简体中文](readme/README_zh_CN.md)
- [繁体中文](readme/README_zh_TW.md)
- [English](readme/README_en.md)

## 说明

基于djangorestframework的serializer解析基类, 封装了常用功能, 方便快速开发.

## 源码仓库

- <a href="https://github.com/xy-web-service/xy_django_serializer.git" target="_blank">Github地址</a>  
- <a href="https://gitee.com/xy-web-service/xy_django_serializer.git" target="_blank">Gitee地址</a>

## 安装

```bash
# bash
pip install xy_django_serializer
```

## 使用

#### 1. 创建解析类
```python
# serializers.py

from rest_framework import viewsets
from xy_django_serializer.serializers import Serializer

from .models import MImage


class SImage(Serializer):
    default_value = ""

    class Meta:
        model = MImage
        fields = "__all__"

class VSImage(viewsets.ModelViewSet):
    queryset = MImage.objects.all()
    serializer_class = SImage

```
#### 2. 实现解析

###### 1. 在Django项目的manage.py shell中调用

```python
# Python解释器
from Demo.models import MDemo
from Demo.serializers import SDemo

demo_list = MDemo.objects.all()
demo_dict_list = SDemo(demo_list, many=True).data
print(demo_list)
print(demo_dict_list))
```

###### 2. 在Tornado等其他运行环境中调用

> <b>注意:</b> 必须先加载Django工程到运行的项目中

```Python
# Demoes.py
from xy_request_handler_api.Api import Api
from Demo.models import MDemo
from Demo.serializers import SDemo

class DemoApi(Api):
    def check_xsrf_cookie(self) -> None:
        return None

    def check_origin(self, _):
        return False

    def fetch(self):
        all_demo_list = MDemo.objects.all()
        all_demo_dict_list = SDemo(all_demo_list, many=True).data
        self.success()
        self.data = {"all_demo_list": all_demo_dict_list}
        self.xy_response()

    def get(self):
        self.fetch()

    def post(self):
        self.fetch()

```

##### 运行 [样例工程](./samples/xy_web_server_demo)

> 样例工程具体使用方式请移步 <b style="color: blue">xy_web_server.git</b> 下列仓库
> - <a href="https://github.com/xy-web-service/xy_web_server.git" target="_blank">Github地址</a>  
> - <a href="https://gitee.com/xy-web-service/xy_web_server.git" target="_blank">Gitee地址</a>


## 许可证
xy_django_serializer 根据 <木兰宽松许可证, 第2版> 获得许可。有关详细信息，请参阅 [LICENSE](LICENSE) 文件。

## 捐赠
如果小伙伴们觉得这些工具还不错的话，能否请咱喝一杯咖啡呢?  

![Pay-Total](./readme/Pay-Total.png)


## 联系方式

```
微信: yuyangiit
邮箱: yuyangit.0515@qq.com
```