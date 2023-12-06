from name_generator import NameGenerator

def main():
    name_generator = NameGenerator()
    for _ in range(10):
        print("Generated Name:", name_generator.generate_name())

if __name__ == "__main__":
    main()
