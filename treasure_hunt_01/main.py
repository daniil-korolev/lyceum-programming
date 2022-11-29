import urllib.request
import cryptocode
from os.path import exists
import string
import random

def gs(lg):
    l = string.ascii_lowercase
    r = ''.join(random.choice(l) for i in range(60))
    return r

def dcd(s, p):
    c = cryptocode.decrypt(s, p)
    if c != False and c == c[0:len(c)]:
        return c
    else:
        return gs(len(s)) 

encoded_res_1 = "bJ2xAqj/DsXgMFauFVixP8HuOUQBUK6WQbsLJCyaW5XjuSfnUvJ2nqfeBX/S/Aob4/6k8JxFkShEPL0SGCC3VvnvL2qdGcrdWUHTShUzS1fD2ttIGwd79U5/3tIWyHZUUiU7BEl9wda7rBpS74Aa3DRqWG/j69fH5psqSQMzYbgV0YukE24GVW7lClLPAerA4s1b9HML8XkisXv0O2Ldtaq9XQoSfAwLd09fouDvuQ0SkC43HNwhInwgVvMjqHUTjMdbf/Bdb6XcF04NaldWg/U8wM2+WDsiJgyw4jSY54vQ9rVbxeRx6C4Vi3ob4oD9pQEFmf6yPFDLU55QmkKM3mQtYq6BbZqAOvjLsDg5mM9Lzb2b2W8uOoJEokAz3dKIQspwaKIYqEFYFMprRlxMtyx9qittsOBzhrmm/Plvl+h6Fc5ySGoQW8RHau1V/Ws9sfk2TU7IeQ41CeUbcQ==*nGBtRATdTxC+rNT36SuLXQ==*9Q00Dxsg635m++S0DWFnbw==*+tqgecpJhiF+8LT/avltpQ=="
encoded_res_2 = "bVgmbVhNzJxcMDc0ykxWjLQ9TM/q40oZhFF2MVy0AmME3CDUfqAmSYO8SdAC4GGaR41S7TfyHwY8VyglFk+g8MOqzb0aRQY8lOh7JRWClDBrJNmZK9Fhur73+NilEDT7LaxjF//2/Ou2gOB5R36e/XSnSaHwbSHTWzRurPmThhLmTmgfhsn/FKmwd2Z7leWkAlaR+WOkyhDvYfXmJohms88=*0gZKZ9JQQkhQnHt6zKOvTQ==*jrDTCK9ja8BZTxqRYPtqHw==*i2Ow86fO1N2gSfieJndTPw=="
encoded_res_3 = "TkGKuA69SH3P7I4TgqjlUvhFkp1fnXq2LOAloe1e7jjweAYVSN3/k+KAKQ82moN7KkqfiBAjEYigZNtLFQXJW3ltkmeUEsu6IwXqYPewbt0iwljZJ+z8DlYhaw8MTfiYejkEnNbVHY/oqRqMZ9KxyP5ypVyMyYjEYdgFJGhujFWxbLwckWV7mO25KYGLlMj9SDiLBZ7Sr5AXRScrhih/t1UnWuUMYpjtfNfabv5DmFQrk+Z0Qm88Ozw065AsOLfEgxx1zBGLMRjU8jAJ3FBGrS3GnPuAXDFXiL7XVbmuTSUUcrmUi8n1OKOCxCCOMX4CDDO5AlcyWlAb7GTN4BuryNHcdOp4ZGXxvaz/Fxl2IOtdJHS+U7INsNiTRFdlyo4EX8oTNJ3MUSI2B6u2cBs1Si/sXO2j3Yny3/2Onmc3Udei3n/UbPVyrAjkGy4I/1Xlt1r6sJh3jpaGFyKfRKEqOPON4DqQBesRYDEwUqpqFBSMCtam8fQjnJR2lgidPGAM5kGQnKqLfC7lxkN0GqLF1kPv6WqkFGyfMgeOUTLOzx0PKfGociFB16es1C1jnjuX681R4+aF/hT27G3d3j+6bTpeDbMFv9nZIMonHxrYWTyoom4m8a9WAPVRDbKQ+X0w+AsdltHlPm4TnlMtnVavWn0mEx8XL6l6yyADKTP/6GnAVgMPF1Jj2fd5CagD+Tl1jsk=*/62hzp2d5vcsZ1ucZbO0hg==*Wz2WLyK+UrOXZLeCwKTUtw==*xhgNNACgdq800H5jLvEEFA=="
f1_exists = exists("f1.txt")
if not f1_exists:
    urllib.request.urlretrieve("https://raw.githubusercontent.com/daniil-korolev/lyceum-programming/main/treasure_hunt_01/resources/f1.txt", "f1.txt")

words = []
with open("f1.txt") as file:
    for line in file:
        words.append(line.rstrip())

# Добро пожаловать на цифровой остров приключений
# Первые трое из вас, сообщив секретное слово преподавателю - получат клад!
# Для победы понадобится: быстрота ума, умение гуглить, ну и немного знание питона 
# Удачи!


# Задание номер 1!
# В массиве words лежит много тысяч слов
# Вам необходимо найти последние 5 символов второго самого большого слова в массиве
# И ввести их в переменную res_1 снизу
# пример: 3 слова в массиве ["террариум", "кот", "прокрастинация"]. Второе самое большое слово - террариум, последние 5 букв - ариум

# в res_1 введите ответ на первое задание и получите следующее
res_1 = ""
decoded_res_1 = dcd(encoded_res_1, res_1)
print("1: " + decoded_res_1)

# в res_2 введите ответ на второе задание и получите следующее
res_2 = ""
decoded_res_2 = dcd(encoded_res_2, res_2)
print("2: " + decoded_res_2)

# в res_3 введите ответ на третье задание и получите следующее
res_3 = ""
decoded_res_3 = dcd(encoded_res_3, res_3)
print("3: " + decoded_res_3)

# ответ на 4 задание пришлите Дане в телеграме :)