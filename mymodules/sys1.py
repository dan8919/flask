import sys
import mysys ,os  #mysys파일 모듈로 import

mysys.clear() #파일.함수


 
from mysys import clear #mysys 파일중 clear 함수를 import
clear() #함수 자체를 쓰면 됨



#sys.path.append()
dir_name = os.path.dirname(__file__)
a_path = os.path.abspath(dir_name)
print("a_path>>",a_path)#/Users/cuixindan/workspace/python/mymodules
up_dir = os.path.join(a_path,"..")#c:\ws\...   ad/sdf/
os.path.abspath(up_dir)
print("BASE CAMP>>",os.path.abspath(up_dir)) #/Users/cuixindan/workspace/python
sys.path.append(os.path.abspath(up_dir))


print("__file__===>",__file__) #파일 명이 나옴. sys1.py
print("dirname===>",os.path.dirname(__file__))#아무것도 안 찍히면 현재 폴더
print("abspath===>",os.path.abspath(__file__))#abspath 절대 경로

print(sys.argv,len(sys.argv))
print("11111")

def print_sys_vars():
    for i in [sys.version,sys.copyright,sys.platform]:
        print("--->",i)

sa = sys.argv   # 파일list
if  len(sa)<2:
    sys.exit()

with open(sa[1],"r",encoding ='utf-8') as file:
    for line in file:
        print (line)