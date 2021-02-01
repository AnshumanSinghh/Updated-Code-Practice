def generate_otp(order_id):
    otp = 1
    for x in order_Id:
        otp *= int(x)
    return otp

# Driver Code Starts
if __name__ == "__main__":
    order_Id = input("Enter the OrderId: ")
    print(generate_otp(order_Id))
