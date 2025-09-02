""" เขียน function ชื่อ welcome_message ที่มีคุณสมบัติดังนี้:
 
รับ parameter 2 ตัว คือ name และ course
return ข้อความต้อนรับในรูปแบบ string
รูปแบบ: "Welcome [name] to [course] class!"
 
"""
def welcome_message(name, course):
    # Your Problem 1 solution
    return "Welcome" + name + "to" + course + "class!"
    return f"Welcome {name} to {coutse} class!"
""" เขียน function ชื่อ calculate_circle ที่มีคุณสมบัติดังนี้:
 
รับ parameter 1 ตัว คือ radius
return dictionary ที่มี area และ circumference
ใช้ค่า π = 3.14159
ปัดเศษทั้งสองค่าให้เหลือ 2 ตำแหน่งหลังจุดทศนิยม """
def get_circle_info(radius):
    #Your Problem 2 solution
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return {
        "area":area,
        "circumference":circumference
    }
""" เขียน function ชื่อ create_user_profile ที่มีคุณสมบัติดังนี้:
 
รับ parameters: username (จำเป็น), age (ค่าเริ่มต้น 18), premium (ค่าเริ่มต้น False)
return string ที่จัดรูปแบบข้อมูลผู้ใช้
รูปแบบ: "[username] (age: [age]) - [Premium User / Standard User]"
 
"""
def create_user_profile(username, age=18,premium=False):
    #Your Problem 3 solution
    if premium == True:
        return f"{username} (age: {age}) - Premium User"
    else :
        return f"{username} (age: {age}) - Standard User"
   
""" เขียน function ชื่อ analyze_scores ที่มีคุณสมบัติดังนี้:
 
รับ list ของคะแนน (ตัวเลข)
return dictionary ที่มี:
 
total: ผลรวมของคะแนนทั้งหมด
average: คะแนนเฉลี่ย (ปัดเศษ 1 ตำแหน่งหลังจุดทศนิยม)
highest: คะแนนสูงสุด
lowest: คะแนนต่ำสุด
passed: จำนวนคะแนนที่ >= 70 """
def analyze_scores(numbers):
    #Your Problem 4 solution
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    minimum = min(numbers)
    maximum = max(numbers)
    counter = 0
 
    for number in numbers:
        if number >=70:
            counter += 1
 
    return {
        'sum': total,
        'count': count,
        'average': round(average,2),
        'lowest': lowest,
        'highest': highest,
        'passed': counter
    }
 
 
""" เขียน function ชื่อ count_vowels_consonants ที่มีคุณสมบัติดังนี้:
 
รับ parameter text เป็น string
นับสระ (a, e, i, o, u) และพยัญชนะ (ไม่นับช่องว่างและตัวเลข)
return dictionary ที่มี vowels และ consonants counts
ไม่สนใจตัวใหญ่ตัวเล็ก (case insensitive) """
 
def count_vowels_consonants(text):
    #Your Problem 5 solution
    text = "I'm Iron Man"
    text.lower() #i'm iron man
    text.replace(" ","") #i'm iron man
    text.replace("0","")
    text.replace("1","")
    text.replace("2","")
    text.replace("3","")
    text.replace("4","")
    text.replace("5","")
    text.replace("6","")
    text.replace("7","")
    text.replace("8","")
    text.replace("9","")
    vewels = text.count('a') + text.count('e')+text.count+text('i')+text.count+text('o')+text.count+text('u')
    consonants = len(text) - vowels
 
    return {
        'vowels' : vowels,
        'consonants': consonants
    }