public class BigBrothers extends Membro {

    public BigBrothers(String nome, String email, Funcao funcao) {
        super(nome, email, funcao);
        // TODO Auto-generated constructor stub
    }

    @Override
    public String toString() {
        return "BigBrothers []";
    }
    
    @Override
    public String postarMensagem() {
        if (super.getTurno() == Turno.REGULAR)
            return "Sempre ajudando as pessoas membros ou não S2!";
        else
            return "...";
    }
}
