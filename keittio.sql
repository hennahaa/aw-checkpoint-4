-- TEHT 1

-- Luo tietokanta Keittio
CREATE DATABASE Keittio;

-- Luo taulu Astia, johon tallennetaan astian id, nimi ja lkm. Tietokanta huolehtii ID:n päivittämisestä.
CREATE TABLE Astia (
ID SERIAL PRIMARY KEY,
nimi varchar(255) NOT NULL,
lkm int NOT NULL
);

-- TEHT 2

-- Lisätään keittiö-tietokantaan taulu nimeltä toimipaikka

CREATE TABLE Toimipaikka (
id SERIAL PRIMARY KEY,
nimi varchar(255) NOT NULL,
sijainti varchar(255) NOT NULL,
aloitusvuosi int NOT NULL
);

-- Lisätään Toimipaikka-tauluun toimipaikkoja:

INSERT INTO toimipaikka(nimi, sijainti, aloitusvuosi) VALUES ('Academy Finland','Espoo',2017);
INSERT INTO toimipaikka(nimi, sijainti, aloitusvuosi) VALUES ('Academy Sweden','Kista',2015);
INSERT INTO toimipaikka(nimi, sijainti, aloitusvuosi) VALUES ('Academy Germany','Munchen',2018);


-- Muokataan taulua Astia
--lisätään uusi sarake toimipaikka_id
ALTER TABLE astia
    ADD toimipaikka_id int;

--lisätään uudelle sarakkeelle foreign key-viittaus
ALTER TABLE astia
    ADD CONSTRAINT fk_astia_toimipaikka FOREIGN KEY (toimipaikka_id) REFERENCES toimipaikka(id);

