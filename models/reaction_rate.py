def reaction_rate_model(concentration, temperature, config):
    slow_threshold = config["rate_thresholds"]["slow"]
    medium_threshold = config["rate_thresholds"]["medium"]

    print("\nReaction Rate Analysis:")

    if concentration <= 0 or temperature <= 0:
        print("Reaction Rate: NONE")
        print("Reason: Concentration or temperature is zero.")
        print("A reaction cannot occur without particles or energy.")
        return

    normalized_concentration = concentration / 10
    normalized_temperature = temperature / 100

    reaction_score = (normalized_concentration + normalized_temperature) / 2

    if reaction_score < slow_threshold:
        rate = "SLOW"
    elif reaction_score < medium_threshold:
        rate = "MEDIUM"
    else:
        rate = "FAST"

    print(f"Reaction Rate: {rate}")
    print(f"Reaction Score: {reaction_score:.2f}")

    print("\nMathematical Explanation:")
    print("Inputs are scaled into comparable numerical values.")
    print("The reaction score is calculated using an average.")
    print("Thresholds classify the reaction into speed categories.")
    print("Crossing numerical boundaries transforms the reaction rate.")
