# Step 1: Define conversion functions for each temperature scale

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# Step 2: Provide weather advice based on Celsius temperature
def weather_advice(celsius):
    if celsius < 0:
        return "❄️weather_advice: It's freezing! Dress warmly."
    elif celsius < 10:
        return "🧥weather_advice: It's cold. Wear layers."
    elif celsius < 20:
        return "weather_advice:🌤️ Mild weather. A light jacket should be fine."
    elif celsius < 30:
        return "weather_advice:☀️ Warm and pleasant. Stay hydrated."
    else:
        return "weather_advice:🔥 It's hot! Use sunscreen and stay cool."

# Step 3: Validate numeric input for temperature
def get_valid_temperature():
    while True:
        temp_input = input("Enter temperature value: ").strip()
        try:
            return float(temp_input)
        except ValueError:
            print("❌ Invalid input: Please enter a numeric temperature.\n")

# Step 4: Main conversion logic with user menu
def convert_temperature():
    print("=== Weather Temperature Converter ===")
    print("1. Celsius to Fahrenheit and Kelvin")
    print("2. Fahrenheit to Celsius and Kelvin")
    print("3. Kelvin to Celsius and Fahrenheit")
    print("4. Exit")

    while True:
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            c = get_valid_temperature()
            f = celsius_to_fahrenheit(c)
            k = celsius_to_kelvin(c)
            print(f"\n🌡️ {c:.2f}°C = {f:.2f}°F = {k:.2f}K")
            print(weather_advice(c), "\n")

        elif choice == '2':
            f = get_valid_temperature()
            c = fahrenheit_to_celsius(f)
            k = fahrenheit_to_kelvin(f)
            print(f"\n🌡️ {f:.2f}°F = {c:.2f}°C = {k:.2f}K")
            print(weather_advice(c), "\n")

        elif choice == '3':
            k = get_valid_temperature()
            c = kelvin_to_celsius(k)
            f = kelvin_to_fahrenheit(k)
            print(f"\n🌡️ {k:.2f}K = {c:.2f}°C = {f:.2f}°F")
            print(weather_advice(c), "\n")

        elif choice == '4':
            print("👋 Exiting the converter. Safe travels!")
            break

        else:
            print("❌ Invalid choice. Please select 1–4.\n")

# Step 5: Run the program
if __name__ == "__main__":
    convert_temperature()
