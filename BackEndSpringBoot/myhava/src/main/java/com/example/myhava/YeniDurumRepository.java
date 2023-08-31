package com.example.myhava;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.http.converter.json.GsonBuilderUtils;

import java.util.List;

public interface YeniDurumRepository extends JpaRepository<EntityClass, Long> {
    @Query(value = "SELECT sicaklik FROM yenidurum", nativeQuery = true)
    List<String> findSicaklikColumn();

    @Query(value = "SELECT * FROM yenidurum ", nativeQuery = true)
    List<String> findhepsi();

    @Query(value = "SELECT * FROM yenidurum WHERE Name = 'aydin'", nativeQuery = true)
    List<String> findtekveri();

    @Query(value = "SELECT * FROM yenidurum", nativeQuery = true)
    List<String> findveriler();


   /*@Query(value = "SELECT * FROM yenidurum WHERE Name = ?1", nativeQuery = true)
    List<EntityClass> findgonderName(@Param("name") String name);*/

    /* @Query(value = "SELECT * FROM yenidurum WHERE Name = :name", nativeQuery = true)
    List<EntityClass> findgonderName();*/


    @Query(value = "SELECT * FROM yenidurum WHERE name = :name", nativeQuery = true)
    List<EntityClass> findgonderName(@Param("name") String name);







    /*burda param anatasyonu var ama yinede aynı sonucu alıyorum
    @Query(value = "SELECT * FROM yenidurum WHERE Name = :name", nativeQuery = true)
    List<EntityClass> findByName(@Param("name") String name);
    */



















    /*Bu interface, JpaRepository arabirimini genişleterek EntityClass türündeki JPA varlıklarını yönetmek için kullanılır.*/
    /* EntityClass nesneleriyle ilgili veritabanı işlemlerini gerçekleştirecektir.*/
}
/*
 Bu arabirim, EntityClass nesnelerini veritabanı işlemleri için kullanır.
 JpaRepository'den miras alarak, veritabanı işlemlerini otomatik olarak gerçekleştirebilecek çeşitli hazır metotlara sahip olur
 (örneğin save, findById, findAll, delete vb.). Bu sayede veritabanı erişimi ve yönetimi oldukça kolaylaşır.
 */