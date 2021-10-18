# TV Remote Controller Program Model
# Program TV Remote sederhana yang dapat dilakukan 7 fungsi
# KU1102_Pengenalan Komputasi K06 FITB
# Kelompok 4
# 1. Syifa Kamiliya R (16321013)
# 2. Azkiya Tsabitul A (16321017)
# 3. Keisha Prillia Q (16321021)
# 4. Bunga Azzahra (16321...)

# KAMUS
# Stat : str
# V, C : int
# CList: array str

# ALGORITMA

print("TV Remote Controller Program")
print("")
print("""

1. Turn On TV
2. Turn Off TV
3. Volume Adjustmment
4. Channel Amount
5. Add Channel
6. Move Channel
7. TV Info

To Exit, press 'Q' or 'q'

""")

# Keterangan TV yang pre-defined, yaitu Status TV, Volume, Channel dan List Channel
Stat = "OFF"
V = int(25)
C = int(7)
CList = ["KompasTV", "GlobalTV", "TransTV", "Trans7", "RCTI", "TvOne", "HBO", "FOX", "BBC", "Nickelodeon"]

while True:
    Op = input("Choose Operation: ")
    print("")
    if (Op == "Q") or (Op == "q"):              # Command untuk menutup program TV Remote/Tidak jadi mengatur TV
        print("Closing Program...")
        break
    elif (Op == "1"):                           # Command untuk menyalakan TV
        if (Stat == "ON"):
            print("_TV is On.")                 # Output text jika TV sudah menyala
            print("")
        else:
            print("_Turning TV On...")          # Output text jika TV belum menyala
            print("")
            Stat = "ON"
    elif (Op == "2"):                           # Command untuk mematikan TV
        if (Stat == "OFF"):
            print("_TV is Off.")                # Output text jika TV sudah mati
            print("")
        else:
            print("_Turning TV Off...")         # Output text jika TV belum mati
            print("")
            Stat = "OFF"
    elif (Stat == "ON") and (Op == "3"):         # Command untuk mengatur volume suara TV
        while True:                             # Looping pengaturan volume suara TV
            print("Volume Down: '-' \nVolume Up: '+' \nMute: 'M' \nExit: 'exit'")
            A = input("__Input Operation: ")
            print("")
            if (A == "-"):                          # Command untuk mengurangi volume suara TV
                if (0 < V <= 100):                  # Ketentuan volume awal yang bisa diturunkan volumenya
                    V -= 1
                    print("___Volume: ", V)         # Output text volume suara yang telah diatur
                    print("")
            elif (A == "+"):                        # Command untuk menambah volume
                if (0 <= V < 100):                  # Ketentuan volume awal yang bisa ditambah volumenya
                    V += 1
                    print("___Volume: ", V)         # Output text volume suara yang telah diatur
                    print("")
            elif (A == "M"):                        # Command untuk membisukan suara TV
                if (0 < V <= 100):                  # Ketentuan volume awal yang bisa dibisukan
                    V = 0
                    print("___TV has been Muted")   # Output text volume suara yang telah diatur
                    print("")
            elif (A == "exit") or (A == "Exit"):    # Command untuk keluar dari program pengaturan volume suara TV
                print("___Volume has been Updated! Volume:", V) # Output text pasca exit program pengaturan volume
                print("")
                break
            else:                                   # Bila command yang dimasukkan tidak terdefinisi
                print("___Invalid Operation! Please Try Again") # Output text jika command tidak terdefinisi
                print("")
    elif (Stat == "ON") and (Op == "4"):             # Command untuk melihat jumlah channel yang terdapat di TV
        for x in CList:
            print(x)
        print("_Channel Amount: ", len(CList))      # Output jumlah channel yang ada
        print("")
    elif (Stat == "ON") and (Op == "5"):             # Command untuk menambahkan channel baru
        CName = str(input("_Add Channel: "))        # Input dari user, nama channel (string)
        CList.append(CName)
        print("Channel ", CName, "has been Added")          # Output text channel yang sudah ditambahkan dalam list
    elif (Stat == "ON") and (Op == "6"):             # Command untuk memindahkan channel
        while True:                                 # Looping pengaturan channel TV
            print("Previous Channel: '-' \nNext Channel: '+' \nExit: 'exit'")
            a = input("___Input Operation: ")
            print("")
            if (a == "-"):                          # Command untuk pindah satu channel ke bawah
                if (0 < C <= len(CList)):           # Ketentuan nomor channel yang bisa dipindah ke bawah
                    C -= 1
                    print("___Moved to Prevous Channel")    # Output text operasi pemindahan channel
                    print("___Now Watching Channel", C)     # Output text channel yang telah dipindahkan
                    print("")
                elif (C == 0):                      # Ketentuan channel paling awal dan tidak bisa dipindah ke bawah
                    print("___There are no more Channels Before this!") # Output text channel tidak bisa dipindah ke bawah
                    print("")
            elif (a == "+"):                        # Command untuk pindah satu channel ke atas
                if (0 <= C < len(CList)):           # Ketentuan nomor channel yang bisa dipindah ke atas
                    C += 1
                    print("___Moved to Next Channel")       # Output text operasi pemindahan channel
                    print("___Now Watching Channel", C)     # Output text channel yang telah dipindahkan
                    print("")
                elif (C == len(CList)):             # Ketentuan channel paling akhir dan tidak bisa dipindah ke atas
                    print("___There are no more Channels After this!")  # Output text channel tidak bisa dipindah ke atas
                    print("")
            elif (a == "exit") or (a == "Exit"):    # Command untuk keluar dari program pengaturan channel
                print("___Channel has been moved!")             # Output text pasca exit program pengaturan channel
                print("___Now Watching Channel", C)
                print("")
                break
            else:
                print("___Invalid Operation! Please Try Again") # Output text jika command tidak terdefinisi
                print("")
    elif (Stat == "ON") and (Op == "7"):             # Command untuk melihat status TV
        print("_TV Status: ", Stat)
        print("_TV Volume: ", V)
        print("_Channel Amount: ", len(CList))
        print("_Watching Channel Number: ", C)
        print("")
    else:
        print("Invalid Operation!")
