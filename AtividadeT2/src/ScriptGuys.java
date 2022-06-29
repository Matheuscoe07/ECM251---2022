public class ScriptGuys extends Membro {

    public ScriptGuys(String nome, String email, Funcao funcao) {
        super(nome, email, funcao);
        //TODO Auto-generated constructor stub
    }

    @Override
    public String toString() {
        return "ScriptGuys []";
    }
    
    @Override
    public String postarMensagem() {
        if (super.getTurno() == Turno.REGULAR)
            return "Prazer em ajudar novos amigos de código!";
        else
            return "QU3Ro_S3us_r3curs0s.py";
    }
}
