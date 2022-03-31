public class Atividade1 {
    public void run() {
        Usuario usuario1 = new Usuario("Rengoku", "1234", "naoera_minhahora@gmail.com");
        Conta conta1 = new Conta(1234, usuario1);
        System.out.println(conta1);
        
        Usuario usuario2 = new Usuario("Uzui", "5678", "amo.as3@gmail.com");
        Conta conta2 = new Conta(5678, usuario2);
        System.out.println(conta2);

        Usuario usuario3 = new Usuario("Tomioka", "2468", "agua@gmail.com");
        Conta conta3 = new Conta(2468, usuario3);
        System.out.println(conta3);

        //criando QRcode
        Transacao transacao = new Transacao();
    }
}
