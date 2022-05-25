public class App {
    public static void main(String[] args) throws Exception {
    //cria duas referencias para oobjetos do tipo configuracao
    Configuracao c1;
    Configuracao c2;
    //cria as instancias
    c1 = new ConfiguracaoDesenvolvimento("localhost", "localhost:5000");
    c2 = new ConfiguracaoProducao("https://bancodedados.com", "https://maua.br", "Jorge");
    System.out.println("Conf1:" + c1);
    System.out.println("Conf2:" + c2);
    }
}
