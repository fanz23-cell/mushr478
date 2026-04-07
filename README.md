# MuSHR478: Autonomous Driving on the MuSHR Platform



https://github.com/user-attachments/assets/38d2eee8-ae72-4e07-97a7-ace7e0d90ed2



This repository contains my coursework and final system integration for **UW CSE 478: Introduction to Autonomous Robots (Winter 2026)** on the **MuSHR** platform. The project follows a full **sense-plan-act** pipeline for an Ackermann-steered robot car, covering:

- ROS and MuSHR environment setup
- Localization with particle filtering
- Path tracking control
- Sampling-based motion planning
- Final multi-goal autonomous navigation

---

## Overview

The goal of this repository is to build a complete autonomous navigation stack for a MuSHR car in ROS.  
Across the quarter, the system was developed incrementally through five stages:

1. **Introduction**  
   Learned the MuSHR platform, ROS workflows, publishers/subscribers, launch files, and efficient NumPy-based computation.

2. **Localization**  
   Implemented a particle filter with motion model, sensor model, and resampling for online state estimation.

3. **Control**  
   Built path tracking controllers including PID, Pure Pursuit, and MPC for Ackermann vehicle control.

4. **Planning**  
   Implemented sampling-based planning components including Halton sampling, roadmap construction, Lazy A*, and path shortcutting.

5. **Final Project**  
   Integrated localization, planning, and control into a full multi-goal autonomous driving system in a new environment.

---

## Repository Structure

```text
mushr478/
├── introduction/    # ROS + NumPy warmup, basic MuSHR exercises
├── localization/    # Particle filter localization
├── control/         # PID / Pure Pursuit / MPC controllers
├── planning/        # PRM-style roadmap, Lazy A*, shortcutting
├── final/           # Final integrated multi-goal navigation setup
├── cse478/          # Course-related support files
└── README.md
