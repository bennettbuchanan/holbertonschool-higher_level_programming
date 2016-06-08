-- SELECT tvshow_id
-- FROM TVShowPerson
-- WHERE tvshow_id =
--        (SELECT id
--         FROM TVShow
--         WHERE name = 'Game of Thrones');
--

SELECT DISTINCT last_name FROM TVShowPerson INNER JOIN Person
      ON Person.id = TVShowPerson.person_id
      WHERE tvshow_id =
            (SELECT id
             FROM TVShow
             WHERE name = 'Game of Thrones')
      ORDER BY last_name ASC;


SELECT count(age) FROM Person
      WHERE age > 30;


      ALTER TABLE TVShow RENAME TO tmp_TVShow;

      CREATE TABLE TVShow (
        person_id_for_show INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name char(128) NOT NULL
      );

      INSERT INTO TVShow(person_id_for_show, name)
      SELECT id, name
      FROM tmp_TVShow;

      DROP TABLE tmp_TVShow;

      SELECT id, first_name, last_name, age, color, name FROM TVShowPerson, EyesColor, TVShow INNER JOIN Person
            ON Person.id = TVShowPerson.person_id
            AND EyesColor.person_id = Person.id
            AND TVShowPerson.tvshow_id = TVShow.person_id_for_show;

SELECT sum(age) FROM Person;
