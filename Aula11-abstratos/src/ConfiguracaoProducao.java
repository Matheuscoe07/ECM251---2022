public class ConfiguracaoProducao extends Configuracao {

    private String currentUser;

    public ConfiguracaoProducao(String bANCO_DE_DADOS_URL, String aPLICACAO_URL, String user) {
        super(bANCO_DE_DADOS_URL, aPLICACAO_URL, false, true);
        //TODO Auto-generated constructor stub
        setUser(user);
    }

    @Override
    public String getUser() {
        // TODO Auto-generated method stub
        return currentUser;
    }

    @Override
    protected boolean setUser(String user) {
        // TODO Auto-generated method stub
        if(user.isEmpty())
            return false;
        this.currentUser = user;
        return true;
    }
    
}
