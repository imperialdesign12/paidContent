import json

class User:
    def __init__(self, username, balance=0):
        self.username = username
        self.balance = balance

class Content:
    def __init__(self, content_id, title, price):
        self.content_id = content_id
        self.title = title
        self.price = price

class ContentService:
    def __init__(self):
        self.users = {}  # Store users
        self.contents = {}  # Store content items

    def register_user(self, username):
        if username not in self.users:
            self.users[username] = User(username)
            return True
        return False

    def create_content(self, content_id, title, price):
        if content_id not in self.contents:
            self.contents[content_id] = Content(content_id, title, price)
            return True
        return False

    def purchase_content(self, buyer_username, content_id):
        if buyer_username in self.users and content_id in self.contents:
            buyer = self.users[buyer_username]
            content = self.contents[content_id]

            return buyer, content

        return None, None

    def add_funds(self, username, amount):
        if username in self.users:
            self.users[username].balance += amount
            return True
        return False

    def get_user_balance(self, username):
        if username in self.users:
            return self.users[username].balance
        return "User not found."

# Example Usage with User Input
content_service = ContentService()

# Register users
username1 = input("Enter username for User 1: ")
content_service.register_user(username1)

username2 = input("Enter username for User 2: ")
content_service.register_user(username2)

# Create content
content_id1 = input("Enter content ID for Content 1: ")
title1 = input("Enter title for Content 1: ")
price1 = float(input("Enter price for Content 1: "))
content_service.create_content(content_id1, title1, price1)

content_id2 = input("Enter content ID for Content 2: ")
title2 = input("Enter title for Content 2: ")
price2 = float(input("Enter price for Content 2: "))
content_service.create_content(content_id2, title2, price2)

# Add funds
amount_user1 = float(input(f"Enter funds for {username1}: "))
content_service.add_funds(username1, amount_user1)

amount_user2 = float(input(f"Enter funds for {username2}: "))
content_service.add_funds(username2, amount_user2)

# Purchase content
buyer, content = content_service.purchase_content(username1, content_id1)
if buyer and content:
    if buyer.balance >= content.price:
        buyer.balance -= content.price
        print(f"Content '{content.title}' purchased successfully by {buyer.username}.")
    else:
        print(f"Insufficient balance for {buyer.username}. Please add funds to your account.")

buyer, content = content_service.purchase_content(username2, content_id2)
if buyer and content:
    if buyer.balance >= content.price:
        buyer.balance -= content.price
        print(f"Content '{content.title}' purchased successfully by {buyer.username}.")
    else:
        print(f"Insufficient balance for {buyer.username}. Please add funds to your account.")

# Get user balance
print(f"{username1} balance: {content_service.get_user_balance(username1)}")
print(f"{username2} balance: {content_service.get_user_balance(username2)}")
