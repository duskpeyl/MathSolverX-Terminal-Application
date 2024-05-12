import datetime
import random

class Problem:
    stored_problems = []
    total_number_of_attempted_problems = 0
    number_of_solved_problems = 0
    
    def __init__(self, problem_id, topic, difficulty, statement, solution):
        """
        Initializes a Problem instance.

        Args:
            problem_id (int): The ID of the problem.
            topic (str): The topic of the problem.
            difficulty (str): The difficulty level of the problem.
            statement (str): The problem statement.
            solution (int or str): The correct solution to the problem.
        """
        self.problem_id = problem_id
        self.difficulty = difficulty
        self.statement = statement
        self.solution = solution
        self.datetime_solved = None
        self.topic = topic
    
    @classmethod
    def add_new_problem(cls, new_problem_given_by_system):
        """
        Adds a new problem to the list of stored problems.

        Args:
            new_problem_given_by_system (Problem): The problem to add.
        """
        cls.stored_problems.append(new_problem_given_by_system)
    
    @classmethod
    def remove_old_problem(cls):
        """
        Removes the oldest problem from the list of stored problems.
        """
        cls.stored_problems.pop(0)
    
    @classmethod
    def increase_number_of_solved_problems(cls):
        """
        Increases the number of solved problems by 1.
        """
        cls.number_of_solved_problems += 1

    @classmethod
    def increase_number_of_attempted_problems(cls):
        """
        Increases the number of attempted problems by 1.
        """
        cls.total_number_of_attempted_problems += 1


class MathLearningSystem:
    def __init__(self):
        self.skill_exp = 0
        self.level = 1
        self.solved_problems = []
    
    def fetch_problems(self):
        """Fetches math problems from math competitions"""
        problemset =  [
             {  'id': 1,
                'topic': 'Algebra',
                'difficulty': 'Easy',
                'statement': 'Solve for x: 2x + 5 = 15',
                'solution': 5
            },
            {
                'id': 2,
                'topic': 'Geometry',
                'difficulty': 'Medium',
                'statement': 'Find the area of a triangle with base 6 and height 4',
                'solution': 12
            },
            {
                'id': 3,
                'topic': 'Calculus',
                'difficulty': 'Hard',
                'statement': 'Find the derivative of f(x) = x^3 + 2x^2 - 5x + 1',
                'solution': '3x^2 + 4x - 5'
            }
        ]

        for current_item in problemset:
            item_problem_id = current_item['id']
            item_topic = current_item['topic']
            item_difficulty = current_item['difficulty']
            item_statement = current_item['statement']
            item_solution = current_item['solution']
            problem_given_by_system = Problem(problem_id=item_problem_id, topic=item_topic, difficulty=item_difficulty, statement=item_statement, solution=item_solution)

            Problem.add_new_problem(problem_given_by_system)
        
    
    def display_problem_solving_window(self):
        """Displays a math problem from the problemset for the user to solve."""
        self.fetch_problems()
        displayed_problem = random.choice(Problem.stored_problems)
        print("Problem ID: ", displayed_problem.problem_id)
        print("Topic: ", displayed_problem.topic)
        print("Difficulty: ", displayed_problem.difficulty)
        print("Statement: ", displayed_problem.statement)

        solution = int(input("Enter your solution: "))
        if solution == displayed_problem.solution:
            self.skill_exp += 10
            displayed_problem.solved = True
            displayed_problem.datetime_solved = datetime.datetime.now()
            self.solved_problems.append(displayed_problem)

            Problem.increase_number_of_solved_problems()
            Problem.increase_number_of_attempted_problems()
            print("Congratulations! You solved the problem.")
        else:
            Problem.increase_number_of_attempted_problems()
            print("Sorry, your solution is incorrect.")
    
    def display_progress_window(self):
        """Displays previously solved problems sorted by datetime or topic."""
        print("=== Progress Window ===")
        print("1. Sort by datetime (earliest solved)")
        print("2. Sort by datetime (oldest solved)")
        print("3. Sort by topic")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            sorted_problems = sorted(self.solved_problems, key=lambda x: x.datetime_solved)
        elif choice == '2':
            sorted_problems = sorted(self.solved_problems, key=lambda x: x.datetime_solved, reverse=True)
        elif choice == '3':
            topic = input("Enter the topic: ")
            sorted_problems = [problem for problem in self.solved_problems if problem.topic() == topic]
        else:
            print("Invalid choice.")
            return

        for loop in sorted_problems:
            print("Problem ID: ", loop.problem_id)
            print("Topic: ", loop.topic)
            print("Difficulty: ", loop.difficulty)
            print("Statement: ", loop.statement)
            print("Solution: ", loop.solution)
            print("Date Solved: ", loop.datetime_solved)
    
    def display_user_stats_window(self):
        """displays user stats"""
        print(f'Skill Exp: {self.skill_exp}')
        print(f'Level: {self.level}')
        print(f'Number of Solved Problems: {Problem.number_of_solved_problems}')
        print(f'Percentage of correct answers: {Problem.number_of_solved_problems / Problem.total_number_of_attempted_problems * 100}')

    def main_menu(self):
        """Displays the main menu and handles user input."""
        while True:
            print("\n== Math Learning System ==")
            print("1. Problem-Solving Window")
            print("2. Progress Window")
            print("3. User Stats Window")
            print("4. Quit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.display_problem_solving_window()
            elif choice == '2':
                self.display_progress_window()
            elif choice == '3':
                self.display_user_stats_window()
            elif choice == '4':
                break
            else:
                print("Invalid choice.")

    def run(self):
        """Runs the math learning system."""
        self.main_menu()
        print('Where would you like to go?')

learning_system = MathLearningSystem()
learning_system.run()
