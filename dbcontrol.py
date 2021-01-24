import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

def exists(user):
    c.execute("SELECT * FROM rep WHERE userid = (?)", (user,))
    ret = c.fetchall()
    if ret:
        return True
    else:
        c.execute('INSERT INTO rep (userid, reps, repers) VALUES ((?),0,"")', (user,))
        return exists(user)

def showrep(user):
    if exists(user):
        c.execute("SELECT reps FROM rep WHERE userid = (?)", (user,))
        rep = c.fetchone()
        rep = str(rep)[1:-2]
        return int(rep)

def getrepers(user):
    c.execute("SELECT repers FROM rep WHERE userid = (?)", (user,))
    ret = c.fetchone()
    return str(ret)[2:-3]
    
def addrep(user, source):
    if exists(user):
        reper = getrepers(user)
        print(reper)
        for r in reper.split("-"):
            if str(r) == str(source):
                return str("You have already repped them!")

        reper = str(reper) + "-" + str(source)

        rep = showrep(user)
        rep += 1
        c.execute("UPDATE rep SET reps = (?), repers = (?) WHERE userid = (?)", (rep, reper, user))
        conn.commit()
        return str("Rep added!")

def adm_remrep(user, amount:int):
    if exists(user):
        reper = showrep(user)
        final = int(reper) - int(amount)
        c.execute("UPDATE rep SET reps = (?) WHERE userid = (?)", (final, user,))
        conn.commit()
        return str(amount) + " has been removed!"

def adm_addrep(user, amount: int):
    if exists(user):
        reper = showrep(user)
        final = int(reper) + int(amount)
        c.execute("UPDATE rep SET reps = (?) WHERE userid = (?)", (final, user,))
        conn.commit()
        return str(amount) + " has been added!" 
