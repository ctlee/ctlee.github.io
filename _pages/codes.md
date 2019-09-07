---
layout: archive
title: "Software and Codes"
permalink: /codes/
author_profile: true
classes: wide
---
## Geometry-preserving Adaptive MeshER (GAMer) 2
[Code](https://github.com/ctlee/gamer){: .btn .btn--inverse .btn--small}
[Documentation](https://gamer.readthedocs.io){: .btn .btn--inverse .btn--small} [![DOI](https://zenodo.org/badge/122682242.svg)](https://zenodo.org/badge/latestdoi/122682242)

GAMer is a surface mesh improvement library developed to condition surface meshes derived from noisy biological imaging data.
The library is written in C++ but we has a full python interface (PyGAMer).
There is also a Blender addon (BlendGAMer) which enables interactive calls to GAMer mesh conditioning operations.

## Colored Abstract Simplicial Complex
[Code](https://github.com/ctlee/casc){: .btn .btn--inverse .btn--small}
[Documentation](https://ctlee.github.io/casc){: .btn .btn--inverse .btn--small} [![DOI](https://zenodo.org/badge/121550288.svg)](https://zenodo.org/badge/latestdoi/121550288)

CASC is a modern and header-only C++ library which provides a data structure to represent arbitrary dimension abstract simplicial complexes with user-defined classes stored directly on the simplices at each dimension. This is achieved by taking advantage of the combinatorial nature of simplicial complexes and new C++ code features such as: variadic templates and automatic function return type deduction. Essentially CASC stores the full topology of the complex according to a Hasse diagram. The representation of the topology is decoupled from interactions of user data through the use of metatemplate programming.
