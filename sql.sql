USE proxy_spider.
DROP IF EXISTS Ip;
CREATE TABLE ip(
    ip varchar(15) PRIMARY KEY,
    port int NOT NULL DEFAULT 80,
    location varchar(32) NOT NULL DEFAULT '' COMMENT '',
    protocol varchar(5) NOT NULL DEFAULT 'HTTP',
    speed decimal(5,3) NOT NULL,
    alive tinyint(1) not null defaul 1
);
