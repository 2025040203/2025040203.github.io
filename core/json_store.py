import json
import os
from core.exception_handler import ParamEmptyError, DataDuplicateError

# 数据存储文件路径
DATA_PATH = "./data/store.json"
# 默认初始化数据
DEFAULT_DATA = {
    "records": [],
    "create_time": "",
    "version": "1.0"
}


class JsonStore:
    def __init__(self):
        # 自动初始化文件
        self.init_file()

    def init_file(self):
        """1. 数据文件初始化，不存在则创建并写入默认模板"""
        dir_path = os.path.dirname(DATA_PATH)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        if not os.path.exists(DATA_PATH):
            with open(DATA_PATH, "w", encoding="utf-8") as f:
                json.dump(DEFAULT_DATA, f, ensure_ascii=False, indent=2)

    def read_data(self) -> dict:
        """2. 读取全部JSON数据"""
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_record(self, new_record: dict):
        """3. 保存单条数据，自动校验重复"""
        data = self.read_data()
        records = data["records"]
        # 简单重复校验：通过唯一id判断
        record_id = new_record.get("id")
        for item in records:
            if item.get("id") == record_id:
                raise DataDuplicateError(f"数据id:{record_id} 已存在，禁止重复写入")
        records.append(new_record)
        data["records"] = records
        # 写入文件持久化
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def reset_data(self):
        """4. 重置数据为初始模板"""
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_DATA, f, ensure_ascii=False, indent=2)
