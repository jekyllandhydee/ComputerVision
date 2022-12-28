#Sıkıştırma fonksiyonu
#Bir array tipinden item değişkenini, dizinin olması gereken eleman(eksen) sayısına kadar tüm değğişkenlerini min ve max değerleri kullanarak matematiksel sıkıştırma fonk ile sıkıştırır.
#Mesela bizim kullandığımız 4 değişkenli ancak 5 boyutlu düzlemde yer alması gerekiyor. O durumda bu fonk bir tane daha eksen ekler.
def arrange(item,dim,min,max):
    item_count,i = len(item),0
    for i in range(dim):
        if(i<=item_count):
            item[i] = item[i]/((max-min)/100)
        else:
            item[i] = 50/((max-min)/100)
    return item

#Öklid uzaklık formülünde kullanmamız gereken hesaplama fonksiyonları
def kokal(x):
    return x**(1/2)

def usal(x):
    return x**2

def vectorSimilarity(A,B):
    #fonksiyona gönderilen A ve B nin eksen sayısı aynı değilse fonk çalışmaz
    if len(A) != len(B):
        return -1
    #eksenler aynı sayıda ise öklid kullanılarak mesafe hesaplamaya devam edilir
    else:
        len_ = len(A)
        total = 0
        for i in range(len_):
            total += usal(B[i] - (A[i]))
        distance = kokal(total)
        #Eğer benzerlik değil de KÜMELEME yapılacasa işlem burada durdurulur.
        #3 eksenli renk uzayımızda olabileccek en uzun meafeyi max_dist değişkeni olarak hesapladık.
        #Bir önceki işlemde bulunan distance değişkenini maks mesafeye bölerek uzaklık oranını 0-1 arasında yaptık
        max_dist = 0
        for i in range(len_):
            max_dist += usal(100)
        max_dist = kokal(max_dist)
        return 1-(distance/max_dist)
    return 0

#Renklerin RGB gösterimi
kirmizi = [255,0,0]
koyuKirmizi = [181,25,25]
kahverengi = [48,34,15]
siyah = [0,0,0]
beyaz = [255,255,255]
gri = [82,82,82]

#arrange(rengin kendisi, RGB = 3  boyutlu, min değer =0,max değer = 255)
#Renklerin normalize edilmiş değerleri üzerinden vektör uzay benzerliği algoritması modellenebildiğinden arrange fonksiyonu ile tüm renkleri normalize etmemiz gerekir.

kirmizi_normalized = arrange(kirmizi,3,0,255)
koyuKirmizi_normalized = arrange(koyuKirmizi,3,0,255)
kahverengi_normalized = arrange(kahverengi,3,0,255)
siyah_normalized = arrange(siyah,3,0,255)
beyaz_normalized = arrange(beyaz,3,0,255)
gri_normalized = arrange(gri,3,0,255)

benzerlik_oranı = vectorSimilarity(siyah_normalized, beyaz_normalized)
print(benzerlik_oranı)
