# query_system
一个快速查询信息的网页系统，默认的模板是抗原检测查询系统
# 1.安装
## 1.1 创建数据库
创建一个mysql数据库,在数据库执行以下sql命令：
```sql
CREATE TABLE results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    query_code VARCHAR(191) NOT NULL UNIQUE,
    result VARCHAR(255) NOT NULL,
    upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
## 1.2 安装依赖
```bash
pip install pymysql
pip install bottle
```
## 1.3 修改设置
将源码下载到目录，解压，打开run.py文件，修改全局设置
![image](https://github.com/AZ-Studio-2023/query_system/assets/76240341/f3a59042-48e1-49c4-b4e4-5099e7d2d2cc)
## 1.4 程序运行
```bash
python3 run.py
```
或nohup后台运行
```bash
nohup python3 run.py
```
# 2.Bug|建议
每个程序总有一些Bug，请大家为我们找出Bug或提出建议，在lssues中提交，谢谢！

