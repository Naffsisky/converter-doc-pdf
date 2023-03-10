# Created by. Prinafsika (21081010278)
import docx2pdf as doc

print("1. Single File")
print("2. Multiple File")
print("3. Exit")
pilihan = int(input("Masukan pilihan : "))
if pilihan == 1:
    print("Masukan nama file dengan format .docx")
    file = input("Masukan nama file : ")
    fileOutput = input("Masukan nama file output : ")
    print("Wait...")
    doc.convert(file + ".docx", fileOutput + ".pdf")
    if doc.convert(file + ".docx", fileOutput + ".pdf"):
        print("File berhasil di convert")
    else:
        print("File gagal di convert")
elif pilihan == 2:
    folder = input("Masukan nama folder : ")
    folderOutput = input("Masukan nama folder output : ")
    print("Wait...")
    doc.convert(folder, folderOutput)
    print("File berhasil di convert")
else:
    exit()
