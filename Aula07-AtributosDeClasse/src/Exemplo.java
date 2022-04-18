public class Exemplo {
    private String texto;
    private double valor;
    private static int contador;
    
    public Exemplo(String texto, double valor) {//construtor
        this.texto = texto;
        this.valor = valor;
        contador += 1; //cada vez que cria o contador ele sobe 1
    }

    public String toString() {//devolve como texto
        return "{texto:" + this.texto + "\nvalor:" + this.valor + "\ncontador:" + contador + "}";
    }

    //método de classe
    public static int getContador(){
        return contador;
    }
}
