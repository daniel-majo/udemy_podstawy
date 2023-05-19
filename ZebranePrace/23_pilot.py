'''Pilot przed wystartowaniem powinien sprawdzić listę kontrolną.
Właśnie piszesz kod, który odpowiada za wyświetlenie napisu
"CHECK IS COMPLETED" jeżeli lista kontrolna została już pomyślnie wykonana
i zamknięta, w przeciwnym razie powinien być wyświetlany komunikat
"CHECK NOT DONE YET!". Zmienna True/False, która zawiera informację o tym
czy lista kontrolna została już wykonana nazywa sie isCheckCompleted.
Korzystając z ternary operator przygotuj polecenie if wyświetlające odpowiedni
komunikat'''

isCheckCompleted=False

print ("CHECK IS COMPLETED" if isCheckCompleted else "CHECK NOT DONE YET!")
