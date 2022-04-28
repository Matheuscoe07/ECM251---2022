//Matheus Coelho Rocha Pinto - 20.00391-9

public class Sistema {
    public static void run() {
        Usuario usuario1 = new Usuario("Murilo", "Carro");
        Veiculo carro = new Carro(10.0, "Carro");
        Veiculo bicicleta = new Bicicleta(15.0, "Bicicleta");
        Veiculo Moto = new Moto(20.0, "Moto");
        Veiculo patinete = new Patinete(10.0, "Patinete");

        usuario1.setVeiculoAtual("Carro").troca("Bicicleta");

        System.out.println("Troca 1:" + usuario1.getVeiculoAtual());
    }
}
