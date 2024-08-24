import os

def print_files_in_directory(directory):
    # ディレクトリ内のすべてのファイルとサブディレクトリをリストアップし、名前順にソート
    for filename in sorted(os.listdir(directory)):
        file_path = os.path.join(directory, filename)
        
        # ファイルのみを対象とする（サブディレクトリは無視）
        if os.path.isfile(file_path):
            print(filename)

# 使用例
directory = '/Users/user/scripts/original_insect_images'
print_files_in_directory(directory)
