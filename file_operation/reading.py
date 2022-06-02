try:
    file = open("/file_operation/newfile.txt", "r", encoding='utf-8')
    # for i in file:
    #     print(file.readLine(), end="") # tek tek satır okur.Okuduktan sonra \n bırakır.
    #content = file.read() #Okuduksan sonra imleci en sonda bırakır tekrar read yapmak istersek içerik vermez çünkü imleç en sonda.
    #read içine yazdığın sayı kaç tane okuduğunu söyler ve imleç bıraktığın yerde kalır.
    content =file.readlines() #tek tek satırları listeye aktarır. Okuduktan sonra \n bırakır.
    print(content)
except FileNotFoundError:
    print("Dosya okuma hatası!")
finally:
    file.close()
    print("\nDosya Kapandı.")
with open("/file_operation/newfile.txt", "r", encoding='utf-8') as file: # with ile açtığında kapsadığı işlemleri yapıp dosyayı kapatır.
    content = file.read()
    print(content)
    print(file.tell()) #imlecin yerini söyler
    file.seek(10) # imleci nereye götüreceğimizi yazarız
    print(file.read()) # imleç tekrar başa geldiği için okur koymasaydık sonda olduğu için bişey okumazdı

