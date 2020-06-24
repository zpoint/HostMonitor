# 设计方案

![framework](./HostMonitor.png)

需要通过统一的管理平台管理不同数据库的元信息, 和数据本身信息查询

基于 [sanic](https://github.com/huge-success/sanic) 框架搭建API服务, 借助 [sanic-restplus](https://github.com/ashleysommer/sanic-restplus) 提供 rest api

# 流程

用户请求 -> 网关 -> api server -> 权限校验 -> 进入接口代码 -> 路径定位操作的数据库类型,实例 -> 生成Query实例 -> 解析请求body和方法定位到具体的操作 -> 生成 Operator 实例 -> Operator 调用 Query 方法得到结果 -> 经过中间件格式化 -> 返回给用户

* Operator 可以是查询, 添加修改, 拼接, 过滤, 聚合等操作
* Query 实现具体的查询, 添加修改方法, 比如 ESQuery, influxdbQuery, 或者是 mixQuery 同时拿到 ESQuery 和 influxdbQuery 结果聚合后向上层调用者返回
* 解耦后能支持任意类型的自定义查询组合, 或者自定义DSL, 只要语法/查询条件 -> 解析器 -> Operator 能对应上即可

