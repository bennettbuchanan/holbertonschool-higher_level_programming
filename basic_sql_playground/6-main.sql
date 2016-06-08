ALTER TABLE TVShow RENAME TO tmp_TVShow;

CREATE TABLE TVShow (
  person_id_for_show INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  name char(128) NOT NULL
);

INSERT INTO TVShow(person_id_for_show, name)
SELECT id, name
FROM tmp_TVShow;

DROP TABLE tmp_TVShow;

CREATE TABLE age_sum (
  name TEXT,
  age_sum INTEGER
);

CREATE TABLE min_age (
  name TEXT,
  first_name TEXT,
  last_name TEXT,
  min_age INTEGER
);

INSERT INTO age_sum(name, age_sum)
SELECT "Game of Thrones", (SELECT sum(age) FROM TVShowPerson, EyesColor, TVShow INNER JOIN Person
      ON Person.id = TVShowPerson.person_id
      AND EyesColor.person_id = Person.id
      AND TVShowPerson.tvshow_id = TVShow.person_id_for_show
      WHERE
        TVShow.name = 'Game of Thrones');

INSERT INTO age_sum(name, age_sum)
SELECT "Breaking bad", (SELECT sum(age) FROM TVShowPerson, EyesColor, TVShow INNER JOIN Person
      ON Person.id = TVShowPerson.person_id
      AND EyesColor.person_id = Person.id
      AND TVShowPerson.tvshow_id = TVShow.person_id_for_show
      WHERE
        TVShow.name = 'Breaking bad');

INSERT INTO age_sum(name, age_sum)
SELECT "The big bang theory", (SELECT sum(age) FROM TVShowPerson, EyesColor, TVShow INNER JOIN Person
      ON Person.id = TVShowPerson.person_id
      AND EyesColor.person_id = Person.id
      AND TVShowPerson.tvshow_id = TVShow.person_id_for_show
      WHERE
        TVShow.name = 'The big bang theory');

INSERT INTO min_age(name, first_name, last_name, min_age)
SELECT "Game of Thrones",
(SELECT first_name FROM TVShowPerson, EyesColor, TVShow INNER JOIN Person
        ON Person.id = TVShowPerson.person_id
        AND EyesColor.person_id = Person.id
        AND TVShowPerson.tvshow_id = TVShow.person_id_for_show
        WHERE
          TVShow.name = 'Game of Thrones'
          AND Person.age = (SELECT min(age) FROM TVShowPerson, EyesColor, TVShow INNER JOIN Person
              ON Person.id = TVShowPerson.person_id
              AND EyesColor.person_id = Person.id
              AND TVShowPerson.tvshow_id = TVShow.person_id_for_show
              WHERE
                TVShow.name = 'Game of Thrones')),

    (SELECT last_name FROM TVShowPerson, EyesColor, TVShow INNER JOIN Person
        ON Person.id = TVShowPerson.person_id
        AND EyesColor.person_id = Person.id
        AND TVShowPerson.tvshow_id = TVShow.person_id_for_show
        WHERE
          TVShow.name = 'Game of Thrones'
          AND Person.age = (SELECT min(age) FROM TVShowPerson, EyesColor, TVShow INNER JOIN Person
              ON Person.id = TVShowPerson.person_id
              AND EyesColor.person_id = Person.id
              AND TVShowPerson.tvshow_id = TVShow.person_id_for_show
              WHERE
                TVShow.name = 'Game of Thrones')),

    (SELECT min(age) FROM TVShowPerson, EyesColor, TVShow INNER JOIN Person
        ON Person.id = TVShowPerson.person_id
        AND EyesColor.person_id = Person.id
        AND TVShowPerson.tvshow_id = TVShow.person_id_for_show
        WHERE
          TVShow.name = 'Game of Thrones');


INSERT INTO min_age(name, first_name, last_name, min_age)
SELECT "Breaking bad",
(SELECT first_name FROM TVShowPerson, EyesColor, TVShow INNER JOIN Person
        ON Person.id = TVShowPerson.person_id
        AND EyesColor.person_id = Person.id
        AND TVShowPerson.tvshow_id = TVShow.person_id_for_show
        WHERE
          TVShow.name = 'Breaking bad'
          AND Person.age = (SELECT min(age) FROM TVShowPerson, EyesColor, TVShow INNER JOIN Person
              ON Person.id = TVShowPerson.person_id
              AND EyesColor.person_id = Person.id
              AND TVShowPerson.tvshow_id = TVShow.person_id_for_show
              WHERE
                TVShow.name = 'Breaking bad')),

    (SELECT last_name FROM TVShowPerson, EyesColor, TVShow INNER JOIN Person
        ON Person.id = TVShowPerson.person_id
        AND EyesColor.person_id = Person.id
        AND TVShowPerson.tvshow_id = TVShow.person_id_for_show
        WHERE
          TVShow.name = 'Breaking bad'
          AND Person.age = (SELECT min(age) FROM TVShowPerson, EyesColor, TVShow INNER JOIN Person
              ON Person.id = TVShowPerson.person_id
              AND EyesColor.person_id = Person.id
              AND TVShowPerson.tvshow_id = TVShow.person_id_for_show
              WHERE
                TVShow.name = 'Breaking bad')),

      (SELECT min(age) FROM TVShowPerson, EyesColor, TVShow INNER JOIN Person
          ON Person.id = TVShowPerson.person_id
          AND EyesColor.person_id = Person.id
          AND TVShowPerson.tvshow_id = TVShow.person_id_for_show
          WHERE
            TVShow.name = 'Breaking bad');

INSERT INTO min_age(name, first_name, last_name, min_age)
SELECT "The big bang theory",
  (SELECT first_name FROM TVShowPerson, EyesColor, TVShow INNER JOIN Person
          ON Person.id = TVShowPerson.person_id
          AND EyesColor.person_id = Person.id
          AND TVShowPerson.tvshow_id = TVShow.person_id_for_show
          WHERE
            TVShow.name = 'The big bang theory'
            AND Person.age = (SELECT min(age) FROM TVShowPerson, EyesColor, TVShow INNER JOIN Person
                ON Person.id = TVShowPerson.person_id
                AND EyesColor.person_id = Person.id
                AND TVShowPerson.tvshow_id = TVShow.person_id_for_show
                WHERE
                  TVShow.name = 'The big bang theory')),

      (SELECT last_name FROM TVShowPerson, EyesColor, TVShow INNER JOIN Person
          ON Person.id = TVShowPerson.person_id
          AND EyesColor.person_id = Person.id
          AND TVShowPerson.tvshow_id = TVShow.person_id_for_show
          WHERE
            TVShow.name = 'The big bang theory'
            AND Person.age = (SELECT min(age) FROM TVShowPerson, EyesColor, TVShow INNER JOIN Person
                ON Person.id = TVShowPerson.person_id
                AND EyesColor.person_id = Person.id
                AND TVShowPerson.tvshow_id = TVShow.person_id_for_show
                WHERE
                  TVShow.name = 'The big bang theory')),

      (SELECT min(age) FROM TVShowPerson, EyesColor, TVShow INNER JOIN Person
          ON Person.id = TVShowPerson.person_id
          AND EyesColor.person_id = Person.id
          AND TVShowPerson.tvshow_id = TVShow.person_id_for_show
          WHERE
            TVShow.name = 'The big bang theory');

SELECT * FROM age_sum
ORDER BY age_sum ASC;

SELECT * FROM min_age
ORDER BY min_age ASC;
