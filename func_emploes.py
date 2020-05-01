import CDB

ID_number = 100000

def gen_ID():
    global ID_number
    ID = ID_number
    ID_number += 1
    return ID

Card_number = 10000000000000000
def gen_card_ID():
    global Card_number
    CardID = Card_number
    Card_number += 1
    return CardID

def reg_client(first_name, last_name,midlle_name,phone_number,home_address,date, login, password, currency):
    new_client_registration_form = {}
    new_client_registration_form['FirstName'] = first_name
    new_client_registration_form['LastName'] = last_name
    new_client_registration_form['MidlleName'] = midlle_name
    new_client_registration_form['PhoneNumber'] = phone_number
    new_client_registration_form['HomeAddress'] = home_address
    new_client_registration_form['Date'] = date
    new_client_registration_form['Login'] = login
    new_client_registration_form['Password'] = password
    new_client_registration_form['Currency'] = currency
    new_client_registration_form['ID'] = gen_ID()
    new_client_registration_form['CardBlock'] = False
    new_client_registration_form['CardID'] = 0
    new_client_registration_form['CardPassword'] = 0
    new_client_registration_form['CreditAmount'] = 0
    new_client_registration_form['CreditPeriod'] = 0
    new_client_registration_form['Deposit'] = None
    new_client_registration_form['is3DActive'] = False
    new_client_registration_form['Balance'] = 600
    CDB.lst.append(new_client_registration_form)
    del new_client_registration_form

def card_CL(id,password):
    for dict in CDB.lst:
        for item in dict:
            if dict [item] == id:
                dict['CardID'] = gen_card_ID()
                dict['CardPassword'] = hash(password)

def account_transaction(id, reciver_id, amount):
    for dict in CDB.lst:
        for item in dict:
            if dict[item] == id:
                dict['Balance'] -= amount
    for dict in CDB.lst:
        for item in dict:
            if dict[item] == reciver_id:
                dict['Balance'] += amount

def credit_registration(id, credit_amount, credit_period):
    for dict in CDB.lst:
        for item in dict:
            if dict[item] == id:
                dict['CreditAmount'] = credit_amount
                dict['CreditPeriod'] = credit_period

def card_block (id):
    for dict in CDB.lst:
        for item in dict:
            if dict[item] == id:
                dict['CardBlock'] = True

def card_unblock (id):
    for dict in CDB.lst:
        for item in dict:
            if dict[item] == id:
                dict['CardBlock'] = False

def deposit (id, credit_amount, credit_period, possessions):
    for dict in CDB.lst:
        for item in dict:
            if dict[item] == id:
                dict['CreditAmount'] = credit_amount
                dict['CreditPeriod'] = credit_period
                dict['Deposit'] = possessions


reg_client('Ilqar','Akberov','AliMagomed','0553493484','Miami','14.4.1998','Jack','8668','USD')
print(CDB.lst)
card_block(100000)
print(CDB.lst)
