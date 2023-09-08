def filemove(O_path,n_path):
    import shutil
    import os
    # 取得原始資料夾中的所有檔案路徑
    file_paths = [os.path.join(O_path, f) for f in os.listdir(O_path) if
                  os.path.isfile(os.path.join(O_path, f))]

    # 將原始資料夾中的所有檔案移到目標資料夾中
    for file_path in file_paths:
        shutil.move(file_path,n_path)







