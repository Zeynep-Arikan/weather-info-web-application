package com.example.myhava;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service  /*sınıfının bir Spring servisi olduğunu belirtir.*/
public class ServiceClass {
    private final YeniDurumRepository yeniDurumRepository; //adlı bir arayüz türünde özel bir alan tanımlanmıştır.
    //Bu arayüz, EntityClass nesnelerinin veri erişim işlemlerini yapmak için kullanılacaktır.

    @Autowired
    public ServiceClass(YeniDurumRepository yeniDurumRepository) {
        this.yeniDurumRepository = yeniDurumRepository;
    }

    public List<String> findSicaklikColumn() {
        return yeniDurumRepository.findSicaklikColumn();
    }
    public List<String> hepsi() {
        return yeniDurumRepository.findhepsi();
    }
    public List<String> tekveri() {
        return yeniDurumRepository.findtekveri();
    }
    public List<String> veriler(){return yeniDurumRepository.findveriler();}


    //Sehir Bilgileri: {"name":"bilecik"} bu kodu çıkartan yer
   //public List<EntityClass> gonderName() { return yeniDurumRepository.findgonderName();}
    // alttaki kodun çıktısı Response: Veri alındı: {"name":"ankara"}
    public List<EntityClass> gonderName(String name) {
        return yeniDurumRepository.findgonderName(name);

    }







}
/*Bu kod parçası, Spring Boot tabanlı bir RESTful API'nin controller'ını tanımlar. YeniDurumController sınıfı,
/api/yenidurum yolundaki GET isteklerini işler ve ServiceClass aracılığıyla veriyi çekerek cevaplar.
Bu sayede istemciler, belirtilen yolu kullanarak EntityClass nesnelerini alabilirler.*/