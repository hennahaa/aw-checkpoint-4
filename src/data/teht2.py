#!/usr/bin/python
import psycopg2
from config import config

# Lisätään astia tauluun

def lisaa_astiat(nimi,lkm,toimipaikka):
    conn = None
    try:
        conn = psycopg2.connect(**config())
        cursor = conn.cursor()
        SQL = """INSERT INTO astia(nimi, lkm, toimipaikka_id) VALUES (%s, %s, %s);"""
        record_to_insert = (nimi,lkm,toimipaikka)
        cursor.execute(SQL, record_to_insert)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            #print('Tietokantayhteys suljettu.')

# Tulosta astiat taulusta

def tulosta_astiat():
    conn = None
    try:
        conn = psycopg2.connect(**config())
        cursor = conn.cursor()
        SQL = """SELECT toimipaikka.sijainti, astia.nimi, astia.lkm FROM astia INNER JOIN toimipaikka ON toimipaikka.id = astia.toimipaikka_id;"""
        cursor.execute(SQL)
        rows = cursor.fetchall()
        for row in rows:
            print(f"{row[0]}: {row[1]}, {row[2]}kpl")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            #print('Tietokantayhteys suljettu.')

#Päivitä espoossa sijaitsevan toimipisteen lasien määrä 80 -> 100
#jostain syystä päivitys siirtää päivitetyn rivin taulukon alimmaksi, ja mulla ei ole mitään hajua siitä että miksi
#mutta se toimii! :D
#Lasi unohtui kovakoodatuksi

def paivita(lkm,sijainti):
    conn = None
    try:
        conn = psycopg2.connect(**config())
        cursor = conn.cursor()
        SQL = """UPDATE astia SET lkm = %s WHERE nimi = 'Lasi' AND toimipaikka_id = (SELECT id FROM toimipaikka WHERE sijainti = %s);"""
        record_to_insert = (lkm,sijainti)
        cursor.execute(SQL, record_to_insert)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

#lisää astia tauluun rivejä siten, että jokaisella toimipaikalla on 100 mukia

def lisaa(nimi,lkm):
    conn = None
    try:
        conn = psycopg2.connect(**config())
        cursor = conn.cursor()
        #hakee toimipaikkojen id:t jotka EIVÄT ole vielä astia-taulussa
        SQL_1 = """SELECT toimipaikka.id FROM toimipaikka LEFT JOIN astia ON toimipaikka.id = astia.toimipaikka_id WHERE toimipaikka.id NOT IN (SELECT toimipaikka_id FROM astia);"""
        cursor.execute(SQL_1)
        rows = cursor.fetchall()
        #sitten näihin toimipaikoihin tuupataan haluttu määrä lisättävää astiaa
        for row in rows:
            #print(row[0])
            SQL_2 = """INSERT INTO astia(nimi, lkm, toimipaikka_id) VALUES (%s, %s, %s);"""
            record_to_insert = (nimi,lkm,row[0])
            cursor.execute(SQL_2, record_to_insert)
            conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            #print('Tietokantayhteys suljettu.')

#Poistetaan espoon toimipisteestä pieni lautanen

def poista(nimi,toimipaikka):
    conn = None
    try:
        conn = psycopg2.connect(**config())
        cursor = conn.cursor()
        SQL = """DELETE FROM astia WHERE nimi = %s and toimipaikka_id = (SELECT id FROM toimipaikka WHERE sijainti = %s);"""
        record_to_insert = (nimi,toimipaikka)
        cursor.execute(SQL, record_to_insert)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

#Lisätään astiat ja sitten tulostetaan ne (teht1 mukaillen)
lisaa_astiat("Muki", 100,1)
lisaa_astiat("Lasi",80,1)
lisaa_astiat("Iso lautanen",40,1)
lisaa_astiat("Pieni lautanen",40,1)

#teht 2
lisaa("Muki",100)
paivita(100,"Espoo")
poista("Pieni lautanen","Espoo")
tulosta_astiat()