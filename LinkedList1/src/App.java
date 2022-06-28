import java.util.List;
import java.util.ArrayList;

public class App {
    public static void main(String[] args) throws Exception {
        List<Pokemon> pokemons = new ArrayList<Pokemon>();
        pokemons.add(new PokemonGrama(1, "Bulbasauro", new Status(10,10,10,10)));
        pokemons.add(new PokemonFogo(4, "Charmander", new Status(10, 10, 10, 10)));
        pokemons.add(new PokemonAgua(7, "Squirtle", new Status(10, 10, 10, 10)));
        mostraPokemons(pokemons);
        evoluirTodos(pokemons, new Status(1, 1, 1, 1));
        mostraPokemons(pokemons);
    }

    public static void mostraPokemons(List<Pokemon> pokemons) {
        for(Pokemon pokemon : pokemons) {
            System.out.println(pokemon);
        }
    }

    public static void evoluirTodos(List<Pokemon> pokemons, Status status) {
        for (Pokemon pokemon : pokemons) {
            pokemon.evoluir(status);
        }
    }
}
