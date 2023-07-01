print("""
1'den 10'a kadar Çarpım Tablosu

""")

sayi = range(1,11)

for i in sayi:
    print("**************")
    for x in sayi:
        carpim = i * x
        print("{} x {} = {}".format(i, x, carpim))