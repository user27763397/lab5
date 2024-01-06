# Клас кандидата для зберігання інформації про окремого кандидата
class Candidate:
    # Ініціалізатор для створення нового кандидата з ім'ям та кількістю голосів
    def __init__(self, name, votes):
        self.name = name
        self.votes = votes

    # Деструктор, який викликається при видаленні об'єкта кандидата
    def __del__(self):
        print(f"Candidate {self.name} is deleted from the record.")

    # Метод для отримання імені кандидата
    def get_name(self):
        return self.name

    # Метод для отримання кількості голосів кандидата
    def get_votes(self):
        return self.votes

    # Метод для встановлення кількості голосів кандидата
    def set_votes(self, votes):
        self.votes = votes

    # Метод для виведення інформації про кандидата
    def display_info(self):
        print(f"Candidate: {self.name}, Votes: {self.votes}")


# Клас для управління виборами
class Elections:
    # Ініціалізатор для створення нового об'єкта виборів
    def __init__(self):
        self.candidates = []

    # Метод для додавання кандидата до виборів
    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    # Метод для підрахунку загальної кількості голосів
    def calculate_total_votes(self):
        return sum(candidate.get_votes() for candidate in self.candidates)

    # Метод для виведення результатів виборів
    def display_results(self):
        total_votes = self.calculate_total_votes()
        for candidate in self.candidates:
            vote_percent = (candidate.get_votes() / total_votes) * 100 if total_votes else 0
            print(f"{candidate.get_name()} - Votes: {candidate.get_votes()}, Percentage: {vote_percent:.2f}%")

    # Метод для знаходження переможця виборів
    def find_winner(self):
        if not self.candidates:
            return "No candidates"
        winner = max(self.candidates, key=lambda c: c.get_votes())
        return winner.get_name()


# Основна функція для демонстрації роботи класів
def main():
    # Створення об'єкта виборів
    election = Elections()

    # Додавання кандидатів
    for _ in range(5):
        name = input("Enter candidate's name: ")
        votes = int(input(f"Enter votes for {name}: "))
        election.add_candidate(Candidate(name, votes))

    # Виведення результатів виборів
    election.display_results()

    # Знаходження та виведення переможця
    winner = election.find_winner()
    print(f"The winner is: {winner}")


# Виконання основної функції
main()
