import re
import xlrd
import xlwt
import os

allfiles = ''


def Back(dayID, classLetter):
    classNumber = int(11)
    if classLetter == "P":
        classNumber = int(11)
    if classLetter == "O":
        classNumber = int(10)
    if classLetter == "N":
        classNumber = int(9)
    if classLetter == "M":
        classNumber = int(8)
    if classLetter == "L":
        classNumber = int(7)

    for files in os.walk('../gitHome/ExcelStorage/'):
        for _file in files:
            allfiles = _file

    raspbody = xlrd.open_workbook('../gitHome/ExcelStorage/' + allfiles[-1], formatting_info=True)
    sheet = raspbody.sheet_by_index(-3)
    predmemultitlist = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
    nasherasp1 = [[str(sheet.row_values(3, -1 - (11 - classNumber), -(11 - classNumber))),
                   str(sheet.row_values(6, -1 - (11 - classNumber), -(11 - classNumber))),
                   str(sheet.row_values(9, -1 - (11 - classNumber), -1 - (11 - classNumber))),
                   str(sheet.row_values(12, -1 - (11 - classNumber), -(11 - classNumber)))],
                  [str(sheet.row_values(15, -1 - (11 - classNumber), -(11 - classNumber))),
                   str(sheet.row_values(18, -1 - (11 - classNumber), -(11 - classNumber))),
                   str(sheet.row_values(21, -1 - (11 - classNumber), -(11 - classNumber))),
                   str(sheet.row_values(24, -1 - (11 - classNumber), -(11 - classNumber)))],
                  [str(sheet.row_values(27, -1 - (11 - classNumber), -(11 - classNumber))),
                   str(sheet.row_values(30, -1 - (11 - classNumber), -(11 - classNumber))),
                   str(sheet.row_values(33, -1 - (11 - classNumber), -(11 - classNumber))),
                   str(sheet.row_values(36, -1 - (11 - classNumber), -(11 - classNumber)))]
                  ]

    # Перенос данных со второй страницы
    sheet = raspbody.sheet_by_index(-2)
    nasherasp1.append([[str(sheet.row_values(3, 15 - (11 - classNumber), 16 - (11 - classNumber))),
                        str(sheet.row_values(6, 15 - (11 - classNumber), 16 - (11 - classNumber))),
                        str(sheet.row_values(9, 15 - (11 - classNumber), 16 - (11 - classNumber))),
                        str(sheet.row_values(12, 15 - (11 - classNumber), 16 - (11 - classNumber)))],
                       [str(sheet.row_values(15, 15 - (11 - classNumber), 16 - (11 - classNumber))),
                        str(sheet.row_values(18, 15 - (11 - classNumber), 16 - (11 - classNumber))),
                        str(sheet.row_values(21, 15 - (11 - classNumber), 16 - (11 - classNumber))),
                        str(sheet.row_values(24, 15 - (11 - classNumber), 16 - (11 - classNumber)))],
                       [str(sheet.row_values(27, 15 - (11 - classNumber), 16 - (11 - classNumber))),
                        str(sheet.row_values(30, 15 - (11 - classNumber), 16 - (11 - classNumber))),
                        str(sheet.row_values(33, 15 - (11 - classNumber), 16 - (11 - classNumber))),
                        str(sheet.row_values(36, 15 - (11 - classNumber), 16 - (11 - classNumber)))]])

    dayrasp = ''
    if (dayID == 6) or (dayID == 7):
        dayID = 0

    # обьявление дня
    if dayID == 0:
        dayrasp = "Понедельник:\n"
    if dayID == 1:
        dayrasp = "Вторник:\n"
    if dayID == 2:
        dayrasp = "Среда:\n"
    if dayID == 3:
        dayrasp = "Четверг:\n"
    if dayID == 4:
        dayrasp = "Пятница:\n"
    if dayID == 5:
        dayrasp = "Суббота:\n"

    # добавление в день предметов
    if dayID <= 2:
        for i in range(0, 3):
            predmet = str(nasherasp1[dayID][i])
            predmet = re.sub(r"['[]", "", predmet)
            predmet = re.sub(r"]", "", predmet)
            predmet = re.sub(r"n", "", predmet)
            dayrasp = dayrasp + predmet + '\n'
    if dayID >= 3:
        for i in range(0, 3):
            predmet = str(nasherasp1[3][dayID - 3][i])
            predmet = re.sub(r"['[]", "", predmet)
            predmet = re.sub(r"]", "", predmet)
            predmet = re.sub(r"n", "", predmet)
            dayrasp = dayrasp + predmet + '\n'

    return dayrasp


def LastRasp():
    allfiles = ''
    for files in os.walk('../VkBot/ExcelStorage/'):
        for _file in files:
            allfiles = _file

    return (allfiles[-1])
