begin;
drop DATABASE IF EXISTS PyCity;
create DATABASE PyCity;
USE PyCity;
commit;

begin;
CREATE TABLE IF NOT EXISTS City (
code VARCHAR(255) NOT NULL PRIMARY KEY,
city VARCHAR(255) NOT NULL,
population INTEGER,
country VARCHAR(255)
);
commit;

