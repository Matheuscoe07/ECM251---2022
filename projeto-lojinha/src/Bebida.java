public class Bebida extends Produto {
    private final int volume;
    private final EnumTemperaturas temperatura;
    private final EnumAlergias alergias;
    private final EnumTiposBebida tipo;
    
    public Bebida(int volume, EnumTemperaturas temperatura, EnumAlergias alergias, EnumTiposBebida tipo) {
        this.volume = volume;
        this.temperatura = temperatura;
        this.alergias = alergias;
        this.tipo = tipo;
    }

    public int getVolume() {
        return volume;
    }

    public EnumTemperaturas getTemperatura() {
        return temperatura;
    }

    public EnumAlergias getAlergias() {
        return alergias;
    }

    public EnumTiposBebida getTipo() {
        return tipo;
    }
}
