registered = input()
fee_paid = input()
identity_verified = input()
system_check = input()
# Check whether the student can access t
    if registered == "Yes":
        if fee_paid == "Yes" and identity_verified == "yes":
            if system_check == "pass":
                print("Access Granted")
            else:
                print("Access Denied: System Check Failed")
        else:
            print("Access Denied: Verification pending")
    else:
        print("Access Denied: Registration Incomplete")