String figura = ""; //odczytanie jaka figure chcemy wyliczyc
String dlugoscBoku1 = ""; //zmienna dla dlugosci boku podana
int dlugoscBoku1INT = 0; //zmienan dla dlugosic boku INT
String dlugoscBoku2 = ""; //zmienna dla dlugosci boku podana
int dlugoscBoku2INT = 0; //zmienan dla dlugosic boku INT
String promien = ""; //zmienna dla promienia podana
int promienINT = 0; //zmienna dla promienia
String wysokosc = ""; //zmienan dla wysokosci podana
int wysokoscINT = 0; //zmienna dla wysokosci

void setup()
{
    Serial.begin(9600); //rozpoczecie komunikacji z pc

}

void loop()
{
    Serial.println("Pole jakiej figury checsz obliczyc? Prostokąt - p, Koło - k, Trójkąt - t");
    //zapytanie jaka figure chcemy obliczyc
    czekaj();

    if (Serial.available() > 0)
    { //jesli uzytkownik podal cos z klawiatury
        figura = Serial.readStringUntil('\n');
    }

    if (figura == "k")
    { //jesli wybieramy koło

        Serial.println("Podaj długość promienia."); //prosimy użytkownika o podanie długości promienia
        czekaj();

        if (Serial.available() > 0)
        { //odczytanie wartości podanej przez użytkownika
            promien = Serial.readStringUntil('\n');
            promienINT = promien.toInt();
        }

        double poleKolo = kolo(promienINT); //obliczenie pola za pomocą funkcji
        Serial.println("Pole twojego koła to: " + String(poleKolo) + " [mm^2]");

    } else if (figura == "p")
    { //jesli wybieramy prostokąt

        Serial.println("Podaj długość pierwszego boku."); //prosimy o podanie długości pierwszego boku
        czekaj();
        if (Serial.available() > 0)
        { //odczytanie wartości podanej przez użytkownika
            dlugoscBoku1 = Serial.readStringUntil('\n');
            dlugoscBoku1INT = dlugoscBoku1.toInt();
        }

        Serial.println("Podaj długość drugiego boku.");
        czekaj();
        if (Serial.available() > 0)
        { //odczytanie wartosci podanej przez użytkownika
            dlugoscBoku2 = Serial.readStringUntil('\n');
            dlugoscBoku2INT = dlugoscBoku2.toInt();
        }

        int poleProstokat = prostokat(dlugoscBoku1INT, dlugoscBoku2INT); //obliczenie pola za pomocą funkcji
        Serial.println("Pole twojego prostokąta to: " + String(poleProstokat) + " [mm^2]");

    } else if (figura == "t")
    { //jesli wybieramy trójkąt

        Serial.println("Podaj wysokość."); //prosimy użytkownika o podanie wysokości
        czekaj();

        if (Serial.available() > 0)
        { //odczytanie wartości podanej przez użytkownika
            wysokosc = Serial.readStringUntil('\n');
            wysokoscINT = wysokosc.toInt();
        }

        Serial.println("Podaj dlugość podstawy.");
        czekaj();

        if (Serial.available() > 0)
        { //odczytanie wartosci podanej przez użytkownika
            dlugoscBoku1 = Serial.readStringUntil('\n');
            dlugoscBoku1INT = dlugoscBoku1.toInt();
        }

        double poleTrojkat = trojkat(dlugoscBoku1INT, wysokoscINT); //obliczenie pola za pomoca funkcji
        Serial.println("Pole twojego trójkąta to: " + String(poleTrojkat) + " [mm^2]");

    } else
    {
        Serial.println("Podałeś zły argument!");
    }


}

int prostokat(int a, int b)
{ //funkcja odpowiedzialna za obliczanie pola kwardratu
    int poleProstokat = 0;
    poleProstokat = a * b;

    return poleProstokat;
}

double kolo(double r)
{ //funkcja odpowiedzialna za obliczanie pola kola
    double poleKolo = 0;
    poleKolo = 3.14 * r * r;

    return poleKolo;
}

double trojkat(double a, double h)
{ //funkcja odpowiedzialna za obliczanie pola trojkata
    double poleTrojkat = 0;
    poleTrojkat = 0.5 * a * h;

    return poleTrojkat;
}

void czekaj()
{
    while (Serial.available() == 0)
    {
        delay(50);
    }
}