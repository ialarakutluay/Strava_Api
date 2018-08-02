## Popular Segment List and Leaderboard 
Bu uygulamada [Strava](https://www.strava.com/) sitesindeki **Istanbul** konumundaki en çok kullanilan 10 yolu listeler. Ve seçilen yolun lider tablosunu gösterir. 

## Code Style
Proje Python programlama dili ile yazilmiştir. 

## How to Use?
KullaniciGiris.py adlı dosyayı çaliştiriyoruz.
Karşınıza asagidaki gibi bir liste gelecektir.

        MOST POPULAR 10 CYCLİNG SEGMENT İN İSTANBUL
        0.) Segment ID: 992412  - Segment Adı: Kartal sprint  - Distance: 561.1
        1.) Segment ID: 6093112  - Segment Adı: Ortakoy - Bebek  - Distance: 4226.1
        2.) Segment ID: 867957  - Segment Adı: tnirps neet ekil sllems  - Distance: 823.8
        3.) Segment ID: 7171356  - Segment Adı: Tarabya - Yeniköy  - Distance: 2302.5
        4.) Segment ID: 5601561  - Segment Adı: Dolmabahçe Yolu  - Distance: 695.9
        5.) Segment ID: 4238266  - Segment Adı: Galleria - Hava Harp Okulu  - Distance: 2284.9
        6.) Segment ID: 1550831  - Segment Adı: Kaynarca - İdealtepe  - Distance: 15443.7
        7.) Segment ID: 5842093  - Segment Adı: hayal kahvesi rampasi  - Distance: 937.0
        8.) Segment ID: 5169525  - Segment Adı: Çayırbaşı-İstinye  - Distance: 7488.9
        9.) Segment ID: 2659588  - Segment Adı: Taşköprü climb-1  - Distance: 420.2
        
         Lider Tablosunu Görmek İstediğiniz Segmenti Seçiniz:
         
Listenin en sonunda sizden bir segment numarası isteyecektir.
>Örneğin 1. Segment olan Ortaköy-Bebek güzargahının lidertablosunu görmek için "1" yazınız.

Karşınıza aşağıdaki tarza 50 kişilik bir liste çıkacaktır.

	Atlet Adı: Andy R.  - Bitirme Zamanı: 357  - Derecesi: 1  - Skor: 19776
	Atlet Adı: Alikemal G.  - Bitirme Zamanı: 361  - Derecesi: 2  - Skor: 14824
	Atlet Adı: Mert B.  - Bitirme Zamanı: 361  - Derecesi: 2  - Skor: 14824
	Atlet Adı: Ali D.  - Bitirme Zamanı: 362  - Derecesi: 4  - Skor: 13807
	Atlet Adı: Guclu G.  - Bitirme Zamanı: 363  - Derecesi: 5  - Skor: 12865
	Atlet Adı: Oguz A.  - Bitirme Zamanı: 364  - Derecesi: 6  - Skor: 11992
	Atlet Adı: Ahmet P.  - Bitirme Zamanı: 364  - Derecesi: 6  - Skor: 11992       

Listenin en sonunda bir atlet ismi girmeniz istenecektir.
*Atlet ismi nasıl girilir?*
>Örneğin aradığınız atletin adı Murat Kaya için Murat K.

Atlet ismi girildiğinde dönen sonuç o atletin o listede kaç kere bulunduğudur. 

En son olarak eğer segmentleri tekrar görmek istiyorsanız 0 a istemiyorsanız rastgele bir tuşa basarak çıkabileceğiz bir soru gelir. 

0 dışında başka tuşa bastıysanız program sonlanır.
