import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        System.out.println("Matheus");
        Scanner scan = new Scanner(System.in);
        System.out.println("Informe dois numeros");
        double n1, n2;
        n1 = scan.nextDouble();
        n2 = scan.nextDouble();
        System.out.println("Saida:" + (n1+n2));
    }
}
