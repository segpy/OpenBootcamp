package Introduccion;
public class Main {
    public static void main(String[] args) {
        System.out.println("Primera parte: ");
        System.out.println(ejercicio1(5, 10, 15)+"\n");
    

        System.out.println("Segunda parte: ");
        Coche miCoche = new Coche(5);
        System.out.println("El coche tiene " + miCoche.getPuertas() + " puertas");
        miCoche.setPuertas(10);
        System.out.println("Ahora el coche tiene " + miCoche.getPuertas() + " puertas");
        System.out.println("Incrementando el numero de puertas...");
        miCoche.incrementarPuertas();
        System.out.println("El coche tiene " + miCoche.getPuertas() + " puertas");


    }

    public static int ejercicio1(int a, int b, int c){
        return a + b + c;
    }
}
