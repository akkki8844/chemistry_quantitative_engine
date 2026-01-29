def limiting_reactant_model(a, b, config):
    ratio_a = config["reaction"]["ratio"]["A"]
    ratio_b = config["reaction"]["ratio"]["B"]

    print("\nReaction Analysis:")

    max_product_from_a = a / ratio_a
    max_product_from_b = b / ratio_b

    product_formed = min(max_product_from_a, max_product_from_b)

    if product_formed == max_product_from_a:
        limiting = "A"
        excess = b - (product_formed * ratio_b)
    else:
        limiting = "B"
        excess = a - (product_formed * ratio_a)

    print(f"Limiting Reactant: {limiting}")
    print(f"Product Formed: {product_formed:.2f} moles")

    if excess > 0:
        print(f"Excess Reactant Remaining: {excess:.2f} moles")
    else:
        print("No excess reactant remaining")

    print("\nMathematical Explanation:")
    print("Product formation is calculated using ratios and division.")
    print("The limiting reactant is determined using the minimum value.")
    print("The reaction stops when one quantity reaches its numerical limit.")
