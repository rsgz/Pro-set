def compare_domains(new_domains_file, all_domains_file, output_file):
    """
    比较新域名文件和总域名文件中的域名，并将完全新的域名写入输出文件。
    Args:
        new_domains_file (str): 新域名文件路径。
        all_domains_file (str): 总域名文件路径。
        output_file (str): 输出文件路径。
    """
    try:
        with open(all_domains_file, 'r', encoding='utf-8') as f:
            all_domains = set(line.strip() for line in f)  # 使用 set 提高查找效率
        with open(new_domains_file, 'r', encoding='utf-8') as f:
            new_domains = [line.strip() for line in f]
        completely_new_domains = [
            domain for domain in new_domains if domain not in all_domains]
        with open(output_file, 'w', encoding='utf-8') as f:
            for domain in completely_new_domains:
                f.write(domain + '\n')
        print(f"完全新的域名已写入 {output_file}")
    except FileNotFoundError:
        print("文件未找到，请检查文件路径是否正确。")
    except Exception as e:
        print(f"发生错误：{e}")
if __name__ == "__main__":
    new_domains_file = r"C:\Users\Administrator\Desktop\数据\新域名.txt"
    all_domains_file = r"C:\Users\Administrator\Desktop\数据\1-域名\域名all4.txt"
    output_file = r"C:\Users\Administrator\Desktop\数据\完全新域名.txt"
    compare_domains(new_domains_file, all_domains_file, output_file)