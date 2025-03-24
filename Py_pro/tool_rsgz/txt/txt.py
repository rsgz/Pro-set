import os

class Txt:
    def __init__(self):
        pass

    # 获取文本列表
    def get_txt_to_list(self,txt_file_path):
        r"""获取文本列表"""
        with open(txt_file_path, 'r', encoding='utf-8') as file:
            return file.readlines()

    # 获取文本列表 迭代文件对象
    def get_txt_to_list_gaoxiao(self,file_path):
        r"""获取文本列表 迭代文件对象"""
        with open(file_path, 'r', encoding='utf-8') as file:
            return [line.strip()  for line in file]

    # 获取文本列表 去空行
    def get_txt_to_list_gaoxiao_qukonghang(self,file_path):
        r"""获取文本列表 去空行 迭代文件对象"""
        with open(file_path, 'r', encoding='utf-8') as file:
            return [line.strip()  for line in file]

    # 列表-->txt
    def list_to_txt_append(self, date_list, txt_path):
        r"""列表-->txt 追加不清空txt"""
        try:
            # 确保目录存在
            os.makedirs(os.path.dirname(txt_path), exist_ok=True)
            with open(txt_path, 'a', encoding="utf-8") as f:
                f.writelines(str(info) + '\n' for info in date_list)
        except FileNotFoundError:
            print(f"文件 {txt_path} 未找到。")
        except PermissionError:
            print(f"没有写入 {txt_path} 的权限。")
        except OSError as err:
            print(f"{txt_path} 写入信息时出错: {err}")
        else:
            print(f"{txt_path} 已成功写入！")

    # 合并多个txt文档
    def hebing_txt_files(self, txt_dir, output_file):
        r"""合并多个txt文档"""
        input_files = [os.path.join(txt_dir, f) for f in os.listdir(txt_dir)]
        with open(output_file, 'a+', encoding='utf-8') as outfile:
            for file in input_files:
                if os.path.isfile(file):  # 确保文件存在
                    with open(file, 'r', encoding='utf-8') as infile:
                        # 使用迭代器逐行读取并写入
                        for line in infile:
                            outfile.write(line)

    # 新建txt
    def xinjian_txt(self, txt_path):
        r"""新建txt"""
        try:
            # 确保目录存在
            os.makedirs(os.path.dirname(txt_path), exist_ok=True)
            with open(txt_path, 'w') as f:  # 以写入模式打开，如果文件不存在，会自动创建
                pass  # 不写入任何内容，直接关闭，创建一个空文件
            print(f"成功创建文件: {txt_path}")
        except FileNotFoundError:
            print(f"创建文件 {txt_path} 时出错: 目录不存在。")
        except PermissionError:
            print(f"创建文件 {txt_path} 时出错: 没有权限。")
        except OSError as e:
            print(f"创建文件 {txt_path} 时出错: {e}")

    # 追加文本到 txt 新行
    def zhuijia_str_to_txt(self,str_content,txt_path):
        try:
            info=str_content
            file_txt=txt_path
            with open(file_txt, 'a+', encoding="utf-8") as f:
                f.write(str(info)+ '\n')
        except OSError as err:
            print(file_txt, "写入信息的时候出现了问题")
            print(err)
        else:
            print(file_txt, "已经写入到本地!!!")

if __name__ == '__main__':
    t=Txt()
    t.xinjian_txt(r"C:\Users\Administrator\Desktop\0001_rsgz__data_moni\000.txt")
