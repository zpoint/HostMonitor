# -*- coding: utf-8 -*-
"""
目前的实现比较简单, 先抽象处理并只支持一层
如果时间允许, 可以参考语法解析树的接收一个树形结构, 递归操作后获取最终数据
"""
from query.query_factory import QueryFactory


class Operator(object):
    def __init__(self, unpacked_results: tuple):
        self.query_name, self.action, self.result_meta_with_query, self.result_query = unpacked_results

    async def operate(self):
        query = QueryFactory.create_query(self.query_name, self.result_meta_with_query, self.result_query)
        return await getattr(query, self.action)()
