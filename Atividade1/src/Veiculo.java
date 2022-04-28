//Matheus Coelho Rocha Pinto - 20.00391-9
import java.util.concurrent.ThreadLocalRandom;

public class Veiculo {
    //veículos: carro, moto, bicicleta e patinete
    protected int id;
    protected Double custo;
    protected String tipo;
    
    public Veiculo(Double custo, String tipo) {
        id = ThreadLocalRandom.current().nextInt(1000, 10000);
        this.custo = custo;
        this.tipo = tipo;
    }

    public int getId() {
        return id;
    }
    
    public Double getCusto() {
        return custo;
    }

    public void setCusto(Double custo) {
        this.custo = custo;
    }

    public String getTipo() {
        return tipo;
    }

    @Override
    public String toString() {
        return "Veiculo [custo=" + custo + ", id=" + id + ", tipo=" + tipo + "]";
    }

    public String testar(int id, double custo) {
        return String.format("O veículo de id %i tem custo %d", id, custo);
    }

}
