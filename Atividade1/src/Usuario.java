//Matheus Coelho Rocha Pinto - 20.00391-9

public class Usuario {
    //possui um 
    // utiliza apenas um veículo
    private String nome;
    private String veiculoAtual;
    
    public Usuario(String nome, String veiculoAtual) {
        this.nome = nome;
        this.veiculoAtual = veiculoAtual;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getVeiculoAtual() {
        return veiculoAtual;
    }

    public void setVeiculoAtual(String veiculoAtual) {
        this.veiculoAtual = veiculoAtual;
    }

    public boolean troca(String coisa) {
        this.veiculoAtual = coisa;
        return true;
    }

    
}
