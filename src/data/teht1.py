#!/usr/bin/python
import psycopg2
from config import config

# Lisätään astia tauluun

def lisaa_astiat(nimi,lkm):
    conn = None
    try:
        conn = psycopg2.connect(**config())
        cursor = conn.cursor()
        SQL = """INSERT INTO astia(nimi, lkm) VALUES (%s, %s);"""
        record_to_insert = (nimi,lkm)
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
        SQL = """SELECT * FROM astia;"""
        cursor.execute(SQL)
        rows = cursor.fetchall()
        for row in rows:
            print(f"{row[1]}, {row[2]}kpl")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            #print('Tietokantayhteys suljettu.')

#Lisätään astiat ja sitten tulostetaan ne
lisaa_astiat("Muki", 100)
lisaa_astiat("Lasi",80)
lisaa_astiat("Iso lautanen",40)
lisaa_astiat("Pieni lautanen",40)
tulosta_astiat()
