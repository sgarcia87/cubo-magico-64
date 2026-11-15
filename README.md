# Cubo Mágico 64

**Matemática, geometría y lectura simbólica** · Sergi Garcia Mecinas

Página web estática e interactiva para presentar el proyecto *Cubo 64*: una retícula de orden **4 × 4 × 4**, una numeración definida mediante el campo finito **GF(4)**, 12 planos cuadrados mágicos de constante **64**, la estrella octángula formada por dos tetraedros regulares y una interpretación simbólica inspirada en el manuscrito personal *La Realidad*.

## Ver la web

Abre `index.html` en el navegador. No necesita servidor, dependencias, conexión a Internet ni compilación. Se puede publicar directamente con GitHub Pages.

## Qué contiene

- Modelo tridimensional que gira con ratón o dedo.
- Modos de cubo completo, octantes, hexagrama, tetraedros, núcleo y lectura simbólica.
- Seis matrices exteriores y seis secciones interiores generadas por una misma función.
- Auditoría reproducible con resultados visibles en la propia web y script Python independiente.
- Explicación de qué propiedades están demostradas y cuáles son interpretaciones simbólicas.

## Fórmula

Codificamos los elementos de GF(4) como `0,1,2,3`, con suma XOR y tablas de multiplicación del campo:

```text
2*y = [0, 2, 3, 1][y]
3*y = [0, 3, 1, 2][y]

u = x XOR (2*y) XOR (3*z)
v = x XOR (3*y) XOR (2*z)
F(x,y,z) = 1 + 2*(4*u + v)
```

Para `(x,y,z) ∈ {0,1,2,3}³`, la función produce 16 valores impares del 1 al 31, cada uno cuatro veces. Cada uno de los 12 planos coordenados contiene los 16 impares una vez y es un cuadrado mágico 4 × 4 de suma 64.

**Precisiones:** 72 de las 76 líneas principales consideradas son mágicas. Las cuatro diagonales espaciales suman 4, 52, 76 y 124. No es un cubo mágico perfecto. Los tetraedros regulares tienen vértices que suman 64, pero esa suma no es una nueva línea mágica.

## Comprobar las matemáticas

```bash
python3 verificar.py
```

No se necesitan paquetes externos.

## Publicar en GitHub Pages

1. Crea un repositorio nuevo en GitHub (por ejemplo `cubo-64`).
2. Sube los archivos `index.html`, `README.md` y `verificar.py` a la rama principal (`main`).
3. Ve a **Settings → Pages → Build and deployment**.
4. Elige **Deploy from a branch**, rama `main`, carpeta `/ (root)` y guarda.
5. GitHub mostrará la dirección pública de tu página al terminar el despliegue.

## Créditos y alcance

- **Idea e investigación:** Sergi Garcia Mecinas.
- **Inspiración simbólica:** *La Realidad*, capítulos sobre dualidad, cubo, hexagrama, centro y consciencia.
- **Contexto matemático relacionado:** [Tríada Emergente](https://github.com/sgarcia87/Triada-emergente), [IA_m](https://github.com/sgarcia87/IA_m) y [Q-Reality-12D](https://github.com/sgarcia87/Q-Reality-12D).

El proyecto presenta una construcción matemática reproducible y una lectura filosófica personal. No pretende demostrar una teoría física de la consciencia, del universo ni de la geometría sagrada. El modelo tridimensional es una visualización interactiva de la construcción algebraica, sus simetrías y sus relaciones geométricas.

**Licencia:** pendiente de elección por el autor. No se incluye una licencia automática.