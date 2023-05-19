'''Twój zespół opracowuje przeglądarkę internetową w Pythonie!
Twoim zadaniem jest sprawdzenie, czy operacja pobierania pliku na dysk
ma się szansę udać, czy jest od razy skazana na porażkę ze względu
na brak miejsca na dysku. Na wejściu masz następujące zmienne:'''

diskSize = 140          # oznaczająca wielkość dysku w GB
diskSizeUsed = 133      # oznaczająca ilosć zajętego miejsca na dysku w GB
fileSize = 8           # oznaczająca wielkość pobieranego pliku w GB

if diskSize-diskSizeUsed>=fileSize:
    print ("File can be downloaded")
else:
    print ("There isn\'t enough free disk space to download the file. Sorry :(")
