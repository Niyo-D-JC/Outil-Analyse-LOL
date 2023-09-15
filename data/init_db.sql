DROP SCHEMA IF EXISTS projet CASCADE;
CREATE SCHEMA projet;


-----------------------------------------------------
-- User
-----------------------------------------------------
DROP TABLE IF EXISTS projet.user CASCADE ;
CREATE TABLE projet.user(
    puuid    TEXT PRIMARY KEY,
    name_       TEXT UNIQUE,
    password_          TEXT,
    role_          TEXT
);

-----------------------------------------------------
-- Team
-----------------------------------------------------
DROP TABLE IF EXISTS projet.team CASCADE ;
CREATE TABLE projet.team(
    team_id  INT PRIMARY KEY,
    match_id   INT UNIQUE
);

-----------------------------------------------------
-- Match
-----------------------------------------------------
DROP TABLE IF EXISTS projet.match CASCADE ;
CREATE TABLE projet.match(
    match_id    INT PRIMARY KEY,
    duration   INT,
    team_id  INT REFERENCES projet.team(team_id)
);

-----------------------------------------------------
-- Item
-----------------------------------------------------
DROP TABLE IF EXISTS projet.item CASCADE ;
CREATE TABLE projet.item(
    id  INT PRIMARY KEY,
    name_   TEXT UNIQUE
);

-----------------------------------------------------
-- Champion
-----------------------------------------------------
DROP TABLE IF EXISTS projet.champion CASCADE ;
CREATE TABLE projet.champion(
    id  INT PRIMARY KEY,
    name_   TEXT UNIQUE
);

-----------------------------------------------------
-- JoueurInTeam
-----------------------------------------------------
DROP TABLE IF EXISTS projet.joueurInTeam CASCADE;
CREATE TABLE projet.joueurInTeam(
    puuid TEXT REFERENCES projet.user(puuid),
    team_id INT REFERENCES projet.team(team_id),
    champion_id INT REFERENCES projet.champion(id),
    team_position TEXT NOT NULL
    PRIMARY KEY (puuid, team_id),
);

-----------------------------------------------------
-- joueurInTeam_Item
-----------------------------------------------------
DROP TABLE IF EXISTS projet.joueurInTeam_Item CASCADE ;
CREATE TABLE projet.joueurInTeam_Item(
    puuid TEXT,
    team_id INT,
    item_id  INT,
    PRIMARY KEY (puuid, team_id, item_id),
    FOREIGN KEY (puuid, team_id) REFERENCES projet.joueurInTeam(puuid, team_id)
    FOREIGN KEY (item_id) REFERENCES projet.Item(id)
);
