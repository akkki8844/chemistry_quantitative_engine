def failure_detector_model(a, b, config):
    ratio_a = config["reaction"]["ratio"]["A"]
    ratio_b = config["reaction"]["ratio"]["B"]

    print("\nSystem Analysis:")

    if a <= 0 or b <= 0:
        print("Reaction Status: FAILED")
        print("Reason: One or more reactants are zero.")
        print("Mathematical Explanation:")
        print("A reaction cannot proceed when a required quantity is zero.")
        return

    max_product_from_a = a / ratio_a
    max_product_from_b = b / ratio_b

    if max_product_from_a <= 0 or max_product_from_b <= 0:
        print("Reaction Status: FAILED")
        print("Reason: Insufficient reactant quantities.")
        return

    limiting_value = min(max_product_from_a, max_product_from_b)

    if limiting_value <= 0:
        print("Reaction Status: FAILED")
        print("Reason: Quantitative constraints prevent product formation.")
    else:
        print("Reaction Status: SUCCESS")
        print("Reaction can proceed normally.")

    print("\nMathematical Explanation:")
    print("The system checks boundary conditions and inequalities.")
    print("When quantities fall below required ratios, the reaction fails.")
    print("Crossing numerical limits transforms success into failure.")
