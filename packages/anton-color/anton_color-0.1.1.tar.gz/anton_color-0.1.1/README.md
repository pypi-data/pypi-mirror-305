# Anton-Color

**Anton-Color** adalah modul Python sederhana yang digunakan untuk memberikan warna pada teks di terminal menggunakan ANSI escape codes. Modul ini memungkinkan pengguna untuk menampilkan teks dalam berbagai warna dan latar belakang yang berbeda, serta memberikan gaya tambahan seperti bold.

## Instalasi

Untuk menginstal modul ini, gunakan pip:

```bash
pip install anton-color
```

## WARNA TEKS
Berikut adalah daftar warna teks yang dapat digunakan:

- `red`: Warna merah.
- `green`: Warna hijau.
- `yellow`: Warna kuning.
- `blue`: Warna biru.
- `purple`: Warna ungu.
- `cyan`: Warna cyan.
- `white`: Warna putih.
- `black`: Warna hitam.

## WARNA TEKS BRIGHT
Warna teks cerah yang dapat digunakan:

- `brightRed`: Merah cerah.
- `brightGreen`: Hijau cerah.
- `brightYellow`: Kuning cerah.
- `brightBlue`: Biru cerah.
- `brightPurple`: Ungu cerah.
- `brightCyan`: Cyan cerah.
- `brightWhite`: Putih cerah.
- `brightBlack`: Hitam cerah.

## WARNA LATAR BELAKANG
Berikut adalah daftar warna latar belakang yang dapat digunakan:

- `bgRed`: Latar belakang merah.
- `bgGreen`: Latar belakang hijau.
- `bgYellow`: Latar belakang kuning.
- `bgBlue`: Latar belakang biru.
- `bgPurple`: Latar belakang ungu.
- `bgCyan`: Latar belakang cyan.
- `bgWhite`: Latar belakang putih.
- `bgBlack`: Latar belakang hitam.

## WARNA LATAR BELAKANG BRIGHT
Warna latar belakang cerah yang dapat digunakan:

- `bgBrightRed`: Latar belakang merah cerah.
- `bgBrightGreen`: Latar belakang hijau cerah.
- `bgBrightYellow`: Latar belakang kuning cerah.
- `bgBrightBlue`: Latar belakang biru cerah.
- `bgBrightPurple`: Latar belakang ungu cerah.
- `bgBrightCyan`: Latar belakang cyan cerah.
- `bgBrightWhite`: Latar belakang putih cerah.
- `bgBrightBlack`: Latar belakang hitam cerah.

## COLOR BOLD
Berikut adalah warna dengan gaya bold:

- `boldRed`: Merah tebal.
- `boldGreen`: Hijau tebal.
- `boldYellow`: Kuning tebal.
- `boldBlue`: Biru tebal.
- `boldPurple`: Ungu tebal.
- `boldCyan`: Cyan tebal.
- `boldWhite`: Putih tebal.
- `boldBlack`: Hitam tebal.

## WARNA DYNAMIC
Warna dinamis yang dapat digunakan:

- `dynamicOrange`: Warna oranye dinamis.
- `dynamicPink`: Warna pink dinamis.
- `dynamicAqua`: Warna aqua dinamis.
- `dynamicSoftPurple`: Warna ungu lembut dinamis.
- `dynamicSkyBlue`: Warna biru langit dinamis.
- `dynamicMintGreen`: Warna hijau mint dinamis.

## WARNA TAMBAHAN
Berikut adalah warna tambahan yang tersedia:

- `teal`: Warna teal.
- `peach`: Warna peach.
- `lavender`: Warna lavender.
- `olive`: Warna olive.
- `magentaCerah`: Warna magenta cerah.
- `chartreuse`: Warna chartreuse.
- `orangeTerang`: Warna oranye terang.
- `rosePink`: Warna pink mawar.
- `coral`: Warna koral.
- `seaGreen`: Warna hijau laut.
- `goldenrod`: Warna goldenrod.
- `turquoise`: Warna turquoise.
- `salmon`: Warna salmon.
- `limeGreen`: Warna hijau limau.

## RESET COLOR
- `reset`: Mengembalikan warna ke pengaturan default.

## Contoh Penggunaan
Berikut adalah contoh cara menggunakan warna dalam teks:

```python
from anton_color import Clr

print(Clr.red("Ini teks merah"))  # Menampilkan teks merah
print(Clr.bgGreen("Ini latar belakang hijau"))  # Menampilkan teks dengan latar belakang hijau
print(Clr.brightYellow("Ini teks kuning cerah"))  # Menampilkan teks kuning cerah
print(Clr.boldBlue("Ini teks biru tebal"))  # Menampilkan teks biru dengan gaya tebal
```

## Lisensi

Modul ini dilisensikan di bawah [MIT License](LICENSE).