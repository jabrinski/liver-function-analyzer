def calculate_liver_score(ast, alt, ggt):
    try:
        ast = float(ast)
        alt = float(alt)
        ggt = float(ggt)
        score = (ast + alt + ggt) / 3
        return round(score, 2)
    except ValueError:
        return "Invalid input: please enter numeric values only."


if __name__ == "__main__":
    print("Liver Wellness Score Calculator")
    ast_input = input("Enter AST value: ")
    alt_input = input("Enter ALT value: ")
    ggt_input = input("Enter GGT value: ")

    result = calculate_liver_score(ast_input, alt_input, ggt_input)
    print("Your liver score:", result)
