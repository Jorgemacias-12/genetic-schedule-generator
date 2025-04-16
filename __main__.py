import random as r
import numpy as np
from colorama import init, Fore, Style
from rich.console import Console
from rich.table import Table


class Program():
    NUM_OF_DAYS = 5
    NUM_OF_CLASSROOMS = 5
    NUM_OF_TEACHERS = 5
    NUM_OF_BLOCKS = 7
    NUM_OF_SUBJECTS = 5
    POPULATION_SIZE = 50
    NUM_OF_GENRATIONS = 100
    MUTATION_RATE = 0.1

    subjects = {
        1: "Matemáticas",
        2: "Historia",
        3: "Quimica",
        4: "Física",
        5: "Biología"
    }

    classrooms = {
        1: "A113",
        2: "B005",
        3: "C001",
        4: "C002",
        5: "D005"
    }

    teachers = {
        1: "Jorge",
        2: "Juan",
        3: "Elias",
        4: "Aaron",
        5: "Haidee"
    }

    def generate(self, array_of_content):
        return np.random.randint(0, self.NUM_OF_SUBJECTS + 1, size=(self.NUM_OF_BLOCKS,
                                                                    self.NUM_OF_DAYS))

    def run(self):
        init(autoreset=True)

        print(
            F"{Fore.LIGHTBLUE_EX}¡Bienvenido al generador de horarios usando algoritmos genéticos!")


if __name__ == "__main__":
    program = Program()
    program.run()
