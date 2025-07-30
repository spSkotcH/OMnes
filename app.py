from traceback import print_tb

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def update_data():
    conn = sqlite3.connect('TData.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(name) FROM AllTimeRate")
    count = cursor.fetchall()[0][0]
    for i in range(count):
        cursor.execute(f"SELECT name FROM AllTimeRate WHERE id = {i+1}")
        name = cursor.fetchall()[0][0]
        cursor.execute(f"SELECT COUNT(`{name}`) FROM AllRate")
        scr = cursor.fetchall()[0][0]
        if scr >= 50:
            cursor.execute(f"SELECT AVG(`{name}`) FROM AllRate")
            nm = cursor.fetchall()[0][0]
            num = round(nm, 2)
            print('done')
            q = "UPDATE AllTimeRate SET number = ? WHERE id = ?"
            cursor.execute(q, (num, i+1))
        else:
            q = "UPDATE AllTimeRate SET number = ? WHERE id = ?"
            cursor.execute(q, (99, i + 1))
        conn.commit()
    conn.close()
    print('yeah')
    season_r()
    year_r()
    print('hell yeah')

def season_r():
    conn = sqlite3.connect('TData.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(name) FROM AllTimeRate")
    count = cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT(GameID) FROM AllRate")
    count_games = cursor.fetchall()[0][0]
    for i in range(count):
        cursor.execute(f"SELECT name FROM AllTimeRate WHERE id = {i + 1}")
        name = cursor.fetchall()[0][0]
        cursor.execute(f"SELECT `{name}` FROM AllRate WHERE GameID = 227 OR GameID = 228 OR GameID = 229 OR GameID = 230 OR GameID = 231 OR GameID = 232 OR GameID = 233 OR GameID = 234 OR GameID = 235 OR GameID = 236 OR GameID = 237 OR GameID = 238 OR GameID = 239")
        score = cursor.fetchall()
        games_score = len(score)
        x = 0
        t = 0
        for b in range(games_score):
            if type(score[b][0]) == int:
                x += score[b][0]
                t += 1
            else:
                continue
        if t >= 7:
            nm = x / t
            if type(nm) == 'float' or 'int':
                num = round(nm, 2)
                q = "UPDATE LastSeason SET number = ?, name = ? WHERE id = ?"
                cursor.execute(q, (num, name, i + 1))
                conn.commit()
            else:
                continue
    conn.close()

def year_r():
    conn = sqlite3.connect('TData.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(name) FROM AllTimeRate")
    count = cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT(GameID) FROM AllRate")
    count_games = cursor.fetchall()[0][0]
    for i in range(count):
        cursor.execute(f"SELECT name FROM AllTimeRate WHERE id = {i + 1}")
        name = cursor.fetchall()[0][0]
        cursor.execute(f"SELECT `{name}` FROM AllRate WHERE GameID = 206 OR GameID = 207 OR GameID = 208 OR GameID = 209 OR GameID = 210 OR GameID = 211 OR GameID = 212 OR GameID = 213 OR GameID = 214 OR GameID = 215 OR GameID = 216 OR GameID = 217 OR GameID = 218 OR GameID = 219 OR GameID = 220 OR GameID = 221 OR GameID = 222 OR GameID = 223 OR GameID = 224 OR GameID = 225 OR GameID = 226 OR GameID = 227 OR GameID = 228 OR GameID = 229 OR GameID = 230 OR GameID = 231 OR GameID = 232 OR GameID = 233 OR GameID = 234 OR GameID = 235 OR GameID = 236 OR GameID = 237 OR GameID = 238 OR GameID = 239 OR GameID = 240")
        score = cursor.fetchall()
        games_score = len(score)
        x = 0
        t = 0
        for b in range(games_score):
            if type(score[b][0]) == int:
                x += score[b][0]
                t += 1
            else:
                continue
        if t >= 25:
            nm = x / t
            if type(nm) == 'float' or 'int':
                num = round(nm, 2)
                q = "UPDATE LastYear SET number = ?, name = ? WHERE id = ?"
                cursor.execute(q, (num, name, i + 1))
                conn.commit()
            else:
                continue
    conn.close()

def ShowResult(GmID):
    conn = sqlite3.connect('TData.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM AllTimeRate")
    names = cursor.fetchall()
    print(names)
    namelist = []
    for name in range(len(names)):
        namelist.append(names[name][0])
    reslist = []
    for res in range(len(names)):
        cursor.execute(f"SELECT `{namelist[res]}` FROM AllRate WHERE GameID = {GmID}")
        reslist.append(cursor.fetchall()[0][0])
    conn.close()

    return namelist, reslist

def Skol():
    conn = sqlite3.connect('TData.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(name) FROM AllTimeRate")

    return cursor.fetchall()[0][0]

def CountGames():
    conn = sqlite3.connect('TData.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(GameID) FROM AllRate")
    count = cursor.fetchall()[0][0]

    return count


def AddCommand(new_nm):
    conn = sqlite3.connect('TData.db')
    cursor = conn.cursor()
    cursor.execute(f"ALTER TABLE AllRate ADD COLUMN {new_nm} INTEGER")
    cursor.execute(f"INSERT INTO AllTimeRate (name, number) VALUES ('{new_nm}', 99)")
    conn.commit()

    conn.close()

def CheckRate(comm):
    conn = sqlite3.connect('TData.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(GameID) FROM AllRate WHERE `{comm}` = 1")
    first = cursor.fetchall()[0][0]
    cursor.execute(f"SELECT COUNT(GameID) FROM AllRate WHERE `{comm}` = 2")
    second = cursor.fetchall()[0][0]
    cursor.execute(f"SELECT COUNT(GameID) FROM AllRate WHERE `{comm}` = 3")
    third = cursor.fetchall()[0][0]
    cursor.execute(f"SELECT Photo FROM AllTimeRate WHERE name = '{comm}' ")
    photo = cursor.fetchall()[0][0]

    return first, second, third, photo

def command_statistic(command):
    conn = sqlite3.connect('TData.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT cb FROM AllTimeRate WHERE name = '{command}'")
    cat = cursor.fetchall()[0][0]
    cursor.execute(f"SELECT fa FROM AllTimeRate WHERE name = '{command}'")
    funny = cursor.fetchall()[0][0]
    cursor.execute(f"SELECT cf FROM AllTimeRate WHERE name = '{command}'")
    city = cursor.fetchall()[0][0]
    cursor.execute(f"SELECT ht FROM AllTimeRate WHERE name = '{command}'")
    head = cursor.fetchall()[0][0]
    cursor.execute(f"SELECT gm FROM AllTimeRate WHERE name = '{command}'")
    middle = cursor.fetchall()[0][0]
    cursor.execute(f"SELECT Photo FROM AllTimeRate WHERE name = '{command}'")
    photo = cursor.fetchall()[0][0]

    return cat, funny, city, head, middle, photo

def get_data():
    # Подключение к базе данных
    conn = sqlite3.connect('TData.db')
    cursor = conn.cursor()

    # Выполнение запроса для получения данных
    cursor.execute("SELECT name, number FROM AllTimeRate")
    data = cursor.fetchall()

    conn.close()
    return data

def get_names():
    conn = sqlite3.connect('TData.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM AllTimeRate")
    data = cursor.fetchall()
    conn.close()
    names = []
    for i in range(len(data)):
        names.append(data[i][0])
    return names

def get_y_data():
    conn = sqlite3.connect('TData.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name, number FROM LastYear")
    data = cursor.fetchall()
    while (None, None) in data:
        data.remove((None, None))
    new_data = []
    for i in range(len(data)):
        if data[i][1] != 0.0:
            new_data.append(data[i])
        else:
            continue
    data = new_data

    conn.close()
    return data

def get_s_data():
    conn = sqlite3.connect('TData.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name, number FROM LastSeason")
    data = cursor.fetchall()
    while (None, None) in data:
        data.remove((None, None))
    new_data = []
    for i in range(len(data)):
        if data[i][1] != 0.0:
            new_data.append(data[i])
        else:
            continue
    data = new_data

    conn.close()
    return data

@app.route('/')
def index():
    data = get_data()
    data.sort(key=lambda x: x[1])
    return render_template('index.html', data=data)

@app.route('/season')
def season():
    data = get_s_data()
    data.sort(key=lambda x: x[1])
    season_name = "лето"
    if season_name == "зима":
        col = "#4b86c9"
    elif season_name == "осень":
        col = "#cc8b29"
    elif season_name == "лето":
        col = "#ccc729"
    elif season_name == "весна":
        col = "#4aa81e"
    return render_template('Season.html', data=data, season_name=season_name, col=col)

@app.route('/year')
def year():
    data = get_y_data()
    data.sort(key=lambda x: x[1])
    return render_template('Year.html', data=data)

@app.route('/teams')
def teams():
    skol = Skol()
    names = get_names()
    data = []
    for i in range(skol):
        data.append(CheckRate(names[i]))
    return render_template('photos.html', skol=skol, names=names, data=data)

@app.route('/team/<comm>')
def gocomand(comm):
    command = comm
    rate = CheckRate(comm)
    stat_list = command_statistic(command)
    print(stat_list)
    cb = stat_list[0]
    if cb == None:
        cb = 0
    fa = stat_list[1]
    if fa == None:
        fa = 0
    cf = stat_list[2]
    if cf == None:
        cf = 0
    ht = stat_list[3]
    if ht == None:
        ht = 0
    gm = stat_list[4]
    if gm == None:
        gm = 0
    photo = stat_list[5]
    return render_template('command.html', command=command, rate=rate, cb=cb,fa=fa , cf=cf, ht=ht, gm=gm, photo=photo)

@app.route('/admin')
def admin_page():
    countgames = CountGames()
    update_data()
    gameID = 1
    res = ShowResult(gameID)
    lenght = Skol()
    return render_template('admin.html', countgames=countgames, res=res, lenght=lenght)

@app.route('/AddCom', methods=['GET', 'POST'])
def addcomm():
    countgames = CountGames()
    gameID = 1
    res = ShowResult(gameID)
    new_name = request.form['newname']
    lenght = Skol()
    print(new_name)
    AddCommand(new_name)
    return render_template('admin.html', countgames=countgames, res=res, lenght=lenght)

@app.route('/SetGame', methods=['GET', 'POST'])
def setgame():
    countgames = CountGames()
    gameID = request.form['namesetgm']
    res = ShowResult(gameID)
    lenght = Skol()
    print(res)
    return render_template('admin.html', countgames=countgames, res=res, lenght=lenght)


if __name__ == '__main__':
    app.run()