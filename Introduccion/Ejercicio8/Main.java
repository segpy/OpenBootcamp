package Ejercicio8;

public class Main {
    public static void main(String[] args) {
        Persona persona = new Persona();
        persona.setNombre("Juan");
        persona.setEdad(23);
        persona.setTelefono(123456789);
        System.out.printf("Nombre : %s\n", persona.getNombre());
        System.out.printf("Edad : %d\n", persona.getEdad());
        System.out.printf("Telefono : %d\n", persona.getTelefono());
    }
}
