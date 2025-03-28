def syntheticDivisionSolver(numberOfCoefficients, xValue):
    previousValue = int(input("coefficient 1: "))
    answerList = [previousValue]

    for nth in range(numberOfCoefficients - 1):
        nthcoefficient = int(input(f"coefficient {nth + 2}: ")) # the f allows the stuff inside braces to be calculated as if they where functions
        previousValue = nthcoefficient + (previousValue * xValue)
        answerList.append(previousValue)

    print(f"Synthetic Division Results: {answerList}")

# Run the function
syntheticDivisionSolver(int(input("Number of Coefficients: ")), int(input("Value of X: ")))