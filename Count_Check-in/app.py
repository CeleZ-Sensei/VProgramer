import ast

def function():
    """This programe is everything for check-in"""
    ### รับค่าชื่อเป็นข้อความ ###
    name = str(input())

    ### อ่านค่า และ ดึงข้อมูลจาก Database.txt และเปลี่ยนเป็น dict ###
    f = open("Database.txt", "r")
    test_db = f.read()
    student_db = ast.literal_eval(test_db)

    ### ประกาศตัวแปร ###
    count = 1
    c_db = len(student_db)

    ### ลูปเพื่อดึงข้อมูลและทำ Process ###
    for key, value in student_db.items():
        if name == key:
            kanan = value
            kanan += 1
            student_db[name] = kanan
            print(name, student_db[name])
            break
        elif count == c_db:
            inp = {name:0}
            student_db.update(inp)
            print(name, student_db[name])
            break
        count += 1

    ### เขียนค่าคืนใส่ Database.txt ###
    file = open("Database.txt", "w")
    file.write(str(student_db))
    file.close()

function()
