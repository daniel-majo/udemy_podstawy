bool blokadastart=0; // blokada pierwszego if'a
int wybor=0; // deklarowanie wyboru obliczenia

int a=0; // pole prostokata
int b=0;

float aa=0; // pole trojkata zmienne
float h=0;

float r=0; // pole kola
float wynik=0;

void setup(){
  Serial.begin(9600);
}

void loop(){

  if (blokadastart==0){
  Serial.println("Wybierz ktore pole chcesz obliczyc");
  Serial.println("Pole kwadratu wcisnij   1");
  Serial.println("Pole prostokata wcisnij 2");
  Serial.println("Pole trojkata wcisnij   3");
  Serial.println("Pole kola wcisnij       4");

    blokadastart=1;
  }

  if (Serial.available()>0){
    String zmienna=Serial.readStringUntil('\n');
    wybor=zmienna.toInt();
  }


  switch(wybor){

    case 1: // pole kwadratu
    Serial.println("Wybrales pomiar pola kwadratu");
    Serial.println("Podaj wymiar boku a");
    while (Serial.available()==0){}
    if (Serial.available()>0){
      String dane=Serial.readStringUntil('\n');
      int a=dane.toInt();
      Serial.print("Podany wymiar: ");
        Serial.println(a);
      int wynik=polekwardaru(a);
        Serial.print("Pole powierzchni kwadratu wynosi: ");
        Serial.println(wynik);
    }
    blokadastart=0;
    wybor=0;
      break;

    case 2: //pole prostokata
    Serial.println("Wybrales pomiar pola prostokata");
    Serial.println("Podaj wymiar boku a");
    while (Serial.available()==0){}
    if (Serial.available()>0){
      String dane=Serial.readStringUntil('\n');
      a=dane.toInt();
      Serial.print("Podany wymiar boku a: ");
        Serial.println(a);
    }
      Serial.println("Teraz prosze podac wymiar boku b");
    while (Serial.available()==0){}
    if (Serial.available()>0){
      String dane=Serial.readStringUntil('\n');
      b=dane.toInt();
      Serial.print("Podany wymiar boku b: ");
        Serial.println(b);
      int wynik=prostokatpole(a,b);
        Serial.print("Pole powierzchni prostokatu wynosi: ");
        Serial.println(wynik);
    }
      blokadastart=0;
      wybor=0;
      break;

    case 3: //pole trojkata

    Serial.println("Podaj wymiar podstawy a");
    while (Serial.available()==0){}
    if (Serial.available()>0){
      String dane=Serial.readStringUntil('\n');
      aa=dane.toInt();
      Serial.print("Wartosc podstawy to: ");
      Serial.println(aa);
    }
          Serial.println("Podaj wysokosc trojkata");
          while (Serial.available()==0){}
          if (Serial.available()>0){
          String dane=Serial.readStringUntil('\n');
          h=dane.toInt();
          Serial.print("Wartosc wysokosci to: ");
          Serial.println(h);
        }
        wynik=poletrojkata(aa,h);
        Serial.print("Pole powierzchni prostokata wynosi: ");
        Serial.println(wynik);
        blokadastart=0;
        wybor=0;
        break;

    case 4: //pole kola

    Serial.println("Wybrales pomiar powierzchni kola");
    Serial.println("Podaj wartosc promienia kola");
    while(Serial.available()==0){}
    if (Serial.available()>0){
      String dane=Serial.readStringUntil('\n');
      r=dane.toInt();
      float wynik=polekola(r);
      Serial.print("pole kola: ");
      Serial.println(wynik);
    }
       blokadastart=0;
       wybor=0;
    break;

    }  // zakonczenie funkcji switch case
} // zakonczenie void loop


// funkcje


int polekwardaru (int a){
  int wynik=a*a;
  return wynik;
}

int prostokatpole (int a, int b){  //funkcja na pole pow. prostokatu
  int wynik=a*b;  //zmienna lokalna wynik
    return wynik;  // wynik dzialania ktore pokaze zmienna int wynik
}

float poletrojkata (float a, float h){ //funkcja na pole trojkata
  float wynik=0.5*(a*h); //zmienna lokalna wynik
    return wynik; // wynik dzialania pole trojkata
}

float polekola (float r){ //funkcja na pole kola
  float wynik=PI*(r*r); //zmienna lokalna wynik
    return wynik; // wynik dzialania pole kola
}