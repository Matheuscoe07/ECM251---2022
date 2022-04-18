import java.util.List;
import java.util.ArrayList;


public class ValidadorCPF {
    private static List<String> cpfInvalido = new ArrayList<String>(){
    {add("11111111111"); add("22222222222"); add("33333333333");
    add("44444444444"); add("55555555555"); add("66666666666"); 
    add("77777777777"); add("88888888888"); add("99999999999"); 
    add("00000000000");}};

    public static boolean validar(String cpf) {
        if (cpfInvalido.contains(cpf)){
            return false;
        }     

    // public static boolean validar(String cpf){
    //     if(cpf.equals("11111111111") || 
    //        cpf.equals("22222222222") ||
    //        cpf.equals("33333333333") ||
    //        cpf.equals("44444444444") ||
    //        cpf.equals("55555555555") ||
    //        cpf.equals("66666666666") ||
    //        cpf.equals("77777777777") ||
    //        cpf.equals("88888888888") ||
    //        cpf.equals("99999999999") ||
    //        cpf.equals("00000000000")  ){
    //         return false;
    //        }
           
        
        int soma = Integer.parseInt("" + cpf.charAt(0)) * 10;
        for(int i = 1; i < 9; i++)
            soma += Integer.parseInt("" + cpf.charAt(i)) * 10 - i;

        // soma += Integer.parseInt("" + cpf.charAt(1)) * 9;
        // soma += Integer.parseInt("" + cpf.charAt(2)) * 8;
        // soma += Integer.parseInt("" + cpf.charAt(3)) * 7;
        // soma += Integer.parseInt("" + cpf.charAt(4)) * 6;
        // soma += Integer.parseInt("" + cpf.charAt(5)) * 5;
        // soma += Integer.parseInt("" + cpf.charAt(6)) * 4;
        // soma += Integer.parseInt("" + cpf.charAt(7)) * 3;
        // soma += Integer.parseInt("" + cpf.charAt(8)) * 2;
        soma = (soma * 10) % 11;
        if(soma != Integer.parseInt("" + cpf.charAt(9))){
            return false;
        }

        soma = Integer.parseInt("" + cpf.charAt(0)) * 11;
        for (int i = 1; i < 10; i++)
            soma += Integer.parseInt("" + cpf.charAt(i)) * 11 - i;

        // soma += Integer.parseInt("" + cpf.charAt(1)) * 10;
        // soma += Integer.parseInt("" + cpf.charAt(2)) * 9;
        // soma += Integer.parseInt("" + cpf.charAt(3)) * 8;
        // soma += Integer.parseInt("" + cpf.charAt(4)) * 7;
        // soma += Integer.parseInt("" + cpf.charAt(5)) * 6;
        // soma += Integer.parseInt("" + cpf.charAt(6)) * 5;
        // soma += Integer.parseInt("" + cpf.charAt(7)) * 4;
        // soma += Integer.parseInt("" + cpf.charAt(8)) * 3;
        // soma += Integer.parseInt("" + cpf.charAt(9)) * 2;
        soma = (soma * 10) % 11;
        if (soma != Integer.parseInt("" + cpf.charAt(10))) {
            return false;
        }

        return true;
    }
}
