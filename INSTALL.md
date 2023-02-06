## 前端安装

**本项目前后端不分离，前端模板文件存放于每个app的templates目录下，静态文件存放于每个app的static目录下**

## 后端安装

**1.创建Mysql数据库：**

需创建login用户，login数据库，并设置login用户的启动密码

创建完成密码后，在settings.py文件修改DB的配置信息

创建login用户

```sql
CREATE USER 'login'@'localhost' IDENTIFIED BY 'your_password';
```

创建login数据库

```sql
create database login
```

授予login用户login数据库的权限

```sql
GRANT all privileges ON login.* TO 'login'@'localhost';
```

**2.导入sql文件：**

通过Django自动导入model层的表数据

**3.mange.py文件夹cmd启动项目**

```
python manage.py runserver
```


