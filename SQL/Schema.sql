PRAGMA foreign_keys = ON;

CREATE TABLE Source (
    source_id INTEGER PRIMARY KEY AUTOINCREMENT,
    abbr VARCHAR(40),
    link_prefix VARCHAR(40),
    scrape_url VARCHAR(64),
);

CREATE TABLE Article (
    article_id INTEGER PRIMARY KEY AUTOINCREMENT,
    link_suffix VARCHAR(256) UNIQUE,
    title VARCHAR(256),
    scraped DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (source_id) REFERENCES Source(source_id) ON DELETE CASCADE
);


