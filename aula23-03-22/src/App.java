import java.util.IdentityHashMap;

public class App {
    public static void main(String[] args) throws Exception {
        ////Conta c1= new Conta();
        //c1.saldo = 250; //NÃO PODE pois vai estar passadno por cima do depositar
        //c1.saldo += 200; //De novo não pode pq vai estar acessando diretamente essa seção
        ////if(c1.sacar(200)) {
            ////System.out.println("Você sacou 200!"); //Não funciona se não tiver dinheiro na conta
        ////}

        //Para resolver esse problema do acesso deireto utilizamos os modificadores de acesso
        //a ideia é controlar como os elementos vão ser acessados
        //modificadores de acesso: public (todo mundo acessa), private (só os membros da classe acessam ele), protected (a familia de herança pode alterar ele), padrão (semelhante ao público)
        //modificadores de acesso utilizados na "Conta.java"
        //quem quiser acessar esse campo de forma indiscriminada recebe um erro no terminal
        //agora sim TEMOS QUE passar pelo depositar
        ////c1.depositar(200);
        ////c1.visualizarSaldo();
        //o recomendado é liberar acesso apenas quando necessário

        //--------ENCAPSULAMENTO--------
        //cria-se uma interface do objeto e por meio dela conversa-se com o objeto
        //encapsular é fornecer uma interface para acessar oq for preciso e ocultar e proteger os detalhers de implementação
        //"programe voltado para a interface e não para a implementação"

        ////Cliente c1 = new Cliente();
        ////c1.nome = "Matheus Coelho"; //isso não vai dar certo pq nome é privado
        //pra poder acionar o nome criou-se o método publico para acessar o nome
        Cliente c1 = new Cliente("Matheus", "123456789", "aaaaaaa@aaaaa.com", new Conta(1234));
        
        //Não são mais necessarias por causa da nova seção public Cliente()
        //c1.setNome("Matheus");
        //c1.setCpf("123456789");
        //c1.setEmail("coelho284@gmail.com");
        //c1.setConta(new Conta());
        
        System.out.println("Nome do cliente:" + c1.getNome());
        System.out.println("E-mail do cliente:" + c1.getEmail());
        System.out.println("CPF do cliente:" + c1.getCpf());
        System.out.println("Conta do cliente:" + c1.getConta());
        c1.getConta().visualizarSaldo();

        //----------CONSTRUTORES----------
        //inicializam os dados de forma organizada, são criados com o que é necessário
    }
}
