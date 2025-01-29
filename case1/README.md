
### Case-1

### Tamamlanan Görevler

1- Django ve DRF Yapısı Prof. şekidle oluşturuldu

2- Modeller istenilen şekilde hazırlandı

3- Data migration yapılarak fix. klasöründeki veriler Dbye eklendi

4- Custom manager ve queryset kullanılarak localtion modellerine özel search metod Unaccent çalışacak şekilde  yazıldı

5- Tüm Location Modeller için Search End Point yazıldı.

6- Tüm Location Modeller için Select End Point yazıldı

7- Deselect End Point yazıldı

8- search_count' artırımları status kodları ile istenilen şekilde yazıldı

9- Counry Most Searched Cities End Point yazıldı.

10- Country Search Ratio end-point yazıldı

11- search_text için custom manage komutu yazılarak seracg_textlerin oluşturulması sağlandı.

### Ekstralar

1- Knox ile bearer tabanlı auth sistemi ekledim. Ancak sizi yormamak adına permission_class'ları boş bıraktım. Dielrseniz test edebilirsiniz. Şu  anda auth. zorunluluğu yok.

2- API dökümantasyonu için swagger UI kullanarak end-point request-response şemaları oluşturdum böyleleikle open-api standartlarında bir rest-api yazılmış olundu.


3- custom exception hadnler eklenerek uygulamadaki tüm bad requestler ve raislenmeler (serializrer validationları dahil) global bir şekilde ele alınarak otomatik exception responseları oluşturuldu bunlar aynı zamanda swagger şemalarında eklendi

4- Sistemin code QA arttırmak için pre-commit kuruldu ve  pyQA hookları kurularak pep ve flake 8 gibi python standartlarına uyuldu. hatta commit öncesi bunların otomasyonu sağlandı.

5- sistem dockerize edilerek compose yardımıyla ayağa kaldırılması sağlanarak küçük bir Devops çalışması yapıldı.

## Kurum
1.  Docker
    - docker installation
    - docker-compose build
    - docker-compose up -d

        http://localhost:8000/api/

2. Manuel

    - create env
    - install requirements.txt
    - cd src
    - python manage.py migrate
    - python manage.py search_text
    - python manage.py runserver

## Sonuç

- istenilen görevlerin hepsinin yapıp test ettim sağlıklı çalışıyordu. Case güzel olmuş yaparken çok beğendim ancak biraz daha zamanım olsaydı;

    - postgreSQL entegrasyonu
    - .env ve secret yönetimi
    - unit ve entegrasyon test yazılması
    - testler CI da github actionsa bağlanması vs.

    gibi yapmak istediğim ekstra görevleride ekleyecektim :)
