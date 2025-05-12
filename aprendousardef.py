def greet_user():
    """exibe um simples cumprimento"""
    print("Hello!")
greet_user()

def greet_user(username):
    """Exibe um cumprimento"""
    print(f"Hello, {username.title()}!")
greet_user('Junior')

def display_message():
    """exibir informação"""
    print("usar def!")
display_message()

def favorite_book(book):
    """Exibir meu livro favorito"""
    print(f"Meu livro favorito, {book.title()}!")
favorite_book('Java')

def describe_pet(animal_type, pet_name):
    """exibe as informações sobre um animal de estimação"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster' , 'Harry')