# Python Aquarium Simulation – OOP Project

## Overview
Academic project developed in **Python**, simulating an **aquarium** that contains different aquatic species interacting with each other.  
Each species has its own behavior, movement, and life cycle, implemented through **object-oriented programming (OOP)** concepts such as inheritance and polymorphism.

---

## 🐠 Features
- Simulation of an aquarium with multiple species:
  - `Scalar`, `Molly`, `Ocypode`, and `Shrimp`
- Object-oriented hierarchy:
  - Base class `Animal` with subclasses defining specific behavior
- Step-based simulation:
  - Movement, aging, hunger, and death mechanics
- Exception handling for invalid interactions or configurations
- Unit testing for selected classes (e.g., `Molly`)

---

## 🧩 System Architecture
- **Animal.py** – base class defining shared properties and actions  
- **Scalar.py, Molly.py, Ocypode.py, Shrimp.py** – specific fish classes implementing unique movement patterns  
- **Aquarium.py** – manages all animals, collisions, and simulation steps  
- **main.py** – entry point for running the simulation  
- **test_molly.py** – example of unit testing a subclass  

---

## 🧠 Technologies
- **Language:** Python  
- **Paradigm:** Object-Oriented Programming  
- **Tools:** PyCharm / VSCode, unittest  

---

## 👩‍💻 Author
Developed by **Hadar Shir**  
B.Sc. Information Systems and Software Engineering  
Ben-Gurion University of the Negev  

---

## 📚 Notes
This project demonstrates practical application of **inheritance**, **encapsulation**, **polymorphism**, and **modular software design** in Python.
