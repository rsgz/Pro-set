import os

z = os.system

u_str = r"""
E:\z\0-up1220-1\App_Data\Logs\*
E:\z\0-up1220-1\StaticFiles\*
E:\z\0-up1220-2\App_Data\Logs\*
E:\z\0-up1220-2\StaticFiles\*
E:\z\up1230b-1\App_Data\Logs\*
E:\z\up1230b-1\StaticFiles\*
E:\z\up1230b-2\App_Data\Logs\*
E:\z\up1230b-2\StaticFiles\*
"""
path_set = [line.strip('"') for line in u_str.splitlines() if line.strip()]
# print(*path_set, sep="\n")

for p in path_set:
    m = f"""del /q /s {p}"""
    ret = z(m)
    if ret == 0:
        print(f"{p} 清除成功!")
    else:
        print(f"{p} 清除失败! 返回值: {ret}")