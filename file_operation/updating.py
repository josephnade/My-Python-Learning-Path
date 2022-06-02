#*****************Sayfa Başına ekleme yapma************************
# with open("newfile.txt","r+",encoding="utf-8") as file:
#     file.write("Updating\n")
# with open("newfile.txt", "r+", encoding="utf-8") as file:
#     print(file.read())
#*****************Sayfa sonuna ekleme yapma************************
# with open("newfile.txt","a",encoding="utf-8") as file:
#     file.write("\nAppending")
# with open("newfile.txt", "r+", encoding="utf-8") as file:
#     print(file.read())
#*****************Sayfa başına ekleme yapma************************
with open("newfile.txt","r+",encoding="utf-8") as file:
    content = file.read()
    content = "Hello World\n" + content
    file.seek(0)
    file.write(content)
with open("newfile.txt", "r+", encoding="utf-8") as file:
    print(file.read())
#*****************Sayfa ortasına ekleme yapma************************
with open("newfile.txt","r+",encoding="utf-8") as file:
    list = file.readlines()
    file.seek(0)
    list.insert(2,"3. Row\n")
    file.writelines(list)
    # for i in list:
    #     file.write(i)
with open("newfile.txt", "r+", encoding="utf-8") as file:
    print(file.read())