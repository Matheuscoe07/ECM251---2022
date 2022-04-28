public class Conta {
    private int idConta;
    private double saldo;
    private static int totalContas = 0;
    public Conta() {
        this.saldo = 0; //devemos evitar dois estilos em um mesmo código, se um tem this. todos devem ter o this.
        this.idConta = totalContas; //o totalcontas nao tem this. e se ele for referenciado dps em outro lugar tem que ser Conta.totalcontas
        totalContas++;
    }

    public boolean depositar(double valor){
        this.saldo += valor;
        return true;
    }

    public boolean sacar(double valor){
        if(valor > this.saldo)
            return false;
        this.saldo -= valor;
        return true;
    }

    public boolean transferir(double valor, Conta destino){
        if(!sacar(valor))
            return false;
        return destino.depositar(valor);
    }

    @Override
    public String toString() {
        return "Conta [idConta=" + idConta + ", saldo=" + saldo + "]";
    }
}
