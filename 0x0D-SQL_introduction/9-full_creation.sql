-- A script that create a second table 
CREATE TABLE IF NOT EXISTS second_table(id INT, name VARCHAR(256), score INT);

-- A script that insert 4 values into the table created

INSERT INTO `second_table` (`id`,`name`, `score`) VALUES (1, "john", 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (2, "alex", 3);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (3, "Bob", 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (4, "George", 8);
