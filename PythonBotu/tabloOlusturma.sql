
CREATE TABLE `Cities`(
	`id` int AUTO_INCREMENT NOT NULL,
	`name` varchar(50) NOT NULL,
	`plate` varchar(5) NOT NULL,
	`latitude` varchar(20) NOT NULL,
	`longitude` varchar(20) NOT NULL,
PRIMARY KEY 
(
	`id` ASC
)
)
;
/****** Object:  Table `Counties`    Script Date: 11/08/2023 13:35:58 ******/


CREATE TABLE `Counties`(
	`id` int AUTO_INCREMENT NOT NULL,
	`city_id` int NOT NULL,
	`county_name` varchar(50) NOT NULL,
PRIMARY KEY 
(
	`id` ASC
)
)
;
/****** Object:  Table `YeniDurum`    Script Date: 11/08/2023 13:35:58 ******/


CREATE TABLE `YeniDurum`(
	`Name` varchar(255) NULL,
	`GuncellemeZamani` varchar(255) NULL,
	`Sicaklik` varchar(255) NULL,
	`;kyuzu` varchar(255) NULL,
	`YuksekDusuk` varchar(255) NULL,
	`Ruzgar` varchar(255) NULL,
	`Gunduz` varchar(255) NULL,
	`Gece` varchar(255) NULL,
	`GunDogumU` varchar(255) NULL,
	`GunBatimi` varchar(255) NULL,
	`Basinc` varchar(255) NULL,
	`Nem` varchar(255) NULL
)
;

