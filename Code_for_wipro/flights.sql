CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL
);

INSERT INTO flights
(origin, destination, duration)
Values("New York", "New Delhi", 415);

INSERT INTO flights
(origin, destination, duration)
Values("Chennai", "New Delhi", 315);

INSERT INTO flights
(origin, destination, duration)
Values("Patna", "New Delhi", 715);

INSERT INTO flights
(origin, destination, duration)
Values("New York", "Chhapra", 815);

SELECT * FROM flights;
SELECT origin, destination FROM flights;
SELECT * FROM flights WHERE origin = "New York";