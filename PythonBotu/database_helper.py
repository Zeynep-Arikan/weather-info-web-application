import mysql.connector

def connect_to_database(host, user, password, database):
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='sevval157',
        database='havadurumu'
    )

def create_table_if_not_exists(cursor):
    check_table_query = '''
    CREATE TABLE IF NOT EXISTS YeniDurum (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(255),
        GuncellemeZamani VARCHAR(255), 
        Sicaklik VARCHAR(255),
        Gokyuzu VARCHAR(255),
        YuksekDusuk VARCHAR(255),
        Ruzgar VARCHAR(255),
        Gunduz VARCHAR(255),
        Gece VARCHAR(255),
        GunDogumU VARCHAR(255),
        GunBatimi VARCHAR(255),
        Basinc VARCHAR(255),
        Nem VARCHAR(255)
    )
    '''
    
    # Execute the query to create the table
    cursor.execute(check_table_query)

    
def update_weather_data(cursor, name, lastupdatetime, temperature_box, sky_status, up_down, windspeeds, day_night, night, sunrise, sunset, specific, humidity):
    update_query = f'''
    UPDATE YeniDurum
    SET GuncellemeZamani = '{lastupdatetime}',
    Sicaklik = '{temperature_box}',
    Gokyuzu = '{sky_status}',
    YuksekDusuk = '{up_down}',
    Ruzgar = '{windspeeds}',
    Gunduz = '{day_night}',
    Gece = '{night}',
    GunDogumu = '{sunrise}',
    GunBatimi = '{sunset}',
    Basinc = '{specific}',
    Nem = '{humidity}'
    WHERE Name = '{name}'
    '''

    cursor.execute(update_query)

    

