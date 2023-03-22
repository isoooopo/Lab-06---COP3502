

encoded_password = ""

if __name__ == '__main__':
    flag = True
    while flag == True:


        #Menu
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")

        option = int(input("Please enter an option: "))

        if option == 1:

            #Encoder

            password = input("Please enter your password to decode: ")
            for i in password:
                if int(i) < 7:
                    encoded_password += str(int(i) + 3)
                elif int(i) >= 7:
                    encoded_password += str((int(i) +3) % 10)

            # Changing it so can't just call OG password for decode
            password = encoded_password

            print("Your password has been encoded and stored!")
            print("")
        elif option == 2:
            #Decoder
            


        elif option == 3:
            break





