import os
import sys

# 检查是否有足够的命令行参数
if len(sys.argv) < 2:
    print("Usage: script.py <IP:Port>")
    sys.exit(1)

# 获取命令行传入的新基础URL
new_base_url = sys.argv[1]

# 设置目标目录和替换内容
target_dir = '.'  # 当前目录
old_string = r'{{interactsh-url}}'

# 遍历目标目录
for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file.endswith('.yaml'):
            # 生成新字符串，将exp替换为文件名（无扩展名）
            file_name_without_extension = os.path.splitext(file)[0]
            new_string = new_base_url +'/'+ file_name_without_extension  # 使用命令行参数

            file_path = os.path.join(root, file)
            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 替换内容
            new_content = content.replace(old_string, new_string)
            
            # 如果内容发生变化，则写回文件
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated: {file_path}")
