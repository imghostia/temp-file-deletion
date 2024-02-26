import shutil

del_dir = r'C:\Windows\Temp'
del_dir2 = r'C:\Users\hmbhu\AppData\Local\Temp'
shutil.rmtree(del_dir, ignore_errors=True)
shutil.rmtree(del_dir2, ignore_errors=True)
print('Deleted', del_dir, del_dir2)
