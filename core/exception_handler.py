# 自定义业务异常
class BaseBusinessError(Exception):
    """基础业务异常父类"""
    pass


class ParamEmptyError(BaseBusinessError):
    """参数为空异常"""
    pass


class ParamInvalidError(BaseBusinessError):
    """非法参数异常"""
    pass


class DataDuplicateError(BaseBusinessError):
    """重复数据异常"""
    pass


def param_check(params: dict, required_keys: list):
    """参数统一校验工具
    :param params: 待校验参数字典
    :param required_keys: 必填字段列表
    """
    # 校验空输入
    if not params:
        raise ParamEmptyError("输入参数不能为空")
    # 校验必填字段缺失/空值
    for key in required_keys:
        val = params.get(key)
        if val is None or str(val).strip() == "":
            raise ParamEmptyError(f"必填参数【{key}】不能为空")
        # 简单非法参数校验示例：id必须是数字
        if key == "id" and not isinstance(val, (int, float)):
            raise ParamInvalidError(f"参数【id】非法，必须为数字")


def global_exception_wrapper(func):
    """全局异常捕获装饰器，统一格式化错误输出"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BaseBusinessError as e:
            print(f"【业务异常】{e}")
        except Exception as e:
            print(f"【系统未知异常】错误信息：{str(e)}")
    return wrapper
