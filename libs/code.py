# -*- coding: utf-8 -*-


class ValidationError(Exception):
    """
    API 基础验证异常
    """
    status_code = 400
    errors = {}

    def __init__(self, code, status_code=None, data=None, msg=None):
        self.code = code
        self.data = data
        self.message = self.errors.get(code) if not msg else msg
        if status_code is not None:
            self.status_code = status_code
        super(ValidationError, self).__init__(self.message)


class CodeType(type):
    def __new__(cls, name, bases, attrs):
        attrs_value = {}
        error = {}
        for k, v in attrs.items():
            if k.startswith('__'):
                continue
            if isinstance(v, (tuple, list)) and len(v) == 2:
                code, msg = v
                attrs_value[k] = ValidationError(code=code, msg=msg)
                error[code] = msg
            else:
                attrs_value[k] = v

        obj = type.__new__(cls, name, bases, attrs_value)
        ValidationError.errors.update(error)
        return obj


class Code(metaclass=CodeType):

    SUCCESS = (200, 'SUCCESS')
    UNAUTHORIZED = (401, '未认证')
    FORBIDDEN = (403, '无权限')
    NOTFOUND = (404, '数据不存在')
    SYSTEM_ERROR = (500, '服务器开小差了，请稍后重试~')  # 系统错误

    # 全局的业务代码，以 10 开头
    PARAM_MISS = (20000, u'参数缺失！')
    PARAM_ERROR = (30000, u'参数错误！')

