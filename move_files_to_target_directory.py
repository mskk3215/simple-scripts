import os
import shutil

# ディレクトリ内のファイルを指定のディレクトリに移動する
def move_files_to_target_directory(directory):
    # 再帰的にディレクトリ内のファイルをリストする
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            destination_path = os.path.join(directory, filename)
            
            # 同じ名前のファイルが既に存在する場合は上書きしないように、別名で保存
            if os.path.exists(destination_path):
                base, ext = os.path.splitext(filename)
                destination_path = os.path.join(directory, f"{base}_copy{ext}")
            
            shutil.move(file_path, destination_path)
            print(f"Moved: {file_path} to {destination_path}")
    
    # 空になったサブディレクトリを削除（オプション）
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in dirs:
            dir_path = os.path.join(root, name)
            try:
                os.rmdir(dir_path)
                print(f"Removed empty directory: {dir_path}")
            except OSError as e:
                print(f"Directory not empty or cannot be removed: {dir_path} - {e}")

# 使用例
directory = '/Users/user/scripts/original_insect_images'
move_files_to_target_directory(directory)
