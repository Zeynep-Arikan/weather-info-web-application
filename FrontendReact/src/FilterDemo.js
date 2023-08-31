import React, { useState } from "react";
import { Dropdown } from "primereact/dropdown";
import axios from "axios";
import "./Navbar.css";

//theme
import "primereact/resources/themes/lara-light-indigo/theme.css";

//core
import "primereact/resources/primereact.min.css";

export default function FilterDemo() {
  const [selectedCountry, setSelectedCountry] = useState(null);
  const [cityData, setCityData] = useState(null);
  const countries = [
    { name: "Adana", code: "01" },
    { name: "Adıyaman", code: "02" },
    { name: "Afyonkarahisar", code: "03" },
    { name: "Ağrı", code: "04" },
    { name: "Amasya", code: "05" },
    { name: "Ankara", code: "06" },
    { name: "Antalya", code: "07" },
    { name: "Artvin", code: "08" },
    { name: "Aydın", code: "09" },
    { name: "Balıkesir", code: "10" },
    { name: "Bilecik", code: "11" },
    { name: "Bingöl", code: "12" },
    { name: "Bitlis", code: "13" },
    { name: "Bolu", code: "14" },
    { name: "Burdur", code: "15" },
    { name: "Bursa", code: "16" },
    { name: "Çanakkale", code: "17" },
    { name: "Çankırı", code: "18" },
    { name: "Çorum", code: "19" },
    { name: "Denizli", code: "20" },
    { name: "Diyarbakır", code: "21" },
    { name: "Edirne", code: "22" },
    { name: "Elazığ", code: "23" },
    { name: "Erzincan", code: "24" },
    { name: "Erzurum", code: "25" },
    { name: "Eskişehir", code: "26" },
    { name: "Gaziantep", code: "27" },
    { name: "Giresun", code: "28" },
    { name: "Gümüşhane", code: "29" },
    { name: "Hakkâri", code: "30" },
    { name: "Hatay", code: "31" },
    { name: "Isparta", code: "32" },
    { name: "Mersin", code: "33" },
    { name: "İstanbul", code: "34" },
    { name: "İzmir", code: "35" },
    { name: "Kars", code: "36" },
    { name: "Kastamonu", code: "37" },
    { name: "Kayseri", code: "38" },
    { name: "Kırklareli", code: "39" },
    { name: "Kırşehir", code: "40" },
    { name: "Kocaeli", code: "41" },
    { name: "Konya", code: "42" },
    { name: "Kütahya", code: "43" },
    { name: "Malatya", code: "44" },
    { name: "Manisa", code: "45" },
    { name: "Kahramanmaraş", code: "46" },
    { name: "Mardin", code: "47" },
    { name: "Muğla", code: "48" },
    { name: "Muş", code: "49" },
    { name: "Nevşehir", code: "50" },
    { name: "Niğde", code: "51" },
    { name: "Ordu", code: "52" },
    { name: "Rize", code: "53" },
    { name: "Sakarya", code: "54" },
    { name: "Samsun", code: "55" },
    { name: "Siirt", code: "56" },
    { name: "Sinop", code: "57" },
    { name: "Sivas", code: "58" },
    { name: "Tekirdağ", code: "59" },
    { name: "Tokat", code: "60" },
    { name: "Trabzon", code: "61" },
    { name: "Tunceli", code: "62" },
    { name: "Şanlıurfa", code: "63" },
    { name: "Uşak", code: "64" },
    { name: "Van", code: "65" },
    { name: "Yozgat", code: "66" },
    { name: "Zonguldak", code: "67" },
    { name: "Aksaray", code: "68" },
    { name: "Bayburt", code: "69" },
    { name: "Karaman", code: "70" },
    { name: "Kırıkkale", code: "71" },
    { name: "Batman", code: "72" },

    { name: "Şırnak", code: "73" },
    { name: "Bartın", code: "74" },
    { name: "Ardahan", code: "75" },
    { name: "Iğdır", code: "76" },
    { name: "Yalova", code: "77" },
    { name: "Karabük", code: "78" },
    { name: "Kilis", code: "79" },
    { name: "Osmaniye", code: "80" },
    { name: "Düzce", code: "81" },
  ];

  const transliteration = require('transliteration');

  const transformedCountries = countries.map(country => ({
    name: transliteration.slugify(country.name),
    code: country.code
}));

  const selectedCountryTemplate = (option, props) => {
    if (option) {
      return (
        <div className="flex align-items-center">
          <img
            alt={option.name}
            src="https://primefaces.org/cdn/primereact/images/flag/flag_placeholder.png"
            className={`mr-2 flag flag-${option.code.toLowerCase()}`}
            style={{ width: "18px" }}
          />
          <div>{option.name}</div>
        </div>
      );
    }

    return <span>{props.placeholder}</span>;
  };

  const countryOptionTemplate = (option) => {
    return (
      <div className="flex align-items-center">
        <img
          alt={option.name}
          src="https://primefaces.org/cdn/primereact/images/flag/flag_placeholder.png"
          className={`mr-2 flag flag-${option.code.toLowerCase()}`}
          style={{ width: "18px" }}
        />
        <div>{option.name}</div>
      </div>
    );
  };
  const fetchWeatherData = async () => {
    try {
      const response = await axios.post(
        "http://localhost:8090/api/yenidurum/gonder",
        {
          name: selectedCountry.name,
        }
      );
      setCityData(response.data);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div className="navbar">
    <div className="navbar-container">
      <Dropdown
        value={selectedCountry}
        onChange={(e) => setSelectedCountry(e.value)}
        options={transformedCountries}
        optionLabel="name"
        placeholder="Şehir ismi girin"
        filter
        valueTemplate={selectedCountryTemplate}
        itemTemplate={countryOptionTemplate}
        className="w-full md:w-14rem"
      />

      <button onClick={fetchWeatherData}>Gönder</button>
      <div className="veriler">
      {cityData && (
        <div className="header-data">
          <h2>Şehir Bİlgileri: {cityData[0].name}</h2>
          <p>GuncellemeZamani: {cityData[0].guncellemeZamani}</p>
          <p>Sıcaklık: {cityData[0].sicaklik}°C</p>
          <p>Gokyüzü: {cityData[0].gokyuzu}</p>
          <p>Yüksek/Düşük: {cityData[0].yuksekDusuk}</p>
          <p>Rüzgar: {cityData[0].ruzgar}</p>
          <p>Gündüz: {cityData[0].gunduz}</p>
          <p>Gece: {cityData[0].gece}</p>
          <p>Gün Doğumu: {cityData[0].gunDogumU}</p>
          <p>Gün Batımı: {cityData[0].gunBatimi}</p>
          <p>Basınç: {cityData[0].basinc}</p>
          <p>Nem: {cityData[0].nem}</p>
        </div>
      )}</div>
    </div>
    </div>
  );
}
