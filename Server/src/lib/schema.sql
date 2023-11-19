CREATE TABLE score (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(50) NOT NULL,
  problem_0 FLOAT,
  problem_1 FLOAT,
  problem_3 FLOAT,
  problem_2 FLOAT,
  average_time FLOAT,
  PRIMARY KEY (id)
);

UPDATE score 
SET average_time = ( problem_1 + problem_2 + problem_3) / 3
WHERE average_time IS NULL;


select * from score order by average_time ASC LIMIT 3;