# Expert System Inference Engines – Experimental Study

This repository contains the implementation and experiments for **Report 3 (Technical Report)** of the Knowledge-Based Systems course.

The goal of this project is to experimentally compare **forward chaining** and **backward chaining** inference mechanisms in a small rule-based expert system. The study is a replication-style experiment aligned with the theoretical and literature review reports.

---

## Project Overview

The implemented expert system:
- uses symbolic rules of the form  
  **IF conditions THEN conclusion**
- represents facts and conclusions as simple symbolic labels
- supports two inference strategies:
  - forward chaining (data-driven)
  - backward chaining (goal-driven)

The experiments compare the two strategies in terms of:
- number of rule evaluations
- goal resolution behavior

The system is intentionally simple and synthetic to clearly illustrate inference behavior without domain-specific complexity.

---

## Project Structure

