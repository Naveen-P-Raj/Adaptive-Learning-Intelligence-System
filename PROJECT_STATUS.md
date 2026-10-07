# Project Status

**Status: Portfolio-ready MVP**

Implemented:
- Registration and login
- SHA-256 password hashing
- Session-based authentication
- 16-subject selection
- Topic and score tracking
- Per-user CSV storage
- Rule-based retention score
- Revision alerts
- Dashboard metrics
- Retention trend
- Subject performance analysis
- Logout

Known limitations:
- CSV files are used instead of a database.
- PINs are stored directly rather than hashed.
- The retention score does not use elapsed time.
- The recommendation layer is threshold-based rather than learned from student history.
- Production deployment would require stronger authentication and data protection.
