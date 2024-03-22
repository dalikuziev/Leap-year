print("Kiritilgan yil kabisa yilimi yoki yo'qligini aniqlaymiz")
year = int(input("yil kiriting: "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"Siz kiritgan {year} kabisa yili ekan")
    else:
      print(f"Siz kiritgan {year} kabisa yili emas")
  else:
    print(f"Siz kiritgan {year} kabisa yili ekan")
else:
  print(f"Siz kiritgan {year} kabisa yili emas")
