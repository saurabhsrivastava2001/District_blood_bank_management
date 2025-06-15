-- Users table (for login)
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role TEXT CHECK(role IN ('admin', 'hospital')) NOT NULL
);

-- Donors table
CREATE TABLE IF NOT EXISTS donors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    blood_group TEXT NOT NULL,
    contact TEXT NOT NULL
);

-- Hospital blood requests
CREATE TABLE IF NOT EXISTS hospital_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hospital_name TEXT NOT NULL,
    blood_group TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    status TEXT DEFAULT 'Pending'
);
