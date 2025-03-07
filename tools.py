import os

def merge_md_files(folder_path, output_file):
    # 确保输出文件的扩展名是 .md
    if not output_file.endswith('.md'):
        output_file += '.md'

    # 打开输出文件
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # 遍历文件夹中的所有文件
        for filename in os.listdir(folder_path):
            # 只处理 .md 文件
            if filename.endswith('.md'):
                file_path = os.path.join(folder_path, filename)
                # 写入文件名作为标题
                outfile.write(f"# {filename}\n\n")
                # 读取并写入文件内容
                with open(file_path, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
                outfile.write("\n\n")  # 添加一些空格以分隔不同文件的内容

    print(f"所有 .md 文件已合并到 {output_file}")

# 使用示例
folder_path = './api'  # 替换为你的文件夹路径
output_file = 'merged_output.md'  # 输出文件名
merge_md_files(folder_path, output_file)