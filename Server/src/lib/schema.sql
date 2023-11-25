CREATE TABLE score (
  id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(50) NOT NULL,
  problem_0 DOUBLE(16,8),
  problem_1 DOUBLE(16,8),
  problem_3 DOUBLE(16,8),
  problem_2 DOUBLE(16,8),
  average_time DOUBLE(16,8),
  PRIMARY KEY (id)
);

UPDATE score 
SET average_time = ( problem_1 + problem_2 + problem_3) / 3
WHERE average_time IS NULL;


select * from score order by average_time ASC LIMIT 3;