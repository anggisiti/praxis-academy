print("Selamat Datang di ATM saya")
print("Pilih Option :")
print("1. Check Uang Saya")
print("2. Ambil Uang Saya")
print("3. Tabung Uang Saya")
option=int(input(" Silahkan pilih option :"))
if option==1:
    print("Uang Kamu Berjumlah Rp.400.000")
elif option==2:
    print("Uang Kamu Berjumlah Rp.400.000, Mau Ambil Berapa?")
    print("1. Rp. 200.000")
    print("2. Rp. 300.000")
    uang_kamu=200000
    option2==int(input("Option :"))
    if option2==1:
        hasil1=uang_kamu-100000
        print("Uang Kamu Sekarang Berjumlah :",hasil1)
    elif option2==2:
        hasil2=uang_kamu-400000
        print("Uang Kamu Sekarang Berjumlah :",hasil2)
    else:
        print("Keyword Anda Salah!")
elif option==3:
    uang_kamu=400000
    print("Uang Berjumlah Rp.400.000, Mau Nabung Berapa?")
    option3=int(input("Masukkan Jumlah Uang :"))
    hasil3==uang_kamu+option3
    print("Jumlah Uang Kamu Sekarang Adalah ",hasil3)
else:
    print("Keyword Anda Salah, Silahkan Coba Lagi")