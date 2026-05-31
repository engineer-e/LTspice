<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>

<script>
document.getElementById("content").innerHTML =
  marked.parse(markdownText);
</script>


# Electronic Devices and Circuit Theory


> 11th Edition ,Author of Electronics Devices and Circuit theory book are Robert L.Boylestad, Louis Nashelsky 

# Content

1. Semiconductor Diodes
   1. [Introduction](https://engineer-e.github.io/LTspice/electronic%20devices%20and%20circuit%20theory/edct/Semiconductor%20Diodes/Introduction/page.html)
   2. [Semiconductor Materials: Ge, Si, and GaAs](https://engineer-e.github.io/LTspice/electronic%20devices%20and%20circuit%20theory/edct/Semiconductor%20Diodes/Semiconductor%20Materials%20Ge,%20Si,%20and%20GaAs/page.html)
   3. [Covalent Bonding and Intrinsic Materials](https://engineer-e.github.io/LTspice/electronic%20devices%20and%20circuit%20theory/edct/Semiconductor%20Diodes/Covalent%20Bonding%20and%20Intrinsic%20Materials/page.html)
   4. [Energy Levels](https://engineer-e.github.io/LTspice/electronic%20devices%20and%20circuit%20theory/edct/Semiconductor%20Diodes/Energy%20Levels/page.html)
   5. [n-Type and p-Type Materials](https://engineer-e.github.io/LTspice/electronic%20devices%20and%20circuit%20theory/edct/Semiconductor%20Diodes/n-Type%20and%20p-Type%20Materials/page.html)
   6. [Semiconductor Diode](https://engineer-e.github.io/LTspice/electronic%20devices%20and%20circuit%20theory/edct/Semiconductor%20Diodes/Semiconductor%20Diode/page.html)
   7. [Ideal Versus Practical](https://engineer-e.github.io/LTspice/electronic%20devices%20and%20circuit%20theory/edct/Semiconductor%20Diodes/Ideal%20Versus%20Practical/page.html)
   8. [Resistance Levels](https://engineer-e.github.io/LTspice/electronic%20devices%20and%20circuit%20theory/edct/Semiconductor%20Diodes/Resistance%20Levels/page.html)     
   9. Diode Equivalent Circuits
   10. Transition and Diffusion Capacitance
   11. Reverse Recovery Time
   12. Diode Specification Sheet
   13. Semiconductor Diode Notation
   14. Diode Testing
   15. Zener Diodes
   16. Light-Emitting Diodes
   17. Summary
   18. Computer Analysis
2. Diode Applications
   1. Introducton
   2. Load-Line Analysis
   3. Series Diode Configurations
   4. Parallel and Series-Parallel Configurations
   5. AND/OR Gates
   6. Sinusoidal Inputs - Halfwave Rectification
   7. Full-Wave Rectification
   8. Clippers
   9. Clampers
   10. Networks with a dc and ac source
   11. Zener Diodes
   12. Voltage-Multiplier Circuits
   13. Practical Applications
   14. Summary
   15. Computer Analysis 
3. Bipolar Junction Transistors
   1. Introduction
   2. Transistor Construction
   3. Transistor Operation
   4. Common-Base Configuration
   5. Common-Emitter Configuration
   6. Common-Collector Configuration
   7. Limits of Operation
   8. Transistor Specification Sheet
   9. Transistor Testing
   10. Transistor Casing and Terminal Identification
   11. Transistor Development
   12. Summary
   13. Computer Analysis 
4. DC Biasing - BJTs
   1. Introduction
   2. Operating Point
   3. Fixed-Bias Configuration
   4. Emitter-Bias Configuration
   5. Voltage-Divider Bias Configuration
   6. Collector Feedback Configuration
   7. Emitter-Follower Configuration
   8. Common-Base Configuration
   9. Miscellaneous Bias Configurations
   10. Summary Table
   11. Design Operations
   12. Multiple BJT Networks
   13. Current Mirrors
   14. Current Source Circuits
   15. pnp Transistors
   16. Transistor Switching Networks
   17. Troubleshooting Techniques
   18. Bias Stabilization
   19. Practical Applications
   20. Summary
   21. Computer Analysis
5. BJT AC Analysis
   1. Introduction
   2. Amplification in the AC Domain
   3. BJT Transistor Modeling
   4. The $r_e$ Transistor Model
   5. Common-Emitter Fixed-Bias Configuration
   6. Voltage-Divider Bias
   7. CE Emitter-Bias Configuration
   8. Emitter-Follower Configuration
   9. Common-Base Configuration
   10. Collector Feedback Configuration
   11. Collector DC Feedback Configuration
   12. Effect of $R_L$ and $R_s$
   13. Determining the Current Gain
   14. Summary Tables
   15. Two-Port Systems Approach
   16. Cascaded Systems
   17. Darlington Connection
   18. Feedback Pair
   19. The Hybrid Equivalent Model
   20. Approximate Hybrid Equivalent Circuit
   21. Complete Hybrid Equivalent Model
   22. Hybrid $pi$ Model
   23. Variations of Transistor Parameters
   24. Troubleshooting
   25. Practical Applications
   26. Summary
   27. Computer Analysis
6. Field-Effect Transistors
   1. Introduction
   2. Construction and Characteristics of JFETs
   3. Transfer Characteristics
   4. Specification Sheets (JFETs)
   5. Instrumentation
   6. Important Relationships
   7. Depletion-Type MOSFET
   8. Enhancement-Type MOSFET
   9. MOSFET Handling
   10. VMOS and UMOS Power and MOSFETs
   11. CMOS
   12. MESFETs
   13. Summary Table
   14. Summary
   15. Computer Analysis
7. FET Biasing
   1. Introduction
   2. Fixed-Bias Configuration
   3. Self-Bias Configuration
   4. Voltage-Divider Biasing
   5. Common-Gate Configuration
   6. Special Case $V_GS_Q$ = 0 V
   7. Depletion-Type MOSFETs
   8. Enhancement-Type MOSFETs
   9. Summary Table
   10. Combination Networks
   11. Design
   12. Troubleshooting
   13. p-Channel FETs
   14. Universal JFET Bias Curve
   15. Practical Applications
   16. Summary
   17. Computer Analysis
8. FET Amplifiers
   1. Introduction
   2. JFET Small-Signal Model
   3. Fixed-Bias Configuration
   4. Self-Bias Configuration
   5. Voltage-Divider Configuration
   6. Common-Gate Configuration
   7. Source-Follower (Common-Drain) Configuration
   8. Depletion-Type MOSFETs
   9. Enhancement-Type MOSFETs
   10. E-MOSFET Drain-Feedback Configuration
   11. E-MOSFET Voltage-Divider Configuration
   12. Designing FET Amplifier Networks
   13. Summary Table
   14. Effect of $R_L$ and $R_\sigma$
   15. Cascade Configuration
   16. Troubleshooting
   17. Practical Applications
   18. Summary
   19. Computer Analysis
9. BJT and JFET Frequency Response
   1. Introduction
   2. Logarithms
   3. Decibels
   4. General Frequency Considerations
   5. Normalization Process
   6. Low-Frequency Analysis-Blot Plot
   7. Low-Frequency Response-BJT Amplifier with $R_L$
   8. Impact of $R_s$ on the BJT Low-Frequency Response 
   9. Low-Frequency Response - FET Amplifier
   10. Miller Effect Capacitance
   11. High Frequency Response-BJT Amplifier
   12. High Frequency Response-FET Amplifier
   13. Multistage Frequency Effects
   14. Square-Wave Testing
   15. Summary
   16. Computer Analysis
10. Operational Amplifiers
    1. Introduction
    2. Differential Amplifier Circuit
    3. BiFET, BiMOS, and CMOS Differential Amplifier Circuits
    4. Op-Amp Basics
    5. Practical Op-Amp Circuits
    6. Op-Amp Specifications - DC Offset Parameters
    7. Op-Amp Specifications - Frequency Parameters
    8. Op-Amp Unit Specifications
    9. Differential and Common-Mode Operation
    10. Summary 
    11. Computer Analysis
11. Op-Amp Applications
    1. Constant-Gain Multiplier
    2. Voltage Summing
    3. Voltage Buffer
    4. Controlled Sources
    5. Instrumentation Circuits
    6. Active Filters
    7. Summary
    8. Computer Analysis
12. Power Amplifiers
    1. Introduction-Definitions and Amplifier Types
    2. Series-Fed Class A Amplifier
    3. Transformer-Coupled Class A Amplifier
    4. Class B Amplifier Operation
    5. Class B Amplifier Circuits
    6. Amplifier Distortion
    7. Power Transistor Heat Sinking
    8. Class C and Class D Amplifiers
    9. Summary
    10. Computer Analysis
13. Linear-Digital ICs
    1. Introduction
    2. Comparator Unit Operation
    3. Digital-Analog Converters
    4. Timer IC Unit Operations
    5. Voltage-Controlled Oscillator
    6. Phase-Locked Loop
    7. Interfacing Circuitry
    8. Summary 
    9. Computer Analysis
14. Feedback and Oscillator Circuits
    1. Feedback Concepts
    2. Feedback Connection Types
    3. Practical Feedback Circuits
    4. Feedback Amplifier - Phase and Frequency Considerations
    5. Oscillator Operation
    6. Phase-Shift Oscillator
    7. Wien Bridge Osicllator
    8. Tuned Oscillator Circuit
    9. Crystal Oscillator
    10. Unijunction Oscillator
    11. Summary
    12. Computer Analysis
15. Power Supplies (Voltage Regulators)
    1. Introduction
    2. General Filter Considerations
    3. Capacitor Filter
    4. RC Filter
    5. Discrete Transistor Voltage Regulation
    6. IC Voltage Regulators
    7. Practical Applications
    8. Summary
    9. Computer Analysis
16. Other Two-Terminal Devices
    1. Introduction
    2. Schottky Barrier (Hot-Carrier) Diodes
    3. Varactor (Varicap) Diodes
    4. Solar Cells
    5. Photodiodes
    6. Photoconductive Cells
    7. IR Emitters
    8. Liquid-Crystal Displays
    9. Thermistors
    10. Tunnel Diodes
    11. Summary
17. pnpn and Other Devices
    1. Introduction
    2. Silicon-Controlled Rectifier
    3. Basic Silicon-Controlled Rectifier Operation
    4. SCR Characteristics and Ratings
    5. SCR Applications
    6. Silicon-Controlled Switch
    7. Gate Turn-Off Switch
    8. Light-Activated SCR
    9. Shockley Diode
    10. Diac
    11. Triac
    12. Unijunction Transistor
    13. Phototransistors
    14. Opto-Isolators
    15. Programmable Unijunction Transistor
    16. Summary

A. Hybrid Parameters
   1. Graphical Determination of the h-Parameter
   2. Exact Conversion Equations
   3. Approximate Conversion Equations

B. Ripple Factor and Voltage Calculations
   1. Ripple Factor of Rectifier
   2. Ripple Voltage of Capacitor Filter
   3. Relation of $V_{dc}$ and $V_{m}$ to Ripple r
   4. Relation of $V_{r}$ and $V_{m}$ to Ripple r
   5. Relation Connecting Conduction Angle, Percentage Ripple, and $I_{peak}$/$I_{dc}$ for rectifier-capacitor filter circuits

C. Charts and Table

D. Solutions to Selected Odd-Numbered Problems