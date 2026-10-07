# Architecture

## Components

1. **Streamlit UI**
   - Registration and login
   - Topic entry
   - Dashboard
   - Alerts and charts

2. **Authentication Layer**
   - Username/password verification
   - SHA-256 password hashing
   - Streamlit session state

3. **CSV Storage**
   - `users.csv` stores account records
   - `<username>_data.csv` stores study topics

4. **Retention Engine**
   - Computes retention from score and revision count
   - Clips the result to 0–100

5. **Recommendation/Status Layer**
   - Converts retention into:
     - Revise Now
     - Revise Soon
     - Good

6. **Visualization Layer**
   - Topic count
   - Average score
   - Average retention
   - Retention trend
   - Subject-level average score
