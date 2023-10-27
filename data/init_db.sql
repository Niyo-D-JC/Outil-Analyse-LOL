DROP SCHEMA IF EXISTS projet CASCADE;
CREATE SCHEMA projet;



-----------------------------------------------------
-- Joueur
-----------------------------------------------------
DROP TABLE IF EXISTS projet.joueur CASCADE ;
CREATE TABLE projet.joueur(
    puuid    TEXT PRIMARY KEY,
    name       TEXT,
    tier TEXT
);


-----------------------------------------------------
-- User
-----------------------------------------------------
DROP TABLE IF EXISTS projet.user CASCADE ;
CREATE TABLE projet.user(
    user_id    SERIAL PRIMARY KEY,
    puuid  TEXT REFERENCES projet.joueur(puuid),
    name       TEXT UNIQUE,
    password          TEXT,
    role          TEXT
);


-----------------------------------------------------
-- Item
-----------------------------------------------------
DROP TABLE IF EXISTS projet.item CASCADE ;
CREATE TABLE projet.item(
    item_id  INT PRIMARY KEY,
    name   TEXT
);


-----------------------------------------------------
-- Champion
-----------------------------------------------------
DROP TABLE IF EXISTS projet.champion CASCADE ;
CREATE TABLE projet.champion(
    champion_id  INT PRIMARY KEY,
    name   TEXT
);


-----------------------------------------------------
-- Lane
-----------------------------------------------------
DROP TABLE IF EXISTS projet.lane CASCADE ;
CREATE TABLE projet.lane(
    lane_id  INT PRIMARY KEY,
    name   TEXT UNIQUE
);


-----------------------------------------------------
-- Team
-----------------------------------------------------
DROP TABLE IF EXISTS projet.team CASCADE ;
CREATE TABLE projet.team(
    team_id  INT PRIMARY KEY,
    side   TEXT
);


-----------------------------------------------------
-- MatchJoueur
-----------------------------------------------------
DROP TABLE IF EXISTS projet.match CASCADE ;
CREATE TABLE projet.matchjoueur(
    match_id    TEXT,
    puuid TEXT REFERENCES projet.joueur(puuid),
    lane_id  INT REFERENCES projet.lane(lane_id),
    champion_id  INT REFERENCES projet.champion(champion_id),
    team_id  INT REFERENCES projet.team(team_id),
    total_damage_deal   INT,
    total_damage_take   INT,
    total_heal   INT,
    kda   FLOAT ,
    kills INT, 
    deaths INT,
    assists INT,
    win   BOOLEAN,
    CONSTRAINT pk_match PRIMARY KEY (match_id, puuid)
);



-----------------------------------------------------
-- ItemMatch
-----------------------------------------------------
DROP TABLE IF EXISTS projet.itemmatch CASCADE;
CREATE TABLE projet.itemmatch(
    match_id TEXT,
    puuid TEXT,
    item_id INT REFERENCES projet.item(item_id),
    item_position INT,
    CONSTRAINT fk_puuid_match FOREIGN KEY (match_id, puuid) REFERENCES projet.matchjoueur(match_id, puuid),
    PRIMARY KEY (match_id, puuid, item_id)
);


INSERT INTO projet.lane(lane_id, name) VALUES
(1, 'TOP'),
(2, 'JUNGLE'),
(3,'BOTTOM'),
(4,'MIDDLE'),
(5,'NONE');

INSERT INTO projet.team(team_id, side) VALUES
(100, 'Blue'),
(200,'Purple');