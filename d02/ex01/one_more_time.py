#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import calendar
import re
import time


def ass_mo_num(month):
    if month == "janvier" or month == "Janvier":
        month = "January"
        return month
    elif month == "février" or month == "Février" or month == "fevrier" or month == "Fevrier":
        month = "February"
        return month
    elif month == "mars" or month == "Mars":
        month = "March"
        return month
    elif month == "avril" or month == "Avril":
        month = 'April'
        return month
    elif month == "mai" or month == "Mai":
        month = 'May'
        return month
    elif month == "juin" or month == "Juin":
        month = 'June'
        return month
    elif month == "juillet" or month == "Juillet":
        month = 'July'
        return month
    elif month == "août" or month == "Août" or month == "aout" or month == "Aout":
        month = 'August'
        return month
    elif month == "septembre" or month == "Septembre":
        month = 'September'
        return month
    elif month == "octobre" or month == "Octobre":
        month = 'October'
        return month
    elif month == "novembre" or month == "Novembre":
        month = 'November'
        return month
    elif month == "décembre" or month == "Décembre" or month == "decembre" or month == "Decembre":
        month = 'December'
        return month
    else:
        return -1

def ass_day_num(day):
    if day == "lundi" or day == "Lundi":
        day = 'Monday'
        return day
    if day == "mardi" or day == "Mardi":
        day = 'Tuesday'
        return day
    if day == "mercredi" or day == "Mercredi":
        day = 'Wendesday'
        return day
    if day == "jeudi" or day == "Jeudi":
        day = 'Thursday'
        return day
    if day == "vendredi" or day == "Vendredi":
        day = 'Friday'
        return day
    if day == "samedi" or day == "Samedi":
        day = 'Saturday'
        return day
    if day == "dimanche" or day == "Dimanche":
        day = 'Sunday'
        return day

def main():
    lc_days = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    up_days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "vendredi", "Samedi", "Dimanche"]
    lc_mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre",
               "décembre"]
    up_mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre",
               "Décembre"]
    lc_na_mois = ["janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre",
               "decembre"]
    up_na_mois = ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre",
               "Decembre"]
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            array = sys.argv[i].split(' ')
        if len(array) != 5:
            print "Wrong Format"
            exit()
        else:
            day = array[0]
            if day in lc_days or day in up_days:
                daynum = ass_day_num(day)
                day = daynum
            else:
                print ("Wrong Format")
                exit()
            date = array[1]
            if len(date) == 1 or len(date) == 2:
                if len(date) == 1:
                    date = '0' + date
                    print (date)
                try:
                    date = int(array[1])
                except (TypeError, ValueError, AttributeError):
                    print ('Wrong Format')
                    exit()
                date = str(date)
            else:
                print "Wrong Format"
                exit()

            month = array[2]
            if month in lc_mois or month in up_mois or month in lc_na_mois or month in up_na_mois:
                monum = ass_mo_num(month)
                month = monum
            else:
                print ("Wrong Format")
                exit()
            year = array[3]
            if len(year) == 4:
                try:
                    year = int(array[3])
                except (TypeError, ValueError, AttributeError):
                    print ("Wrong Format")
                    exit()
                year = str(year)
            else:
                print "Wrong Format"
                exit()
            timestamp = array[4]
            if len(timestamp) == 8:

                if re.match(r'([0-9][0-9]:[0-9]{2}:[0-9]{2})', timestamp):
                    hours = timestamp[0:2]
                    hourss = int(hours)
                    if hourss > 23:
                        print "Wrong Format"
                        exit()
                    minutes = timestamp[3:5]
                    minutess = int(minutes)
                    if minutess > 59:
                        print "Wrong Format"
                        exit()
                    seconds = timestamp[6:]
                    secondss = int(seconds)
                    if secondss > 59:
                        print "Wrong Format"
                        exit()
                else:
                    print "Wrong Format"
                    exit()
            else:
                print "Wrong Format"
                exit()
            items = [day, month, date, hours, minutes, seconds, year]
            stuff = ' '.join(items)
            times = time.strptime(stuff, "%A %B %d %H %M %S %Y")
            mktim = time.mktime(times)
            print mktim
    else:
        print ("\n"),



if __name__ == "__main__":
    main()