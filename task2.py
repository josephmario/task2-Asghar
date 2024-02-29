class User:
    def __init__(self, username):
        self.username = username
        self.balance = 0

    def mp(self, amount):
        self.balance += amount

    def rp(self, amount, payer):
        self.balance += amount
        payer.balance -= amount


def main():
    num_type_mp = int(input("Enter user 1 make payment: "))
    num_type_rp = int(input("Enter user 2 received payment: "))
    num_type_rp_two = int(input("Enter user 3 received payment: "))
    u1 = User("User1")
    u2 = User("User2")
    u3 = User("User3")

    u1.mp(num_type_mp)

    u2.rp(num_type_rp, u1)
    u3.rp(num_type_rp_two, u1)

    total_received = u2.balance + u3.balance
    
    total = num_type_mp - total_received

    if(total > 1):
        print('You Have balance amount {} from user1'.format(total))
    else:
        print('Paid Thank you')

if __name__ == "__main__":
    main()
