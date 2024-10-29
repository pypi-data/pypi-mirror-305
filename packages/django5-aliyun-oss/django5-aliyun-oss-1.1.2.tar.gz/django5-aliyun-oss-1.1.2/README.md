# Django 5 阿里云 OSS 存储

用于阿里云 OSS（对象存储服务）的 Django 存储后端。

## 安装

```bash
pip install django5-aliyun-oss
```

## 配置
在您的 Django settings.py INSTALLED_APPS 中添加以下设置：

```python
INSTALLED_APPS = [
    ...
    'django5_aliyun_oss',
    ...
]
```


在您的 Django settings.py 中添加以下设置：

```python
ALIYUN_OSS = {
    'ACCESS_KEY_ID': '您的访问密钥ID',
    'ACCESS_KEY_SECRET': '您的访问密钥密码',
    'ENDPOINT': '您的终端节点',
    'BUCKET_NAME': '您的存储桶名称',
    'URL_EXPIRE_SECONDS': 3600,  # 可选，默认为3600
}

# 设置为默认存储器
STORAGES = {
    'default': {
        'BACKEND': 'django5_aliyun_oss.storage.AliyunOSSStorage',
    },
    'staticfiles': {
        'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage',
    }
}
```

## 使用

```python
from django.db import models

class YourModel(models.Model):
    file = models.FileField(upload_to='uploads/')
    image = models.ImageField(upload_to='images/')
```

## 特性

- 兼容 Django 5.0+
- 支持所有基本文件操作
- 处理文件删除
- 返回的URL是带签名的URL
- 可配置的上传路径
- 支持静态文件存储

## 许可证

MIT 许可证

## 贡献

欢迎贡献！请随时提交拉取请求。