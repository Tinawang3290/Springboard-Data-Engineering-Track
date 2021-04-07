# Music Schema 

-- from the terminal run:
-- psql < music.sql

DROP DATABASE IF EXISTS music;

CREATE DATABASE music;

-- \c music
-- improvements:
-- 1. Change the data types to optimize the performance
-- 2. Create the composite PK to avoid duplicate entries, Seriel cannot be performed as a PK.
-- 3. Change the inserted value - release_date

CREATE TABLE music.songs (
    id SERIAL,
    title VARCHAR(50) NOT NULL,
    duration_in_seconds INTEGER NOT NULL,
    release_date TEXT NOT NULL,
    artists VARCHAR(50) NOT NULL,
    album VARCHAR(50) NOT NULL,
    producers VARCHAR(255) NOT NULL,
    CONSTRAINT PRIMARY KEY (title , artists , album)
);

INSERT INTO music.songs
  (title, duration_in_seconds, release_date, artists, album, producers)
VALUES
 ('MMMBop', 238,  '1997-04-15' , '{"Hanson"}', 'Middle of Nowhere', '{"Dust Brothers", "Stephen Lironi"}'),
 ('Bohemian Rhapsody', 355, '1975-10-31', '{"Queen"}', 'A Night at the Opera', '{"Roy Thomas Baker"}'),
 ('One Sweet Day', 282, '1995-11-14', '{"Mariah Cary", "Boyz II Men"}', 'Daydream', '{"Walter Afanasieff"}'),
 ('Shallow', 216, '2018-09-27', '{"Lady Gaga", "Bradley Cooper"}', 'A Star Is Born', '{"Benjamin Rice"}'),
 ('How You Remind Me', 223, '2001-08-21', '{"Nickelback"}', 'Silver Side Up', '{"Rick Parashar"}'),
 ('New York State of Mind', 276, '2009-10-20', '{"Jay Z", "Alicia Keys"}', 'The Blueprint 3', '{"Al Shux"}'),
('Dark Horse', 215, '2013-12-17', '{"Katy Perry", "Juicy J"}', 'Prism', '{"Max Martin", "Cirkut"}'),
('Moves Like Jagger', 201, '2011-06-21',  '{"Maroon 5", "Christina Aguilera"}', 'Hands All Over', '{"Shellback", "Benny Blanco"}'),
('Complicated', 244, '2002-05-14', '{"Avril Lavigne"}', 'Let Go', '{"The Matrix"}'),
 ('Say My Name', 240,'1999-11-07', '{"Destiny''s Child"}', 'The Writing''s on the Wall', '{"Darkchild"}');   

# Air Traffic schema 

-- from the terminal run:
-- psql < air_traffic.sql

DROP DATABASE IF EXISTS air_traffic;

CREATE DATABASE air_traffic;

-- \c air_traffic
# Approach_1
-- Improvements:
-- 1. Specify the specific database that you want the tables to live in, otherwise, they will be added to sys database by default
-- 2. Change the data types to optimize the performance
-- 3. Create the composite PK to avoid duplicate entries, Seriel cannot be performed as a PK.

CREATE TABLE air_traffic.tickets (
    id SERIAL,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(25)  NOT NULL,
    seat VARCHAR(10)  NOT NULL,
    departure TIMESTAMP NOT NULL,
    arrival TIMESTAMP NOT NULL,
    airline VARCHAR(25)  NOT NULL,
    from_city VARCHAR(25)  NOT NULL,
    from_country VARCHAR(25)  NOT NULL,
    to_city VARCHAR(25)  NOT NULL,
    to_country VARCHAR(25)  NOT NULL,
    CONSTRAINT PRIMARY KEY(first_name, last_name, seat)
);

INSERT INTO  air_traffic.tickets
  (first_name, last_name, seat, departure, arrival, airline, from_city, from_country, to_city, to_country)
VALUES
  ('Jennifer', 'Finch', '33B', '2018-04-08 09:00:00', '2018-04-08 12:00:00', 'United', 'Washington DC', 'United States', 'Seattle', 'United States'),
  ('Thadeus', 'Gathercoal', '8A', '2018-12-19 12:45:00', '2018-12-19 16:15:00', 'British Airways', 'Tokyo', 'Japan', 'London', 'United Kingdom'),
  ('Sonja', 'Pauley', '12F', '2018-01-02 07:00:00', '2018-01-02 08:03:00', 'Delta', 'Los Angeles', 'United States', 'Las Vegas', 'United States'),
  ('Jennifer', 'Finch', '20A', '2018-04-15 16:50:00', '2018-04-15 21:00:00', 'Delta', 'Seattle', 'United States', 'Mexico City', 'Mexico'),
  ('Waneta', 'Skeleton', '23D', '2018-08-01 18:30:00', '2018-08-01 21:50:00', 'TUI Fly Belgium', 'Paris', 'France', 'Casablanca', 'Morocco'),
  ('Thadeus', 'Gathercoal', '18C', '2018-10-31 01:15:00', '2018-10-31 12:55:00', 'Air China', 'Dubai', 'UAE', 'Beijing', 'China'),
  ('Berkie', 'Wycliff', '9E', '2019-02-06 06:00:00', '2019-02-06 07:47:00', 'United', 'New York', 'United States', 'Charlotte', 'United States'),
  ('Alvin', 'Leathes', '1A', '2018-12-22 14:42:00', '2018-12-22 15:56:00', 'American Airlines', 'Cedar Rapids', 'United States', 'Chicago', 'United States'),
  ('Berkie', 'Wycliff', '32B', '2019-02-06 16:28:00', '2019-02-06 19:18:00', 'American Airlines', 'Charlotte', 'United States', 'New Orleans', 'United States'),
  ('Cory', 'Squibbes', '10D', '2019-01-20 19:30:00', '2019-01-20 22:45:00', 'Avianca Brasil', 'Sao Paolo', 'Brazil', 'Santiago', 'Chile');
  
# Approach_2 
-- from the terminal run:
-- psql < air_traffic.sql

DROP DATABASE IF EXISTS air_traffic2;

CREATE DATABASE air_traffic2;


-- \c air_traffic

-- Improvements:
-- 1. Specify the specific database that you want the tables to live in, otherwise, they will be added to sys database by default
-- 2. Change the data types to optimize the performance
-- 3. Create the composite PK to avoid duplicate entries, Seriel cannot be performed as a PK.
-- 4. Decompose to 3NF.
  
  CREATE TABLE air_traffic2.guests (
   guest_id SERIAL,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(25) NOT NULL,
    CONSTRAINT PRIMARY KEY (first_name , last_name)
);


    INSERT INTO  air_traffic2.guests
    (first_name, last_name)
    VALUES
    ('Jennifer', 'Finch'),
    ('Thadeus', 'Gathercoal'),
    ('Sonja', 'Pauley'),
    ('Waneta', 'Skeleton'),
	('Alvin', 'Leathes'),
	('Berkie', 'Wycliff'),
	('Cory', 'Squibbes');
    
	CREATE TABLE air_traffic2.airlines (
    airline_id SERIAL,
    airline VARCHAR(25)  NOT NULL PRIMARY KEY
    );
    
INSERT INTO  air_traffic2.airlines
(airline)
VALUES
('United'),
('British Airways'),
('Delta'),
('TUI Fly Belgium'),
( 'Air China'),
('American Airlines'),
( 'Avianca Brasil');
 
CREATE TABLE air_traffic2.flights(
	flight_id SERIAL,
    from_city VARCHAR(25)  NOT NULL,
    from_country VARCHAR(25)  NOT NULL,
    to_city VARCHAR(25)  NOT NULL,
    to_country VARCHAR(25)  NOT NULL,
	seat VARCHAR(10)  NOT NULL,
    departure TIMESTAMP NOT NULL,
	arrival TIMESTAMP NOT NULL,
    airline_id INT NOT NULL,
    guest_id INT NOT NULL,
	CONSTRAINT PRIMARY KEY(departure, arrival, from_city, to_city)
    );
    
ALTER TABLE air_traffic2.flights
ADD CONSTRAINT FK_airline_ID 
FOREIGN KEY (airline_id)  REFERENCES air_traffic2.airlines(airline_id),
ADD CONSTRAINT FK_guest_ID 
FOREIGN KEY (guest_id) REFERENCES air_traffic2.guests(guest_id);

-- ALTER TABLE air_traffic2.flights
-- ADD CONSTRAINT FK_guest_ID 
-- FOREIGN KEY (guest_id) REFERENCES air_traffic2.guests(guest_id);

INSERT INTO  air_traffic2.flights
  (from_city, from_country, to_city, to_country, seat, departure, arrival, airline_id, guest_id)
VALUES
  ('Washington DC', 'United States', 'Seattle', 'United States', '33B', '2018-04-08 09:00:00', '2018-04-08 12:00:00', 1, 1),
  ('Tokyo', 'Japan', 'London', 'United Kingdom', '8A', '2018-12-19 12:45:00', '2018-12-19 16:15:00', 2, 2),
  ('Los Angeles', 'United States', 'Las Vegas', 'United States', '12F', '2018-01-02 07:00:00', '2018-01-02 08:03:00', 3, 3),
  ( 'Seattle', 'United States', 'Mexico City', 'Mexico', '20A', '2018-04-15 16:50:00', '2018-04-15 21:00:00', 3, 1),
  ('Paris', 'France', 'Casablanca', 'Morocco', '23D', '2018-08-01 18:30:00', '2018-08-01 21:50:00', 4,4),
  ('Dubai', 'UAE', 'Beijing', 'China','18C', '2018-10-31 01:15:00', '2018-10-31 12:55:00', 5, 2),
  ('New York', 'United States', 'Charlotte', 'United State', '9E', '2019-02-06 06:00:00', '2019-02-06 07:47:00',1,6 ),
  ('Cedar Rapids', 'United States', 'Chicago', 'United States', '1A', '2018-12-22 14:42:00', '2018-12-22 15:56:00', 6,5),
  ('Charlotte', 'United States', 'New Orleans', 'United States','32B', '2019-02-06 16:28:00', '2019-02-06 19:18:00', 6,6),
  ( 'Sao Paolo', 'Brazil', 'Santiago', 'Chile', '10D', '2019-01-20 19:30:00', '2019-01-20 22:45:00', 7,7);
  
  
  # Outer space schema
  
  -- from the terminal run:
-- psql < outer_space.sql

DROP DATABASE IF EXISTS outer_space;

CREATE DATABASE outer_space;

-- \c outer_space

-- Improvements:
-- 1. Specify the specific database that you want the tables to live in, otherwise, they will be added to sys database by default
-- 2. Change the data types to optimize the performance
-- 3. Create the composite PK to avoid duplicate entries, Seriel cannot be performed as a PK.

CREATE TABLE outer_space.planets (
    id SERIAL,
    name VARCHAR(50) NOT NULL,
    orbital_period_in_years FLOAT(2) NOT NULL,
    orbits_around VARCHAR(50) NOT NULL,
    galaxy VARCHAR(25) NOT NULL,
    moons VARCHAR(255),
    CONSTRAINT PRIMARY KEY (name)
);

INSERT INTO outer_space.planets
  (name, orbital_period_in_years, orbits_around, galaxy, moons)
VALUES
  ('Earth', 1.00, 'The Sun', 'Milky Way', '{"The Moon"}'),
  ('Mars', 1.88, 'The Sun', 'Milky Way', '{"Phobos", "Deimos"}'),
  ('Venus', 0.62, 'The Sun', 'Milky Way', '{}'),
  ('Neptune', 164.8, 'The Sun', 'Milky Way', '{"Naiad", "Thalassa", "Despina", "Galatea", "Larissa", "S/2004 N 1", "Proteus", "Triton", "Nereid", "Halimede", "Sao", "Laomedeia", "Psamathe", "Neso"}'),
  ('Proxima Centauri b', 0.03, 'Proxima Centauri', 'Milky Way', '{}'),
  ('Gliese 876 b', 0.23, 'Gliese 876', 'Milky Way', '{}');
