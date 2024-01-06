"""
Цей код містить класи та функції для управління та проведення виборів,
включаючи зберігання інформації про кандидатів та розрахунок результатів виборів
"""

class Candidate:
    """
    Представляє політичного кандидата на виборах
    """
    def __init__(self, name, votes):
        """
        Ініціалізує нового кандидата

        Аргументи:
            name (str): Ім'я кандидата
            votes (int): Кількість голосів, отриманих кандидатом
        """
        self.name = name
        self.votes = votes

    def __del__(self):
        """
        Деструктор, який повідомляє, коли екземпляр кандидата видаляється
        """
        print(f"Кандидат {self.name} Видалено.")

    def get_name(self):
        """
        Повертає ім'я кандидата

        Повертає:
            str: Ім'я кандидата
        """
        return self.name

    def get_votes(self):
        """
        Повертає кількість голосів, отриманих кандидатом

        Повертає:
            int: Кількість голосів
        """
        return self.votes

    def set_votes(self, votes):
        """
        Встановлює кількість голосів для кандидата

        Аргументи:
            votes (int): Нова кількість голосів
        """
        self.votes = votes

    def display_info(self):
        """
        Виводить інформацію про кандидата
        """
        print(f"Candidate: {self.name}, Votes: {self.votes}")


class Elections:
    """
    Управляє процесом виборів, включаючи зберігання кандидатів та розрахунок результатів
    """
    def __init__(self):
        """
        Ініціалізує об'єкт Elections з порожнім списком кандидатів
        """
        self.candidates = []

    def add_candidate(self, candidate):
        """
        Додає кандидата до виборів

        Аргументи:
            candidate (Candidate): Кандидат, якого додають
        """
        self.candidates.append(candidate)

    def calculate_total_votes(self):
        """
        Розраховує загальну кількість голосів на виборах

        Повертає:
            int: Загальна кількість голосів
        """
        return sum(candidate.get_votes() for candidate in self.candidates)

    def display_results(self):
        """
        Відображає результати виборів, включаючи кількість голосів кожного кандидата та відсоток
        """
        total_votes = self.calculate_total_votes()
        for candidate in self.candidates:
            vote_percent = (candidate.get_votes() / total_votes) * 100 if total_votes else 0
            print(f"{candidate.get_name()}"
                  f" - Голосів: {candidate.get_votes()}, "
                  f"Відсоток: {vote_percent:.2f}%")

    def find_winner(self):
        """
        Визначає переможця виборів

        Повертає:
            str: Ім'я переможця або повідомлення, якщо кандидатів немає
        """
        if not self.candidates:
            return "No candidates"
        winner = max(self.candidates, key=lambda c: c.get_votes())
        return winner.get_name()


def main():
    """
    Головна функція для запуску виборів
    """
    election = Elections()

    for _ in range(5):
        name = input("Enter candidate's name: ")
        votes = int(input(f"Enter votes for {name}: "))
        election.add_candidate(Candidate(name, votes))

    election.display_results()

    winner = election.find_winner()
    print(f"The winner is: {winner}")


"""
Виконання основної функції
"""
if __name__ == "__main__":
    main()