# Reaction Wheel Attitude Control

## Overview

This project presents the design and simulation of a reaction wheel based spacecraft attitude control system using a PD controller.

The controller gains were obtained through analytical modelling and Levenberg-Marquardt optimization. Since the desired overshoot specification could not be achieved for large-angle maneuvers using a single command, a step maneuver strategy was implemented in Simulink.

## Features

- Spacecraft attitude dynamics modelling
- PD controller design
- Levenberg-Marquardt based gain tuning
- Step maneuver strategy for large-angle rotations
- MATLAB/Simulink implementation and validation

## Files

- `Satellite.slx` – Simulink model
- `Satellite_Attitude_Control_Report.pdf` – Project report
- `Step_Maneuver_Simulink_Model.png` – Simulink implementation screenshot

## Software Used

- MATLAB
- Simulink
- Overleaf (LaTeX)

## Author

Srujana Patil
