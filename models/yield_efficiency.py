def yield_efficiency_model(theoretical_yield, efficiency):
    print("\nYield Analysis:")

    if theoretical_yield <= 0 or efficiency <= 0:
        print("Actual Yield: 0")
        print("Reason: Invalid theoretical yield or efficiency.")
        print("Quantities must be positive for production to occur.")
        return

    if efficiency > 100:
        efficiency = 100

    actual_yield = theoretical_yield * (efficiency / 100)
    loss = theoretical_yield - actual_yield

    print(f"Theoretical Yield: {theoretical_yield:.2f}")
    print(f"Efficiency: {efficiency:.2f}%")
    print(f"Actual Yield: {actual_yield:.2f}")
    print(f"Yield Loss: {loss:.2f}")

    print("\nMathematical Explanation:")
    print("Efficiency is treated as a percentage of the total.")
    print("Actual yield is calculated using multiplication.")
    print("Loss is determined using subtraction.")
    print("Small percentage changes cause large outcome differences.")
