'''Dosya açmak veya oluşturmak için open() fonk kullanılır.
Kullanımı : open(dosya_adi,dosya_erisim_modu)
dosya_erisim_modu => dosyayı hangi amaçla açtığımızı belirtir.
"w" = write. Dosyayı konumda oluşturur. Eğer dosya varsa içindekileri siler.
"a" = append. Dosya konumda yoksa oluşturur. Eğer dosya varsa içindekilere ekleme yapar.
"x" = create. Dosya konumda yoksa hata verir.
"r" = read. Dosya konumda yoksa hata verir.'''
# file = open("C:/Users/Asus/PycharmProjects/learningpython/file_operation/newfile.txt", "w",encoding='utf-8') # Direkt newfile.txt yazarsan proje konumuna açar.
# print(file)
# file.write("Yusuf Akın") # write ile çalıştırdığımız için içeriği siler.
# file.close()
file = open("/file_operation/newfile.txt", "a", encoding='utf-8')
file.write("\nYusuf AKIN") #append ile çalıştırdığımız için silmez
file.close()