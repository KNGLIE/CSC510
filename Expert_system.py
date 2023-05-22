from experta import *
import random

class Income(Fact):
   '''Income, Expenses, credit card debt, savings account, retirement savings
   '''
   income = Field(int, mandatory=True)
class Expenses(Fact):
   expenses = Field(int, mandatory=True)

class CreditCard(Fact):
   credit_card_debt = Field(int, mandatory=True)

class Savings(Fact):
   savings_account = Field(str, mandatory=True)

class EmergencyFund(Fact):
   emergency_fund = Field(bool, mandatory=True)

class RetirementSavings(Fact):
   retirement_savings = Field(int, mandatory=True)


class FinancialAdvice(KnowledgeEngine):   
    @Rule(Expenses(expenses=MATCH.expenses))   
    def expenses_rule(self, expenses):       
        if expenses > 0:           
            print("You should try to reduce your expenses.")       
        else:           
            print("You are doing a great job managing your expenses.")   
    @Rule(Income(income=MATCH.income))  
    def income_rule(self, income):       
        if income > 0:           
            print("You should try to increase your income.")       
        else:           
            print("You are doing a great job managing your income.")   
    @Rule(CreditCard(credit_card_debt=MATCH.credit_card_debt))   
    def credit_card_rule(self, credit_card_debt):      
        if credit_card_debt > 0:           
            print("You should try to pay off your credit card debt.")       
        else:           
            print("You are doing a great job managing your credit card debt.")   
            
    @Rule(Savings(savings_account=MATCH.savings_account))   
    def savings_rule(self, savings_account):       
        if savings_account == "none":           
            print("You should try to open a savings account.")       
        else:           
            print("You are doing a great job managing your savings account.")   
    @Rule(EmergencyFund(emergency_fund=MATCH.emergency_fund))   
    def emergency_fund_rule(self, emergency_fund):       
        if emergency_fund == False:           
            print("You should try to build an emergency fund.")       
        else:           
            print("You are doing a great job managing your emergency fund.")   
    @Rule(RetirementSavings(retirement_savings=MATCH.retirement_savings))   
    def retirement_savings_rule(self, retirement_savings):       
        if retirement_savings == 0:           
            print("You should try to increase your retirement savings.")       
        else:           
            print("You are doing a great job managing your retirement savings.")




engine = FinancialAdvice()
engine.reset()
engine.declare(Income(income=random.randint(0, 10000)))
engine.declare(Expenses(expenses=random.randint(0, 10000)))
engine.declare(CreditCard(credit_card_debt=random.randint(0, 10000)))
engine.declare(Savings(savings_account=random.choice(['none', 'some'])))
engine.declare(EmergencyFund(emergency_fund=random.choice([True, False])))
engine.declare(RetirementSavings(retirement_savings=random.randint(0, 10000)))
engine.run()
