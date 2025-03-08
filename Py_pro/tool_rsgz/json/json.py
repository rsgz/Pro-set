import json

class Json:
    def __init__(self):
        pass

    # 打印json
    def print_json(self,json_date):
        r"""打印json"""
        print(json.dumps(json_date, indent=4, ensure_ascii=False))

    # 打开json文件
    def dakai_json(self,file_path="pic_json.json"):
        r"""打开json文件"""
        r"""
        pic_json = dakai_json(file_path="pic_json.json")
        """
        # 尝试读取 JSON 文件并返回映射字典
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            # 如果文件不存在或者文件格式有误，返回一个空字典
            print("文件未找到或格式错误。")
            return {}

    # 保存
    def save_data(self, data, filename="data.json"):
        with open(filename, "w") as f:
            json.dump(data, f)

    # 读取
    def load_data(self, filename="data.json"):
        try:
            with open(filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

if __name__ == '__main__':
    pass
    # 示例用法
    j = Json()
    data = {"name": "Alice", "age": 30, "city": "Beijing"}
    j.save_data(data)
    loaded_data = j.load_data()
    print(loaded_data)