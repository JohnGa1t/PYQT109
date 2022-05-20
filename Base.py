import sqlite3
import os


def ReadBase(nomer):
    try:    
        db = "base\\" +nomer[0:3] + ".db"
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute("select * from AbonInfo where nomer=:c",{"c":nomer}) 
        search = cursor.fetchall()

        for row in search:
                    print("NOMER:", row[0])
                    print("MG:", row[1])
                    print("VID:", row[2])
                    print("ABON:", row[3])


        return search
    except sqlite3.OperationalError as e:
        search = [(' ', ' ', ' ', ' ',  str(e),' ', ' ')]
        
        return search
    except :
        search = [('null', 'null', 'null', 'null',  "null",'null', 'null')]
        
        return search    
def WriteAll_BaseSql(nomer,mg,tip,abon,adress,mobile,prim):
    db = "base\\" +nomer[0:3] + ".db"
    #print(dpg.get_value(modal_TXT5.id))
    # nomer = dpg.get_value(modal_TXT1.id)
    # mg = dpg.get_value(modal_TXT6.id)
    # abon = dpg.get_value(modal_TXT2.id)
    # adress = dpg.get_value(modal_TXT3.id)
    # mobile = dpg.get_value(modal_TXT4.id)
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    sql_update_query = """Update AbonInfo set mg =:m,vid_podkl =:t, abon = :a,adress =:aa,mobile =:mb,coment =:c where nomer =:n """
    cursor.execute(sql_update_query,{"n":nomer,"m":mg,"t":tip,"a":abon,"aa":adress,"mb":mobile,"c":prim})
    #print(a)
    conn.commit()
    conn.close()

def WriteMG_BaseSql(nomer,mg):
    db = "base\\" +nomer[0:3] + ".db"
    #print(dpg.get_value(modal_TXT5.id))
    # nomer = dpg.get_value(modal_TXT1.id)
    # mg = dpg.get_value(modal_TXT6.id)
    # abon = dpg.get_value(modal_TXT2.id)
    # adress = dpg.get_value(modal_TXT3.id)
    # mobile = dpg.get_value(modal_TXT4.id)
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    sql_update_query = """Update AbonInfo set mg =:m where nomer =:n """
    cursor.execute(sql_update_query,{"n":nomer,"m":mg})
    #print(a)
    conn.commit()
    conn.close()