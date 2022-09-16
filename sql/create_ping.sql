CREATE TABLE IF NOT EXISTS ping (
    'id' INTEGER PRIMARY KEY,
    'address_dest' TEXT,
    'address_source' TEXT,
    'unit' TEXT,
    'ping' REAL NULL,
    'timestamp' DATETIME NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%f','now'))
);