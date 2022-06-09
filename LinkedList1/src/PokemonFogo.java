public class PokemonFogo extends Pokemon { // filho de pokemon

    public PokemonFogo(int numero, String nome, Status status) {
        super(numero, nome, status);
    } 
    
    @Override
    public boolean evoluir(Status status) {
        return false;
    }
}
