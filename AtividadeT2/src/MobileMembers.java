public class MobileMembers extends Membro {

    public MobileMembers(String nome, String email, Funcao funcao) {
        super(nome, email, funcao);
        //TODO Auto-generated constructor stub
    }

    @Override
    public String toString() {
        return "MobileMembers []";
    }
    
    @Override
    public String postarMensagem() {
        if (super.getTurno() == Turno.REGULAR)
            return "Happy Coding!";
        else
            return "Happy_C0d1ng. Maskers";
    }
}
