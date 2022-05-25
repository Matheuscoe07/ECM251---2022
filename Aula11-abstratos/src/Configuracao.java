//representacao de configuracao de sistema de desenvolvimento para depois ser enviada no deploit
//filhos de configuracao: desenvolvimento de deploit (ambos vao ser concretos)

public abstract class Configuracao { 
    public final String BANCO_DE_DADOS_URL; //http://www.google.com.br
    public final String APLICACAO_URL;
    public final boolean DEBUG;
    public final boolean LOG;
    
    //CONSTRUTOR
    public Configuracao(String bANCO_DE_DADOS_URL, String aPLICACAO_URL, boolean dEBUG, boolean lOG) {
        BANCO_DE_DADOS_URL = bANCO_DE_DADOS_URL;
        APLICACAO_URL = aPLICACAO_URL;
        DEBUG = dEBUG;
        LOG = lOG;
    }

    //quando os filhos herdares são eeles que fazem a execução dessas partes
    public abstract String getUser(); //não é definido aqui, a definição depende de outros fatores
    protected abstract boolean setUser(String user);

    //toString
    @Override
    public String toString() {
        return "Configuracao [APLICACAO_URL=" + APLICACAO_URL + ", BANCO_DE_DADOS_URL=" + BANCO_DE_DADOS_URL
                + ", DEBUG=" + DEBUG + ", LOG=" + LOG + "]";
    }
}
