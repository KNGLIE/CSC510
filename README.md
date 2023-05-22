README
Python 3.9.7 was needed to use experta

To run this program all that is needed is to run it. 
To select different variables than what is already randomly generated you would just need to 
edit the following lines with whatever appropriate variable you would like:

engine.declare(Income(income=random.randint(0, 10000)))
engine.declare(Expenses(expenses=random.randint(0, 10000)))
engine.declare(CreditCard(credit_card_debt=random.randint(0, 10000)))
engine.declare(Savings(savings_account=random.choice(['none', 'some'])))
engine.declare(EmergencyFund(emergency_fund=random.choice([True, False])))
engine.declare(RetirementSavings(retirement_savings=random.randint(0, 10000)))

