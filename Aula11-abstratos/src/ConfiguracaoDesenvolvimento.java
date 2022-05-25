public class ConfiguracaoDesenvolvimento extends Configuracao {

    private String user;

    public ConfiguracaoDesenvolvimento(String bANCO_DE_DADOS_URL, String aPLICACAO_URL) {
        super(bANCO_DE_DADOS_URL, aPLICACAO_URL, true, true);
        //TODO Auto-generated constructor stub
        setUser("localhost");
    }

    @Override
    public String getUser() {
        // TODO Auto-generated method stub
        return this.user;
    }

    @Override
    protected boolean setUser(String user) {
        // TODO Auto-generated method stub
        if(user.isEmpty())
            return false;
        this.user = user;
        return true;
    }
    
}
