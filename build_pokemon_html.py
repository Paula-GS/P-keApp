from string import Template
import damage as d
import informacion_condensada as ic
import traducciones

with open('base.html', 'r', encoding = 'utf-8') as index:
    html = index.read()

document_template = Template(html)

def crea_pokedex(nombre):
    data_base = ic.Nombre(nombre)
    data_species = ic.Species(ic.id_n(data_base))
    biblio_tipos = d.Damage(data_base)
    document_template_nuevo = document_template.substitute(
        nombre = ic.name(data_base).capitalize(),
        id_n = ic.id_n(data_base),
        img_url = ic.img_url(data_base),
        pok_hp = ic.hp(data_base),
        ataque = ic.ataque(data_base),
        defensa = ic.defensa(data_base),
        sp_ataque = ic.sp_ataque(data_base),
        sp_defensa = ic.sp_defensa(data_base),
        velocidad = ic.velocidad(data_base),
        peso = ic.peso(data_base),
        talla = ic.talla(data_base),
        etapa_previa = ic.etapa_previa(data_species),
        p_comentario = ic.comentarios(data_species),
        baby = ic.baby(data_species),
        legendary = ic.legendary(data_species),
        mythical = ic.mythical(data_species),
        span_tipo = traducciones.span_tipo(data_base),
        span_efectivo = traducciones.span_efectivo(biblio_tipos),
        span_debil = traducciones.span_debil(biblio_tipos),
        span_resistente = traducciones.span_resistente(biblio_tipos),
        span_peficaz = traducciones.span_peficaz(biblio_tipos),
        span_inmune = traducciones.span_inmune(biblio_tipos),
        span_ineficaz = traducciones.span_ineficaz(biblio_tipos)
    )
    return document_template_nuevo

if __name__ == "__main__":
    print(crea_pokedex("articuno"))
