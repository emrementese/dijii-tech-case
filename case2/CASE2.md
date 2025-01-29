
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