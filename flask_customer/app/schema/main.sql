CREATE TABLE memberTable(
    id     INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    pw     VARCHAR(23) NOT NULL,
    name    VARCHAR(30) NOT NULL,
    age    INT UNSIGNED NOT NULL 
) CHARSET=utf8;




-- source /Users/cuixindan/workspace/python/flask_customer/app/schema/main.sql