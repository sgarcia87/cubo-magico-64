# Cubo Mágico 64

**Matemática, geometría y lectura simbólica** · Sergi Garcia Mecinas

Página web estática e interactiva para presentar el proyecto *Cubo 64*: una retícula de orden **4 × 4 × 4**, una numeración definida mediante el campo finito **GF(4)**, 12 planos cuadrados mágicos de constante **64**, la estrella octángula formada por dos tetraedros regulares y una lectura simbólica de dualidad, complementariedad, equilibrio y relación entre las partes y el conjunto.

## Ver la web

Abre `index.html` en el navegador. No necesita servidor, dependencias, conexión a Internet ni compilación. Se puede publicar directamente con GitHub Pages.

## Qué contiene

- Modelo tridimensional que gira con ratón o dedo.
- Modos de cubo completo, octantes, hexagrama, tetraedros, núcleo y lectura simbólica.
- Seis matrices exteriores y seis secciones interiores generadas por una misma función.
- Auditoría reproducible con resultados visibles en la propia web y script Python independiente (semilla, traslación diagonal GF(4), 8 octantes, 12 planos, 72 líneas y tetraedros).
- Guía de ocho pasos con botones que activan la vista correspondiente en el visor 3D.
- Explicación de qué propiedades están demostradas y cuáles son interpretaciones simbólicas.

## Fórmula

Codificamos los elementos de GF(4) como `0,1,2,3`, con suma XOR y tablas de multiplicación del campo:

```text
2*y = [0, 2, 3, 1][y]
3*y = [0, 3, 1, 2][y]

u = x XOR (2*y) XOR (3*z)
v = x XOR (3*y) XOR (2*z)
G(x,y,z) = 4*u + v
F(x,y,z) = 2*G(x,y,z) + 1
```

Para `(x,y,z) ∈ {0,1,2,3}³`, **G** produce los 16 enteros de 0 a 15, repetidos cuatro veces cada uno, y **F** los convierte en los 16 impares de 1 a 31. Los doce planos coordenados (seis exteriores y seis interiores) contienen cada impar una vez y son cuadrados mágicos 4 × 4 de constante 64.

**¿Por qué elegir 1, 3, ..., 31?** La suma de los cuatro términos de cualquier línea axial o diagonal plana es 30 para G. Aplicar `F = 2G + 1` transforma esas sumas en `2×30 + 4×1 = 64`. Esta normalización afín explica la elección numérica: el campo GF(4) no obliga a que la constante sea 64.

**Precisiones:** 72 de las 76 líneas principales consideradas son mágicas (48 axiales y 24 diagonales planas). Las cuatro diagonales espaciales suman 4, 52, 76 y 124. No es un cubo mágico normal ni perfecto: uno normal de orden 4 usaría 1 a 64 una sola vez y tendría constante 130. Los vértices de cada tetraedro regular suman 30 en G y 64 en F; esas sumas no son líneas mágicas adicionales.

## Justificación matemática

La matriz de la aplicación lineal `(x,y,z) → (u,v)` sobre GF(4) es:

```text
A = [1  2  3]
    [1  3  2]
```

- **Doce planos:** los determinantes de cada una de las tres submatrices de dos columnas son 1 en GF(4). Fijar una coordenada produce una biyección entre las dieciséis parejas restantes y los dieciséis valores de G.
- **72 líneas:** en cada dirección axial y en las diagonales principales/secundarias de los doce planos, `u` y `v` recorren los cuatro elementos una vez. Como `0+1+2+3 = 6`, las sumas aritméticas son `ΣG=4×6+6=30` y `ΣF=2×30+4=64`. En diagonales secundarias, `3−t=t XOR 3`.
- **Invarianza diagonal:** como `1 XOR 2 XOR 3 = 0`, para cualquier `t ∈ GF(4)` se cumple `F(x XOR t, y XOR t, z XOR t)=F(x,y,z)`. Explica `F(t,t,t)=1`, la simetría central y las ocho correspondencias de vértices exterior/núcleo. Es una simetría algebraica, no una traslación euclidiana.
- **Ocho octantes:** en cada bloque de 2 × 2 × 2, `u` y `v` recorren cada valor de 0 a 3 exactamente dos veces. Así `ΣG=4×12+12=60` y `ΣF=2×60+8=128`. Los ocho bloques suman 1024 en conjunto.
- **Tetraedros:** los dos tetraedros regulares de vértices alternos (estrella octángula, figura geométrica clásica) tienen arista `3√2` y centroide `(1.5,1.5,1.5)`. Sus cuatro valores G suman `15+6+9+0=30`; los de F suman `31+13+19+1=64`.

Estos argumentos explican las propiedades de la construcción. El archivo `verificar.py` las comprueba exhaustivamente sobre sus 64 posiciones.

## Guía paso a paso

La web permite seguir la construcción en ocho etapas, con botones para cambiar la vista del modelo: retícula 4 × 4 × 4; semilla G y transformación F; doce planos mágicos; 72 líneas de suma 64; hexagrama; dos tetraedros regulares; núcleo interior; e interpretación simbólica opcional. El apartado «Base matemática» añade una demostración desplegable.

## Comprobar las matemáticas

```bash
python3 verificar.py
```

No se necesitan paquetes externos. La auditoría incluye los ocho octantes de suma 128 y las 256 igualdades de la simetría de traslación diagonal (64 puntos × 4 desplazamientos).

## Publicar en GitHub Pages

1. Crea un repositorio nuevo en GitHub (por ejemplo `cubo-64`).
2. Sube los archivos `index.html`, `README.md` y `verificar.py` a la rama principal (`main`).
3. Ve a **Settings → Pages → Build and deployment**.
4. Elige **Deploy from a branch**, rama `main`, carpeta `/ (root)` y guarda.
5. GitHub mostrará la dirección pública de tu página al terminar el despliegue.

## Créditos y alcance

- **Idea e investigación:** Sergi Garcia Mecinas.
- **Interpretación simbólica:** dualidad, equilibrio, síntesis, cubo y hexagrama, diferenciados explícitamente de los resultados matemáticos.
- **Contexto matemático relacionado:** [Tríada Emergente](https://github.com/sgarcia87/Triada-emergente), [IA_m](https://github.com/sgarcia87/IA_m) y [Q-Reality-12D](https://github.com/sgarcia87/Q-Reality-12D).

La pieza principal es finita. La rama fractal relacionada requiere definir expresamente una iteración de 4×4×4 subdivisiones conservando las 60 posiciones no nulas de G: bajo esa construcción autosimilar, el soporte límite tiene dimensión log₄(60); no es una propiedad automática del cubo F sin iterar.

El proyecto presenta una construcción matemática reproducible y una lectura filosófica personal. No pretende demostrar una teoría física de la consciencia, del universo ni de la geometría sagrada. El modelo tridimensional es una visualización interactiva de la construcción algebraica, sus simetrías y sus relaciones geométricas.

**Licencia:** pendiente de elección por el autor. No se incluye una licencia automática.