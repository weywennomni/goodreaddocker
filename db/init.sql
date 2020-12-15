-- CREATE DATABASE new_db;
use test_db;

-- CREATE TABLE query_results (
--     id INT(11) PRIMARY KEY AUTO_INCREMENT,
--     query VARCHAR(512) NOT NULL,
--     result VARCHAR(8000)
-- );


CREATE TABLE query_results (
  id int NOT NULL AUTO_INCREMENT,
  keyword varchar(255) NOT NULL,
  data_keyword JSON,
  PRIMARY KEY (id)
);


INSERT INTO
  query_results (keyword, data_keyword)
VALUES
  ('test1', '{"test1":"test1"}');

-- INSERT INTO query_results ('keyword', 'data_keyword')
-- VALUES ('test1', '{"test1":"test1"}');


-- ,
    -- 'created' DATETIME DEFAULT CURRENT_TIMESTAMP(),
    -- 'updated' DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP()

-- --   data_keyword VARCHAR(8000),