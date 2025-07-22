
# PURWADHIKA CAPSTONE PROJECT - MODULE 1 (PYTHON PROGRAMMING LANGUAGE) - CRUD PROJECT (Create - Read - Update - Delete)
# Nama Siswa: Wildan Kharisma Putra Perdana
# Kelas: JCDSOH01-003

# =========================================================================================================================================================================================
# Judul Project: Academic Information Platform for Students of Harapan Bangsa International Academy
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Deskripsi:
# Program ini dibuat untuk mengelola data pribadi siswa, nilai ujian, dan rangkuman hasil nilai 
# dimana pada program ini dilengkapi dengan fitur utama CRUD (Create - Read - Update - Delete).
# Struktur code pada program ini sendiri dibagi menjadi 3 bagian diantaranya:
# 
# 1. Main Program / Main Code
#    Berisi perulangan utama (`while True`) untuk menjalankan alur program,
#    serta pemanggilan fungsi menu berdasarkan input pengguna.
# 2. Main Menu Handler Functions
#    Kumpulan fungsi yang menangani masing-masing menu utama (menu 1–5)
# 3. Support Functions
#    Berisi fungsi-fungsi bantu yang terstruktur untuk memproses data siswa,
#    menampilkan informasi, dan menangani input/output.
# 4. List of Dictionaries
#    Berisi 3 source dictioanry, 3 blank dictionary, dan 1 summary dictionary
# =========================================================================================================================================================================================




# =================================================================================  LIST OF DICTIONARIES  =================================================================================
# -------------------  Dictionary [Data Source] Data Diri Siswa, Nilai UTS Siswa, dan Nilai UAS Siswa  -------------------
# // Dictionary ini menyimpan source database utama yang berupa data dummy,
#    dictionary ini digunakan pada setiap menu
dataSiswa = {
    'Student Id' : [2025003,2025006,2025010,2025018,2025029,
                    2025044,2025056,2025058,2025074,2025080,
                    2025096,2025111,2025123,2025129,2025138],
    'Nama Siswa' : ["Rafi Pratama","Alya Putri","Andi Saputra","Bima Nugraha","Nadia Lestari",
                    "Dinda Kartika","Salsabila Zahra","Fajar Ramadhan","Vina Amelia","Ilham Maulana",
                    "Laras Ayu","Rani Oktaviani","Jaka Setiawan","Rizky Hidayat","Intan Cahya"],
    'Kelas' : [12,12,12,12,12,
               11,11,11,11,11,
               10,10,10,10,10],
    'Jenis Kelamin' : ["Laki - Laki","Perempuan","Laki - Laki","Laki - Laki","Perempuan",
                       "Perempuan","Perempuan","Laki - Laki","Perempuan","Laki - Laki",
                       "Perempuan","Perempuan","Laki - Laki","Laki - Laki","Perempuan"],
    'Kota Asal' : ["Surabaya","Tangerang","Jakarta","Yogyakarta","Bandung",
                    "Semarang","Bogor","Bali","Jakarta","Bandung",
                    "Yogyakarta","Jakarta","Tangerang","Surabaya","Jakarta"],
    'Nilai UTS' : [85.50,80.75,90.50,53.75,68.25,
                   90.00,87.25,55.25,66.75,60.00,
                   80.75,57.50,75.50,69.75,53.75],
    'Nilai UAS' : [80.00,72.75,91.25,56.75,68.50,
                   90.00,84.00,54.00,66.00,55.50,
                   83.00,50.50,75.25,62.50,56.50]
}
nilaiUTSSiswa = {
    'Matematika' : [98,80,84,45,65,
                    95,85,55,55,63,
                    80,45,72,68,55],
    'IPA' : [80,86,88,70,80,
             89,83,60,72,74,
             78,60,70,65,35],
    'IPS' : [85,92,90,40,72,
             78,92,48,65,56,
             85,55,78,75,60],
    'B.Inggris' : [79,65,100,60,56,
                   98,89,58,75,47,
                   80,70,82,71,65]
}
nilaiUASSiswa = {
    'Matematika' : [90,78,86,50,64,
                    100,80,60,50,62,
                    82,50,70,62,58],
    'IPA' : [86,69,87,72,82,
             85,84,55,70,63,
             80,58,75,68,38],
    'IPS' : [79,74,93,42,68,
             80,79,45,67,54,
             88,46,76,58,62],
    'B.Inggris' : [65,70,99,63,60,
                   95,93,56,77,43,
                   82,48,80,62,68]
}

# -----------------  Dictionary [Data Sementara] Data Diri Siswa, Nilai UTS Siswa, dan Nilai UAS Siswa  -----------------
# // Dictionary ini menyimpan database yang disimpan sementara untuk kemudian ditampilkan sesuai dengan pilihan 
#    dibutuhkan user, dictionary ini digunakan pada menu 1 dan menu 2
dictDS = {
    'Student Id' : [],
    'Nama Siswa' : [],
    'Kelas' : [],
    'Jenis Kelamin' : [],
    'Kota Asal' : [],
    'Nilai UTS' : [],
    'Nilai UAS' : []
}
dictNSUTS = {
    'Matematika' : [],
    'IPA' : [],
    'IPS' : [],
    'B.Inggris' : []
}
dictNSUAS = {
    'Matematika' : [],
    'IPA' : [],
    'IPS' : [],
    'B.Inggris' : []
}

# -----------------------  Dictionary [Data Sementara] Data Diri Siswa dan Rangkuman Hasil Akhir  -----------------------
# // Dictionary ini menyimpan data hasil rangkuman yang disimpan sementara untuk kemudian ditampilkan sesuai dengan 
#    pilihan dibutuhkan user, dictionary ini digunakan pada menu 5
dictSummary = {
    'Student Id' : [],
    'Nama Siswa' : [],
    'Kelas' : [],
    'Nilai UTS' : [],
    'Nilai UAS' : [],
    'Grades' : [],
    'Kelulusan' : []
}




# ==============================================================================  SUPPORT / UTILITY FUNCTIONS  ==============================================================================
# // Functions pendukung atau tambahan untuk membantu menjalankan fitur - fitur utama program lebih efisien, dimana 
#    proses - proses nya dilakukan secara berulang. 
# // Jenis - jenis functions nya adalah sebagai berikut: validasi input, manipulasi data, mengatur tampilan, 
#    generate hasil rangkuman


# Function untuk memberikan warning message dengan warna merah, pada saat user salah input data atau data tidak sesuai
def warnMsg(txt):
    return "\033[91m"+"\n=== "+txt+" ==="+"\033[0m"+"\n"


# Function untuk memberikan confirmation message dengan warna hijau, bahwa perubahan atau generate data yang dihendaki
# user telah berhasil dijalankan
def succeedMsg(txt):
    return "\033[32m"+"\n=== "+txt+" ==="+"\033[0m"+"\n"


# Function untuk menampilkan judul beserta header dari sebuah tabel yang telah ditentukan oleh user
def headerConfig(title,dictData,dictData1=None,excepted=None):
    header = ""
    tabLenght = 0
    def spaceBorder(key):
        if key == 'Nama Siswa' or key == 'Jenis Kelamin':
            return 15
        else:
            return 10
    if excepted:
        listData = list(dictData1.keys())[:excepted] + list(dictData.keys())
    else:
        if dictData1 != None:
            listData = list(dictData1.keys())
        else:
            listData = list(dictData.keys())
    for i in listData:
        space = spaceBorder(i)
        header += f"{i:^{space}} | "
        tabLenght += space
    tabLenght = tabLenght + (4 * 5)
    print(f"\n{"="*tabLenght}")
    print(f"{title:^{tabLenght}}")
    print(f"{"="*tabLenght}\n")
    print("-"*tabLenght)
    print(header[:-3])
    print("-"*tabLenght)


# Function untuk menampilkan data tabel sesuai dengan apa yang telah ditentukan oleh user
def tableConfig(dictData,dictData1=None,excepted=None):
    def spaceBorder(key):
        if key == 'Nama Siswa' or key == 'Jenis Kelamin':
            return 15
        else:
            return 10
    if excepted:
        listHeader = list(dictData1.keys())[:excepted] + list(dictData.keys())
        totalData =  range(len(dictData1[listHeader[0]]))
    else:
        if dictData1 != None:
            listHeader = list(dictData1.keys())
            totalData =  range(len(dictData1[listHeader[0]]))
        else:
            listHeader = list(dictData.keys())
            totalData =  range(len(dictData[listHeader[0]]))
    for i in totalData:
        tables = ""
        for j in listHeader:
            space = spaceBorder(j)
            if dictData1 != None and j in dictData1:
                val = dictData1[j][i]
            else:
                val = dictData[j][i]
            if j == 'Nilai UTS' or j == 'Nilai UAS':
                tables += f"{val:^{space}.2f} | "
            else:
                tables += f"{val:^{space}} | "
        print(tables[:-3])


# Function untuk me-generate grades dari data nilai
def finalGrades(nilai):
    if nilai >= 80 and nilai <=100 : 
        return "A" 
    elif nilai >= 70 and nilai < 80 :
        return "B"
    elif nilai >= 60 and nilai < 70 :
        return "C"
    else:
        return "D"


# Function untuk menentukan kelulusan atau hasil akhir dengan warna hijau untuk lulus dan merah untuk tidak lulus
def summary(grade):
    if grade in ['A','B','C']: 
        return "\033[32mLulus\033[0m"
    else:
        return "\033[91mTidak Lulus\033[0m"


# Function untuk membuat dan atau mengolah data sesuai dengan kebutuhan yang dikehendaki user yang melibatkan antara
# dictionary sementara dan dictionary source
def dataConfig(src1,tgt1,num,src2=None,tgt2=None,src3=None,tgt3=None): 
    listHeader = []
    if tgt1 is not None:
        listHeader += list(tgt1.keys())
    if tgt2 is not None:
        listHeader += list(tgt2.keys())        
    listDict = {"dictDS":tgt1,"dictUTS":tgt2,"dictUAS":tgt3}
    listRef = {"dictDS":src1,"dictUTS":src2,"dictUAS":src3}
    totalNilai = 0
    for j in listHeader:
        for k in listDict:
            dictCreate = listDict[k]
            dictRef = listRef[k]
            if dictCreate is None or dictRef is None:
                continue
            if j not in dictCreate:
                continue
            if j == 'Nilai UTS' or j == 'Nilai UAS':
                totalNilai += dictRef[j][num]
            if j == 'Grades':
                finalMark = int(totalNilai / 2)
                dictCreate[j].append(finalGrades(finalMark))
                continue
            if j == 'Kelulusan':
                finalMark = totalNilai / 2
                dictCreate[j].append(summary(finalGrades(finalMark)))
                continue
            dictCreate[j].append(dictRef[j][num])


# Function untuk membuat list Module dan Data Scope pada setiap Module nya apabila ada
def listOptions(data,type,num):
    y = 0
    print(f"\n{"-"*60}\n")
    for i in data:
        if y == 0:
            if type == "Menu":
                print(f"{" " * 5 + "=" * 45}")
                print(f"{" " * 5 + "---- " + type + " " + str(num) + ": " + i + " ----"}")
                print(f"{" " * 5 + "=" * 45}\n")
            else:
                print(f"{" " * 5 + "==== " + type + " " + str(num) + ": " + i + " ===="}\n")
        else:
            print(f"{" " * 5 + str(y) + ". " + i}")
        y += 1
    print("\n")


# Function untuk input data atau pilihan sekaligus validasi terkait dengan data yang telah di-input
def inputValidation(dataList,txt,type,datatype=None,loopProcess=None):
    while True:
        if datatype == "string":
            key = input(f"Masukkan {txt} yang ingin di proses: ")
        else:
            key = int(input(f"Masukkan {txt} yang ingin di proses: "))
        if key in dataList:
            if type == "check":
                return key
            else:
                print(warnMsg(f"{txt} yang anda masukkan sudah terdapat pada data!"))
                if loopProcess != None:
                    continue
        else:
            if type == "check":
                print(warnMsg(f"{txt} yang anda masukkan salah, silahkan masukkan kembali!"))
                if loopProcess != None:
                    continue
            else:
                return key
        return None


# Function untuk menghapus data pada dictionary sementara
def deleteDict(src):
    listHeader = []
    listDict = {}
    for i in range(len(src)):
        data = src[i]
        listHeader += list(data.keys())
        listDict[f"dict{i}"] = data
    for j in listHeader:
        for k in listDict:
            if j not in listDict[k]:
                continue
            listDict[k][j].clear()


# Function untuk menampilka data dalam bentuk list sesuai dengan apa yang telah ditentukan oleh user
def listofData(key):
    print(f"\n{"-"*60}\nData siswa yang akan di hapus: \n")
    idx = dataSiswa["Student Id"].index(key)
    listHeader = list(dataSiswa.keys()) + list(nilaiUTSSiswa.keys()) + list(nilaiUASSiswa.keys())
    listDict = {"dictDs":dataSiswa,"dictUTS":nilaiUTSSiswa,"dictUAS":nilaiUASSiswa}
    checkUTS = []
    for i in listHeader:
        esc = False
        for j in listDict:
            if i not in listDict[j]:
                continue
            if j == "dictUTS":
                if i in checkUTS:
                    continue
                print(f"- Nilai UTS {i}: {listDict[j][i][idx]}")
                checkUTS.append(i)
                esc = True
                continue
            elif j == "dictUAS":
                if esc:
                    continue
                print(f"- Nilai UAS {i}: {listDict[j][i][idx]}")
                continue
            print(f"- {i}: {listDict[j][i][idx]}")


# Function untuk membuat, mengolah, dan menampilkan data, yang mana function ini mengcompile function dataConfig, 
# headerConfig, dan tableConfig sehingga bisa menjadi lebih efisien
def tableDataDisplay(msg,key,listData,src1,tgt1,src2=None,tgt2=None,src3=None,tgt3=None,header=None,madeuplist=None,excepted=None):
    if madeuplist:
        for i in listData:
            dataConfig(src1,tgt1,i,src2,tgt2,src3,tgt3)
    else:
        for i in range(len(listData)):
            if listData[i] == key:
                dataConfig(src1,tgt1,i,src2,tgt2,src3,tgt3)
    if header != None:
        headerConfig("Informasi Data Diri Siswa Harapan Bangsa Academy",tgt1)
        tableConfig(tgt1)
        print("\n")
    for i in msg:
        if i == "Nilai Ujian Akhir Semester":
            data = tgt3
        else:
            data = tgt2
        headerConfig(f"Informasi {i} Siswa Harapan Bangsa Academy",data,tgt1,excepted)
        tableConfig(data,tgt1,excepted)
        print("\n")


# Function untuk meminta konfirmasi user sebelum melanjutkan proses data
def confirmation(txt,ans1,ans2):
    while True:
        answer = input(txt)
        if answer == ans1:
            return True
        elif answer == ans2:
            return False
        else:
            print(warnMsg("Pilihan yang anda masukkan salah, silahkan masukkan kembali!"))


# Function untuk membuat title atau penutup sehingga ada border dan juga center align
def titlePlatform(title,num):
    print(f"\n{"="*num:^100}")
    for i in title.split("\n"):
        print(f"{i:^100}")
    print(f"{"="*num:^100}\n")



# =============================================================================  MAIN MENU HANDLER FUNCTIONS  =============================================================================
# // Functions yang digunakan untuk memproses masing-masing menu utama yang di jalankan berdasarkan input atau 
#    pilihan dari user.
# // Functions ini dipanggil pada bagian Main Program / Main Code


# Handler functions untuk menampilkan pilihan menu pada program Academic Information Platform for Students
def mainMenu():
    titlePlatform("Academic Informastion Platform for Students of\nHarapan Bangsa International Academy",50)
    menuProgram = (f"Menu Platform Informasi Data Siswa\n"
                   f"{"-"*35}\n"
                   f"1. Penyajian Data Siswa\n"
                   f"2. Penambahan Data Siswa Baru\n"
                   f"3. Pembaharuan Data Siswa\n"
                   f"4. Penghapusan Data Siswa\n"
                   f"5. Rangkuman Data Siswa\n"
                   f"6. Keluar Platform")
    for y in menuProgram.split("\n"):
        print(" " * 25 + y)
    print("\n\n")
    global programInput 
    programInput = int(input("Masukkan nomor menu yang akan diproses: "))
    return programInput


# Handler functions untuk menjalankan proses menu 1: Penyajian Data Siswa
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Deskripsi:
# - Terdapat 3 Information Module dan 3 Jenis Data Scope pada Information Module 2, dengan struktur sebagai berikut:
#     1. Module 1: Informasi Data Diri Siswa
#     2. Module 2: Informasi Detail Nilai Siswa
#          a. Data Scope 1: Detail Nilai Pribadi Siswa
#          b. Data Scope 2: Detail Nilai Berdasarkan Kelas
#          c. Data Scope 3: Kembali ke Module
#     3. Module 3: Kembali ke Menu Utama
def menu1():
    while True:
        try:
            programs = ['Penyajian Data Siswa' , 'Informasi Data Diri Siswa' ,                          # -- List text untuk ditampilkan di Display Module (Menu 1) process
                        'Informasi Detail Nilai Siswa' , 'Kembali ke Menu Utama']
            listOptions(programs,"Menu",1)                                                              # -- Display Module (Menu 1)
            subMenu = int(input("Masukkan nomor Information Module Menu 1: "))                          # -- User input pilihan Module (Menu 1)
            if subMenu == 1:                                                                            # -- Processing Module 1 == informasi Data Diri Siswa
                headerConfig("Informasi Data Diri Siswa Harapan Bangsa Academy",dataSiswa)              # -- Membuat judul dan header table informasi data diri siswa
                tableConfig(dataSiswa)                                                                  # -- Membuat tabel informasi data diri siswa secara keseluruhan 
                print("\n\n")
            elif subMenu == 2:                                                                          # -- Processing Module 2 == informasi Detail Nilai Siswa
                while True:
                    programs = ['Informasi Detail Nilai Siswa' , 'Detail Nilai Pribadi Siswa' ,         # -- List text untuk ditampilkan di Data Scope Module 2 process
                                'Detail Nilai Berdasarkan Kelas' , 'Kembali ke Module']
                    listOptions(programs,"Module",2)                                                    # -- Display Data Scope Module 2
                    dataType = int(input("Masukkan Data Scope yang ingin diproses: "))                  # -- User input pilihan Data Scope pada Module 2
                    dataInfo = ['Nilai Ujian Tengah Semester','Nilai Ujian Akhir Semester']             # -- List text sebagai judul pada saat menampilkan data tabel
                    if dataType == 1:                                                                   # -- Porcessing Data Scope 1 == Informasi Nilai per Siswa
                        primKey = inputValidation(dataSiswa["Student Id"],"Student Id","check")         # -- User input student Id sekaligus validasi input tersebut 
                        if primKey == None:                                                             # -- Hasil return input student id tidak ditemukan > break loop
                            break
                        tableDataDisplay(dataInfo,primKey,dataSiswa["Student Id"],dataSiswa,dictDS,     # -- Process function untuk membuat, mengolah, dan menampilkan
                                       nilaiUTSSiswa,dictNSUTS,nilaiUASSiswa,dictNSUAS,excepted=3)      #    informasi nilai siswa sesuai dengan Student Id yang di input
                        print("\n")
                    elif dataType == 2:                                                                 # -- Porcessing Data Scope 2 == Informasi Nilai per Kelas
                        kelasIdx = []                                                                   # -- List kosong untuk menyimpan index daftar setiap siswa
                        primKey = inputValidation([10,11,12],"kelas","check")                           # -- User input kelas sekaligus validasi input tersebut
                        if primKey == None:                                                             # -- Hasil return input kelas tidak ditemukan > break loop
                            break
                        for i in range(len(dataSiswa["Kelas"])):                                        # -- Process loop untuk mengumpulkan index daftar setiap siswa
                            if dataSiswa["Kelas"][i] == primKey:                                        #    pada list kosong kelasIdx berdasarkan kelas yang telah diinput
                                kelasIdx.append(i)
                        tableDataDisplay(dataInfo,primKey,kelasIdx,dataSiswa,dictDS,nilaiUTSSiswa,      # -- Process function untuk membuat, mengolah, dan menampilkan
                                       dictNSUTS,nilaiUASSiswa,dictNSUAS,madeuplist="Yes",excepted=3)   #    informasi nilai siswa sesuai dengan kelas yang di input
                        print("\n")
                    elif dataType == 3:                                                                 # -- Porcessing Data Scope 3 == Kembali ke Module
                        break
                    else:
                        print(warnMsg("Pilihan yang anda masukkan salah, silahkan masukkan kembali!"))  # -- Warning message jika input pada Data Scope tidak sesuai
                        continue
                    if confirmation("Apakah anda ingin menghapus permohonan " \
                    "tampilan data saat ini? (Ya/Tidak): ","Ya","Tidak"):                               # -- Function konfirmasi terkait dengan tampilan data saat ini
                        deleteDict([dictDS,dictNSUTS,dictNSUAS])                                        # -- Menghapus data pada dictionary sementara, supaya tidak tumpang tindih                        
            elif subMenu == 3:                                                                          # -- Processing Module 3 == Kembali ke Menu Utama
                break
            else:
                print(warnMsg("Nomor yang anda masukkan salah, silahkan masukkan kembali!"))            # -- Warning message jika input pada Module tidak sesuai
        except ValueError:
            print(warnMsg("Dimohon input angka!"))                                                      # -- Warning message jika input harus angka tapi tidak sesuai


# Handler functions untuk menjalankan proses menu 2: Penambahan Data Siswa
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Deskripsi:
# - Terdapat 3 Information Module, dengan struktur sebagai berikut:
#     1. Module 1: Input Data Diri dan Nilai Siswa Baru
#     2. Module 2: Kembali ke Menu Utama
def menu2():
    while True:
        try:
            programs = ['Penambahan Data Siswa Baru' , 'Input Data Diri dan Nilai Siswa Baru' ,         # -- List text untuk ditampilkan di Display Module (Menu 2) process
                        'Kembali ke Menu Utama']
            listOptions(programs,"Menu",2)                                                              # -- Display Module (Menu 2)
            subMenu = int(input("Masukkan nomor Information Module Menu 2: "))                          # -- User input pilihan Module (Menu 2)
            if subMenu == 1:                                                                            # -- Processing Module 1 == PInput Data Diri dan Nilai Siswa Baru
                primKey = inputValidation(dataSiswa["Student Id"],"Student Id","add")                   # -- User input student Id sekaligus validasi input tersebut 
                if primKey == None:                                                                     # -- Hasil return input student id tidak ditemukan > break loop
                    continue
                listHeader =(list(dataSiswa.keys())[:5] +                                               # -- List kolom berdasarkan header dari dictionary source untuk
                             list(nilaiUTSSiswa.keys()) + list(nilaiUASSiswa.keys()))                   #    membuat data tabel baru
                listDict = {"dictDS":dictDS,"dictNSUTS":dictNSUTS,"dictNSUAS":dictNSUAS}                # -- List dictionary sementara untuk menampung dan membuat data baru
                listCheck = []                                                                          # -- List kosong untuk menyimpan header yang sudah di proses, untuk
                                                                                                        #    membedakan input nilai UTS dan UAS pada proses loop header
                for i in listHeader:                                                                    # -- Proses looping untuk menambahkan data ke dictionary sementara
                    if i in ['Student Id','Kelas','Matematika','IPA','IPS','B.Inggris']:                # -- Proses input data apabila data type nya berupa integer
                        if i in listCheck and i in ['Matematika','IPA','IPS','B.Inggris']:              # -- Proses input data nilai siswa dengan redaksi Ujian Akhir Semester
                            data = int(input(f"Masukkan data nilai {i} "                                #    jika header mapel sudah ter looping dan tertampung pada listCheck
                                             f"Ujian Akhir Semester siswa baru: "))
                        elif i in ['Matematika','IPA','IPS','B.Inggris']:                               # -- Proses input data nilai siswa dengan redaksi Ujian Tengah Semester
                            data = int(input(f"Masukkan data nilai {i} "                                #    jika header mapel baru ter looping dan tidak add pada listCheck
                                             f"Ujian Tengah Semester siswa baru: "))
                        else:
                            if i == 'Student Id':                                                       # -- Jika proses loop header nya adalah Student Id, maka tidak perlu
                                data = primKey                                                          #    input, data diambil saat proses input dan validasi Student Id 
                            else:
                                data = int(input(f"Masukkan data {i} siswa baru: "))                    # -- Proses untuk menginput kelas, data selain nilai dan Student Id 
                        listCheck.append(i)                                                             # -- Menambahkan value loop header (i) pada listCheck
                    else:
                        data = input(f"Masukkan data {i} siswa baru: ")                                 # -- Proses input data apabila data type nya selain integer
                    check = []                                                                          # -- List kosong untuk menyimpan header yang sudah di proses, untuk
                                                                                                        #    membedakan input nilai UTS dan UAS, pada proses loop dictionary
                    for j in listDict:                                                                  # -- Proses loop memasukkan value header (i) ke dalam dictionary masing - masing
                        dictCreate = listDict[j]                                                        # -- Membuat variable untuk masing - masing dictionary (j) pada proses loop
                        if i not in dictCreate:                                                         # -- Jika header (i) tidak terdapat dalam dictionary (j), maka
                                continue                                                                #    lanjutkan proses loop ke dictionary selanjutnya
                        else:
                            if j == "dictNSUTS" or j == "dictNSUAS":                                    # -- Menentukan header nilai (i) untuk dimasukkan di dictionary UTS atau UAS
                                if len(dictCreate[i]) >= len(dictDS["Student Id"]):                     # -- Kondisi ini akan terjadi pada saat prosees loop header nilai (i) bagian
                                    continue                                                            #    dictionary (j) UTS
                                if i in check:                                                          # -- Kondisi ini akan terjadi pada saat prosees loop header nilai (i) bagian
                                    continue                                                            #    dictionary (j) UAS
                        dictCreate[i].append(data)                                                      # -- Menambahkan value (i) pada dictionary (j) yang telah sesuai dan divalidasi
                        check.append(i)                                                                 # -- Menambahkan value loop header (i) pada check
                scoreEx = {"UTS":dictNSUTS,"UAS":dictNSUAS}                                             # -- List dictionary sementara UTS dan dictionary sementara UAS
                for k in scoreEx:                                                                       # -- Proses loop untuk membuat nilai rata - rata UTS dan UAS yang baru
                    nilai = 0
                    for l in range(len(dictDS["Student Id"])):                                          # -- Proses loop untuk mencari index student id yang sesuai dengan primKey
                        if dictDS["Student Id"][l] == primKey:
                            for j in list(scoreEx[k].keys()):                                           # -- Proses loop untuk menjumlahkan setiap nilai pada dictioanry (k) yang
                                val = scoreEx[k][j][l]                                                  #    telah sesuai dengan primKey       
                                nilai += val
                    dictDS[f"Nilai {k}"].append(nilai/4)                                                # -- Proses menambahkan nilai yang telah dijumlahkan ke header nilai UTS/UAS
                if confirmation("\nApakah anda yakin ingin " \
                "menyimpan data nya? (Ya/Tidak): ","Ya","Tidak"):                                       # -- Process function untuk meminta konfirmasi user untuk menyimpan data baru
                    dataInfo = ['Nilai Ujian Tengah Semester','Nilai Ujian Akhir Semester']             
                    tableDataDisplay(dataInfo,primKey,dictDS["Student Id"],dictDS,dataSiswa,dictNSUTS,  # -- Process function untuk menambahkan data siswa baru ke dalam dictionary
                                   nilaiUTSSiswa,dictNSUAS,nilaiUASSiswa,"Yes",excepted=3)              #    source dan menampilkan informasi data diri beserta nilai
                    print(succeedMsg("Selamat data siswa baru telah berhasil dimasukkan!"))             # -- Confirmation message bahwa data baru berhasil di simpan
                    print("\n")
                    break
                deleteDict([dictDS,dictNSUTS,dictNSUAS])                                                # -- Menghapus data pada dictionary sementara, supaya tidak tumpang tindih
                break
            elif subMenu == 2:                                                                          # -- Processing Module 2 == Kembali ke Menu Utama
                break
            else:
                print(warnMsg("Nomor yang anda masukkan salah, silahkan masukkan kembali!"))            # -- Warning message jika input pada Module tidak sesuai
        except ValueError:
            print(warnMsg("Dimohon input angka!"))                                                      # -- Warning message jika input harus angka tapi tidak sesuai
            deleteDict([dictDS,dictNSUTS,dictNSUAS])                                                    # -- Menghapus data pada dictionary sementara pada saat error


# Handler functions untuk menjalankan proses menu 3: Pembaharuan Data Siswa
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Deskripsi:
# - Terdapat 2 Information Module, dengan struktur sebagai berikut:
#     1. Module 1: Perbarui Data Diri atau Nilai Siswa
#     2. Module 2: Kembali ke Menu Utama
def menu3():
    while True:
        try:
            programs = ['Pembaharuan Data Siswa' , 'Perbarui Data Diri atau Nilai Siswa' ,              # -- List text untuk ditampilkan di Display Module (Menu 3) process
                         'Kembali ke Menu Utama']
            listOptions(programs,"Menu",3)                                                              # -- Display Module (Menu 3)
            subMenu = int(input("Masukkan nomor Information Module Menu 3: "))                          # -- User input pilihan Module (Menu 3)
            if subMenu == 1:                                                                            # -- Processing Module 1 == Perbarui Data Diri atau Nilai Siswa
                primKey = inputValidation(dataSiswa["Student Id"],"Student Id","check")                 # -- User input student Id sekaligus validasi input tersebut
                if primKey == None:                                                                     # -- Hasil return input student id tidak ditemukan > break loop
                    continue
                idx = dataSiswa["Student Id"].index(primKey)                                            # -- Mendpatkan index pada Student Id yang telah diinput
                listofData(primKey)                                                                     # -- Menampilkan data sesuai dengan Student Id dalam bentuk list
                print("\n\n")
                if confirmation("Apakah anda ingin melanjutkan untuk " \
                "melakukan perubahan? (Ya/Tidak): ","Ya","Tidak"):                                      # -- Function konfirmasi terkait dengan kelanjutan perubahan data
                    while True:
                        listHeader = (list(dataSiswa.keys()) +                                          # -- List kolom berdasarkan header dari dictionary source sebagai
                                      list(nilaiUTSSiswa.keys()) + list(nilaiUASSiswa.keys()))          #    reference kolom pada saat update data
                        listDict = {"dictDS":dataSiswa,"dictNSUTS":nilaiUTSSiswa,
                                    "dictNSUAS":nilaiUASSiswa}                                          # -- List dictionary source sebagai reference saat update data
                        valChange = inputValidation(listHeader,"Key Data","check","string","Yes")       # -- User input key/header yang akan di update sekaligus validasi
                        updateUTSUAS = False                                                            # -- Variable untuk menyesuaikan data akumulasi nilai UTS / UAS
                        if valChange in ["Student Id" , "Kelas" , "Matematika" ,                        # -- Proses input data input adalah Student Id, kelas, dan nilai
                                         "IPA" , "IPS" , "B.Inggris"]:
                            val = int(input(f"Masukkan data baru pada {valChange} "                     # -- Proses input data apabila data type nya berupa integer
                                            f"yang akan di rubah: "))
                            if valChange in ["Matematika" , "IPA" , "IPS" , "B.Inggris"]:               # -- Proses penambahan dataType jika header yang diganti adalah nilai Siswa
                                updateUTSUAS = True                                                     # -- Value True, maka proses penyesuaian akumulasi nilai UTS / UAS akan diproses
                                if confirmation("Anda akan merubah data pada nilai, " \
                                "nilai tersebut pada UTS atau UAS (UTS/UAS): ","UTS","UAS"):            # -- Function konfirmasi terkait dengan nilai ujian yang akan dirubah
                                    dataType = "UTS"                                                    # -- Jika input UTS maka datatype = UTS
                                else:
                                    dataType = "UAS"                                                    # -- Jika input UAS maka datatype = UAS
                        else:
                            val = input(f"Masukkan data baru pada {valChange} yang akan di rubah: ")    # -- Proses input data apabila data type nya selain integer
                        if confirmation("\nApakah Anda yakin ingin melanjutkan " \
                        "pembaruan data? (Ya/Tidak): ","Ya","Tidak"):                                   # -- Function konfirmasi terkait dengan kelanjutan perubahan data
                            for i in listHeader:                                                        # -- Proses looping untuk mencari header yang sesuai dengan yang sudah diinput
                                if i == valChange:                                                      #    untuk kemudian akan diupdate datanya
                                    for j in listDict:                                                  # -- Proses looping untuk mencari dictioanry tempat header yang sudah diinput
                                        if i not in listDict[j]:                                        # -- Jika header (i) tidak terdapat dalam dictionary (j), maka
                                            continue                                                    #    lanjutkan proses loop ke dictionary selanjutnya
                                        if listDict[j] != dataSiswa:                                    # -- Proses update data jika header (i) berada di dcitionary UTS dan UAS
                                            if dataType == "UTS":                                       # -- Proses update data jika header (i) adalah nilai dan dalam dictionary UTS
                                                nilaiUTSSiswa[i][idx] = val
                                                break
                                            elif dataType == "UAS":                                     # -- Proses update data jika header (i) adalah nilai dan dalam dictionary UAS
                                                nilaiUASSiswa[i][idx] = val
                                                break
                                        listDict[j][i][idx] = val                                       # -- Proses update data jika header (i) adalah selain nilai
                        else:
                            break
                        if updateUTSUAS:                                                                # -- Proses update nilai akumulasi UTS / UAS jika key yang diupdate adalah nilai
                            nilai = 0                                                                   # -- Variable untuk menjumlahkan nilai berdasarkan dataType
                            for k in ["Matematika" , "IPA" , "IPS" , "B.Inggris"]:                      # -- Proses looping untuk menjumlahkan semua nilai berdasarkan dataType
                                if dataType == "UTS":                                                   # -- Proses menjumlahkan nilai dengan dataType UTS
                                    nilai += nilaiUTSSiswa[k][idx]
                                elif dataType == "UAS":                                                 # -- Proses menjumlahkan nilai dengan dataType UTS
                                    nilai += nilaiUASSiswa[k][idx]
                            dataSiswa[f"Nilai {dataType}"][idx] = nilai/4                               # -- Proses merubah data nilai akumulasi UTS / UAS pada dictionary dataSiswa
                        print(succeedMsg(f"Data siswa dengan Student Id {primKey} "
                                         F"telah berhasil diperbarui!"))
                        if confirmation("\nApakah anda ingin melakukan perubahan kembali pada " \
                        "Student Id yang sama? (Ya/Tidak): ","Ya","Tidak"):                             # -- Function konfirmasi terkait dengan perubahan data dengan Student Id sama
                            continue
                        else:
                            break
            elif subMenu == 2:                                                                          # -- Processing Module 2 == Kembali ke Menu Utama
                break
            else:
                print(warnMsg("Nomor yang anda masukkan salah, silahkan masukkan kembali!"))            # -- Warning message jika input pada Module tidak sesuai
        except ValueError:
            print(warnMsg("Dimohon input angka!"))                                                      # -- Warning message jika input harus angka tapi tidak sesuai
            deleteDict([dictDS,dictNSUTS,dictNSUAS])                                                    # -- Menghapus data pada dictionary sementara pada saat error


# Handler functions untuk menjalankan proses menu 4: Penghapusan Data Siswa
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Deskripsi:
# - Terdapat 2 Information Module, dengan struktur sebagai berikut:
#     1. Module 1: Hapus Data Diri atau Nilai Siswa
#     2. Module 2: Kembali ke Menu Utama
def menu4():
    while True:
        try:
            programs = ['Penghapusan Data Siswa' , 'Hapus Data Diri atau Nilai Siswa' ,                 # -- List text untuk ditampilkan di Display Module (Menu 4) process
                        'Kembali ke Menu Utama']
            listOptions(programs,"Menu",4)                                                              # -- Display Module (Menu 4)
            subMenu = int(input("Masukkan nomor Information Module Menu 4: "))                          # -- User input pilihan Module (Menu 4)
            if subMenu == 1:                                                                            # -- Processing Module 1 == Hapus Data Diri atau Nilai Siswa
                primKey = inputValidation(dataSiswa["Student Id"],"Student Id","check")                 # -- User input student Id sekaligus validasi input tersebut
                if primKey == None:                                                                     # -- Hasil return input student id tidak ditemukan > break loop
                    continue
                idx = dataSiswa["Student Id"].index(primKey)                                            # -- Mendpatkan index pada Student Id yang telah diinput
                listofData(primKey)                                                                     # -- Menampilkan data sesuai dengan Student Id dalam bentuk list
                if confirmation(f"\nApakah anda yakin akan menghapus data pada "
                                f"Student Id {primKey}? (Ya/Tidak): ","Ya","Tidak"):                    # -- Function konfirmasi terkait dengan penghapusan data
                    listHeader = (list(dataSiswa.keys()) +                                              # -- List kolom berdasarkan header dari dictionary source sebagai
                                  list(nilaiUTSSiswa.keys()) + list(nilaiUASSiswa.keys()))              #    reference kolom pada saat menghapus data
                    listDict = {"dictDs":dataSiswa,"dictUTS":nilaiUTSSiswa,"dictUAS":nilaiUASSiswa}     # -- List dictionary source sebagai reference saat menghapus data
                    checkUTS = []                                                                       # -- List kosong untuk menyimpan header yang sudah di proses, untuk
                                                                                                        #    membedakan data nilai UTS dan UAS yang akan dihapus
                    for i in listHeader:                                                                # -- Proses looping untuk menghapus data pada dictionary source
                        esc = False                                                                     # -- Escape untuk melanjutkan proses loop pada dictionary UTS / UAS
                        for j in listDict:                                                              # -- Proses looping untuk menyesuaikan header (i) dengan dictionary
                            if i not in listDict[j]:                                                    # -- Jika header (i) tidak terdapat dalam dictionary (j), maka
                                continue                                                                #    lanjutkan proses loop ke dictionary selanjutnya
                            if j == "dictUTS":                                                          # -- Jika dictionary (j) adalah UTS dan header value (i) sudah ada
                                if i in checkUTS:                                                       #    di check UTS maka lanjutkan proses loop dictionary
                                    continue
                                esc = True                                                              # -- Value True supay tidak overlaping ketika looping dictionary UAS
                            elif j == "dictUAS":                                                        # -- Jika dictionary (j) adalah UAS, maka jika esc True header mapel
                                if esc:                                                                 #    nilai yang di proses loop saat ini masih dalam kelompok dictioanry
                                    continue                                                            #    UTS, sehingga lanjut proses loop berikuitnya
                            listDict[j][i].pop(idx)                                                     # -- Proses menghapus data berdasarkan index dictionary, header dan Student Id
                            checkUTS.append(i)                                                          # -- Menambahkan value loop header (i) pada checkUTS
                    print(succeedMsg(f"Data siswa dengan Student Id {primKey} "
                                     f"telah berhasil dihapus!"))                                       # -- Confirmation message bahwa data berhasil di hapus
            elif subMenu == 2:                                                                          # -- Processing Module 1 == Kembali ke Menu Utama
                break
            else:
                print(warnMsg("Nomor yang anda masukkan salah, silahkan masukkan kembali!"))            # -- Warning message jika input pada Module tidak sesuai
        except ValueError:
            print(warnMsg("Dimohon input angka!"))                                                      # -- Warning message jika input harus angka tapi tidak sesuai


# Handler functions untuk menjalankan proses menu 5: Rangkuman Data Siswa
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Deskripsi:
# - Terdapat 2 Information Module dan 3 Data Scope pada Module 1, dengan struktur sebagai berikut:
#     1. Module 1: Rangkuman Nilai dan Status Kelulusan Siswa
#          a. Data Scope 1: Rangkuman Nilai Pribadi Siswa
#          b. Data Scope 2: Rangkuman Nilai Berdasarkan Kelas
#          c. Data Scope 3: Kembali ke Module
#     3. Module 2: Kembali ke Menu Utama
def menu5():
    while True:
        try:
            programs = ['Rangkuman Data Siswa' , 'Rangkuman Nilai dan Status Kelulusan Siswa' ,         # -- List text untuk ditampilkan di Display Module (Menu 5) process
                        'Kembali ke Menu Utama']
            listOptions(programs,"Menu",5)                                                              # -- Display Module (Menu 5)
            subMenu = int(input("Masukkan nomor Information Module Menu 5: "))                          # -- User input pilihan Module (Menu 5)
            if subMenu == 1:                                                                            # -- Processing Module 1 == Rangkuman Nilai dan Status Kelulusan Siswa
                while True:
                    programs = ['Rangkuman Kelulusan Nilai Siswa' , 'Rangkuman Nilai Pribadi Siswa' ,   # -- List text untuk ditampilkan di Data Scope Module 1 process
                                'Rangkuman Nilai Berdasarkan Kelas' , 'Kembali ke Module']
                    listOptions(programs,"Module",1)                                                    # -- Display Data Scope Module 2
                    dataType = int(input("Masukkan Data Scope yang ingin diproses: "))                  # -- User input pilihan Data Scope pada Module 2
                    dataInfo = ['Rangkuman Nilai Hasil Akhir']                                          # -- List text sebagai judul pada saat menampilkan data tabel
                    if dataType == 1:                                                                   # -- Porcessing Data Scope 1 == Rangkuman Nilai Pribadi Siswa
                        primKey = inputValidation(dataSiswa["Student Id"],"Student Id","check")         # -- User input student Id sekaligus validasi input tersebut 
                        if primKey == None:                                                             # -- Hasil return input student id tidak ditemukan > break loop
                            break
                        tableDataDisplay(dataInfo,primKey,dataSiswa["Student Id"],                      # -- Process function untuk membuat, mengolah, dan menampilkan informasi
                                       dataSiswa,dictSummary)                                           #    rangkuman hasil akhir siswa sesuai dengan Student Id yang di input
                    elif dataType == 2:                                                                 # -- Porcessing Data Scope 2 == Rangkuman Nilai Berdasarkan Kelas
                        kelasIdx = []                                                                   # -- List kosong untuk menyimpan index daftar setiap siswa
                        primKey = inputValidation([10,11,12],"kelas","check")                           # -- User input kelas sekaligus validasi input tersebut
                        if primKey == None:                                                             # -- Hasil return input kelas tidak ditemukan > break loop
                            break
                        for i in range(len(dataSiswa["Kelas"])):                                        # -- Process loop untuk mengumpulkan index daftar setiap siswa
                            if dataSiswa["Kelas"][i] == primKey:                                        #    pada list kosong kelasIdx berdasarkan kelas yang telah diinput
                                kelasIdx.append(i)
                        tableDataDisplay(dataInfo,primKey,kelasIdx,dataSiswa,                           # -- Process function untuk membuat, mengolah, dan menampilkan informasi
                                       dictSummary,madeuplist="Yes")                                    #    rangkuman hasil akhir siswa sesuai dengan kelas yang di input
                        print("\n")
                    elif dataType == 3:                                                                 # -- Porcessing Data Scope 3 == Kembali ke Module
                        break
                    else:
                        print(warnMsg("Pilihan yang anda masukkan salah, silahkan masukkan kembali!"))  # -- Warning message jika input pada Data Scope tidak sesuai
                        continue
                    print(succeedMsg(f"Selamat data rangkuman hasil akhir siswa telah berhasil"
                                     "di-generate!"))                                                   # -- Confirmation message bahwa data berhasil di generate
                    if confirmation("Apakah anda ingin menghapus permohonan " \
                    "tampilan data saat ini? (Ya/Tidak): ","Ya","Tidak"):                               # -- Function konfirmasi terkait dengan tampilan data saat ini
                        deleteDict([dictSummary])                                                       # -- Menghapus data pada dictionary sementara, supaya tidak tumpang tindih
            elif subMenu == 2:                                                                          # -- Processing Module 2 == Kembali ke Menu Utama
                break
            else:
                print(warnMsg("Nomor yang anda masukkan salah, silahkan masukkan kembali!"))            # -- Warning message jika input pada Module tidak sesuai
        except ValueError:
            print(warnMsg("Dimohon input angka!"))                                                      # -- Warning message jika input harus angka tapi tidak sesuai



# ===============================================================================  MAIN PROGAM / MAIN CODE  ===============================================================================
# // Ini merupakan main code yang berisi alur utama dari program ini, dimana terdapat pengulangan yang akan diiterasi
#    dan menjalankan masing - masing menu nya sesuai dengan pilihan yang telah ditentukan oleh user
while True:
    try:
        deleteDict([dictDS,dictNSUTS,dictNSUAS])
        mainMenu()
        if programInput == 1:
            menu1()
        elif programInput == 2:
            menu2()
        elif programInput == 3:
            menu3()
        elif programInput == 4:
            menu4()
        elif programInput == 5:
            menu5()
        elif programInput == 6:
            titlePlatform("Terimakasih anda telah keluar dari program Academic Platform for Students of\nHarapan Bangsa International Academy",80)
            break
        else:
            print(warnMsg("Nomor yang anda masukkan salah, silahkan masukkan kembali!"))
    except ValueError:
            print(warnMsg("Dimohon input angka!"))