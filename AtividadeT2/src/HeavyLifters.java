public class HeavyLifters extends Membro {

    public HeavyLifters(String nome, String email, Funcao funcao) {
        super(nome, email, funcao);
        //TODO Auto-generated constructor stub
    }

    @Override
    public String toString() {
        return "HeavyLifters []";
    }
    
    @Override
    public String postarMensagem() {
        if (super.getTurno() == Turno.REGULAR)
            return "Podem contar conosco!";
        else
            return "N00b_qu3_n_Se_r3pita.bat";
    }
}
