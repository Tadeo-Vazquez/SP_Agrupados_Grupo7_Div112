from difflib import Differ

differ = Differ()

# Nueva comparación entre las dos listas proporcionadas
lista1_nueva = [
    ['Animales domésticos', 'Perro', 'Gato', 'Conejo', 'Hámster'], ['Animales salvajes', 'León', 'Tigre', 'Jirafa', 'Elefante'],
    ['Árboles', 'Roble', 'Pino', 'Abeto', 'Secuoya'], ['Aves', 'Águila', 'Loro', 'Cóndor', 'Flamenco'], 
    ['Comidas saludables', 'Ensalada', 'Yogur', 'Avena', 'Frutas'], ['Deportes', 'Fútbol', 'Baloncesto', 'Tenis', 'Natación'],
    ['Electrodomésticos', 'Lavadora', 'Nevera', 'Microondas', 'Tostadora'], ['Electrónica', 'Resistencia', 'Capacitor', 'Inductor', 'Diodo'],
    ['Elementos de seguridad', 'Casco', 'Chaleco', 'Extintor', 'Señales'], ['Elementos químicos', 'Oro', 'Plata', 'Hidrógeno', 'Oxígeno'],
    ['Estaciones del año', 'Primavera', 'Verano', 'Otoño', 'Invierno'], ['Estados de la materia', 'Sólido', 'Líquido', 'Gaseoso', 'Plasma'],
    ['Famosos científicos', 'Einstein', 'Newton', 'Curie', 'Galileo'], ['Fenómenos meteorológicos', 'Lluvia', 'Nieve', 'Granizo', 'Viento'],
    ['Fenómenos naturales', 'Tornado', 'Terremoto', 'Volcán', 'Inundación'], ['Festividades', 'Navidad', 'Halloween', 'Pascua', 'Año Nuevo'],
    ['Fiestas populares', 'Carnaval', 'Oktoberfest', 'San Fermín', 'Tomatina'], ['Flores', 'Rosa', 'Margarita', 'Tulipán', 'Orquídea'],
    ['Frutas', 'Manzana', 'Plátano', 'Uva', 'Naranja'], ['Géneros literarios', 'Novela', 'Poesía', 'Ensayo', 'Teatro'],
    ['Géneros musicales', 'Rock', 'Pop', 'Clásica', 'Jazz'], ['Idiomas', 'Inglés', 'Español', 'Francés', 'Chino'],
    ['Instrumentos de viento', 'Flauta', 'Trombón', 'Saxofón', 'Clarinete'], ['Inventos de Tesla', 'Bobina', 'Corriente Alterna', 'Radio', 'Motor Eléctrico'],
    ['Juegos', 'Jenga', 'Damas', 'Monopoly', 'Cartas'], ['Juguetes', 'Lego', 'Barbie', 'Beyblade', 'Hot Wheels'],
    ['Lenguajes de programación', 'Python', 'Java', 'C++', 'Ruby'], ['Marcas de ropa', 'Nike', 'Adidas', 'Puma', 'Jordan'],
    ['Materias escolares', 'Matemáticas', 'Lengua', 'Historia', 'Geografía'], ['Monedas del mundo', 'Euro', 'Peso', 'Dólar', 'Yen'],
    ['Monumentos', 'Coliseo', 'Torre Eiffel', 'Gran Muralla', 'Cabildo'], ['Muebles', 'Silla', 'Mesa', 'Sofá', 'Cama'],
    ['Parientes', 'Madre', 'Padre', 'Hermano', 'Hermana'], ['Partes del cuerpo', 'Mano', 'Cabeza', 'Pierna', 'Torso'],
    ['Planetas', 'Mercurio', 'Venus', 'Marte', 'Júpiter'], ['Reptiles', 'Iguana', 'Cocodrilo', 'Serpiente', 'Tortuga'],
    ['Transportes públicos', 'Autobús', 'Metro', 'Tranvía', 'Taxi'], ['Vehículos', 'Carro', 'Moto', 'Bicicleta', 'Avión']
]

lista2_nueva = [
    ['Animales salvajes', 'León', 'Tigre', 'Jirafa', 'Elefante'], ['Árboles', 'Roble', 'Pino', 'Abeto', 'Secuoya'],
    ['Aves', 'Águila', 'Loro', 'Cóndor', 'Flamenco'], ['Comidas saludables', 'Ensalada', 'Yogur', 'Avena', 'Frutas'],
    ['Deportes', 'Fútbol', 'Baloncesto', 'Tenis', 'Natación'], ['Electrodomésticos', 'Lavadora', 'Nevera', 'Microondas', 'Tostadora'],
    ['Electrónica', 'Resistencia', 'Capacitor', 'Inductor', 'Diodo'], ['Elementos de seguridad', 'Casco', 'Chaleco', 'Extintor', 'Señales'],
    ['Elementos químicos', 'Oro', 'Plata', 'Hidrógeno', 'Oxígeno'], ['Estaciones del año', 'Primavera', 'Verano', 'Otoño', 'Invierno'],
    ['Estados de la materia', 'Sólido', 'Líquido', 'Gaseoso', 'Plasma'], ['Famosos científicos', 'Einstein', 'Newton', 'Curie', 'Galileo'],
    ['Fenómenos meteorológicos', 'Lluvia', 'Nieve', 'Granizo', 'Viento'], ['Fenómenos naturales', 'Tornado', 'Terremoto', 'Volcán', 'Inundación'],
    ['Festividades', 'Navidad', 'Halloween', 'Pascua', 'Año Nuevo'], ['Fiestas populares', 'Carnaval', 'Oktoberfest', 'San Fermín', 'Tomatina'],
    ['Flores', 'Rosa', 'Margarita', 'Tulipán', 'Orquídea'], ['Frutas', 'Manzana', 'Plátano', 'Uva', 'Naranja'],
    ['Géneros musicales', 'Rock', 'Pop', 'Clásica', 'Jazz'], ['Idiomas', 'Inglés', 'Español', 'Francés', 'Chino'],
    ['Inventos de Tesla', 'Bobina', 'Corriente Alterna', 'Radio', 'Motor Eléctrico'], ['Juegos', 'Jenga', 'Damas', 'Monopoly', 'Cartas'],
    ['Juguetes', 'Lego', 'Barbie', 'Beyblade', 'Hot Wheels'], ['Lenguajes de programación', 'Python', 'Java', 'C++', 'Ruby'],
    ['Marcas de ropa', 'Nike', 'Adidas', 'Puma', 'Jordan'], ['Materias escolares', 'Matemáticas', 'Lengua', 'Historia', 'Geografía'],
    ['Monedas del mundo', 'Euro', 'Peso', 'Dólar', 'Yen'], ['Monumentos', 'Coliseo', 'Torre Eiffel', 'Gran Muralla', 'Cabildo'],
    ['Muebles', 'Silla', 'Mesa', 'Sofá', 'Cama'], ['Parientes', 'Madre', 'Padre', 'Hermano', 'Hermana'],
    ['Partes del cuerpo', 'Mano', 'Cabeza', 'Pierna', 'Torso'], ['Planetas', 'Mercurio', 'Venus', 'Marte', 'Júpiter'],
    ['Reptiles', 'Iguana', 'Cocodrilo', 'Serpiente', 'Tortuga'], ['Vehículos', 'Carro', 'Moto', 'Bicicleta', 'Avión']
]

# Diferencias entre lista1_nueva y lista2_nueva
diferencias_nueva = list(differ.compare([str(item) for item in lista1_nueva], [str(item) for item in lista2_nueva]))

# Filtrar diferencias detectadas
diferencias_detectadas_nueva = [line for line in diferencias_nueva if line.startswith('- ') or line.startswith('+ ')]
print(diferencias_detectadas_nueva)
