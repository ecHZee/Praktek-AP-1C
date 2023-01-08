# Fase 1 - Bagian Module
import time 
import os

# Fase 2 - Bagian Permulaan
lanjut = "y"  

print("\nAplikasi sedang memuat, Harap menunggu dengan sabar !")
time.sleep(1)
print(".")
time.sleep(1)
print(".") 
time.sleep(1)
print(".")  
time.sleep(1)
os.system("cls")

print('''
__________________________________________________________________________
                SELAMAT DATANG DI APLIKASI KONVERSI WAKTU KAMI
                    semoga program yang kami buat dapat
                    membantu permasalahan kalian dalam
                    menghitung waktu, Keep Enjoy it :)
                    
                    
                    Aplikasi ini dibuat oleh:
                            KELOMPOK 9
                    Hanif Zhafran
                    Alfidzar Lizardi
                    Azriel Sya'ban
                    Syifa Fauziah
___________________________________________________________________________
''') 
time.sleep(1)  

# Fase 3 - Bagian Program
while lanjut == 'y' or lanjut == 'Y':
    print('''
_____________________________
|   Program Konversi Waktu  |
|   ______________________  |
|   [1] Detik ke Jam        |
|   [2] Detik ke Menit      |
|   [3] Menit ke Detik      |
|   [4] Menit ke Jam        |
|   [5] Jam ke Detik        |
|   [6] Jam ke Menit        |
_____________________________
''')
    try: 
        # Input Awal untuk menginput pilihan operasi yang akan dipilih
        input_operasi = int(input("Silahkan pilih Operasi Konversi yang anda inginkan: "))
        print("\nPermintaan anda sedang diproses, mohon menunggu...")
        time.sleep(1) 
        if input_operasi <= 0 or input_operasi >= 7:
            print("_______________________________________________________\n\nAnda menginput pilihan yang salah!")
            time.sleep(2)
            os.system("cls")
            continue
        
        # Fungsi untuk menjalankan Program Detik ke Jam
        def detik_ke_jam(totaldetik): 
            # Variabel yang akan menjalankan proses Konversi Detik ke Jam
            jam_float = totaldetik / 3600 
            waktu_jam = totaldetik // 3600 
            sisadetik = totaldetik % 3600 
            waktu_menit = sisadetik // 60 
            waktu_detik = sisadetik % 60 

            # fungsi untuk mencetak hasil konversi Detik ke Jam
            return(f"\n|%d Detik sama dengan {float(jam_float):.2f} Jam atau rinciannya adalah %d Jam %d Menit %d Detik|\n" %(totaldetik,waktu_jam,waktu_menit,waktu_detik)) # Fungsi ini bertujuan untuk mengembalikan nilai fungsi itu sendiri
            time.sleep(2) 


        # Fungsi untuk menjalankan Program Detik ke Menit
        def detik_ke_menit(totaldetik): 
            # Variabel yang akan menjalankan proses Konversi Detik ke Menit
            sisadetik = totaldetik % 3600 
            sisamenit = totaldetik / 60
            waktu_menit = totaldetik // 60
            waktu_detik = sisadetik % 60

            # fungsi untuk mencetak hasil konversi Detik ke Menit
            return(f"\n|%d Detik sama dengan {float(sisamenit):.2f} Menit atau rinciannya adalah %d Menit %d Detik|\n" %(totaldetik,waktu_menit,waktu_detik))
            time.sleep(2) 
            
        # Fungsi untuk menjalankan Program Menit ke Detik
        def menit_ke_detik(totalmenit):
            # Variabel yang akan menjalankan proses Konversi Menit ke Detik
            waktu_detik = totalmenit * 60
            
            # fungsi untuk mencetak hasil konversi Menit ke Detik
            return("\n|%d Menit sama dengan %d Detik|\n" %(totalmenit,waktu_detik))
            
        # Fungsi untuk menjalankan Program Menit ke Jam
        def menit_ke_jam(totalmenit):
            # Variabel yang akan menjadi proses Menit ke Jam
            jam_float = totalmenit / 60
            waktu_jam = totalmenit / 60
            sisadetik = totalmenit % 60
            waktu_menit = sisadetik % 60
            
            # fungsi untuk mencetak hasil konversi Menit ke Jam
            return(f"\n|%d Menit sama dengan {float(jam_float):.1f} Jam atau dengan rincian %d Jam %d Menit|\n" %(totalmenit,waktu_jam,waktu_menit))
            time.sleep(2) 
            
        # Fungsi untuk menjalankan Program Jam ke Detik
        def jam_ke_detik(totaljam):
            # Variabel yang akan menjalankan proses Konversi Jam ke Detik
            waktu_detik = totaljam * 3600
            
            # fungsi untuk mencetak hasil konversi Jam ke Detik
            return("\n|%d Jam sama dengan %d Detik|\n" %(totaljam,waktu_detik))

        # Fungsi untuk menjalankan Program Jam ke Menit
        def jam_ke_menit(totaljam):
            # Variabel yang akan menjalankan Proses Konversi Jam ke Menit
            waktu_menit = totaljam * 60
            
            # fungsi untuk mencetak hasil konversi Jam ke Menit
            return("\n|%d Jam sama dengan %d Menit|\n" %(totaljam,waktu_menit))

        # Fungsi untuk Program menjalankan Operasi Detik ke Jam
        if input_operasi == 1:
            # Statement yang akan mencetak judul operasi
            print("\nProgram Konversi Detik ke Jam\n_________________________________________")

            # Variabel untuk menginput angka dengan satuan detik
            totaldetik = float(input("Masukkan detik dalam bentuk angka \t: "))
            print("\nProgram sedang diproses, Mohon menunggu!")
            time.sleep(1) 
            print(f"{detik_ke_jam(totaldetik)}")
            

        # Fungsi untuk Program menjalankan Operasi Detik ke Menit
        elif input_operasi == 2:  
            # Statement yang akan mencetak judul operasi
            print("\nProgram Konversi Detik ke Menit\n_________________________________________")

            # Variabel untuk menginput angka dengan satuan detik
            totaldetik = float(input("Masukkan detik dalam bentuk angka \t: "))
            print("\nProgram sedang diproses, Mohon menunggu!")
            time.sleep(1) 
            print(f"{detik_ke_menit(totaldetik)}")
            
        # Fungsi untuk Program menjalankan Operasi Menit ke Detik
        elif input_operasi == 3:
            # Statement yang akan mencetak judul operasi
            print("\nProgram Konversi Menit ke Detik\n_________________________________________")

            # Variabel untuk menginput angka dengan satuan menit
            totalmenit = float(input("Masukkan menit dalam bentuk angka \t: "))
            print("\nProgram sedang diproses, Mohon menunggu!")
            time.sleep(1) 
            print(f"{menit_ke_detik(totalmenit)}")

        # Fungsi untuk Program menjalankan Operasi Menit ke Jam
        elif input_operasi == 4:
            # Statement yang akan mencetak judul operasi
            print("\nProgram Konversi Menit ke Jam\n_________________________________________")

            # Variabel untuk menginput angka dengan satuan menit
            totalmenit = float(input("Masukkan menit dalam bentuk angka \t: "))
            print("\nProgram sedang diproses, Mohon menunggu!")
            time.sleep(1) 
            print(f"{menit_ke_jam(totalmenit)}")
            
        # Fungsi untuk Program menjalankan Operasi Jam ke Detik
        elif input_operasi == 5:
            # Statement yang akan mencetak judul operasi
            print("\nProgram Konversi Jam ke Detik\n_________________________________________")

            # Variabel untuk menginput angka dengan satuan jam
            totaljam = float(input("Masukkan Jam dalam bentuk angka \t: "))
            print("\nProgram sedang diproses, Mohon menunggu!")
            time.sleep(1) 
            print(f"{jam_ke_detik(totaljam)}")
            
        # Fungsi untuk Program menjalankan Operasi Jam ke Menit
        elif input_operasi == 6:
            # Statement yang akan mencetak judul operasi
            print("\nProgram Konversi Jam ke Menit\n_________________________________________")

            # Variabel untuk menginput angka dengan satuan jam
            totaljam = float(input("Masukkan Jam dalam bentuk angka \t: "))
            print("\nProgram sedang diproses, Mohon menunggu!")
            time.sleep(1) 
            print(f"{jam_ke_menit(totaljam)}")
        
        #  Fungsi yang akan berjalan ketika Program sudah berjalan
        time.sleep(1) 
        lanjut = input('\nApakah anda ingin melakukan Konversi lagi? (Y/T)\n>>> ')
        if lanjut == 'y' or lanjut == 'Y':
            time.sleep(1) 
            os.system("cls")
            print("Program sedang memproses ulang, Mohon menunggu!")
            time.sleep(1)
            continue
        elif lanjut == 't' or lanjut == 'T':
            print('\n|Terimakasih sudah menggunakan Aplikasi kami|')
            time.sleep(1) 
            print('\nSampai Jumpa!\n')
            time.sleep(2) 
            break
        if lanjut != 'y' or lanjut != 'Y' or lanjut != 'T' or lanjut != "t":
            time.sleep(1) 
            print('\nApakah kamu typo? ingin melakukan Konversi lagi? (Y/T) ')
            time.sleep(1) 
        lanjut = input('>>> ' )
        if lanjut == 'y' or lanjut == 'Y':
            time.sleep(1) 
            os.system("cls")
            print("Program sedang memproses ulang, Mohon menunggu!")
            time.sleep(1)
            continue
        elif lanjut == 't' or lanjut == 'T':
            print('\n|Terimakasih sudah menggunakan Aplikasi kami|')
            time.sleep(1) 
            print('\nSampai Jumpa!')
            time.sleep(2) 
            break
        elif lanjut != 'y' or lanjut != 'Y' or lanjut != 'T' or lanjut != "t":
            time.sleep(1)
            print('\nMaaf Program ini juga punya hati jadi gabisa dipaksa, jadi Terimakasih sudah menggunakan Aplikasi kami :D\n')
            time.sleep(2) 
            break
    
    # Fungsi Except akan berjalan ketika terjadi error pada program
    except ValueError:
        time.sleep(1) 
        print("\nInput wajib berupa angka!")
        time.sleep(1) 
        lanjut = input('\nApakah anda ingin mengulang Konversinya? (Y/T)\n>>> ')
        time.sleep(1) 
        if lanjut == 'y' or lanjut == 'Y':
            time.sleep(1) 
            os.system("cls")
            print("Program sedang memproses ulang, Mohon menunggu!")
            time.sleep(1)
            continue
        elif lanjut == 't' or lanjut == 'T':
            print('\n|Terimakasih sudah menggunakan Aplikasi kami|')
            time.sleep(1) 
            print('\nSampai Jumpa!')
            time.sleep(2) 
            break
        if lanjut != 'y' or lanjut != 'Y' or lanjut != 'T' or lanjut != "t":
            time.sleep(1) 
            print('\nApakah kamu typo? ingin melakukan Konversi lagi? (Y/T) ')
            time.sleep(1) 
        lanjut = input('>>> ' )
        time.sleep(1) 
        if lanjut == 'y' or lanjut == 'Y':
            time.sleep(1) 
            os.system("cls")
            print("Program sedang memproses ulang, Mohon menunggu!")
            time.sleep(1)
            continue
        elif lanjut == 't' or lanjut == 'T':
            print('\n|Terimakasih sudah menggunakan Aplikasi kami|')
            time.sleep(1) 
            print('\nSampai Jumpa!')
            time.sleep(2) 
            break
        elif lanjut != 'y' or lanjut != 'Y' or lanjut != 'T' or lanjut != "t":
            time.sleep(1)
            print('\nMaaf Program ini juga punya hati jadi gabisa dipaksa, jadi Terimakasih sudah menggunakan Aplikasi kami :D\n')
            time.sleep(2) 
            break