\# 项目分支与提交规范

\## 一、分支命名规范

1\. main：线上稳定主分支，禁止直接提交代码

2\. feat/xxx：新增功能分支（例：feat/json-read-write）

3\. fix/xxx：bug修复分支

4\. docs/xxx：文档、注释修改

5\. refactor/xxx：代码重构无功能变更



\## 二、提交注释规范

格式：\[类型] 简短描述

示例：

\[feat] 完成JSON数据初始化、读写逻辑

\[fix] 修复参数空值校验报错

\[docs] 补充MIT协议说明



\## 三、开发流程

1\. 从main拉取功能分支

2\. 本地开发、提交

3\. 推送远程，发起Pull Request合并main



