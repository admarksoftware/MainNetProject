# Java ile bir kredi başvuru sistemi

Bir kredi başvuru sistem için, kredi başvuru isteklerin alıp ilgili kriterlere göre müşteriye
kredi sonucunu dönen servisin içinde yer alacak restful bir endpoint’in Java 
(Spring Boot) kütüphanesi kullanılarak yazılması ve isteğe bağlı olarak önyüzünün
yazılması.
# - Backend :
Kullanıcıdan kimlik numarası, ad-soyad, aylık gelir ve telefon bilgileri alınarak, kimlik numarasıyla daha önceden yazıldığı kredi skoru servisine gidlir ve ilgili kişiye ait kredi skoru alınarak aşağıdaki kurallara göre kullanıcıya kredi sonucu gösterilir.
(Onay veya Red olarak iki seçenek olabilir.)
# - Frontend:
Kimlik numarası, ad-soyad, aylık gelir ve telefon bilgileri form ile alınır ve kullanıcıya kredi sonucu ve kredi limiti gösterilir.
(Arayüz tasarımı olarak JavaScript, HTML, CSS Kullanılmıştır.)
# - Kurallar
Kredi skoru 500’ün altında ise kullanıcı reddedilir. (Kredi sonucu: Red)
- Kredi skoru 500 puan ile 1000 puan arasında ise ve aylık geliri 5000 TL’nin altında ise kullanıcının kredi başvurusu onaylanır ve kullanıcıya 10.000 TL limit atanır.
(Kredi Sonucu: Onay)
- Kredi skoru 1000 puana eşit veya üzerinde ise kullanıcıya AYLIK GELİR BİLGİSİ *
KREDİ LİMİT ÇARPANI kadar lmt atanır. (Kred Sonucu: Onay)
- Kredinin neticelenmesi sonucunda ilgili başvuru vertabanına kaydedilir  ve
endpoint’ten onay durum bilgisi (red veya onay), limit bilgisi dönülür.
Notlar: Kredi limit çarpanı varsayılan olarak 4’tür.

# - Projeyi Çalıştırdığınızda ;
 - Mysql tarafında db ve tablo otomatik oluştulmakta olup varsayılan 5 kişinin Tc ve Kredi Skoru manuel eklenmiştir.
  - localhost:8080 portu ile arayüze giriş yapılır.
  - Arayüzde Tc Kimlik Numarası,Ad Soyad,Aylık Gelir ve Telefon Numarası girişi beklenir.
  [![N|Solid](https://www.mehmetbozkurt.net/public/home.png)](https://nodesource.com/products/nsolid)
  - Tc Kimlik numarasının db deki karşılığına göre kredi skoru ve aylık gelir hesaplaması sonucu kredi verilip verilmediği hesaplanıp kullanıya dönüş sağlanır.
  - Bu Tc ye ait kullanıcının bilgileri db de güncellenir.

# Ortamda kullanılan ek özellikler

  # *Swagger 
  - localhost:8080/swagger-ui.html ile api dokümantasyonu ile monitoring sağlanır.
    [![N|Solid](https://www.mehmetbozkurt.net/public/swagger.png)](https://nodesource.com/products/nsolid)    
  # *Test
- Mysql testi ve api testi basit bir şekilde örneklendirilmiştir.






