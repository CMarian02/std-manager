import sqlite3

conn = sqlite3.connect('data/discipline.db')
cursor =  conn.cursor()
dis = []
for discipline in cursor.execute('SELECT "Name" FROM disciplines'):
    discipline = discipline[0].replace(" ", "_")
    dis.append(discipline)

conn.commit()
cursor.close()
conn.close()

conn = sqlite3.connect('data/grades.db')
cursor = conn.cursor()

for discipline in dis:
    cursor.execute('ALTER TABLE grades ADD COLUMN {} TEXT'.format(discipline))

conn.commit()
cursor.close()
conn.close()