pin = 1234
current_balance = 100000
banks = [
    "Access Bank", "Zenith Bank", "GTBank", "FCMB", "First Bank", "Fidelity Bank", "UBA",
    "Union Bank", "Polaris Bank", "Keystone Bank", "Heritage Bank", "Wema Bank",
    "Sterling Bank", "Stanbic IBTC", "Unity Bank", "Providus Bank", "Globus Bank",
    "Titan Trust Bank", "Jaiz Bank", "SunTrust Bank", "Parallex Bank"]

packages = {"yanga":        "1000",
           "family":        "2500",
           "compact":       "5000",
           "compact_plus":  "7000",
           "premium":       "10000"}


option1 = input ("1. Airtime \n2. Pay Bills \n3. Transfer \n4. Check Balance \n5. Data \n6. Loans \n\n")
if option1 == "1":
    option2 = input ("1. Self \n2. Others \n\n")
    if option2 == "1":
        amount = input ("Enter Amount: ")
        if current_balance >= int(amount):
            network_provider = input ("1. mtn \n2. airtel \n3. glo \n4. etisalat \n\n")
            if network_provider in ["1","2","3","4"]:
                correct_pin = input ("Enter correct pin: ")
                if pin == int(correct_pin):
                  print("Recharge of", int(amount), "is Successful")
                else:
                    print ("invalid pin")
            else:
                print("invalid selection")
        else:
            print("Insufficient Balance")

    elif option2 == "2":
        amount = input ("Enter Amount: ")
        if current_balance >= int(amount):
            network_provider = input ("1. mtn \n2. airtel \n3. glo \n4. etisalat \n\n")
            if network_provider in ["1","2","3","4"]:
                phone_number = input ("Enter Phone Number: ")
                if len(phone_number) == 11:
                    correct_pin = input ("Enter correct pin: ")
                    if pin == int(correct_pin):
                        print("Recharge of", int(amount), "is Successful to", phone_number)  
                    else:
                        print("invalid Pin")
                else:
                    print("invalid phone number")
            else:
                print ("invalid selection")
        else:
            print("insufficient balance")
    else:
         print("invalid selection")

if option1 == "3":
    option_3 = input ("1. gtb \n2. others \n\n")
    if option_3 == "1":
        amount = input ("Enter Amount: ")
        if current_balance >= int(amount):
            account_number = input ("Enter Account Number: ")
            if len (account_number) == 11 and account_number.isdigit():
                if account_number[:4] == "3055":     #it is assumed gtb acc starts wit 3055..
                    #if account_number.startswith("3055"):  # GTB
                        correct_pin = input ("Enter correct pin: ")
                        if pin == int(correct_pin):
                            print("Transfer of", int(amount), "is Successful to", account_number )
                        else:
                            print ("invalid pin")
                else:
                        print ("not a GTB account number")
            else:
                    print ("Invalid account number")
        else:
                print ("Insufficient funds")

    elif option_3 == "2":
        select_bank = input ("1. Access Bank \n2. Zenith Bank \n5. FCMB \n6. First Bank \n7. Fidelity Bank \n8. UBA \n9. Union Bank \n10. Polaris Bank \n11. Keystone Bank \n12. Heritage Bank \n13. Wema Bank \n14. Sterling Bank \n15. Stanbic IBTC \n16. Unity Bank \n17. Providus Bank \n18. Globus Bank \n19. Titan Trust Bank \n20. Jaiz Bank \n21. SunTrust Bank \n22. Parallex Bank \n\n")
        amount = input ("Enter Amount: ")
        if current_balance >= int(amount):
            account_number = (input ("Enter Account Number: "))
            if len (account_number) == 11:
                correct_pin = input ("Enter correct pin: ")
                if pin == int(correct_pin):
                    print("Transfer of", int(amount), "is Successful to", account_number )
                else:
                    print ("invalid pin")
            else:
                print ("Invalid account number")
        else:
            print ("Insufficient funds")
    else:
        print("invalid selection")

if option1 == "2":
    bills_payment = input ("1. DSTV \n2. Electricity \n")
    if bills_payment == "1":
        decoder_number = input ("Enter Decoder Number: ")
        if len(decoder_number) == 10:
            package_input = input("yanga \nfamily \ncompact \ncompact_plus \npremium \n\n")
            if package_input in packages:
                expected_amount = packages[package_input]
                amount = input ("Enter Amount: ")
                if amount == expected_amount:
                    correct_pin = input ("Enter correct pin: ")
                    if pin == int(correct_pin):
                        if current_balance >= int(amount):
                            print ("The", package_input, "suscription is successful")
                        else:
                            print ("insufficient funds")    
                    else:
                        print ("incorrect pin")
                else:
                    print ("invalid amount for package selection")
            else:
                print ("invalid package selection")
        else:
            print ("invalid decode number")            

    elif bills_payment == "2":
        Disco = input ("1. EKOPHC \n2. PHPHC \n3. JOSPHC \n4. IBADANPHC \n5. ABUJAPHC \n6. IKEJAPHC \n7. ABAPHC \n\n")
        if Disco in ["1","2","3","4"]:
            meter_number = input ("Enter Meter Number: ")
            if len(meter_number) == 8:
                amount = input ("Enter Amount to recharge: ")
                if current_balance >= int(amount):
                    correct_pin = input ("Enter correct pin: ")
                    if pin == int(correct_pin):                
                        unit_bought = int(amount)/50
                        print ("you have successfully bought", unit_bought, "unit worth ₦", amount)
                    else:
                        print("invalid pin")
                else:
                    print("insufficient funds")
            else:
                print("incorrect meter number")
        else:
            print("incorrect Disco")
    else:
        print("invalid selection")

