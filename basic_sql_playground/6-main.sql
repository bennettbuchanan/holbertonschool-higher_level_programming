ALTER TABLE TVShow RENAME TO tmp_TVShow;

CREATE TABLE TVShow (
  person_id_for_show INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  name char(128) NOT NULL
);

INSERT INTO TVShow(person_id_for_show, name)
SELECT id, name
FROM tmp_TVShow;

DROP TABLE tmp_TVShow;

SELECT name, age FROM TVShowPerson, EyesColor, TVShow INNER JOIN Person
      ON Person.id = TVShowPerson.person_id
      AND EyesColor.person_id = Person.id
      AND TVShowPerson.tvshow_id = TVShow.person_id_for_show;
