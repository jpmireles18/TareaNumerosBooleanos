# ============================================================
# Portada
# ============================================================
# Nombre: Saul Eduardo Mireles Reyna
# Matrícula: 2630171
# Grupo: IM-3
# Tarea: Manejo de números y booleanos en Python
#
# ============================================================
# Resumen ejecutivo
# ============================================================
# En Python, int sirve para guardar numeros enteros y float para los
# que tienen decimales, como un precio o una temperatura.
# Los booleanos solo pueden ser True o False y salen, por ejemplo,
# cuando comparamos dos valores con >=, == o !=.
# Es importante revisar los datos antes de hacer las operaciones,
# porque no cualquier valor sirve para todos los calculos.
# Tambien hay que evitar dividir entre cero porque el programa marca error.
# En esta tarea se usan numeros, conversiones, comparaciones y condiciones
# para resolver seis problemas diferentes.
#
# ============================================================
# Principios y buenas practicas
# ============================================================
# - Usar int para cantidades enteras y float para cantidades con decimales.
# - Guardar resultados intermedios en variables para que se entienda mejor.
# - Revisar los datos antes de hacer las operaciones.
# - Poner nombres de variables que tengan sentido y mensajes claros.
# - True significa que se cumple una condicion y False que no se cumple.


def read_float(prompt):
    """Pide un numero y lo convierte a float."""
    return float(input(prompt).strip())


def read_int(prompt):
    """Pide un numero entero."""
    return int(input(prompt).strip())


def show_bool(value):
    """Muestra los booleanos en minusculas como pide el ejemplo."""
    return str(value).lower()


# ============================================================
# Problema 1: Temperature converter and range flag
# Descripcion:
# Convierte grados Celsius a Fahrenheit y Kelvin. Tambien revisa
# si la temperatura es alta cuando llega a 30 grados o mas.
#
# Entradas: temp_c, temperatura en Celsius.
# Salidas: Fahrenheit, Kelvin y High temperature.
# Validaciones: la entrada debe ser numerica y Kelvin no puede ser menor que 0.
# Casos de prueba:
# 1. Normal: 25 -> Fahrenheit 77.00, Kelvin 298.15, false.
# 2. Borde: -273.15 -> Kelvin 0.00, false.
# 3. Error: -300 -> Error: invalid input.
# ============================================================
def problem_1():
    try:
        temp_c = read_float("Enter temperature in Celsius: ")
        temp_k = temp_c + 273.15

        if temp_k < 0:
            print("Error: invalid input")
            return

        temp_f = temp_c * 9 / 5 + 32
        is_high_temperature = temp_c >= 30.0

        print(f"Fahrenheit: {temp_f:.2f}")
        print(f"Kelvin: {temp_k:.2f}")
        print(f"High temperature: {show_bool(is_high_temperature)}")

    except ValueError:
        print("Error: invalid input")


# ============================================================
# Problema 2: Work hours and overtime payment
# Descripcion:
# Calcula el pago de la semana. Las primeras 40 horas se pagan normal
# y las horas que pasen de 40 se pagan al 150 por ciento.
#
# Entradas: horas trabajadas y pago por hora.
# Salidas: Regular pay, Overtime pay, Total pay y Has overtime.
# Validaciones: las horas no pueden ser negativas y la tarifa debe ser mayor a 0.
# Casos de prueba:
# 1. Normal: 45 horas y tarifa 20 -> total 950.00, overtime true.
# 2. Borde: 40 horas y tarifa 20 -> total 800.00, overtime false.
# 3. Error: -1 hora -> Error: invalid input.
# ============================================================
def problem_2():
    try:
        hours_worked = read_float("Enter hours worked this week: ")
        hourly_rate = read_float("Enter hourly rate: ")

        if hours_worked < 0 or hourly_rate <= 0:
            print("Error: invalid input")
            return

        regular_hours = min(hours_worked, 40.0)
        overtime_hours = max(hours_worked - 40.0, 0.0)
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = hours_worked > 40.0

        print(f"Regular pay: {regular_pay:.2f}")
        print(f"Overtime pay: {overtime_pay:.2f}")
        print(f"Total pay: {total_pay:.2f}")
        print(f"Has overtime: {show_bool(has_overtime)}")

    except ValueError:
        print("Error: invalid input")


# ============================================================
# Problema 3: Discount eligibility with booleans
# Descripcion:
# Revisa si el cliente tiene descuento por ser estudiante, adulto mayor
# o por hacer una compra de 1000 o mas. Si aplica, se descuenta el 10%.
#
# Entradas: total de compra y respuestas YES/NO para estudiante y adulto mayor.
# Salidas: Discount eligible y Final total.
# Validaciones: compra no negativa y respuestas que sean YES o NO.
# Casos de prueba:
# 1. Normal: 500, YES, NO -> descuento true y total 450.00.
# 2. Borde: 1000, NO, NO -> descuento true y total 900.00.
# 3. Error: respuesta MAYBE -> Error: invalid input.
# ============================================================
def problem_3():
    try:
        purchase_total = read_float("Enter purchase total: ")
        student_text = input("Is the customer a student? (YES/NO): ").strip().upper()
        senior_text = input("Is the customer a senior? (YES/NO): ").strip().upper()

        if purchase_total < 0 or student_text not in ("YES", "NO") or senior_text not in ("YES", "NO"):
            print("Error: invalid input")
            return

        is_student = student_text == "YES"
        is_senior = senior_text == "YES"
        discount_eligible = is_student or is_senior or purchase_total >= 1000.0

        if discount_eligible:
            final_total = purchase_total * 0.9
        else:
            final_total = purchase_total

        print(f"Discount eligible: {show_bool(discount_eligible)}")
        print(f"Final total: {final_total:.2f}")

    except ValueError:
        print("Error: invalid input")


# ============================================================
# Problema 4: Basic statistics of three integers
# Descripcion:
# Pide tres enteros y muestra la suma, el promedio, el mayor,
# el menor y si todos son pares.
#
# Entradas: n1, n2 y n3. Se aceptan numeros negativos y cero.
# Salidas: Sum, Average, Max, Min y All even.
# Validaciones: las tres entradas deben ser numeros enteros.
# Casos de prueba:
# 1. Normal: 2, 4, 6 -> suma 12, promedio 4.00, todos pares true.
# 2. Borde: 0, -2, 2 -> suma 0, todos pares true.
# 3. Error: 2, hello, 6 -> Error: invalid input.
# ============================================================
def problem_4():
    try:
        n1 = read_int("Enter the first integer: ")
        n2 = read_int("Enter the second integer: ")
        n3 = read_int("Enter the third integer: ")

        numbers = [n1, n2, n3]
        sum_value = sum(numbers)
        average_value = sum_value / 3
        max_value = max(numbers)
        min_value = min(numbers)
        all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

        print(f"Sum: {sum_value}")
        print(f"Average: {average_value:.2f}")
        print(f"Max: {max_value}")
        print(f"Min: {min_value}")
        print(f"All even: {show_bool(all_even)}")

    except ValueError:
        print("Error: invalid input")


# ============================================================
# Problema 5: Loan eligibility (income and debt ratio)
# Descripcion:
# Calcula que parte del ingreso se va a las deudas y revisa si la persona
# cumple los requisitos para ser elegible para un prestamo.
#
# Entradas: ingreso mensual, deuda mensual y puntaje de credito.
# Salidas: Debt ratio y Eligible.
# Validaciones: ingreso mayor que 0; deuda y puntaje no negativos.
# Casos de prueba:
# 1. Normal: ingreso 10000, deuda 2000, credito 700 -> ratio 0.20, true.
# 2. Borde: ingreso 8000, deuda 3200, credito 650 -> ratio 0.40, true.
# 3. Error: ingreso 0 -> Error: invalid input.
# ============================================================
def problem_5():
    try:
        monthly_income = read_float("Enter monthly income: ")
        monthly_debt = read_float("Enter monthly debt payments: ")
        credit_score = read_int("Enter credit score: ")

        if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
            print("Error: invalid input")
            return

        debt_ratio = monthly_debt / monthly_income
        eligible = (
            monthly_income >= 8000.0
            and debt_ratio <= 0.4
            and credit_score >= 650
        )

        print(f"Debt ratio: {debt_ratio:.2f}")
        print(f"Eligible: {show_bool(eligible)}")

    except ValueError:
        print("Error: invalid input")


# ============================================================
# Problema 6: Body Mass Index (BMI) and category flag
# Descripcion:
# Saca el BMI con el peso y la estatura, y despues indica si la persona
# esta en bajo peso, peso normal o sobrepeso.
#
# Entradas: peso en kilos y estatura en metros.
# Salidas: BMI, Underweight, Normal y Overweight.
# Validaciones: peso y estatura deben ser mayores que cero.
# Casos de prueba:
# 1. Normal: 70 kg y 1.75 m -> BMI 22.86, Normal true.
# 2. Borde: 50 kg y 1.60 m -> BMI 19.53, Normal true.
# 3. Error: altura 0 -> Error: invalid input.
# ============================================================
def problem_6():
    try:
        weight_kg = read_float("Enter weight in kilograms: ")
        height_m = read_float("Enter height in meters: ")

        if weight_kg <= 0 or height_m <= 0:
            print("Error: invalid input")
            return

        bmi = weight_kg / (height_m ** 2)
        is_underweight = bmi < 18.5
        is_normal = 18.5 <= bmi < 25.0
        is_overweight = bmi >= 25.0

        print(f"BMI: {round(bmi, 2):.2f}")
        print(f"Underweight: {show_bool(is_underweight)}")
        print(f"Normal: {show_bool(is_normal)}")
        print(f"Overweight: {show_bool(is_overweight)}")

    except ValueError:
        print("Error: invalid input")


def main():
    print("Python Numbers and Booleans Assignment")
    print("1. Temperature converter and range flag")
    print("2. Work hours and overtime payment")
    print("3. Discount eligibility with booleans")
    print("4. Basic statistics of three integers")
    print("5. Loan eligibility")
    print("6. Body Mass Index (BMI)")

    choice = input("Choose a problem (1-6): ").strip()
    problems = {
        "1": problem_1,
        "2": problem_2,
        "3": problem_3,
        "4": problem_4,
        "5": problem_5,
        "6": problem_6,
    }

    if choice not in problems:
        print("Error: invalid input")
    else:
        problems[choice]()


if __name__ == "__main__":
    main()


# ============================================================
# Conclusiones
# ============================================================
# En esta tarea use int y float para trabajar con numeros enteros y decimales.
# Las comparaciones ayudan a obtener True o False segun lo que se cumpla.
# Tambien vi que con if se pueden tomar decisiones usando esas condiciones.
# Validar los datos sirve para evitar resultados que no tienen sentido.
# Revisar antes de dividir es importante para que no falle el programa.
# Los operadores and y or sirven para juntar varias condiciones.
# Esto se puede usar en cosas como pagos, descuentos y calculos de BMI.
#
# ============================================================
# Referencias
# ============================================================
# 1. Python Documentation - Numeric Types
# https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
# 2. Python Documentation - bool()
# https://docs.python.org/3/library/functions.html#bool
# 3. Python Documentation - Built-in Functions
# https://docs.python.org/3/library/functions.html
# 4. Python Documentation - Comparisons
# https://docs.python.org/3/reference/expressions.html#comparisons
# 5. Python Documentation - Errors and Exceptions
# https://docs.python.org/3/tutorial/errors.html
