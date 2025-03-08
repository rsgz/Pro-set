import os
z=os.system

u_str = r"""
E:\up1230b-1\StaticFiles\*
E:\up1230b-2\StaticFiles\*
E:\up1230b-1\App_Data\Logs\*
E:\up1230b-2\App_Data\Logs\*
"""
path_set = [line.strip('"') for line in u_str.splitlines() if line.strip()]
print(*path_set,sep="\n")

for p in path_set:
    m = f"""del /q /s {p}"""
    z(m)
    print(f"{p} 清除成功!")