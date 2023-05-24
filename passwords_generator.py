import string
from itertools import product


class GeneratorDict:
    dict_args = None
    config = {
                "b": string.ascii_uppercase,
                "l": string.ascii_lowercase,
                "s": string.punctuation,
                "n": string.digits
            }

    def __init__(self):
        self.config_generator()

    def check_args(self, data):
        self.dict_args = {sym: data.count(sym) for sym in set(data)}
        for key, val in self.dict_args.items():
            if val != 1 or key not in self.config.keys():
                return False
        return True

    def available_arguments(self):
        while (args := input("Выберите аргументы:\n").lower()) != 'exit':
            try:
                assert self.check_args(args)
            except AssertionError:
                print("Available arguments: B L S N")
            else:
                return True
        return False

    def config_generator(self):
        print("Keyword generator\n"
              "\n"
              "B - большие буквы\n"
              "L - маленькие буквы\n"
              "S - спецсимволы\n"
              "N - числа\n\n")

        if self.available_arguments():
            self.number_symbols()

    def configurate_passwd(self):
        config = ''
        for arg in self.dict_args.keys():
            config += self.config[arg]
        return config

    def generate_password(self, num, config):
        data = list(map(lambda x: ''.join(x) + '\n', product(config, repeat=num)))
        print(f"Количество комбинаций: {len(data)}")
        self.save_to_file(data)

    def save_to_file(self, data):
        with open('gen_dict.txt', 'w') as file:
            file.writelines(data)

    def number_symbols(self):
        while (numbers := input("Количество символов в слове?\n")) != 'exit':
            try:
                assert int(numbers) > 0
            except (TypeError, ValueError) as e:
                print(f"Error: {e}")
            except AssertionError:
                print("Error. Значение должно быть больше 0")
            else:
                config = self.configurate_passwd()
                self.generate_password(int(numbers), config)
                print("Done!")
                break


if __name__ == '__main__':
    GeneratorDict()
