import argparse

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    parser = argparse.ArgumentParser(
        description=" Convert temperatures between Celsius and Fahrenheit easily!"
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-c", "--celsius",
        type=float,
        help="Convert Celsius to Fahrenheit (e.g., -c 25)"
    )
    group.add_argument(
        "-f", "--fahrenheit",
        type=float,
        help="Convert Fahrenheit to Celsius (e.g., -f 98.6)"
    )

    args = parser.parse_args()

    if args.celsius is not None:
        result = celsius_to_fahrenheit(args.celsius)
        print(f"{args.celsius}°C is equal to {result:.2f}°F")
    else:
        result = fahrenheit_to_celsius(args.fahrenheit)
        print(f"{args.fahrenheit}°F is equal to {result:.2f}°C")

if __name__ == "__main__":
    main()
