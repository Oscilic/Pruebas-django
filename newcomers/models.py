from django.db import models

services = [
    "Alimentación transportada",
    "Servicio presencial en sucursales",
    "Concesión de casinos",
    "Coffee Break y eventos",
    "Repostería y snack con tickets"
]
subcat = [["Almuerzo tradicional", "Menú vegetariano", "Menú vegano", "Menú hipocalórico", "Menú especial del día"], ["Sándwiches", "Jugos naturales", "Colaciones dulces", "Colaciones saladas", "Alfajores"], ["Menú de almuerzo empresarial", "Menú de almuerzo ejecutivo", "Menú de almuerzo gourmet", "Menú de almuerzo saludable", "Menú de almuerzo ligero"], ["Cafetería", "Eventos corporativos", "Eventos sociales", "Coffee Break básico", "Coffee Break premium"], ["Queques", "Tortas", "Brownies", "Galletas", "Muffins"]]
products = {
    "00": {
        "nombre": "Almuerzo tradicional",
        "descripcion": "Plato principal con acompañamiento, ensalada y postre.",
        "ingredientes": ["Carne o pollo", "Arroz o papas", "Ensalada fresca", "Postre del día"],
        "condiciones": "Entrega diaria antes de las 13:00 hrs. Consumir caliente."
    },
    "01": {
        "nombre": "Menú vegetariano",
        "descripcion": "Plato principal sin carne, con proteínas vegetales y acompañamientos.",
        "ingredientes": ["Legumbres", "Verduras de estación", "Cereales", "Postre del día"],
        "condiciones": "Entrega diaria antes de las 13:00 hrs. Consumir caliente."
    },
    "02": {
        "nombre": "Menú vegano",
        "descripcion": "Plato principal 100% vegetal, sin productos de origen animal.",
        "ingredientes": ["Tofu", "Verduras frescas", "Cereales integrales", "Fruta de postre"],
        "condiciones": "Entrega diaria antes de las 13:00 hrs. Consumir caliente."
    },
    "03": {
        "nombre": "Menú hipocalórico",
        "descripcion": "Plato bajo en calorías, ideal para dietas de control de peso.",
        "ingredientes": ["Pechuga de pollo", "Verduras al vapor", "Ensalada verde", "Gelatina light"],
        "condiciones": "Entrega diaria antes de las 13:00 hrs. Consumir caliente."
    },
    "04": {
        "nombre": "Menú especial del día",
        "descripcion": "Plato sorpresa con ingredientes seleccionados por el chef.",
        "ingredientes": ["Varía según disponibilidad", "Acompañamiento", "Ensalada", "Postre especial"],
        "condiciones": "Entrega diaria antes de las 13:00 hrs. Consumir caliente."
    },
    "10": {
        "nombre": "Sándwiches",
        "descripcion": "Variedad de sándwiches frescos y saludables.",
        "ingredientes": ["Pan artesanal", "Jamón o queso", "Vegetales frescos"],
        "condiciones": "Entrega bajo pedido. Consumir en el día."
    },
    "11": {
        "nombre": "Jugos naturales",
        "descripcion": "Jugos preparados con frutas frescas de estación.",
        "ingredientes": ["Naranja", "Frutilla", "Mango", "Agua mineral"],
        "condiciones": "Entrega bajo pedido. Consumir frío."
    },
    "12": {
        "nombre": "Colaciones dulces",
        "descripcion": "Snacks dulces para media mañana o tarde.",
        "ingredientes": ["Barritas de cereal", "Fruta deshidratada", "Galletas integrales"],
        "condiciones": "Entrega bajo pedido. Consumir en el día."
    },
    "13": {
        "nombre": "Colaciones saladas",
        "descripcion": "Snacks salados para media mañana o tarde.",
        "ingredientes": ["Mix de frutos secos", "Galletas saladas", "Queso en cubos"],
        "condiciones": "Entrega bajo pedido. Consumir en el día."
    },
    "14": {
        "nombre": "Alfajores",
        "descripcion": "Alfajores artesanales rellenos de manjar.",
        "ingredientes": ["Harina", "Manjar", "Chocolate"],
        "condiciones": "Entrega bajo pedido. Consumir en el día."
    },
    "20": {
        "nombre": "Menú de almuerzo empresarial",
        "descripcion": "Menú completo para empresas, incluye entrada, plato principal y postre.",
        "ingredientes": ["Carne o pescado", "Acompañamiento", "Ensalada", "Postre"],
        "condiciones": "Entrega diaria antes de las 13:00 hrs. Reservar con anticipación."
    },
    "21": {
        "nombre": "Menú de almuerzo ejecutivo",
        "descripcion": "Menú premium para ejecutivos, con opciones gourmet.",
        "ingredientes": ["Cortes premium", "Guarniciones gourmet", "Ensalada especial", "Postre selecto"],
        "condiciones": "Entrega diaria antes de las 13:00 hrs. Reservar con anticipación."
    },
    "22": {
        "nombre": "Menú de almuerzo gourmet",
        "descripcion": "Platos de alta cocina para ocasiones especiales.",
        "ingredientes": ["Ingredientes seleccionados", "Preparación gourmet", "Presentación especial"],
        "condiciones": "Entrega bajo reserva. Consumir caliente."
    },
    "23": {
        "nombre": "Menú de almuerzo saludable",
        "descripcion": "Menú balanceado, bajo en grasas y alto en nutrientes.",
        "ingredientes": ["Proteína magra", "Verduras frescas", "Cereales integrales", "Fruta"],
        "condiciones": "Entrega diaria antes de las 13:00 hrs. Reservar con anticipación."
    },
    "24": {
        "nombre": "Menú de almuerzo ligero",
        "descripcion": "Plato principal liviano, ideal para jornadas cortas.",
        "ingredientes": ["Pollo o pescado", "Ensalada", "Fruta"],
        "condiciones": "Entrega diaria antes de las 13:00 hrs. Reservar con anticipación."
    },
    "30": {
        "nombre": "Cafetería",
        "descripcion": "Servicio de café y acompañamientos para eventos.",
        "ingredientes": ["Café de grano", "Té", "Galletas", "Leche"],
        "condiciones": "Disponible para eventos. Consumir caliente."
    },
    "31": {
        "nombre": "Eventos corporativos",
        "descripcion": "Servicio integral para reuniones y eventos empresariales.",
        "ingredientes": ["Menú personalizado", "Bebidas", "Snacks"],
        "condiciones": "Reservar con anticipación. Servicio en el lugar."
    },
    "32": {
        "nombre": "Eventos sociales",
        "descripcion": "Servicio de alimentación para celebraciones y reuniones familiares.",
        "ingredientes": ["Menú personalizado", "Bebidas", "Postres"],
        "condiciones": "Reservar con anticipación. Servicio en el lugar."
    },
    "33": {
        "nombre": "Coffee Break básico",
        "descripcion": "Servicio de coffee break con opciones sencillas.",
        "ingredientes": ["Café", "Té", "Galletas", "Jugos"],
        "condiciones": "Disponible para eventos. Consumir en el momento."
    },
    "34": {
        "nombre": "Coffee Break premium",
        "descripcion": "Servicio de coffee break con opciones gourmet y variedad de snacks.",
        "ingredientes": ["Café premium", "Snacks gourmet", "Jugos naturales", "Pastelería fina"],
        "condiciones": "Disponible para eventos. Consumir en el momento."
    },
    "40": {
        "nombre": "Queques",
        "descripcion": "Queques artesanales de diferentes sabores.",
        "ingredientes": ["Harina", "Huevos", "Azúcar", "Frutas"],
        "condiciones": "Entrega bajo pedido. Consumir en el día."
    },
    "41": {
        "nombre": "Tortas",
        "descripcion": "Tortas personalizadas para eventos y celebraciones.",
        "ingredientes": ["Bizcocho", "Relleno a elección", "Decoración personalizada"],
        "condiciones": "Entrega bajo pedido. Reservar con anticipación."
    },
    "42": {
        "nombre": "Brownies",
        "descripcion": "Brownies de chocolate artesanal.",
        "ingredientes": ["Chocolate", "Harina", "Huevos", "Nueces"],
        "condiciones": "Entrega bajo pedido. Consumir en el día."
    },
    "43": {
        "nombre": "Galletas",
        "descripcion": "Galletas caseras de diferentes sabores.",
        "ingredientes": ["Harina", "Mantequilla", "Azúcar", "Saborizantes"],
        "condiciones": "Entrega bajo pedido. Consumir en el día."
    },
    "44": {
        "nombre": "Muffins",
        "descripcion": "Muffins artesanales con frutas y chocolate.",
        "ingredientes": ["Harina", "Huevos", "Frutas", "Chocolate"],
        "condiciones": "Entrega bajo pedido. Consumir en el día."
    }
}