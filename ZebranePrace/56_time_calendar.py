'''1. Zaimportuj modul time

2. Wyświetl czas (datę i godzinę) w postaci Unix Epoche
(skorzystaj z metody time)

3. Wyświetl czas (datę i godzinę) w postaci czytelnej dla człowieka.
W tym celu złóż metodę localtime z metodą time

4. Zaimportuj moduł calendar

5. Każdy z nas ma swoje ważne daty: datę urodzenia swoją,
dziewczyny/chłopaka, dziecka, data przyjęcia do pierwszej pracy,
data zakończenia podstawówki itp. Wyświetl miesiąc zawierający tą datę

6. Zmień sposób wyświetlenia daty tak, aby niedziela była
pierwszym dniem tygodnia

7. Wyświetl miesiąc z ważną dla Ciebie datą ponownie

8. Sprawdź czy rok 2000 był przestępny

9. Wyświetl kalendarz za rok 2019 i zobacz czy układ
świąt Bożego Narodzenia wygląda atrakcyjnie czy nie'''

import time

print(time.time())
print (time.localtime(time.time()))
print ('-------------\n')
import calendar
print ('Moje urodziny\n',calendar.month(1979,2))
print ('Eli urodziny\n',calendar.month(1980,3))
print ('Zuzi urodziny\n',calendar.month(2005,9))
print ('Lidii urodziny\n',calendar.month(2011,1))
print ('Poli urodziny\n',calendar.month(2018,8))

calendar.setfirstweekday(6)
print ('Moje urodziny\n',calendar.month(1979,2))
print ('Eli urodziny\n',calendar.month(1980,3))
print ('Zuzi urodziny\n',calendar.month(2005,9))
print ('Lidii urodziny\n',calendar.month(2011,1))
print ('Poli urodziny\n',calendar.month(2018,8))

print (calendar.isleap(2000))
print (calendar.calendar(2019))
