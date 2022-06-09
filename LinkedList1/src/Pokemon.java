public abstract class Pokemon {
    private final int numero;
    private final String nome;
    private final Status status;
    
    public Pokemon(int numero, String nome, Status status) {
        this.numero = numero;
        this.nome = nome;
        this.status = status;
    }

    public int getNumero() {
        return numero;
    }

    public String getNome() {
        return nome;
    }

    @Override
    public String toString() {
        return "Pokemon [nome=" + nome + ", numero=" + numero + ", status=" + status + "]";
    }
}
