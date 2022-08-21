package Test;

public class Main {
    public static void main(String[] args) {
        Animales perro = new Perro("Firulais", 6, "labrador");






    }
}

class Animales{
    private String nombre;
    private int edad;
    
    public Animales(String nombre, int edad){
        this.nombre = nombre;
        this.edad = edad;
    }

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

}

class Perro extends Animales{
    private String raza;

    public Perro(String nombre, int edad, String raza){
        super(nombre, edad);
        this.raza = raza;
    }

    public void ladrar(){
        System.out.println("Guau Guau");
    }
}
