# MSc Thesis

**Title:** Abstract Hoare Logic Framework  
**Author:** Alessio Ferrarini  
**Institution:** University of Padova, Department of Mathematics “Tullio Levi-Civita”  
**Degree:** Master of Computer Science  
**Academic Year:** 2023-2024

You can fine the complete [thesis here (pdf)](out/thesis.pdf).

**EVERYTHING IS STILL WORK IN PROGRESS**

## Thesis Overview

The verification of program correctness is a critical task in computer science. Ensuring that software behaves as expected under all possible conditions is fundamental in a society that increasingly relies on computer programs. Programmers often reason about the behavior of their programs at an intuitive level. While this is definitely better than not reasoning at all, intuition alone becomes insufficient as the size of programs grows.

Writing tests for programs is definitely a useful task, but at best, it can show the presence of bugs, not prove their absence. We cannot feasibly write a test for every possible input of the program. To offer a guarantee of the absence of undesired behavior, we need sound logical models rooted in logic. The field of formal methods in computer science aims to develop the logical tools necessary to prove properties of software systems.

Hoare logic, first popularized by Hoare in the late 60s, provides a set of logical rules to reason about the correctness of computer programs. Hoare logic formalizes, with axioms and inference rules, the relationship between the initial and final states after running a program.

Hoare logic, beyond being one of the first, is arguably also one of the most influential ideas in the field of software verification. It created the whole field of program logics—systems of logical rules aimed at proving properties of programs. Over the years, modifications of Hoare logic have been developed, sometimes to support new language features such as dynamic memory allocation and pointers, or to prove different properties such as equivalence between programs or properties of multiple executions. Every time Hoare logic is modified, it is necessary to prove again that the proof system indeed proves properties about the program (soundness) and that the proof system is powerful enough to prove the properties of interest (completeness).

Most modifications of Hoare logic usually do not alter the fundamental proof principles of the system. Instead, they often extend the assertion language to express new properties and add new commands to support new features in different programming languages.

We introduce Abstract Hoare Logic, which aims to be a framework general enough to serve as an extensible platform for constructing new Hoare-like logics without the burden of proving soundness and completeness anew. We demonstrate, by example, how some properties that are not expressible in standard Hoare logic can be simply instantiated within Abstract Hoare Logic, while keeping the proof system as simple as possible.

The theory of Abstract Hoare Logic is deeply connected to the theory of abstract interpretation. The semantics of the language is defined as an inductive abstract interpreter, and the validity of the Abstract Hoare triples depends on it. By not using the strongest postcondition directly, we are able to reason about properties that are not expressible in the powerset of the states, such as hyperproperties.

## Contents

- **Chapter 1:** Introduce the basic mathematical background of order theory and abstract interpretation.
- **Chapter 2:** Introduce standard Hoare logic and the general framework of Abstract Hoare Logic: the extensible L language, its syntax and semantics, the generalization of the strongest postcondition, and finally, the actual Abstract Hoare Logic and its proof system, proving the general results of soundness and relative completeness.
- **Chapter 3:** Show some interesting instantiations of Abstract Hoare Logic: demonstrate that it is possible to obtain program logic where the implication is decidable, thus making the goal of checking a derivation computable; show how to obtain a proof system for hyperproperties (and introduce the concept of the strongest hyper postcondition); and show that it is possible to obtain a proof system for partial incorrectness.
- **Chapter 4:** Show how to enrich the barebones proof system of Abstract Hoare Logic by adding more restrictions on the assertion language or the semantics.
- **Chapter 5:** Show how to reuse the idea of Abstract Hoare Logic to generalize proof systems for backward reasoning.
- **Chapter 6:** Provide a brief recap of the most important points of the thesis. Discuss possible extensions to the framework of Abstract Hoare Logic and, finally, examine the relationship of Abstract Hoare Logic with other similar work.
