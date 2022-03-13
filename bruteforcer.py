
password = input("Denenmek istenen şifreyi giriniz: ")
from zipfile import ZipFile
yol=r"C:\Users\egitim.sinif2\Desktop\efethefinest\Desktop.zip"
# yol2=r"C:\Users\egitim.sinif2\Desktop\efethefinest\deneme"

obj2=ZipFile(yol,'r')
if len(obj2.filelist) > 1:
    obj2.extractall(pwd=bytes(password, encoding='utf-8'))