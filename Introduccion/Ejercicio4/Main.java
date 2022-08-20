package Ejercicio4;
//importar scanner
import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Primera parte: ");
        System.out.println("Intoduzca el numerolf: ");
        int numero = sc.nextInt();
        if(numero > 0){
            System.out.println("El numero es positivo");
        }else if(numero < 0){
            System.out.println("El numero es negativo");
        }else{
            System.out.println("El numero es 0");
        }

        System.out.println("Segunda parte: ");
        int numeroWhile = 0;
        while(numeroWhile < 3){
            System.out.println(numeroWhile);
            numeroWhile++;
        }

        System.out.println("Tercera parte: ");
        do {
            System.out.println(numeroWhile);
            numeroWhile++;
        } while (numeroWhile < 3);

        System.out.println("Cuarta parte: ");
        for (int i = 0; i <= 3; i++) {
            System.out.println(i);
        }
        sc.nextLine();
        System.out.println("Quinta parte: ");
        //usar scanner para introducir datos con el mensaje
        System.out.println("Introduzca la estacion: ");
        String estacion = sc.nextLine();
        switch(estacion){
            case "verano":
                System.out.println("La estacion es verano");
                break;
            case "invierno":
                System.out.println("La estacion es invierno");
                break;
            case "primavera":
                System.out.println("La estacion es primavera");
                break;
            case "otonio":
                System.out.println("La estacion es otonio");
                break;
            default:
                System.out.println("Estacion no valida");
                break;
        }
        sc.close();
    }
}
