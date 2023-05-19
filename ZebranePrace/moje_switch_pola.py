//czy wprowadzon dane
bool stan = false;
//deklaracja wyboru figury
String figura = "";
// zapisanie w zmiennej wybor naszej decyzji
int wybor = 0;

// zmienne do przechowywania wartości wprowadzonych przez UART
String a = "";
String b = "";
String h = "";
String r = "";
//wartość wyliczona dla dowolnego pola
int pole = 0;

// definicje dla wyznaczenia wartości pól
//wybor == 1
int kwadrat(int a){
  int pole = a*a;
  return pole;
}
//wybor == 2
int prostokat (int a, int b){
  int pole = a * b;
  return pole;
}
//wybor == 3
int trojkat (int a, int h){
  int pole = (a * h )/2;
  return pole;
}
//wybor ==4
int kolo (int r){
  int pole = 3.14 * r * r;
  return pole;
}

void czekaj(){
  while (Serial.available()<=0)
  {}
}

void setup (){
  Serial.begin(9600);

}// zakończenie setup()

void loop(){

  Serial.println("Wpisz pole jakiej figury chcesz wyznaczyć...");
  Serial.println("1-kwadrat \t 2-prostokąt \t 3-trójkąt \t 4-koło");
  czekaj();
  if (Serial.available()>0){
  figura = Serial.readStringUntil('\n');
  wybor = figura.toInt();

  switch(wybor){
    case 1: //kwadrat
    Serial.println("Podaj długość boku a kwadratu");
    czekaj();
      if (Serial.available()>0){
        a = Serial.readStringUntil('\n');
        int pole = kwadrat(a.toInt());
      Serial.print("Pole kwadratu wynosi: ");
      Serial.println(pole);
      } //zakończenie if`a kwadratu
      break;
    case 2: //prostokat
    Serial.println("Podaj długość boku a prostokąta");
    czekaj();
      if (Serial.available()>0){
        a = Serial.readStringUntil('\n');
      }//zakończenie if`a prostokata a
      Serial.println("Podaj długość boku b prostokąta");
      czekaj();
       if (Serial.available()>0){
        b = Serial.readStringUntil('\n');
      }//zakończenie if`a prostokata b
      int pole = prostokat(a.toInt(), b.toInt());
      Serial.print("Pole prostokąta wynosi: ");
      Serial.println(pole);
      break;
    case 3: //trojkat
    Serial.println("Podaj długość podsawy a trójkąta");
    czekaj();
      if (Serial.available()>0){
        a = Serial.readStringUntil('\n');
        }//zakończenie if`a trójkąta podstawy a
      Serial.println("Podaj wysokość h trójkąta");
      czekaj();
        if (Serial.available()>0){
        h = Serial.readStringUntil('\n');
      }//zakończenie if`a wysokości h trójkąta
      pole = trojkat(a.toInt(), h.toInt());
      Serial.print("Pole trójkąta wynosi: ");
      Serial.println(pole);
      break;
    case 4: //koło
    Serial.println("Podaj promień koła r");
    czekaj();
      if (Serial.available()>0){
      r = Serial.readStringUntil('\n');
    //}//zakończenie ifa promienia koła r
    pole = kolo (r.toInt());
    Serial.print("Pole koła wynosi: ");
    Serial.println(pole);
    }//zakończenie ifa promienia koła r
    } //zakończenie switch

    } // zakończenie 1-go ifa wyboru
  }//zakończenie loop