import sys
import art

from rich.traceback import install
from rich.prompt import Prompt
from rich.console import Console
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format


init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
install()
console = Console()
prompt = Prompt()


def invalid_input():
    console.print("Please enter valid value!", style="red")


def calculate_mortgage_payoff(
    balance, annual_interest_rate, monthly_payment, extra_payment=0
):
    """Calculate early mortgage payoff, printing monthly balance."""
    # Convert annual rate to monthly decimal
    monthly_interest_rate = annual_interest_rate / 12 / 100

    months = 0
    while balance > 0:
        months += 1

        # Calculate interest for the month
        interest_payment = balance * monthly_interest_rate

        # Total payment for the month
        total_payment = monthly_payment + extra_payment

        # Apply the payment to the balance
        balance = balance + interest_payment - total_payment
        if balance > 0:
            console.print(f"{months} - ${balance:.2f}")

        # Ensure balance doesn't go negative
        if balance < 0:
            balance = 0
            console.print(f"{months} - ${balance:.2f}")

    years = months // 12
    remaining_months = months % 12

    return years, remaining_months


def main():
    # Example usage:
    cprint(
        figlet_format("Early Mortgage Payoff Calulator"),
        "yellow",
        "on_black",
        attrs=["bold"],
    )

    cb = True
    while cb:
        try:
            current_balance = float(prompt.ask("Enter your current balance"))
            cb = False
        except Exception as e:
            invalid_input()

    air = True
    while air:
        try:
            annual_interest_rate = float(
                prompt.ask("Enter your annual interest rate")
            )  # Annual interest rate (as a percentage)
            air = False
        except Exception as e:
            invalid_input()

    mp = True
    while mp:
        try:
            monthly_payment = float(
                prompt.ask("Enter your monthly mortgage payment")
            )  # Regular monthly payment
            mp = False
        except Exception as e:
            invalid_input()

    ep = True
    while ep:
        try:
            extra_payment = float(prompt.ask("Enter extra payment"))
            ep = False
        except Exception as e:
            invalid_input()

    print("\n")

    years, remaining_months = calculate_mortgage_payoff(
        current_balance, annual_interest_rate, monthly_payment, extra_payment
    )

    console.print(
        f"Your current balance is ${current_balance:.2f}.  At an annual"
        f" interest rate of {annual_interest_rate}%, a monthly payment of"
        f" ${monthly_payment:.2f} and with an extra payment of"
        f" ${extra_payment:.2f} it will take {years} years and"
        f" {remaining_months} months to pay off the mortgage."
    )


if __name__ == "__main__":
    main()
