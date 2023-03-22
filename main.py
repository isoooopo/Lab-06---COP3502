

encoded_password = ""

if __name__ == '__main__':
    flag = True
    while flag == True:

        #Encoder

        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")

        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to decode: ")
            for i in password:
                if int(i) < 7:
                    encoded_password += str(int(i) + 3)
                elif int(i) >= 7:
                    encoded_password += str((int(i) +3) % 10)

            print("Your password has been encoded and stored!")
            print("")
        elif option == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {password}.")
            print("")
        elif option == 3:
            break





