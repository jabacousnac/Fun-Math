import numpy as np

#doomsday rule by Conway finds the day of a particular date, according to Gregorian Calendar
def find_day(date): #date follows format [month, day, year]
    month = date[0]
    day = date[1]
    year = date[2]
    anchor = find_anchor(year)
    days_list = ['W', 'R', 'F', 'S', 'D', 'M', 'T']
    #the doomsdays are:
    #1) Jan 3 in common years (3 years), Jan 4th in leap years (the 4th year)
    #2) last day of February
    #3-7) April 4th, June 6th, August 8th, October 10th, December 12th (4/4, 6/6, 8/8, 10/10, 12/12)
    #8-11) May 9th, 5th September, 7th November, 11th July  (9 to 5 at 7-11)
#**********#
    #IMPORTANT NOTE:
    #for simplicity, in the code the difference can be found between one of the
        #doomsdays. In real life calculation, you'd want to figure out which doomsday is closest
        #e.g. here, 4th April was used
    dif = my_day(date)-my_day([4,4,year])
    swing = dif%7
    final_index = anchor + swing
    if anchor+swing > 7:
        final_index = anchor+swing-7
    return days_list[final_index]


def my_day(date):
    #find the number of days that have elapsed since the start of the year
    month = date[0]
    day = date[1]
    year = date[2]
    ndays = 0
    counter = 1
    if year%4 == 0:
        month_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while counter != month:
        ndays += month_list[counter-1]
        #print(ndays)
        counter+=1
        #print(counter)
    ndays += day
    return ndays

def find_anchor(year):
#rules for anchor day:
#1) anchor days slip one column for every leap year. E.g if for 2007 it was a Wednesday,
    # skip one day for 2008. Anchor day is then a Friday.
#2) cycle has a period of 28 days
#3) rule number 2 is violated for years that are multiples of 100, but not of 400.
    #start with the first reference: 1900 is a Wednesday.
    #for positive year (i.e. after 1900)
    dy = year - 1900
    if year % 100 == 0 and year % 400 != 0: #dealing with an exception to rule#2
        #no gap preceding exceptions
        dy -= 1 #go a year before because that for sure is not an exception
        gaps = int(abs(dy)/4) #number of gaps
        nogaps = dy%7
        index = (gaps + nogaps)%7 + 1
        if index == 7:
            index = 0
    else:
        gaps = int(abs(dy)/4)
        nogaps = dy%7
        index = (gaps + nogaps)%7
    return index






