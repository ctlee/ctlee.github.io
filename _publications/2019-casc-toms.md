---
title: 'The Implementation of the Colored Abstract Simplicial Complex and Its Application to Mesh Generation'

authors: '<b>C. T. Lee<sup>*</sup><sup>$</sup></b>, J. B. Moody<sup>*</sup>, R. E. Amaro, J. A. Mccammon, and M. J. Holst'

journal: 'ACM Trans. Math. Softw.'
doi: 10.1145/3321515
citation: '45.3 (August 2019), pp. 1--20'

biorxiv: 
arxiv: 1807.01417
chemrxiv: 

date: 2019-08-08

collection: publications
permalink:  /publications/2019-casc-toms
---

We introduce the Colored Abstract Simplicial Complex library (CASC): a new, modern, and header-only C++ library that provides a data structure to represent arbitrary dimension abstract simplicial complexes (ASC) with user-defined classes stored directly on the simplices at each dimension. This is accomplished by using the latest C++ language features including variadic template parameters introduced in C++11 and automatic function return type deduction from C++14. Effectively, CASC decouples the representation of the topology from the interactions of user data. We present the innovations and design principles of the data structure and related algorithms. This includes a metadata-aware decimation algorithm, which is general for collapsing simplices of any dimension. We also present an example application of this library to represent an orientable surface mesh.
