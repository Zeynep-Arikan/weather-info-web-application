package com.example.myhava;

import jakarta.persistence.*;

import lombok.Data;

@Entity
@Table(name = "yenidurum")
@Data
public class EntityClass {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "Name")
    private String Name;

    @Column(name = "GuncellemeZamani")
    private String GuncellemeZamani;

    @Column(name = "Sicaklik")
    private String Sicaklik;

    @Column(name = "Gokyuzu")
    private String Gokyuzu;

    @Column(name = "YuksekDusuk")
    private String YuksekDusuk;

    @Column(name = "Ruzgar")
    private String Ruzgar;

    @Column(name = "Gunduz")
    private String Gunduz;

    @Column(name = "Gece")
    private String Gece;

    @Column(name = "GunDogumU")
    private String GunDogumU;

    @Column(name = "GunBatimi")
    private String GunBatimi;

    @Column(name = "Basinc")
    private String Basinc;

    @Column(name = "Nem")
    private String Nem;

    /*@Override
    public String toString() {
        return "EntityClass{" +
                "id=" + id +
                ", Name='" + Name + '\'' +
                ", GuncellemeZamani='" + GuncellemeZamani + '\'' +
                ", Sicaklik='" + Sicaklik + '\'' +
                ", Gokyuzu='" + Gokyuzu + '\'' +
                ", YuksekDusuk='" + YuksekDusuk + '\'' +
                ", Ruzgar='" + Ruzgar + '\'' +
                ", Gunduz='" + Gunduz + '\'' +
                ", Gece='" + Gece + '\'' +
                ", GunDogumU='" + GunDogumU + '\'' +
                ", GunBatimi='" + GunBatimi + '\'' +
                ", Basinc='" + Basinc + '\'' +
                ", Nem='" + Nem + '\'' +
                '}';
    }*/
}
