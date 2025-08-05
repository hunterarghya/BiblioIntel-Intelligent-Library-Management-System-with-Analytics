-- BOOKS TABLE
CREATE TABLE IF NOT EXISTS books (
    bookid TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT,
    subject TEXT,
    dept TEXT,
    qnty INTEGER,
    shelfno TEXT
);

-- STUDENTS TABLE
CREATE TABLE IF NOT EXISTS students (
    studid TEXT PRIMARY KEY,
    name TEXT,
    phone TEXT,
    sem INTEGER,
    year INTEGER,
    dept TEXT
);

-- SUBJECTS TABLE
CREATE TABLE IF NOT EXISTS subjects (
    subid TEXT PRIMARY KEY,
    subname TEXT
);

-- TRANSACTIONS TABLE
CREATE TABLE IF NOT EXISTS transactions (
    tscnid INTEGER PRIMARY KEY AUTOINCREMENT,
    bookid TEXT,
    studid TEXT,
    issue_date TEXT,
    return_date TEXT,
    stud_fine REAL DEFAULT 0,
    FOREIGN KEY(bookid) REFERENCES books(bookid),
    FOREIGN KEY(studid) REFERENCES students(studid)
);

-- SETTINGS TABLE
CREATE TABLE IF NOT EXISTS settings (
    id INTEGER PRIMARY KEY CHECK(id = 1),
    fine REAL DEFAULT 2.0,
    maxdays INTEGER DEFAULT 14,
    maxbk INTEGER DEFAULT 3
);

-- Initialize default settings row
INSERT OR IGNORE INTO settings (id, fine, maxdays, maxbk) VALUES (1, 2.0, 14, 3);

-- MARKS TABLE (for analytics)
CREATE TABLE IF NOT EXISTS marks (
    studid TEXT,
    subid TEXT,
    sem INTEGER,
    year INTEGER,
    marks INTEGER,
    FOREIGN KEY(studid) REFERENCES students(studid),
    FOREIGN KEY(subid) REFERENCES subjects(subid)
);
