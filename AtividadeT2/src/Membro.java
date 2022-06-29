public abstract class Membro implements IPostarMensagem {
    private String nome;
    private String email;
    private Funcao funcao; //NÃO ESQUECER DE IMPLEMENTAR A FUNCAO.JAVA
    private Turno turno; //NÃO ESQUECER DE IMPLEMENTAR A TURNO.JAVA
    
    public Membro(String nome, String email, Funcao funcao) {
        this.nome = nome;
        this.email = email;
        this.funcao = funcao;
        this.turno = turno.REGULAR;
    }

    public String getNome() {
        return nome;
    }

    public String getEmail() {
        return email;
    }

    public Funcao getFuncao() {
        return funcao;
    }

    public Turno getTurno() {
        return turno;
    }

    public void setTurno(Turno turno) {
        this.turno = turno;
    }

    
}
