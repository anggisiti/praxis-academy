menu = {
    "Fried Chicken":15000,
    "Burger Queen":23000,
    "Martabak":22000,
    "Jasmine Tea":10000
}
print("================= Daftar Menu =================")
for i in menu:
    print("Daftar Menu : ", i,"\t Harga : ",menu[i])
print("Pembelian diatas Rp100.000,- mendapatkan diskon 20%")
print("======================================================")
beli = input("Pilih Menu : ")
jumlah = int(input("Jumlah Pesanan :"))
bayar = jumlah * menu[beli]

if bayar > 10000:
    diskon = bayar*15/100
    total = bayar - diskon
else:
    total = bayar

print("================= Daftar Menu =================")
print("Menu yang dipesan        : ",beli)
print("Jumlah yang dipesan      : ",jumlah)
print("Total Biaya              : ",bayar)
print("Total yang harus dibayar : ",total)


