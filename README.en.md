# Cubo 64 — Magic Cube 64

**Mathematics, geometry and symbolic interpretation** · Sergi Garcia Mecinas

[Read the interactive website in English](en.html) · [Leer la documentación en español](README.md) · [Versión web en español](index.html)

Cubo 64 is an interactive 4 × 4 × 4 grid consisting of **64 positions**. One algebraic function over the finite field **GF(4)** generates all its values. Its twelve coordinate planes are magic squares with a line sum of **64**, and the eight corners of the cube form two interpenetrating regular tetrahedra (a **stella octangula**). The work distinguishes mathematical properties that can be reproduced from philosophical and symbolic interpretations.

## Explore the construction

Open `en.html` in a modern browser. The 3D viewer, mathematical proof, audit results, eight-step guide and symbolic section are translated into English. Use **ES / EN** in the navigation to change languages.

The site is standalone HTML and JavaScript: no build tools, external dependencies or internet connection are needed once the files are downloaded. GitHub Pages can serve `index.html` as the Spanish home page, with `en.html` as the English edition.

## Main results and limitations

- **64 positions:** a 4 × 4 × 4 coordinate grid, with every point labelled by the same function.
- **12 magic planes:** six outer faces and six inner sections. Each plane contains every odd number from 1 to 31 exactly once.
- **72 of 76 examined lines:** 48 axial lines and 24 planar diagonals sum to 64. The four body/space diagonals instead sum to **4, 52, 76 and 124**.
- **Two regular tetrahedra:** each has six edges of length **3√2**, a shared centroid at **(1.5, 1.5, 1.5)** and vertex labels summing to **64**.
- **Eight octants:** each 2 × 2 × 2 sub-block sums to **128**, so the complete grid sums to **1024**.
- **Inner/outer correspondence:** the eight outer corners with coordinates in `{0,3}³` have the same labels as their counterparts in `{1,2}³` under `0→1, 3→2`.

**Important:** this is *not* a normal or perfect magic cube. A normal order-4 magic cube would use the integers 1–64 exactly once and have a line constant of 130. The stella octangula is a known geometric figure; the specific relationship between the assigned numbers and its vertices is the feature studied here. The sum of tetrahedral vertex labels is not a new magic line.

## The algebraic rule

Encode GF(4) as the set `{0,1,2,3}`, with field addition given by XOR. Field multiplication by 2 and 3 uses the following lookup tables (not ordinary integer multiplication):

```text
2*y = [0, 2, 3, 1][y]
3*y = [0, 3, 1, 2][y]

u = x XOR (2*y) XOR (3*z)
v = x XOR (3*y) XOR (2*z)

G(x,y,z) = 4*u + v
F(x,y,z) = 2*G(x,y,z) + 1
```

The seed **G** takes the integers 0–15, each repeated four times. Every planar magic line sums to **30** under G. Choosing the affine transformation **F = 2G + 1** gives **2 × 30 + 4 = 64**, and maps the labels to the odd numbers from 1 to 31. This is a deliberate numerical normalization, not a constant forced by GF(4).

The matrix of the linear map `(x,y,z) → (u,v)` is:

```text
A = [1  2  3]
    [1  3  2]
```

Every 2 × 2 submatrix formed by choosing two columns has determinant **1** over GF(4). Thus fixing any one coordinate gives a bijection between the remaining two coordinates and all sixteen pairs `(u,v)`, explaining the twelve magic planes.

Along each axial line and each main or reverse diagonal of a coordinate plane, `u` and `v` each traverse the four GF(4) elements exactly once. Their ordinary integer sums are 6, so `ΣG = 4×6 + 6 = 30` and `ΣF = 2×30 + 4 = 64`.

Because `1 XOR 2 XOR 3 = 0` in GF(4), adding the same field element to all three coordinates leaves the assigned value invariant:

```text
F(x XOR t, y XOR t, z XOR t) = F(x,y,z)
```

This algebraic symmetry accounts for the four positions `(t,t,t)` with label 1, the central symmetry, and the eight outer/inner corner correspondences. It is not a geometric translation in the ordinary Euclidean sense.

## Geometric construction

Viewed along the main diagonal `(1,1,1)`, six corners project onto two overlapping triangles. Each has vertex values **31 + 13 + 19 = 63**. Adding the value-1 corner at the *opposite* end of the diagonal completes a regular tetrahedron:

```text
Tetrahedron A: (3,0,0), (0,3,0), (0,0,3), (3,3,3)
Tetrahedron B: (0,3,3), (3,0,3), (3,3,0), (0,0,0)

31 + 13 + 19 + 1 = 64
```

For the seed G, the corresponding sum is `15 + 6 + 9 + 0 = 30`. Both tetrahedra have edges of length `3√2` and centroid `(1.5, 1.5, 1.5)`.

## Reproduce the tests

Run:

```bash
python3 verificar.py
```

Only the Python standard library is needed. The audit checks the 64 positions, 12 magic planes, 72 magic lines, the four exceptional body diagonals, diagonal GF(4) invariance, the eight octants summing to 128, the corner correspondence and the tetrahedra.

The website has a separate interactive set of checks with the same mathematical goals.

## Related fractal investigation

A separate branch considers the continuous family `Fλ = 16 + λ(F − 16)`. At `λ = 16/15`, it becomes `Fλ = (32/15)G`. Exactly four positions of G are zero. If one *explicitly defines* a self-similar process that subdivides into 4 × 4 × 4 blocks and retains the 60 non-zero sub-blocks at each level, the resulting limit set has dimension **log₄(60)**. This does not turn the uniterated 64-position F construction into an infinite fractal.

## Research background and credit

- **Concept and investigation:** Sergi Garcia Mecinas.
- **Related work:** [IA_m](https://github.com/sgarcia87/IA_m) (semantic duality and graphs), [Tríada Emergente](https://github.com/sgarcia87/Triada-emergente) (equilibrium and discrete symmetries), and [Q-Reality-12D](https://github.com/sgarcia87/Q-Reality-12D) (binary constraints).
- **Symbolic layer:** Nature, Mind, Consciousness, complementarity and balance are philosophical interpretations, not claims established by the mathematical construction.

These conceptual links are not presented as proved mathematical equivalences between the projects. The work does not claim to establish a physical theory of consciousness or the universe.

**License:** the author has not yet selected a license. No automatic open-source license is granted.
