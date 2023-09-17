
def generate_random_data():
    import random
    import string

    data = []
    for _ in range(10):
        random_string = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        random_number = random.randint(1, 100)
        data.append((random_string, random_number))

    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: {random_string}")
        print(f"Random Number: {random_number}")

if __name__ == "__main__":
    main()
