
CREATE TABLE 'Journal_entries' (
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'Concept' TEXT NOT NULL,
    'Entry' TEXT NOT NULL,
    'mood_id' INTEGER NOT NULL,
    'date' INTEGER NOT NULL,
    FOREIGN KEY('mood_id') REFERENCES 'Mood'('id')
)
CREATE TABLE 'Mood' (
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'label' TEXT NOT NULL
);

INSERT INTO 'Journal_entries' VALUES (null, 'First day of school', 'This is wild and crazy', 1, 6543132);
INSERT INTO 'Journal_entries' VALUES (null, 'New Garden', 'Today I made a garden', 2, 65432135);
INSERT INTO 'Journal_entries' VALUES (null, 'First date', 'That was weirdd', 3, 979684);

INSERT INTO 'Mood' VALUES (null, 'Happy');
INSERT INTO 'Mood' VALUES (null, 'Ecstatic');
INSERT INTO 'Mood' VALUES (null, 'Sad');
INSERT INTO 'Mood' VALUES (null, 'Angry');

ALTER TABLE 'Mood' 
RENAME TO 'mood'

CREATE TABLE 'tag' (
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'name' TEXT NOT NULL
)

CREATE TABLE 'entry_tag' (
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'entry_id' INTEGER NOT NULL, 
    'tag_id' INTEGER NOT NULL,
    FOREIGN KEY('entry_id') REFERENCES 'Journal_entries'('id'),
    FOREIGN KEY('tag_id') REFERENCES 'tag'('id')
)

INSERT INTO 'tag' VALUES (null, 'interesting')
INSERT INTO 'tag' VALUES (null, 'funny')
INSERT INTO 'tag' VALUES (null, 'embarassing')
INSERT INTO 'tag' VALUES (null, 'scary')
