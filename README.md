## PREPROCESING DATA ------------------------------------------------------------------
- dalam procesing data saya mengikuti tutorial https://yunusmuhammad007.medium.com/text-preprocessing-menggunakan-pandas-nltk-dan-sastrawi-untuk-large-dataset-5fb3c0a88571
- menggunakan library The Natural Language Toolkit (NLTK) https://pypi.org/project/nltk/

# fajar 2022-09-23
## CLEANSING
- proses menghilangkan / menghapus komponen dari  tweet yang tidak memiliki pengaruh apapun  pada analisis sentimen

# fajar 2022-09-23
## CASE FOLDING
- proses merubah huruf kapital menjadi huruf kecil dengan tujuan agar semua huruf seragam
- menggunakan pandas, df['Tweet'] = df['Tweet'].str.lower()

## KAMUS DATA -------------------------------------------------------------------------

# fajar 2022-09-25
- kamus data saya ambil dari internet
- entak ini sesuai dengan data tweet yang saya punya atau tidak
- karena butuh cepat juga ya
- saya simpan dengan nama kata_positif dan kata_negatif .txt

## SCRAPING DATA ----------------------------------------------------------------------

# fajar 2022-09-23
## proses fetch data / wraping data 
- wrapping data menggunakan library snscrapper
- link gitHub https://github.com/JustAnotherArchivist/snscrape
- kenapa menggunakan snscrapper ?
- karena penggunaan nya mudah dan tidak perlu apiKey, dan tentu snscrape library legal
- tapi documentasi dari library snscape ini kurang menurut saya
- karena hanya ada gitHubnya saja, jadi jika ingin tau cara pakainya bisa cari di pencarian google karena banyak juga yang menyediakan 
- tutorial cara penggunaannya. Atua kalo mau bisa langsung baca kodingnya di gitHub
- meski begitu gitHubnya masih aktif dan terakhir di perbaruai di bulan january 2022
- star gitHubnya 1.6K
- alasan itu menurut saya sudah cukup untuk saya memilih library ini

# fajar 2022-09-23
## ini adalah project TA freelance
- Judul dari TA ini adalah Analisis Sentiment E-sport di indonesian

# husain-python
freelance