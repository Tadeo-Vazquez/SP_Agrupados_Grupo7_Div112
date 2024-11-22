
# 🎮 Agrupados: El Juego de Clasificación 🎲

**Agrupados** es un desafiante juego donde el objetivo es clasificar elementos en categorías correctamente. Inspirado en juegos como [Pixlinks](https://poki.com/es/g/pixlinks), combina lógica, estrategia y un toque de diversión para ofrecer una experiencia emocionante. 🧠✨

## 🚀 Características

- **Juego por niveles:** Supera 5 niveles, cada uno compuesto por 3 partidas.
- **Mecánica de vidas:** Maneja tus combinaciones con cuidado; solo tienes 3 vidas por nivel.
- **Comodines:** Usa herramientas estratégicas para avanzar:
  1. Descubre una categoría y un elemento.
  2. Empareja dos elementos automáticamente.
  3. ¡Más sorpresas por descubrir!
- **Progreso guardado:** Al finalizar, se almacena un archivo JSON con tu nombre, puntaje total, nivel alcanzado y promedio de tiempo entre niveles.

## 🎯 Objetivo

Clasificar correctamente los elementos en sus respectivas categorías. Cada combinación correcta avanza el juego, mientras que los errores restan vidas.

## 📋 Requisitos del Sistema

- **Python 3.10+**
- Bibliotecas requeridas:
  - `pygame`
  - `json`
  - `csv`

Instala las dependencias con:  
```bash
pip install -r requirements.txt
```

## 📖 Instrucciones de Juego

1. Ejecuta el juego:  
   ```bash
   python main.py
   ```
2. Ingresa tu nombre para comenzar.
3. Juega niveles progresivamente más desafiantes.
4. Usa comodines sabiamente para avanzar.

## 🏆 Dinámica

- **Timer entre niveles:** Pausa breve para prepararte.
- **Puntajes:** Recibe una puntuación al final de cada nivel.
- **Reinicios:** Solo puedes reiniciar un nivel 3 veces. ¡Gestiona tus recursos!

## 🛠 Tecnologías Utilizadas

- **Consola:** Versión inicial del juego utilizando técnicas como:
  - Manejo de listas, diccionarios y sets.
  - Lectura y escritura de archivos CSV y JSON.
  - Paradigma funcional y principios DRY.
- **Pygame:** Versión mejorada con:
  - Gráficos estilizados.
  - Sonidos interactivos.
  - Colisiones y eventos.

## 🖼 Capturas

![Captura 1](assets/screenshot1.png)  
_Ejemplo del nivel inicial en consola._  

![Captura 2](assets/screenshot2.png)  
_Pantalla en modo Pygame._

## 📂 Estructura del Proyecto

```
Agrupados/
├── assets/          # Recursos gráficos y de sonido
├── data/            # Archivos CSV con las categorías y elementos
├── main.py          # Código principal del juego
├── utils/           # Funciones auxiliares
└── README.md        # Este archivo
```

## 🤝 Contribuciones

¡Contribuciones son bienvenidas! Si deseas colaborar, abre un issue o envía un pull request.

## 📝 Licencia

Este proyecto es de uso educativo y está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
