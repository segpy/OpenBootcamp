package Ejercicio9;

public class Main {
    public static void main(String[] args) {
        System.out.println("Primera parte ");
        System.out.println("Creacion del objeto Cliente");
        Persona cliente = new Cliente("Juan", 23, 123456789, 1000);
        System.out.printf("Nombre : %s\n", cliente.getNombre());
        System.out.printf("Edad : %d\n", cliente.getEdad());
        System.out.printf("Telefono : %d\n", cliente.getTelefono());
        System.out.printf("Credito : %d\n", ((Cliente)cliente).getCredito()); //(Cliente)cliente es un casting de cliente a Cliente



        System.out.println("\nSegunda parte ");
        System.out.println("Creacion del objeto Trabajador");
        Persona trabajador = new Trabajador("Carlos", 20, 311000, 2000);
        System.out.printf("Nombre : %s\n", trabajador.getNombre());
        System.out.printf("Edad : %d\n", trabajador.getEdad());
        System.out.printf("Telefono : %d\n", trabajador.getTelefono());
        System.out.printf("Salario : %d\n", ((Trabajador)trabajador).getSalario()); //(Trabajador)trabajador es un casting de trabajador a cliente


    }
}

class Persona{
    private String nombre;
    private int edad;
    private int telefono;

    public Persona(String nombre, int edad, int telefono) {
        this.nombre = nombre;
        this.edad = edad;
        this.telefono = telefono;
    }

    //Getters y setters
    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public int getEdad() {
        return edad;
    }
    public void setEdad(int edad) {
        this.edad = edad;
    }
    public int getTelefono() {
        return telefono;
    }
    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }

    
}

class Cliente extends Persona{
    private int credito;

    public Cliente(String nombre, int edad, int telefono, int credito) {
        super(nombre, edad, telefono);
        this.credito = credito;
    }

    public int getCredito() {
        return credito;
    }
    public void setCredito(int credito) {
        this.credito = credito;
    }
}

class Trabajador extends Persona{
    private int salario;

    public Trabajador(String nombre, int edad, int telefono, int salario) {
        super(nombre, edad, telefono);
        this.salario = salario;
    }

    public int getSalario() {
        return salario;
    }
    public void setSalario(int salario) {
        this.salario = salario;
    }
}
