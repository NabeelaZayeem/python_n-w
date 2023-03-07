import os
import datetime as dt
s=os.stat("../data/demo.txt")
print(s)
print(dt.datetime.fromtimestamp(s.st_mtime).strftime('%d-%m-%y %H:%M:%S'))