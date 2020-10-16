
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
