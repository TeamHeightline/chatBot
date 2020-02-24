import re
import xlrd
import xlwt
import os

allfiles = ''

def Back(dayID):
    for files in os.walk('../VkBot/ExcelStorage/'):
        for _file in files:
            allfiles = _file

    raspbody = xlrd.open_workbook('../VkBot/ExcelStorage/' + allfiles[-1], formatting_info=True)
    sheet = raspbody.sheet_by_index(-3)
    predmemultitlist = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
    nasherasp1 = [[str(sheet.row_values(3, -1)), str(sheet.row_values(6, -1)), str(sheet.row_values(9, -1)),
                   str(sheet.row_values(12, -1))],
                  [str(sheet.row_values(15, -1)), str(sheet.row_values(18, -1)), str(sheet.row_values(21, -1)),
                   str(sheet.row_values(24, -1))],
                  [str(sheet.row_values(27, -1)), str(sheet.row_values(30, -1)), str(sheet.row_values(33, -1)),
                   str(sheet.row_values(36, -1))]
                  ]


    # Перенос данных со второй страницы
    sheet = raspbody.sheet_by_index(-2)
    nasherasp1.append([[str(sheet.row_values(3, 15)), str(sheet.row_values(6, 15)), str(sheet.row_values(9, 15)),
                        str(sheet.row_values(12, 15))],
                       [str(sheet.row_values(15, 15)), str(sheet.row_values(18, 15)), str(sheet.row_values(21, 15)),
                        str(sheet.row_values(24, 15))],
                       [str(sheet.row_values(27, 15)), str(sheet.row_values(30, 15)), str(sheet.row_values(33, 15)),
                        str(sheet.row_values(36, 15))]])





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
    for files in os.walk('../VkBot/ExcelStorage/'):
        for _file in files:
            allfiles = _file

    return (allfiles[-1])