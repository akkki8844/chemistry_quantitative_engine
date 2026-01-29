import yaml
from models.limiting_reactant import limiting_reactant_model
from models.reaction_rate import reaction_rate_model
from models.yield_efficiency import yield_efficiency_model
from models.failure_detector import failure_detector_model


def load_config():
    """
    Loads numerical parameters from YAML.
    This separates data (numbers) from logic (math),
    which is a core mathematical modeling principle.
    """
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)


def display_menu():
    print("\n" + "=" * 45)
    print("  QUANTITATIVE TRANSFORMATION ENGINE")
    print("=" * 45)
    print("1. Limiting Reactant Predictor")
    print("2. Reaction Rate Classifier")
    print("3. Yield Efficiency Predictor")
    print("4. Chemical System Failure Detector")
    print("5. Exit")
    print("=" * 45)


def main():
    config = load_config()

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice (1–5): "))
        except ValueError:
            print("\n Invalid input. Pls enter a number.\n")
            continue

        if choice == 1:
            print("\n--- Limiting Reactant Predictor ---")
            a = float(input("Enter moles of Reactant A: "))
            b = float(input("Enter moles of Reactant B: "))

            limiting_reactant_model(a, b, config)

        elif choice == 2:
            print("\n--- Reaction Rate Classifier ---")
            concentration = float(input("Enter concentration (mol/L): "))
            temperature = float(input("Enter temperature (°C): "))

            reaction_rate_model(concentration, temperature, config)

        elif choice == 3:
            print("\n--- Yield Efficiency Predictor ---")
            theoretical = float(input("Enter theoretical yield (grams): "))
            efficiency = float(input("Enter efficiency percentage (%): "))

            yield_efficiency_model(theoretical, efficiency)

        elif choice == 4:
            print("\n--- Chemical System Failure Detector ---")
            a = float(input("Enter moles of Reactant A: "))
            b = float(input("Enter moles of Reactant B: "))

            failure_detector_model(a, b, config)

        elif choice == 5:
            print("\nExiting program.")
            print("Quantitative relationships determine outcomes.\n")
            break

        else:
            print("\n Invalid choice. Select 1-5 pls ty.\n")


if __name__ == "__main__":
    main()
