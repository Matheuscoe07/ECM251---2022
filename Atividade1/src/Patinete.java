//Matheus Coelho Rocha Pinto - 20.00391-9

public class Patinete extends Veiculo {
    public Patinete(Double custo, String tipo) {
        super(custo, tipo);
    }

    @Override
    public String testar(int id, double custo){
        return String.format("O veículo de id %i tem custo %d", id, custo);
    }
}
