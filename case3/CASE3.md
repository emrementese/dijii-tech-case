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