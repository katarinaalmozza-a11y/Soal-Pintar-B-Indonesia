import random

label = ["A", "B", "C", "D"]

# =====================================
# BANK SOAL (10 SOAL PER LEVEL)
# Format: (soal, jawaban, alasan)
# =====================================

bank_soal = {
    "mudah": [
        ("Antonim dari kata 'tinggi' adalah", "rendah",
         "Antonim adalah lawan kata. Lawan dari 'tinggi' adalah 'rendah'."),
        ("Lawan kata dari 'panas' adalah", "dingin",
         "'Dingin' merupakan lawan kata dari 'panas'."),
        ("Kalimat tanya diakhiri tanda", "?",
         "Kalimat tanya selalu diakhiri tanda tanya (?)."),
        ("Media cetak contohnya adalah", "koran",
         "Koran dicetak di kertas sehingga termasuk media cetak."),
        ("Sinonim dari kata 'indah' adalah", "elok",
         "'Elok' memiliki arti yang sama dengan 'indah'."),
        ("Sinonim dari kata 'rajin' adalah", "tekun",
         "'Tekun' berarti giat dan bersungguh-sungguh, sama dengan 'rajin'."),
        ("Kata baku dari 'resiko' adalah", "risiko",
         "Menurut KBBI, bentuk baku yang benar adalah 'risiko'."),
        ("Huruf pertama pada awal kalimat harus menggunakan huruf", "kapital",
         "Setiap awal kalimat harus diawali huruf kapital."),
        ("Tanda baca untuk mengakhiri kalimat berita adalah", ".",
         "Kalimat berita diakhiri tanda titik (.)"),
        ("Lawan kata dari 'besar' adalah", "kecil",
         "'Kecil' merupakan antonim dari 'besar'.")
    ],

    "sulit": [
        ("Paragraf dengan gagasan utama di awal disebut", "deduktif",
         "Paragraf deduktif memiliki gagasan utama di awal paragraf."),
        ("Paragraf dengan gagasan utama di akhir disebut", "induktif",
         "Paragraf induktif memiliki gagasan utama di akhir paragraf."),
        ("Kalimat yang berisi pendapat disebut", "opini",
         "Opini adalah kalimat yang berisi pendapat seseorang."),
        ("Laporan hasil pengamatan harus bersifat", "objektif",
         "Laporan pengamatan harus berdasarkan fakta, bukan pendapat pribadi."),
        ("Cerita yang tidak benar-benar terjadi disebut", "fiksi",
         "Fiksi adalah cerita rekaan atau khayalan."),
        ("Cerita yang berdasarkan kenyataan disebut", "nonfiksi",
         "Nonfiksi adalah karya yang berdasarkan fakta atau kenyataan."),
        ("Puisi yang tidak terikat aturan disebut", "puisi bebas",
         "Puisi bebas tidak terikat jumlah baris, rima, atau suku kata."),
        ("Drama adalah karya sastra yang berbentuk", "dialog",
         "Drama disajikan dalam bentuk percakapan atau dialog."),
        ("Amanat dalam cerita berarti", "pesan",
         "Amanat adalah pesan moral yang ingin disampaikan penulis."),
        ("Tokoh utama dalam cerita disebut", "protagonis",
         "Protagonis adalah tokoh utama dalam cerita.")
    ],

    "sangat sulit": [
        ("Puisi lama yang terikat aturan disebut", "puisi lama",
         "Puisi lama terikat aturan jumlah baris, rima, dan suku kata."),
        ("Sudut pandang 'aku' dalam cerita disebut", "orang pertama",
         "Sudut pandang orang pertama menggunakan kata 'aku' atau 'saya'."),
        ("Sudut pandang 'dia' disebut", "orang ketiga",
         "Sudut pandang orang ketiga menggunakan kata 'dia' atau nama tokoh."),
        ("Persamaan bunyi pada akhir baris puisi disebut", "rima",
         "Rima adalah pengulangan bunyi pada akhir baris puisi."),
        ("Peribahasa 'besar pasak daripada tiang' berarti", "lebih besar pengeluaran daripada pendapatan",
         "Peribahasa ini bermakna pengeluaran lebih besar daripada pemasukan."),
        ("Kata yang memiliki banyak makna disebut", "polisemi",
         "Polisemi adalah kata yang memiliki lebih dari satu makna."),
        ("Gabungan dua kata yang menghasilkan makna baru disebut", "kata majemuk",
         "Kata majemuk adalah gabungan dua kata yang membentuk arti baru."),
        ("Kata hubung disebut juga", "konjungsi",
         "Konjungsi adalah kata penghubung antar kata, frasa, atau kalimat."),
        ("Pengulangan kata dalam bahasa Indonesia disebut", "reduplikasi",
         "Reduplikasi adalah proses pengulangan kata."),
        ("Ungkapan yang maknanya tidak sebenarnya disebut", "idiom",
         "Idiom adalah gabungan kata yang memiliki makna kiasan.")
    ]
}

opsi_salah = [
    "besar", "malas", "fakta", "televisi", "!", 
    "cantik", "rumah", "cepat", "meja", "jalan"
]

# =====================================
# PILIH LEVEL
# =====================================

print("=== KUIS BAHASA INDONESIA ===")
print("1. Mudah")
print("2. Sulit")
print("3. Sangat Sulit")

pilihan = input("Pilih level (1/2/3): ")

if pilihan == "1":
    level = "mudah"
elif pilihan == "2":
    level = "sulit"
elif pilihan == "3":
    level = "sangat sulit"
else:
    print("Pilihan tidak valid, otomatis Mudah.")
    level = "mudah"

soal_terpilih = random.sample(bank_soal[level], 10)
skor = 0

# =====================================
# PROSES KUIS
# =====================================

for i, (soal, jawaban, alasan) in enumerate(soal_terpilih):
    opsi = set()
    opsi.add(jawaban)

    while len(opsi) < 4:
        salah = random.choice(opsi_salah)
        if salah != jawaban:
            opsi.add(salah)

    opsi = list(opsi)
    random.shuffle(opsi)

    print(f"\nSoal {i+1}: {soal} ...")
    for j in range(4):
        print(f"{label[j]}. {opsi[j]}")

    jawab = input("Jawaban (A/B/C/D): ").upper()

    if jawab in label and opsi[label.index(jawab)] == jawaban:
        skor += 10
        print("✅ BENAR")
        print("Alasan:", alasan)
    else:
        print("❌ SALAH")
        print("Jawaban benar:", jawaban)
        print("Alasan:", alasan)

print("\nSkor akhir:", skor)
print("Nilai akhir:", skor, "%")
