from core.json_store import JsonStore
from core.exception_handler import param_check, global_exception_wrapper

# 实例化JSON操作工具
store = JsonStore()


@global_exception_wrapper
def add_user_record(input_params: dict):
    # 1. 参数校验：必填id、name
    param_check(input_params, required_keys=["id", "name"])
    # 2. 写入JSON文件
    store.save_record(input_params)
    print("数据保存成功！")
    print("当前全部数据：", store.read_data())


if __name__ == "__main__":
    print("===== JSON数据管理工具 =====")
    # 测试1：正常新增数据
    add_user_record({"id": 1, "name": "测试用户A"})

    # 测试2：重复id（触发重复数据异常）
    # add_user_record({"id": 1, "name": "测试用户B"})

    # 测试3：空参数（触发空参数异常）
    # add_user_record({})

    # 测试4：id传字符串（非法参数异常）
    # add_user_record({"id": "abc", "name": "测试C"})

    # 重置数据
    # store.reset_data()
