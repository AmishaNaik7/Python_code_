import sqlite3

 
conn = sqlite3.connect("job_applications.db")
cursor = conn.cursor()

 
cursor.execute('''
CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY,
    company TEXT,
    position TEXT,
    date_applied TEXT,
    status TEXT
)
''')

 
def add_application(company, position, date_applied, status):
    cursor.execute("INSERT INTO applications (company, position, date_applied, status) VALUES (?, ?, ?, ?)", 
                   (company, position, date_applied, status))
    conn.commit()
    print(f"✅ Added application for {position} at {company}")

 
def view_applications():
    cursor.execute("SELECT * FROM applications")
    apps = cursor.fetchall()
    for app in apps:
        print(app)

 
add_application("Google", "Software Engineer", "2025-05-19", "Applied")
add_application("Microsoft", "Data Scientist", "2025-05-18", "Interview Scheduled")

print("\n📋 All Applications:")
view_applications()

 
conn.close()