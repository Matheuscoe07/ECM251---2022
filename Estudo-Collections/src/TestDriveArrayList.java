import java.util.ArrayList;

public class TestDriveArrayList {
    public static void main(String[] args) {
    /*      
        //Cria um array de int
        int[] meuArray;
        //Instância o array
        meuArray = new int[4];
        //Colocando valores
        meuArray[0] = 45;
        meuArray[1] = 12;
        meuArray[2] = 9;
        meuArray[3] = 5;

        //Criando um erro
        //na verdade não é um erro de compilação e sim de execução 
        //o índice do array esta fora dos limites
        //meuArray[10] = -1; 
    */

            //Cria um ArrayList para as Canetas
        ArrayList<Caneta> canetas = new ArrayList<Caneta>();
        // ArrayList canetas = new ArrayList<Caneta>();
        //Adiciona uma caneta
        canetas.add(new Caneta("Azul", 0.7));
        canetas.add(new Caneta("Vermelha", 1.0));

        //Estudo do método size()
        System.out.println("Size agora: " + canetas.size());

        //Remove um objeto pelo indice
        // canetas.remove(0);

        //Estudo do método size()
        System.out.println("Size agora: " + canetas.size());

        //Passar pelos elementos
        //Método 1
        // System.out.println("Método 1: for do C");
        // for(int i = 0; i < canetas.size(); i++){
        //     //Chama o toString()
        //     // System.out.println("Cor da Caneta: "+canetas.get(i));
        //     System.out.println("Cor da Caneta: "+((Caneta)canetas.get(i)).cor);
        // }

        //Método 2
        for (Caneta caneta : canetas) {
            System.out.println("Cor da caneta: "+caneta.cor);
        }
    }
}

