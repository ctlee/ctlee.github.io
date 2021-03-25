---
title: 'Independent Markov Decomposition: Towards Modeling Kinetics of Biomolecular Complexes'

authors: 'T. Hempel, M. J. Razo<sup>*</sup>, <b>C. T. Lee<sup>*</sup></b>, B. C. Taylor<sup>*</sup>, R. E. Amaro<sup>$</sup>, and F. Noé<sup>$</sup>'

biorxiv: 10.1101/2021.03.24.436806
arxiv: 
chemrxiv: 

status: 'Submitted'

date: 2021-03-25

collection: inpreps
permalink:  /inpreps/2021-independentmarkovdecomposition
---

In order to advance the mission of in silico cell biology, modeling the interactions of large and complex biological systems becomes increasingly relevant. The combination of molecular dynamics (MD) and Markov state models (MSMs) have enabled the construction of simplified models of molecular kinetics on long timescales. Despite its success, this approach is inherently limited by the size of the molecular system. With increasing size of macromolecular complexes, the number of independent or weakly coupled subsystems increases, and the number of global system states increase exponentially, making the sampling of all distinct global states unfeasible. In this work, we present a technique called Independent Markov Decomposition (IMD) that leverages weak coupling between subsystems in order to compute a global kinetic model without requiring to sample all combinatorial states of subsystems. We give a theoretical basis for IMD and propose an approach for finding and validating such a decomposition. Using empirical few-state MSMs of ion channel models that are well established in electrophysiology, we demonstrate that IMD can reproduce experimental conductance measurements with a major reduction in sampling compared with a standard MSM approach. We further show how to find the optimal partition of all-atom protein simulations into weakly coupled subunits.
