- [DIJI.TECH Backend Quiz](#dijitech-backend-quiz)
  - [CASE-1](#case-1)
    - [Kurulum](#kurulum)
    - [Ortak Görevler (Tüm modeller için Geçerli)](#ortak-görevler-tüm-modeller-için-geçerli)
    - [Görevler](#görevler)
    - [Notlar](#notlar)
    - [Başlarken](#başlarken)
  - [CASE-2](#case-2)
    - [Örnek 1:](#örnek-1)
    - [Örnek 2:](#örnek-2)
    - [Çözüm İçin Notlar](#çözüm-i̇çin-notlar)
  - [CASE-3](#case-3)
    - [Örnek](#örnek)
    - [Örnek 2](#örnek-2-1)
    - [Çözüm İçin Notlar](#çözüm-i̇çin-notlar-1)


# DIJI.TECH Backend Quiz

## CASE-1
Lütfen aşşağıdaki yönergeleri takip ederek görevleri tamamlayın.

### Kurulum
1. Python env oluşturun
2. Requirements.txt oluşturun
3. .gitignore dosyası oluşturun
4. Aşağıdaki Kütüphanelerin Son Versiyonlarını Kurun
   1. Django
   2. Django Rest Framework
      * Başka kütüphaneye ihtiyacınız varsa kurablirsiniz.
5. Django projesi oluşturun
6. Yeni app oluşturun `location` 
7. Modelleri Ekleyin
   1. Country
      1. name
      2. search_text
      3. search_count
      4. code
      5. phone_code
   2. City
      1. name
      2. search_text
      3. search_count
      4. country
   3. Airport
      1. name
      2. search_text
      3. search_count
      4. code
      5. country
      6. city
8. Fixture dosyasındaki verileri data migration oluşturarak yükleyin

### Ortak Görevler (Tüm modeller için Geçerli)

1.  Location Modellerdeki `name`,`search_text` ve `search_count` zorunlu olmalı eklenmediğinde uygulama hata vermeli
2.  Location appte `search_text` alanı için bir management komudu oluşturun.
    1.  `python manage.py XXX`
    2.  Bu command ile tüm location modeller için search text oluşmalı.
    3.  Search text kendi ve üst ilişkideki modellerin name alanını içermeli
           1.  Airport => 'airport.name,airport.city.name,airport.country.name'
3.  Location modelleri için `XXX.objects.search('Ankara')` gibi bir arama yapıldığında en doğru sonuçları getiren `.search` fonksiyonunu yazın.`(models.Manager ve models.QuerySet)`
    1.  Fonksiyon küçük büyük harf duyarlı olmalı
    2.  Unaccent aramalardada sonuç verebilmeli
        1.  Örn: Niğde ve NİgDe aynı sonuçları verebilmeli
4.  Aşağıdaki endpointleri oluşturun (Rest Framework)
    1. Tüm Location Modeller için Search End Point
       1. Yukarıda belirtilen search fonksiyonunu kullanarak en fazla 20 tane sonuç getirecek.
    2. Tüm Location Modeller için Select End Point
       1. Bir lokasyonun seçilmesi sağlanır.
       2. Select olduğunda request içine Cookie ile seçili model ve lokasyonun id'si kayıt edilir.
    3. Deselect End Point
       1. Cookieden seçili olan lokasyonu temizler.
5.  Bir lokasyon seçildiğinde search_count'u artmalı
    1. Aynı Zamanda üst ilişkilerininde search_countu artmalı
6.  Eğer atılan request cookilerinde bir lokasyon seçilmiş ise search_count artmalı
    1. Aynı Zamanda üst ilişkilerininde search_countu artmalı
    2. Response 200 kodu ile dönmüyorsa search_count artmamalı.
7. Eğer yeni bir lokasyon modeli eklenirse örn: `Stations` tüm yapı bu model içinde çalışmalı

### Görevler

1. Counry Most Searched Cities End Point
   1. Ülke kodu gönderilir ve en çok aranan 5 şehiri listelenir
   2. 1 den fazla ülke kodu gönderilebilir.
   3. Sonuçlar ülkeye göre gruplu gelmelidir.
2. Country Search Ratio
   1. Ülke kodu gönderilir ve toplam şehir araması sayısı toplam airport arama sayısına bölünüp bir oran çıkarılır.
   2. Bu oranla birlikte ülke bilgileri geri dönülür.
   3. 1 den fazla ülke kodu gönderilebilir.

### Notlar
1. 1 kullanıcı sadece 1 lokasyon seçebilir.

### Başlarken
1. Projeyi fork edip kendi reponuzu oluşturun
2. `gitignore` ve `requirements.txt` dosyanızın doğru bir şekilde oluşturun.
3. Kodlarınızı olabildiğince temiz ve anlaşılır yazmaya özen gösterin.
4. Kodlarınızı yazarken bildiğiniz en iyi yöntemler ile yazmaya çalışın.
5. Görevlerden çok yazdığınız kodun önemli olduğunu unutmayın.

## CASE-2


Bir ayakkabı firması fabrikaları için en uzakta kalan şubesinin mesafesini hesaplamak istiyor.
Şehirler her zaman 1 km mesafededir, her bir şehirden sadece 1 şehire yol vardır ve yollar dairesel olarak birleşmez.

```
A <-> B <-> C <-> D <-> E
```

Firmanın en az 1 şehirde fabrikası ve her şehirde 1 şubesi olacaktır.
Bu koşullara göre şubelerin en yakın fabrikaya olan mesafelerinin en fazla kaç km olduğunu bulunuz.

### Örnek 1:

Fabrika olan şehiler `[_]` şeklinde gösterilmiştir.

```
[A] <-> B <-> C <-> D <-> [E]
```

-   `A` şehirindeki firmanın en yakın fabrikası `A` şehrindedir -> 0 km
-   `B` şehirindeki firmanın en yakın fabrikası `A` şehrindedir -> 1 km
-   `C` şehirindeki firmanın en yakın fabrikası `A` yada `E` şehrindedir -> 2 km
-   `D` şehirindeki firmanın en yakın fabrikası `E` şehrindedir -> 1 km
-   `E` şehirindeki firmanın en yakın fabrikası `E` şehrindedir -> 0 km

En uzak mesafe 2 km dir ve cevap 2 dir.

### Örnek 2:

Fabrika olan şehiler `[_]` şeklinde gösterilmiştir.

```
[A] <-> [B] <-> [C] <-> [D] <-> [E]
```

-   `A` şehirindeki firmanın en yakın fabrikası `A` şehrindedir -> 0 km
-   `B` şehirindeki firmanın en yakın fabrikası `B` şehrindedir -> 0 km
-   `C` şehirindeki firmanın en yakın fabrikası `C` şehrindedir -> 0 km
-   `D` şehirindeki firmanın en yakın fabrikası `D` şehrindedir -> 0 km
-   `E` şehirindeki firmanın en yakın fabrikası `E` şehrindedir -> 0 km

Her şehirde fabrika olduğu için en uzak mesafe 0 km dir ve cevap 0 dir.

### Çözüm İçin Notlar

-   `case_2.py` dosyası içinde bulunan `getInaccessibleFactory` fonksiyonunda çalışmalarınızı yapınız.
-   `0 < n < 10⁵` değeri şehir sayısıdır.
-   `0 < c <= n` değeri fabrikaların bulunduğu indexlerdir.

```python
def getInaccessibleFactory(n, c):
    # n = 5
    # c = [4,0]
    ...
    ...
    return answer # 2
```


## CASE-3

Farklı grupların 1'er elemanını seçerek seçim kombinasyonları oluşturan fonksiyonu yazınız.

### Örnek

| 1. Grup | 2.Grup |
| ------- | ------ |
| Eylül   | A      |
| Ekim    | B      |

`Eylül` -> `A`,`B` seçimlerini alabilir

`Ekim` -> `A`,`B` seçimlerini alabilir

Seçimler;

Aşağıdaki gibi 4 farklı seçim olabilir

```
- Eylül - A
- Eylül - B
- Ekim - A
- Ekim - B
```

### Örnek 2

| 1. Grup | 2.Grup | 3.Grup |
| ------- | ------ | ------ |
| Eylül   | A      | 1      |
|         | B      | 2      |

`Eylül` -> `A,1`,`A,2`,`B,1`,`B,2` seçimlerini alabilir

Seçimler;

Aşağıdaki gibi 4 farklı seçim olabilir

```
- Eylül - A - 1
- Eylül - A - 2
- Eylül - B - 1
- Eylül - B - 2
```

### Çözüm İçin Notlar

-   `case_3.py` dosyası içinde bulunan `getCombinations` fonksiyonunda çalışmalarınızı yapınız.
-   `2 < n < 7` değeri grup sayısıdır.
-   `c` değeri grupların içerikleridir.
-

```py
def getCombinations(n, c):
    # n = 2
    # c = [[a,j,p],[y,n]]
    ...
    ...
    return answer # [[a,y],[a,n],[j,y],[j,n],[p,y],[p,n]]
```