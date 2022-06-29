import java.util.LinkedList;

public class Sistema {
    
    public static void run() {
        LinkedList<Membro> staff = new LinkedList<Membro>();

        staff.add(new MobileMembers("Asami", "Asami@IndustriasSato.com" , Funcao.MOBILE_MEMBERS));
        staff.add(new HeavyLifters("Entrapta", "Entrapta@s2Hordak.com", Funcao.HEAVY_LIFTERS));
        staff.add(new ScriptGuys("Sasha", "SashaBraus@MorreuInjustamente.com", Funcao.SCRIPT_GUYS));
        staff.add(new BigBrothers("Korra", "Korra@MaiorAvatarVivo.com", Funcao.BIG_BROTHERS));
        staff.add(new HeavyLifters("Dexter", "Dexter@Lab.com", Funcao.HEAVY_LIFTERS));
        staff.add(new MobileMembers("Tenten", "Tenten@MereciaHolofote.com", Funcao.MOBILE_MEMBERS));
        staff.add(new ScriptGuys("Zatanna", "Zatanna@Zutara.com", Funcao.SCRIPT_GUYS));
    
        System.out.println(staff);

        postarMensagens(staff);
        mudarTurno(staff, Turno.EXTRA);
        postarMensagens(staff);
        
        staff.remove(1);
        staff.remove(2);

        System.out.println(staff);
    }

    public static void postarMensagens(LinkedList<Membro> staff) {
        for (Membro m : staff) {
            System.out.println("\n Membro: " + m.getNome() + "\n Mensagem: " + m.postarMensagem() + "\n");
        }
    }

    public static void mudarTurno(LinkedList<Membro> staff, Turno turno){
        for (Membro m : staff) {
            m.setTurno(turno);
        }
    }
}


