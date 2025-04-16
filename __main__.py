import random as r
from rich.console import Console
from rich.table import Table
from rich.style import Style
from colorama import init, Fore

init(autoreset=True)


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
        3: "Química",
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

    hours_labels = [
        "7:00 - 8:00",
        "8:00 - 9:00",
        "9:00 - 10:00",
        "10:00 - 11:00",
        "11:00 - 12:00",
        "12:00 - 13:00",
        "13:00 - 14:00"
    ]

    def generate_fixed_teacher_assignment(self):
        subject_teacher_map = {}
        teacher_ids = list(self.teachers.keys())

        r.shuffle(teacher_ids)

        for i, subject_id in enumerate(self.subjects.keys()):
            subject_teacher_map[subject_id] = teacher_ids[i % len(teacher_ids)]

        return subject_teacher_map

    def generate_schedule(self, subject_teacher_map):
        return [[
            (sid := r.randint(1, self.NUM_OF_SUBJECTS),
             subject_teacher_map[sid],
             r.randint(1, self.NUM_OF_CLASSROOMS))
            for _ in range(self.NUM_OF_DAYS)
        ] for _ in range(self.NUM_OF_BLOCKS)]

    def calculate_fitness(self, schedule):
        score = 0
        teacher_schedule = set()
        classroom_schedule = set()

        for block in range(self.NUM_OF_BLOCKS):
            for day in range(self.NUM_OF_DAYS):
                entry = schedule[block][day]
                if entry:
                    _, teacher_id, classroom_id = entry

                    if (teacher_id, day, block) in teacher_schedule:
                        score -= 10
                    else:
                        teacher_schedule.add((teacher_id, day, block))

                    if (classroom_id, day, block) in classroom_schedule:
                        score -= 10
                    else:
                        classroom_schedule.add((classroom_id, day, block))

        return score

    def crossover(self, parent1, parent2):
        block_split = r.randint(1, self.NUM_OF_BLOCKS - 1)
        return [
            parent2[b] if b < block_split else parent1[b]
            for b in range(self.NUM_OF_BLOCKS)
        ]

    def mutate(self, schedule, subject_teacher_map):
        for _ in range(r.randint(1, 3)):
            if r.random() < self.MUTATION_RATE:
                block = r.randint(0, self.NUM_OF_BLOCKS - 1)
                day = r.randint(0, self.NUM_OF_DAYS - 1)
                sid = r.randint(1, self.NUM_OF_SUBJECTS)
                schedule[block][day] = (
                    sid,
                    subject_teacher_map[sid],
                    r.randint(1, self.NUM_OF_CLASSROOMS)
                )
        return schedule

    def print_schedule(self, schedule):
        console = Console()
        table = Table(
            title="[bold yellow]Horario Generado[/]",
            title_style=Style(color="yellow", bold=True),
            header_style=Style(color="cyan", bold=True)
        )

        table.add_column("[cyan]Hora/Día[/]", justify="center")
        for d in range(self.NUM_OF_DAYS):
            table.add_column(f"[green]Día {d+1}[/]", justify="center")

        for b in range(self.NUM_OF_BLOCKS):
            row = [f"[magenta]{self.hours_labels[b]}[/]"]
            for d in range(self.NUM_OF_DAYS):
                entry = schedule[b][d]
                if entry:
                    s, t, c = entry
                    row.append(
                        f"[blue]{self.subjects[s]}[/]\n"
                        f"[red]{self.teachers[t]}[/]\n"
                        f"[green]{self.classrooms[c]}[/]"
                    )
                else:
                    row.append("[grey50]---[/]")
            table.add_row(*row)
            table.add_row(*[""] * (self.NUM_OF_DAYS + 1))

        console.print(table)

    def run(self):
        print(f"{Fore.LIGHTBLUE_EX}¡Bienvenido al generador de horarios!\n")
        subject_teacher_map = self.generate_fixed_teacher_assignment()
        schedule = self.generate_schedule(subject_teacher_map)
        self.print_schedule(schedule)


if __name__ == "__main__":
    program = Program()
    program.run()
