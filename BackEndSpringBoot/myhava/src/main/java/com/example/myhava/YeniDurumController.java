package com.example.myhava;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*; /*web isteklerini işlemek için gerekli olan import ifadesi.*/
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.List; /*ava koleksiyonlarından List'i kullanabilmek için gerekli olan import ifadesi.*/
import java.util.Map;
import java.util.Optional;

@RestController
@CrossOrigin(origins = "*")
@RequestMapping("/api/yenidurum") /* Bu annotasyon, bu controller'ın /api/yenidurum yolundaki istekleri işleyeceğini belirtir.*/
public class YeniDurumController {

    private final ServiceClass serviceClass;

    @Autowired
    public YeniDurumController(ServiceClass yeniDurumService) {
        this.serviceClass = yeniDurumService;
    }

    @GetMapping("/sicaklik")
    public List<String> findSicaklikColumn() {
        return serviceClass.findSicaklikColumn();
    }

    @GetMapping("/hepsi")
    public List<String> hepsi(){
        return  serviceClass.hepsi();
    }
    @GetMapping("/tekveri")

    public List<String> tekveri(){
        return serviceClass.tekveri();

    }
    @GetMapping("/veriler")
    public List<String> veriler(){return serviceClass.veriler();}

    /* bunda veriyi göstermiyor
    @PostMapping("/gonder")
    public void gonderName(@RequestParam(name = "name", required = false) String name){
        System.out.println(name);
    }*/

    /*burda veri alındı yazıyor sadece
    @PostMapping("/gonder")
    public ResponseEntity<String> gonderName(@RequestParam(name = "name", required = false) String name) {
        System.out.println("Received Name: " + name);
        return ResponseEntity.ok("Veri alındı: " + name);
    }*/



    /* console da bu çıktıyı alıyorum Response: Veri alındı: {"name":"ankara"}*/
    @PostMapping("/gonder")
    public ResponseEntity<List<EntityClass>> gonderName(@RequestBody EntityClass requestJson) {
        System.out.println("Sehir Bilgileri: " + requestJson);

        // JSON verisini işleme işlemleri burada yapabilirsiniz.

        List<EntityClass> entityClasses = serviceClass.gonderName(requestJson.getName());


        // Sonuçları döndürme   Console yazdırma kısmı
        String response = "Veri alındı: " + requestJson  ;

        ResponseEntity.ok(requestJson);
        return ResponseEntity.ok(entityClasses);
    }




}




















