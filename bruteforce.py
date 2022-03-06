import argparse
import sys
import zipfile
import os

sozlukarg = input("Kaça kadar bir sözlük istiyorsun:")


combolist = ""
for i in range(0,int(sozlukarg)+1):
        combolist+=str(i)+"\n"
with open('comb.txt', 'w') as f:
    f.write(combolist)












#args = sys.argv[1:]
#
#parser = argparse.ArgumentParser(description="Bruteforcer.")
#
#parser.add_argument("-z", "--zip", help="Hedef zip dosyasi.")
#parser.add_argument("-p", "--pwds", help="Denenmek istenen şifrelerin bulunduğu dosya.")
#options = parser.parse_args(args)
#
#for password in open(options.pwds).readlines():
#        zipp = zipfile.ZipFile(options.zip, mode='r')
#        zipp.extractall(pwd=bytes(password, 'utf-8'))
#        zipp.close()
#        print(password)




#desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
#
#ZipFiles = []
#
#for fileName in os.listdir(desktop):
#    file_extension = os.path.splitext(fileName)
#    desktop += '\\'
#    if file_extension[1] == ".zip":
#        ZipFiles.append(desktop+file_extension[0]+file_extension[1])
#        print("Found archive file in Desktop.", desktop+file_extension[0]+file_extension[1])


