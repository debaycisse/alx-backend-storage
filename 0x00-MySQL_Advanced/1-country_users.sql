-- Creates a table, named users with fields - id, email, name, and country.
CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, email VARCHAR(255) UNIQUE NOT NULL, name VARCHAR(255), country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US');
