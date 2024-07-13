from requests import get
from pprint import PrettyPrinter
BASE_URL='https://api.currencyapi.com/'
API_KEY="" #input key here
printer=PrettyPrinter()


def get_currencies():
    endpoint=(f'v3/latest?apikey={API_KEY}')
    URL=BASE_URL+endpoint
    currencies=get(URL).json()['data']
    return currencies

DATA=get_currencies()

def EXCHANGE_RATES():
    currency_you_chose=input("CHOSE THE CURRENCY YOU WANT TO SEE THE EXCHANGE RATE Of: ").upper()
    value=DATA[currency_you_chose]['value']
    conversion=(value*83.430099795)
    if currency_you_chose=="INR":
        print (f"{currency_you_chose}-> INR = same man dont joke around!")
    
    elif currency_you_chose in DATA:
        print(f" 1 INR -> {currency_you_chose} = {conversion}")
    else:
        print("invalid input man try again!!")
        EXCHANGE_RATES()
        
def conversion():
    sec_currency=input("Input the CURRENCY you want to change to INR: ").upper()
    amount=int(input("Input the amount you want to convert:"))
    VALUE=DATA[sec_currency]['value']
    conversion_AMOUNT=(VALUE*83.430099795)
    final_conversion=conversion_AMOUNT*amount
    if sec_currency=="INR":
        print(f"{amount} INR-> {sec_currency} = {amount}")
    elif sec_currency in DATA:
        print(f"{amount} INR -> {sec_currency} = {final_conversion}")
    else:
        print("invalid input.. try again!!")
        conversion()
def main():
    input("WELCOME TO THE CURRENCIES CONVERTER.. ")
    print("THIS HAS SEVERAL OPTIONS \nLIST:to list see the list of currencies ")
    print("EXCHANGE: TO SEE THE EXCHANGE RATE of a specific CURRENCY TO INR")
    print("CONVERT:TO CONVERT AMOUNT TO INR ")
    
    while True:
        COMMAND=input("ENTER THE COMMAND OR PRESS Q : ").lower()
    
        if COMMAND == "list":
            printer.pprint(codes)
        elif COMMAND=="exchange":
            EXCHANGE_RATES()
        elif COMMAND=="convert":
            conversion()
        elif COMMAND=="q":
            quit()
    

codes=list(DATA)
main()

