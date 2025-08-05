# BiblioIntel: Intelligent Library Management System with Analytics

**BiblioIntel** is a smart and modular Library Management System built with **Python**, **Tkinter**, and **SQLite**, designed for schools, colleges, and personal collections. It simplifies book tracking, student records, and library operations — while laying the foundation for **data-driven decision-making**, **automation**, and **reader-friendly digital interaction**.

---

## Current Features (MVP)

- Add, View & Manage Books
- Add, View & Manage Students
- Issue / Return Books
- View Transactions
- Update Book Quantity
- Search Transactions by Book ID / Student ID
- Settings for fine configuration
- Export reports to **CSV**
- Login authentication (for future roles like Admin/Student)
- SQLite3 for portable, offline-first database
- Tkinter GUI for ease of use

---

## Future Scope

### Data Analytics

- Top borrowed books
- Department-wise reading trends
- Peak usage hours and demand spikes
- Predictive restocking and inventory forecasts
- Fine optimization insights
- **Toppers’ Book Analysis**: Discover which books are most borrowed by academic toppers.
- **Faculty Book Usage**: Track books issued by faculty and identify the most used materials for teaching.
- **Institutional Preferences**: Identify books preferred by faculty from top colleges.
- **Idle Books Detection**: Highlight books with negligible activity for better space optimization.
- **Smart Selection**: Help students and teachers choose books based on real-world usage and performance.

These analytics will empower librarians to make informed decisions on inventory, and students/teachers to choose the best resources.

### Notifications

- Email / SMS alerts:
  - Due dates
  - Fines
  - Pre-orders ready
- Push notifications via mobile app

### Mobile App (Planned)

- Browse and search catalog
- Pre-order books
- Pay fines / library fees online
- Home delivery of books (Ekart integration)

### UI/UX Overhaul

- Sleek, modern GUI
- Role-based dashboards (Admin/Student)
- Accessibility enhancements

---

## Installation

```bash
pip install -r requirements.txt
python main.py
```

Or run the Windows executable:

```
dist/main.exe
```

---

## Tech Stack

- Python 3.11+
- SQLite3
- Tkinter
- PyInstaller
- Future: Flask/Django, React Native, REST API

---

## Folder Structure

```
BiblioIntel/
├── db/
│   └── schema.sql
├── gui/
│   └── *.py (UI modules)
├── services/
│   └── *.py (logic)
├── library.db
├── main.py
├── README.md
└── LICENSE
```

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Contributions

**Open source contributions are welcome!**

- Fork the repo
- Create a new branch
- Submit a pull request

All contributions will be reviewed before merging.

---

### Project Status: MVP Complete | Analytics & App in Progress
