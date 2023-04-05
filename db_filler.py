import sqlite3
check_dis = False
add_all = False
insert_students = False

check_dis = input('You want to get all disciplines in a list:(Y/N)')
if check_dis == 'Y':
    check_dis = True
    add_all = input('You want to add all disciplines in your db: (Y/N)')
    if add_all == 'Y':
        add_all = True
    else:
        print('NEXT ---->')
else:
    print('Next ->>>')

insert_students = input('You want to add all students from your users.db on your grade.db?: (Y/N)')
if insert_students == 'Y':
    insert_students = True
else:
    print('You app is done!')

if check_dis == True:
    conn = sqlite3.connect('data/discipline.db')
    cursor =  conn.cursor()
    dis = []
    for discipline in cursor.execute('SELECT "Name" FROM disciplines'):
        discipline = discipline[0].replace(" ", "_")
        dis.append(discipline)

    conn.commit()
    cursor.close()
    conn.close()
if add_all == True:
    conn = sqlite3.connect('data/grades.db')
    cursor = conn.cursor()

    for discipline in dis:
        cursor.execute('ALTER TABLE grades ADD COLUMN {} TEXT'.format(discipline))

    conn.commit()
    cursor.close()
    conn.close()
if insert_students == True:
    conn1 = sqlite3.connect('data/grades.db')
    cursor1 = conn1.cursor()
    cnps = []

    for cnp in cursor1.execute('SELECT CNP FROM grades'):
        cnps.append(cnp[0])



    conn = sqlite3.connect('data/users.db')
    cursor = conn.cursor()

    for cnp in cursor.execute('SELECT "CNP" FROM all_users WHERE Student = "Yes"'):
        if cnp[0] in cnps:
            pass
        else:
            cursor1.execute('INSERT INTO grades (CNP) VALUES (?)', (str(cnp[0]),))

    conn1.commit()
    cursor1.close()
    conn1.close()