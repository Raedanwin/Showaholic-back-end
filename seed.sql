DROP TABLE IF EXISTS watchlist;
CREATE TABLE watchlist (
    ID SERIAL UNIQUE,
    Title char(500) NOT NULL DEFAULT '',
    Authour char(500) NOT NULL DEFAULT '',
    PRIMARY KEY (id)
);
INSERT INTO watchlist (title, authour) VALUES ('Fantasy', 'Frodo');
INSERT INTO watchlist (title, authour) VALUES ('Sci-Fi', 'Rick Sanchez');
INSERT INTO watchlist (title, authour) VALUES ('Action', 'John Wick');
INSERT INTO watchlist (title, authour) VALUES ('Anime', 'Kaneki');
INSERT INTO watchlist (title, authour) VALUES ('Comedy', 'Billy Madison');

DROP TABLE IF EXISTS show;
CREATE TABLE show (
    ID SERIAL UNIQUE,
    watchlist_id int NOT NULL,
    Title char(500) NOT NULL DEFAULT '',
    Where_to_watch char(500) NOT NULL DEFAULT '',
    Genre char(500) NOT NULL DEFAULT '',
    Cover char(500) NOT NULL DEFAULT '',
    Release_date char(500) NOT NULL DEFAULT '',
    Runtime char(500) NOT NULL DEFAULT '',
    Synopsis char(10000) NOT NULL DEFAULT '',
    PRIMARY KEY (id),
    FOREIGN KEY (watchlist_id) REFERENCES watchlist(id) ON DELETE CASCADE,
);