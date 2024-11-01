import importlib.util
import os

def get_package_path(package_name):
    # 尝试导入包
    package_spec = importlib.util.find_spec(package_name)
    
    if package_spec is not None:
        # 获取包的路径
        package_path = package_spec.origin
        return os.path.dirname(package_path)  # 返回包所在目录
    else:
        return f"Package '{package_name}' is not installed."

# 示例用法
package_name = 'fucker_zju'  # 替换为你想查询的包
path = get_package_path(package_name)
print(path)