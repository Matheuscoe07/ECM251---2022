public class TestDriveArray {
    public static void main(String[] args) {
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
    }
}
