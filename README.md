# Ajedrez Josias Vilches

Proyecto de Ajedrez de Josías Vilches

Este es un proyecto de ajedrez desarrollado en Python. El objetivo es implementar un juego funcional que siga las reglas tradicionales del ajedrez, permitiendo jugar tanto en modo local como con la opción de prueba a través de Docker.

## Características

- Implementación de todas las piezas de ajedrez y sus movimientos.
- Verificación de reglas y condiciones de victoria.
- Interfaz de línea de comandos (CLI) amigable para el usuario.
- Pruebas unitarias incluidas para garantizar la funcionalidad del código.

## Requisitos

- Python 3.x
- Docker (opcional, para la ejecución en contenedor)

## Instrucciones

El jugador con las piezas blancas siempre comienza el juego. Para realizar un movimiento, cada jugador debe especificar la fila y columna de la pieza a mover, así como las coordenadas de destino. Los jugadores se alternan por turnos, siguiendo las reglas estándar de movimiento de cada pieza: peones avanzan pero capturan en diagonal, torres se mueven en líneas rectas, caballos en "L", alfiles en diagonal, la reina en cualquier dirección, y el rey un casillero en cualquier dirección.

### Requisitos

Para poder correr de forma limpia el proyecto se recomienda el uso de [Docker](https://docs.docker.com) 

### Instalación Docker (terminal):

Instalación de Docker

```bash
sudo apt install docker
```

Clonar el [repositorio] (https://github.com/um-computacion-tm/ajedrez-2024-josiasvilches.git) del juego 

```bash
git clone https://github.com/um-computacion-tm/ajedrez-2024-josiasvilches.git
```
### Ejecutar el juego

Crear imágen de Docker del juego

```bash
docker buildx build -t ajedrez-2024-josiasvilches .
```

Ejecutar los tests y el juego

```bash
docker run -i ajedrez-2024-josiasvilches
```

### Para jugar

1. Clonar repositorio

```
git clone https://github.com/um-computacion-tm/ajedrez-2024-josiasvilches.git
```

2. Instalar dependencias

```
pip install -r requirements.txt
```

3. Ejecutar

```
python3 -m chess.cli
```




# Estado de Badges


## CircleCI
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-josiasvilches/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-josiasvilches/tree/main)

## Maintainability
<a href="https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-josiasvilches/maintainability"><img src="https://api.codeclimate.com/v1/badges/769b2f251549c76da190/maintainability" /></a>

## Test Coverage
<a href="https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-josiasvilches/test_coverage"><img src="https://api.codeclimate.com/v1/badges/769b2f251549c76da190/test_coverage" /></a>
