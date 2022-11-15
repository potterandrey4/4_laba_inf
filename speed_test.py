from datetime import datetime
import subprocess

print('source code')
start_time = datetime.now()
for i in range(100):
    subprocess.run("c.py", shell=True)
print(datetime.now() - start_time)

print("\nc регулярками")
start_time = datetime.now()
for i in range(100):
    subprocess.run("o.py", shell=True)
print(datetime.now() - start_time)

print("\nc библиотеками")
start_time = datetime.now()
for i in range(100):
    subprocess.run("p.py", shell=True)
print(datetime.now() - start_time)