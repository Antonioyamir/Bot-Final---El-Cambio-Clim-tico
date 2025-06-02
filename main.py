import discord 
from discord.ext import commands
import requests
import pyttsx3

intents = discord.Intents.default() #como añadir privilegios de discord
intents.message_content = True #como activar para leer mensajes

bot = commands.Bot(command_prefix='/', intents=intents) # letras con que se puede ahcer el comand por ejemplo: /hola !hola

@bot.event
async def on_ready():
    print(f'Hola! me he iniciado como {bot.user}, soluciones el cambio climatico!')

@bot.command()
async def heh(ctx, count_heh = 5): #ctx para leer mensajes}
    await ctx.send('he' * count_heh)

@bot.command()
async def hola(ctx):
    await ctx.send('Hola user! soy un bot que ayuda a darte un guia sobre el cambio climatico, si quieres ser parte de la solucion escribe /ayuda y te dire que comandos puedes usar!')

@bot.command()
async def adios(ctx):
    await ctx.send('Adios user! espera que hayas aprendido sobre el cambio climático, y te haya gustado este bot! espero verte pronto si tienes alguna duda!')

@bot.command()
async def mrbeast(ctx, count_mrbeast = 3): #ctx para leer mensajes}
    await ctx.send('mrbeast' * count_mrbeast)

def get_weather_info(city):
    base_url = f"https://wttr.in/{city}?format=%C+%t&lang=es"
    response = requests.get(base_url)
    if response.status_code == 200:
        return response.text.strip()
    else:
        return "No se pudo obtener la información del clima. Por favor, inténtalo más tarde."
    
@bot.command()
async def clima(ctx, *, city):
    weather_info = get_weather_info(city)
    await ctx.send(f"Clima en {city}: {weather_info}")

@bot.command()
async def ayuda(ctx):
    """Muestra una lista de comandos disponibles y su descripción."""
    embed = discord.Embed(
        title="Comandos Disponibles",
        description="Estos son los comandos que puedes utilizar:",
        color=0x1ABC9C
    )
    embed.add_field(name="/hola", value="Saluda al bot.", inline=False)
    embed.add_field(name="/clima", value="Obtiene información del estado del clima actual en una ciudad", inline=False)
    embed.add_field(name="/ayuda", value="Muestra este mensaje de ayuda.", inline=False)
    embed.add_field(name="/masinfo", value="Muestra enlaces para obtener mas información.", inline=False)
    embed.add_field(name="/inundaciones", value="Muestra información sobre inundaciones relacionadas al cambio climático.", inline=False)
    embed.add_field(name="/tornados", value="Muestra información sobre tornados extremos.", inline=False)
    embed.add_field(name="/sequias", value="Muestra información sobre sequías prolongadas.", inline=False)
    embed.add_field(name="/catastrofes", value="Muestra información sobre catástrofes climáticas.", inline=False)
    embed.add_field(name="/cambioclimatico", value="Muestra información sobre el cambio climático", inline=False)
    embed.add_field(name="/causas", value="Muestra las causas de porque se origina el cambio climático", inline=False)
    embed.add_field(name="/efectos", value="Muestra que le sucede al planeta", inline=False)
    embed.add_field(name="/soluciones", value="Muestra como proteger al planeta", inline=False)
    embed.add_field(name="/calentamiento", value="Muestra información sobre el calentamiento global", inline=False)
    embed.add_field(name="/adios", value="El bot se despide.", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def masinfo(ctx):
    embed = discord.Embed(
        title="Links para más sobre el cambio climático",
        description="Aquí tiene algunos enlances para obtener más información del cambio climático",
        color=0x1ABC9C
    )
    embed.add_field(name="Más sobre el calentamiento global de la ONU", value="https://www.un.org/es/un75/climate-crisis-race-we-can-win", inline=False)
    embed.add_field(name="Causas y efectos del cambio climático de la ONU", value="https://www.un.org/es/climatechange/science/causes-effects-climate-change", inline=False)
    embed.add_field(name="Que es el cambio climático de la ONU", value="https://www.un.org/es/climatechange/what-is-climate-change", inline=False)
    embed.add_field(name="El acuerdo de París", value="https://unfccc.int/sites/default/files/spanish_paris_agreement.pdf", inline=False)
    embed.add_field(name="El cambio climático de parte de Wikipedia", value="https://es.wikipedia.org/wiki/Cambio_clim%C3%A1tico#", inline=False)
    embed.add_field(name='Pero tu puedes buscar más!, Ve a google y pon "cambio climático" y ahi te saldra todo lo relacionado.', value="Todos podemos ayudar a solucionar este problema!", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def inundaciones(ctx):
    embed = discord.Embed(
        title="Que son las inundaciones?",
        description="Aquí tienes información sobre las inundaciones",
        color=0x1ABC9C
    )
    embed.add_field(name="Causas Naturales", value="Son las lluvias, deshielos, tormentas, huracanes, tifones o tsunamis, esas son las principales causas naturales.", inline=False)
    embed.add_field(name="Causas No Naturales", value="Son por ejemplo, las fallas hidráulicas, la contaminación del agua, y la erosión del terreno.", inline=False)
    embed.add_field(name="Consecuencias Ambientales", value="Las inundaciones pueden generar modificaciones ligeras, moderadas o severas en la topografía afectada. y Si un cultivo es arrasado por una inundación, también se altera el ecosistema del lugar. Los agentes polinizadores y los animales que se beneficiaban de los cultivos, se pueden desplazar hacia otros sitios y afectar negativamente la zona", inline=False)
    embed.add_field(name="Consecuencias Económicas", value="Las inundaciones pueden causar daños estructurales considerables, afectando viviendas, locales comerciales, cultivos. Todo esto tiene un impacto negativo en la economía local, lo que su vez desmejora las condiciones de vida de las personas afectadas.", inline=False)
    embed.add_field(name="Consecuencias sociales", value="En los casos más graves, las inundaciones pueden generar pérdidas humanas o heridos de gravedad. Además, puede inducir desplazamientos poblacionales, como una forma de solucionar la pérdida de la vivienda o de la fuente de trabajo.", inline=False)
    embed.add_field(name="Consecuencias sanitarias", value="Las inundaciones pueden generar focos de enfermedades como el dengue, enfermedades infecciosas, dermatológicas, trastornos digestivos, etc.", inline=False)
    embed.add_field(name='Tu tambien puedes buscar más! por ejemplo yo me guie de este sitio, miralo!', value="https://www.significados.com/inundaciones/", inline=False)
    embed.set_image(url="https://s1.significados.com/foto/inundacion-urbana.jpg?class=article")
    await ctx.send(embed=embed)

@bot.command()
async def tornados(ctx):
    embed = discord.Embed(
        title="Que son los tornados?",
        description="Aquí tienes información sobre los tornados",
        color=0x1ABC9C
    )
    embed.add_field(name="¿Qué son los tornados?", value="Un tornado es una columna de aire giratoria que por uno de sus extremos toca la superficie terrestre y por el otro está en contacto con nubes de tormenta, conocidas como cumulonimbos. Es un fenómeno atmosférico de corta duración pero de gran intensidad..", inline=False)
    embed.add_field(name="Cómo se forma un tornado?", value="Los tornados se gestan en el interior de unas tormentas llamadas superceldas., Allí una corriente descendente de aire frío y seco choca con otra corriente ascendente de aire caliente, el aire frío descendente se mueve en forma giratoria o de remolino, A medida que el aire frío se acerca a la superficie terrestre, su movimiento es más rápido y violento, Cuando la corriente de aire frío comienza a impedir el suministro de aire caliente, la fuente de poder del tornado se pierde. Esto hace que su vórtice se debilite.", inline=False)
    embed.add_field(name="Tipos de tornado", value="Son: Cono o Cuña, Cuerda, Multivórtices, Satélite, Trombas marinas y terrestres.", inline=False)
    embed.add_field(name="La escala Fujita", value="Fue diseñada por los meteorólogos Tetsuya Fujita y Allen Pearson, de la Universidad de Chicago, en 1971. Clasifica a los tornados en seis categorías, desde F0 hasta F5. F0: Vientos 60-117 km/h, daños menores. F1: Vientos 118-181 km/h, arranca tejas y mueve vehículos. F2: Vientos hasta 205 km/h, destruye techos. F3: Vientos 251-320 km/h, arranca árboles y derriba muros. F4: Vientos 321-420 km/h, lanza vehículos y destruye edificaciones. F5: Vientos hasta 510 km/h, destruye todo, incluso casas.", inline=False)
    embed.add_field(name="Consecuencias de un tornado", value="Pérdidas humanas, Pérdidas económicas, Daño ecológico, Familias sin hogar y contaminación ambiental.", inline=False)
    embed.add_field(name='Tu tambien puedes buscar más! por ejemplo yo me guie de este sitio, miralo!', value="https://www.lifeder.com/tornado/", inline=False)
    embed.set_image(url="https://www.lifeder.com/wp-content/uploads/2022/03/tornados-696x392.jpg")
    await ctx.send(embed=embed)

@bot.command()
async def sequias(ctx):
    embed = discord.Embed(
        title="Que son las sequías?",
        description="Aquí tienes información sobre las sequías",
        color=0x1ABC9C
    )
    embed.add_field(name="Qué es la sequía?", value="La sequía es un período prolongado en el que una región no recibe suficiente agua", inline=False)
    embed.add_field(name="Cuales son las causas?", value="Las sequías aparecen por la deforestación, sobreexplotación de areas, uso mal del agua, ciclos climáticos, productos toxicos, y principalmente el cambio climático.", inline=False)
    embed.add_field(name="Tipos de sequías", value="Son: Sequía meteorológica:escasez de precipitaciones durante un período, Sequía agrícola: este afecta más a los cultivos, Sequía hidrológica: este se produce cuando las reservas de agua de la zona están por debajo de la media.", inline=False)
    embed.add_field(name="Consecuencias de la sequía", value="Perdida de productos agrícolas, Malnutrición, Hambruna, Daño del Ecosistema, Aumento de Incendios Forestales, Escasez de Agua Potable y Inestabilidad Mundial.", inline=False)
    embed.add_field(name="Como Evitar la sequía", value="Gestion sostenible del suelo, Reforestación y restauración de ecosistemas, Construcción de presas y embalses, Construcción de trasvases y Reutilización de aguas recicladas y/o residuales.", inline=False)
    embed.add_field(name='Tu tambien puedes buscar más! por ejemplo yo me guie de este sitio, miralo!', value="https://www.ecologiaverde.com/que-es-la-sequia-sus-causas-y-consecuencias-1268.html", inline=False)
    embed.set_image(url="https://cdn0.ecologiaverde.com/es/posts/8/6/2/que_es_la_sequia_y_que_paises_la_sufren_mas_1268_0_600.webp")
    await ctx.send(embed=embed)

@bot.command()
async def catastrofes(ctx):
    embed = discord.Embed(
        title="Que son las catastrofes?",
        description="Aquí tienes información sobre las catastrofes",
        color=0x1ABC9C
    )
    embed.add_field(name="Causas de las catátrofes climáticas", value="Las catástrofes climáticas son eventos extremos que surgen de alteraciones en los patrones climáticos globales. La principal causa de estas alteraciones es el cambio climático, un fenómeno derivado de la acumulación de gases de efecto invernadero en la atmósfera. La actividad humana, especialmente la quema de combustibles fósiles como el carbón, el petróleo y el gas natural, ha incrementado significativamente la concentración de dióxido de carbono (CO₂) y otros gases en la atmósfera, lo que atrapa el calor y altera los sistemas climáticos de la Tierra.", inline=False)
    embed.add_field(name="Tipos de catástrofes", value="Las catástrofes climáticas se manifiestan de diversas formas, desde tormentas devastadoras hasta sequías prolongadas. Cada tipo de desastre tiene su propio conjunto de impactos y desafíos asociados. El artículo detalla cómo estos eventos afectan a las comunidades, economías y ecosistemas, destacando la necesidad de estrategias de mitigación y adaptación eficaces.", inline=False)
    embed.add_field(name="Consecuencias de las catástrofes", value="Las catástrofes climáticas —como huracanes, incendios, sequías o inundaciones— están aumentando en frecuencia e intensidad debido al cambio climático. Sus consecuencias afectan todos los niveles de la vida humana, económica y ambiental..", inline=False)
    embed.add_field(name="Consecuencias en la vida humana", value="En la vida humana, provocan la muerte de miles de personas, lesiones graves y el aumento de enfermedades como el cólera, el dengue o afecciones respiratorias. Además, muchas personas pierden sus hogares o son desplazadas, lo que genera ansiedad, estrés y trauma psicológico.", inline=False)
    embed.add_field(name="Consecuencias en la economía", value="En la economía, los desastres destruyen infraestructura (casas, hospitales, caminos), paralizan la actividad productiva y afectan especialmente a la agricultura. Esto se traduce en pérdida de empleos, escasez de alimentos y aumento de precios, sobre todo en regiones vulnerables.", inline=False)
    embed.add_field(name="Consecuencias en el medio ambiente", value="En el medio ambiente, dañan ecosistemas, contaminan fuentes de agua, erosionan suelos y provocan la pérdida de biodiversidad. Incendios y tormentas liberan grandes cantidades de CO₂, agravando aún más el calentamiento global.", inline=False)
    embed.add_field(name="Como Evitar las catástrofes", value="El artículo también aborda las posibles soluciones para mitigar los impactos de las catástrofes climáticas. Estas incluyen la implementación de políticas de reducción de emisiones de gases de efecto invernadero, el fomento de energías renovables, la mejora de la infraestructura para resistir eventos extremos y la promoción de prácticas agrícolas sostenibles. Además, se destaca la importancia de la educación y la concienciación pública para preparar a las comunidades ante futuros desastres.", inline=False)
    embed.add_field(name='Tu tambien puedes buscar más! por ejemplo yo me guie de este sitio, miralo!', value="https://revistacompleta.com/impacto-de-las-catastrofes-climaticas/", inline=False)
    embed.set_image(url="https://www.arqhys.com/wp-content/uploads/2017/03/tipos-de-desastres-naturales.png")
    await ctx.send(embed=embed)

@bot.command()
async def causas(ctx):
    embed = discord.Embed(
        title="Cuales son las causas del cambio climático?",
        description="Aquí tienes información sobre las causas del cambio climático",
        color=0x1ABC9C
    )
    embed.add_field(name="La generación de energía", value="La generación de energia a travéz de combustibles fosiles, provoca una gran cantidad de emisores, como el CO2 que son potentes gases invernaderos. A nivel global, un cuarto de electricidad proviene de energía renovable eólica y solares, que no contaminan al planeta", inline=False)
    embed.add_field(name="Productos de fabricación", value="Las industrias y fábricas generan muchos emisores, que provienen de la quema de combustible, que da energía para la fabricación de muchas cosas que usamos, Y la maquinaria utilizada para fabricar objetos, necesita de carbón, petróleo o gas, osea las fabricas son unas de las que más atribuyan a los gases de efecto invernadero.", inline=False)
    embed.add_field(name="La tala de bosques", value=" Cada año se destruyen 12 millones de hectáreas de bosques, lo que libera el carbono almacenado en los árboles y reduce la capacidad natural de absorber CO₂. Representa alrededor del 25% de las emisiones globales junto con la agricultura y el uso del suelo.", inline=False)
    embed.add_field(name="El uso del transporte", value="El uso de combustibles fósiles en vehículos, aviones y barcos genera cerca de un cuarto de las emisiones de CO₂ relacionadas con la energía. Las emisiones siguen aumentando con la creciente demanda de transporte.", inline=False)
    embed.add_field(name="La producción de alimentos", value="Contribuye significativamente al cambio climático por la deforestación, el uso de fertilizantes, la ganadería y el consumo de energía en el procesamiento y distribución de alimentos.", inline=False)
    embed.add_field(name="La energía en los edificios", value="Los sistemas de calefacción, climatización y el uso de electricidad en hogares y comercios generan altas emisiones, debido al uso de carbón, gas y petróleo.", inline=False)
    embed.add_field(name="Un consumo excesivo", value=" El estilo de vida, especialmente en los sectores más ricos, influye directamente en las emisiones. El 1% más rico del mundo emite más que el 50% más pobre.", inline=False)
    embed.add_field(name='Tu tambien puedes buscar más! por ejemplo yo me guie de este sitio, miralo!', value="https://www.un.org/es/climatechange/science/causes-effects-climate-change", inline=False)
    embed.set_image(url="https://infomedioambiente.top/wp-content/uploads/cambio-climatico.jpg")
    await ctx.send(embed=embed)

@bot.command()
async def efectos(ctx):
    embed = discord.Embed(
        title="Cuales son los efectos del cambio climático?",
        description="Aquí tienes información sobre los efectos del cambio climático",
        color=0x1ABC9C
    )
    embed.add_field(name="Elevación de las temperaturas", value="Cada década es más cálida que la anterior, lo que incrementa olas de calor, enfermedades relacionadas con el calor e incendios forestales. El Ártico se calienta el doble que el promedio global.", inline=False)
    embed.add_field(name="Tormentas más potentes", value="Las temperaturas más altas provocan más humedad y tormentas destructivas como huracanes y tifones, que afectan gravemente a comunidades y economías.", inline=False)
    embed.add_field(name="Aumento de las sequías", value="La escasez de agua aumenta, afectando cultivos, ecosistemas y provocando tormentas de arena. Se expanden los desiertos y se reduce la tierra cultivable.", inline=False)
    embed.add_field(name="Aumento del nivel del océano y calentamiento del agua", value="El océano se calienta y sube su nivel por la expansión del agua y el deshielo. También se acidifica por el CO₂, dañando la vida marina.", inline=False)
    embed.add_field(name="Desaparición de especies", value="Muchas especies están en peligro de extinción debido a incendios, plagas y cambios extremos. Algunas se adaptan, pero otras no sobreviven.", inline=False)
    embed.add_field(name="Escasez de alimentos", value="Las condiciones extremas afectan la pesca, agricultura y ganadería, lo que agrava la desnutrición, sobre todo en poblaciones vulnerables.", inline=False)
    embed.add_field(name="Más riesgos para la salud", value="El cambio climático causa enfermedades, desplazamientos, estrés mental, hambre y presión sobre los sistemas sanitarios. Contribuye a millones de muertes anuales.", inline=False)
    embed.add_field(name='Tu tambien puedes buscar más! por ejemplo yo me guie de este sitio, miralo!', value="https://www.un.org/es/climatechange/science/causes-effects-climate-change", inline=False)
    embed.set_image(url="https://www.ultimasnotas.com/wp-content/uploads/2017/03/2.jpg")
    await ctx.send(embed=embed)

@bot.command()
async def soluciones(ctx):
    embed = discord.Embed(
        title="Cuales son las soluciones del cambio climático?",
        description="Aquí tienes información sobre las soluciones del cambio climático",
        color=0x1ABC9C
    )
    embed.add_field(name="Compromiso Politico", value="Es necesario que todos los países realicen acuerdos y establezcan medidas de obligado cumplimiento para atajar el cambio climático. ", inline=False)
    embed.add_field(name="Educación", value="Un pilar fundamental para conseguir con éxito un cambio de modelo es concienciar y sensibilizar a la población sobre las consecuencias del cambio climático.", inline=False)
    embed.add_field(name="Energías", value="Otro cambio importante para ponerle solución al cambio climático es el cambio del modelo energético actual, abastecido con combustibles fósiles. Y se soluciona al alimentando nuestra demanda energética con energía procedente de fuentes limpias, como son la solar o la eólica.", inline=False)
    embed.add_field(name="Movilidad", value="Actualmente, el transporte genera una parte de las emisiones GEI a la atmósfera. Una solución es la transición a una movilidad más descarbonizada, Ello se consigue optando por recursos limpios como la bicicleta u optar por vehículos eléctricos.", inline=False)
    embed.add_field(name="Reducción de residuos", value="Los residuos se han convertido en un problema en el planeta. Tanto es así, que cada año acaban en el mar 8 toneladas de plásticos, Esto de ve favorecido por un modelo económico donde la mayoría de productos con plástico son de usar y tirar. Es por ello que una de las principales soluciones para el cambio climático, y los puedes hacer es promociónar de materiales biodegradables, o reciclar!", inline=False)
    embed.add_field(name="Aumento de la protección de áreas", value="Como solución para proteger la biodiversidad actual en los diferentes rincones del planeta, es necesario que aumenten las zonas protegidas. Así, se preservarían los diferentes ecosistemas que hoy en día se ven vulnerables ante la constante intrusión humana.", inline=False)
    embed.add_field(name="Consumo local", value="La promoción del consumo de proximidad debe encontrarse como prioridad en la agenda de todos los países. El abastecimiento de bienes de consumo de procedencia local contribuiría de forma muy eficiente a combatir el cambio climático, ya que las emisiones derivadas del transporte de estos bienes así como la producción de plásticos de embalaje.", inline=False)
    embed.add_field(name='Tu tambien puedes buscar más! por ejemplo yo me guie de este sitio, miralo!', value="https://www.ecologiaverde.com/soluciones-para-el-cambio-climatico-3329.html", inline=False)
    embed.set_image(url="https://eligenio.com/wp-content/uploads/2023/05/soluciones-para-el-cambio-climatico.jpg")
    await ctx.send(embed=embed)


@bot.command()
async def calentamiento(ctx):
    embed = discord.Embed(
        title="El calentamiento global.",
        description="Aquí tienes información sobre el calentamiento global",
        color=0x1ABC9C
    )
    embed.add_field(name="Qué es", value="La definición del calentamiento global hace referencia al aumento de la temperatura media de los océanos y de la atmósfera terrestre, y actualmente ha sido alarmante a nivel mundial en las últimas décadas. ", inline=False)
    embed.add_field(name="Causas", value="Incremento del efecto invernadero, Aumento de los gases de efecto invernadero, Incremento de las actividades humanas contaminantes, como los combustibles fosiles", inline=False)
    embed.add_field(name="Consecuencias", value="Producen fenómenos meteorológicos extremos como fuertes sequías, olas de calor o lluvias torrenciales, la temperatura de los océanos se elevase, provocando su expansión, deshielo de los casquetes polares, desecación de las selvas, y provoca una aceleración de algunas de las extinciones de especies.", inline=False)
    embed.add_field(name="Cómo podemos evitar", value="Reducir las emisiones de gases de efecto invernadero, Promover una dieta más sostenible, Reforestar y conservar los bosques, Reciclar y reducir residuos, Usar transporte sostenible, Mejorar la educación y la concienciación, Apoyar políticas verdes.", inline=False)
    embed.add_field(name='Tu tambien puedes buscar más! por ejemplo yo me guie de este sitio, miralo!', value="https://www.ecologiaverde.com/calentamiento-global-que-es-causas-y-consecuencias-1095.html", inline=False)
    embed.set_image(url="https://cdn0.ecologiaverde.com/es/posts/5/9/0/consecuencias_del_calentamiento_global_1095_2_600.webp")
    await ctx.send(embed=embed)

bot.run(token)
