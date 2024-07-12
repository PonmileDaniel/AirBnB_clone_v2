-- Creating hbnb_dev_db database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the user if the user doesn't exist and set password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';

-- Set password
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
USE hbnb_test_db;

-- Grant all the privilege on the db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
