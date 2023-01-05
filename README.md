## CRAWLING DATA
- data yang di ambil dari twitter
- menggunakan library snscrape, mengapa menggunakan library ini karena lebih simple tidak perlu register di twitter.developer
- data yang di ambil 5000 data (permintaan)

## PREPROCESING
- preprocesing adalah proses pembersiahan data twit
- library yang digunakan adalah ntlk








#######################################################################################

## ANALISIS DATA ----------------------------------------------------------------------
- saya ada masalah untuk mengakses array yang saya simpen di excel / csv yang tersimpan bentuk aray 
- contoh : ['saya', 'keren']. Masalahnya valae ini tidak bisa saya akses. solusinya pakek literal_eval
- Referensi https://stackoverflow.com/questions/23119472/in-pandas-python-reading-array-stored-as-string
- The ast module (Abstract Syntax Tree) allows us to interact with and modify Python code.
- https://www.aipython.in/python-literal_eval/

## PREPROCESING DATA ------------------------------------------------------------------
- dalam procesing data saya mengikuti tutorial https://yunusmuhammad007.medium.com/text-preprocessing-menggunakan-pandas-nltk-dan-sastrawi-untuk-large-dataset-5fb3c0a88571
- menggunakan library The Natural Language Toolkit (NLTK) https://pypi.org/project/nltk/

# fajar 2022-09-25
## CONVERT NEGATION / NORMALIZATION
- Normalization digunakan untuk menyeragamkan term yang memiliki makna sama namun penulisanya berbeda, bisa diakibatkan kesalahan penulisan,

# fajar 2022-09-23
## FILTERING (STOPWORD REMOVAL) / CLEANSING
- menghapus kata yang mempunyai frekuensi kemunculan yang tinggi misalnya kata penghubung seperti “dan”, “atau”, “tapi”, “akan” dan lainnya.

# fajar 2022-09-23
## TOKENIZING
- Proses tokenizing setiap kata pada tweet dipisahkan, pada proses ini tahap
yang dilakukan adalah memisahkan setiap kata yang dipisahkan oleh spasi

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
## refresi sebagai kiblat pembuatan
- https://blog.sanbercode.com/docs/kelas-privat-python-01/materi-penerapan-python/analisis-sentimen/ 

### SENTIMENT ANALISIS
## Tipe sentimen analisis
- Aspect-based sentiment analysis, digunakan untuk mengetahui aspek apa yang mendapat penilaian positif, netral, atau negatif dari pelanggan.
## Teknik analisis
- Rule-based sentiment analysis, menggunakan kamus kata-kata yang diberi label sentimen tertentu.
