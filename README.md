Quantitative Transformation Engine

This project is a terminal-based AI system that demonstrates how quantitative relationships control chemical transformation. Inspired by core chemistry concepts like limiting reactants, reaction rates, and yield, the program uses mathematical rules to predict outcomes. It proves that in chemistry, transformations occur due to numbers, ratios, and limits — not intention.

How the Project Works

The program runs as a menu-driven system in the terminal. When started, it displays multiple chemistry models (similar to tools like SET on Kali Linux).
Each model asks the user for numerical inputs (such as moles, concentration, or efficiency) and then applies mathematical logic to determine the outcome.

All constants and ratios are stored in a YAML configuration file, while Python handles the calculations and decision-making. This separation mirrors real mathematical modeling and makes the system flexible and transparent.

Features / Models Included

Limiting Reactant Predictor
Determines which reactant limits the reaction using ratios and minimum values.

Reaction Rate Classifier
Classifies reactions as slow, medium, or fast based on numerical thresholds.

Yield Efficiency Predictor
Calculates actual yield from theoretical yield and efficiency percentage.

Chemical System Failure Detector
Detects whether a reaction can proceed or fails due to numerical constraints.

How to Run the Program
Step 1: Requirements

Python 3 installed

pyyaml installed

Install PyYAML if needed:

pip install pyyaml

Step 2: Folder Structure

Ensure your project folder looks like this:

quantitative_engine/
├── main.py
├── config.yaml
├── models/
│   ├── limiting_reactant.py
│   ├── reaction_rate.py
│   ├── yield_efficiency.py
│   └── failure_detector.py

Step 3: Run the Program

Navigate to the project folder and run:

python main.py

Step 4: Use the Menu

Choose an option (1–4)

Enter the requested numerical values

View the predicted outcome and explanation

Repeat with different values to observe transformation

Why This Project Matters

This system demonstrates that chemical reactions are controlled by mathematical limits, ratios, and thresholds. By changing quantities, the outcome transforms completely — directly proving the conceptual statement:
quantitative relationships shape transformation.