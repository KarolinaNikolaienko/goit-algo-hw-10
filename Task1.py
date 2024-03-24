import pulp

def main():
    model = pulp.LpProblem("Max_Amount", pulp.LpMaximize)
    x1 = pulp.LpVariable('x1', lowBound=0, cat='Integer') # лимонад
    x2 = pulp.LpVariable('x2', lowBound=0, cat='Integer') # фруктовий сік
    model += x1 + x2, "Problem"

    model += 2*x1 + x2 <= 100, "Constraint_Water"
    model += x1 <= 50, "Constraint_Sugar"
    model += x1 <= 30, "Constraint_Juice"
    model += 2*x2 <= 40, "Constraint_Fruit_Puree"

    model.solve()
    pulp.LpStatus[model.status]

    for variable in model.variables():
        print(f"{variable.name} = {variable.varValue}")

    # Вартість цільової функції
    print(f"Total cost = {pulp.value(model.objective)}")


if __name__ == "__main__":
    main()