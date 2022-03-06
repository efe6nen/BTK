import argparse
import sys

args = sys.argv[1:]

parser = argparse.ArgumentParser(description="Argüman Ayrıştırıcı.")

parser.add_argument("-o", "--output", help="Your destination output file.")
parser.add_argument("-n", "--number", help="A number.")
options = parser.parse_args(args)

if type(options.number) != int:
    parser.error('Lutfen sayi belirtiniz.')

print(options.output)
print(options.number)










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


