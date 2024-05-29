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
            problem_id (int): The ID of the math problem.
            topic (str): The topic of the math problem.
            difficulty (str): The difficulty level of the math problem.
            statement (str): The problem statement of the math problem.
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
    def increase_number_of_solved_problems(cls):
        """
        Increases the number of solved problems by 1.
        """
        cls.number_of_solved_problems += 1
        Problem.increase_number_of_attempted_problems()

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
        self.custom_profile_description = ''
    
    def customize_profile_description(self):
        print('What would you like to change your profile description to?')
        self.custom_profile_description = input()

    def fetch_problems(self):
        """Fetches math problems from math competitions from a list of problems."""
        problemset =  [
             {  'id': 1,
                'topic': 'Addition',
                'difficulty': 'Easy',
                'statement': 'What is the ones digit of: 222,222 - 22,222 - 2,222 - 222 - 22 - 2?',
                'solution': '2'
            },
            {
                'id': 2,
                'topic': 'Fractions',
                'difficulty': 'Medium',
                'statement': 'What is this expression in decimal form? 44/11 + 110/44 + 44/1100',
                'solution': '6.54'
            },
            {
                'id': 3,
                'topic': 'Word Problem',
                'difficulty': 'Hard',
                'statement': 'A roll of tape is 4 inches in diameter and is wrapped around a ring that is 2 inches in diameter. A cross section of the tape is shown in the figure below. The tape is 0.015 inches thick. If the tape is completely unrolled, approximately how long would it be? Round your answer to the nearest 100 inches.',
                'solution': '600'
            },
            {
                'id': 4,
                'topic': 'Word Problem',
                'difficulty': 'Hard',
                'statement': 'Every morning Aya goes for a 9-kilometer-long walk and stops at a coffee shop afterwards. When she walks at a constant speed of s kilometers per hour, the walk takes her 4 hours, including t minutes spent in the coffee shop. When she walks s+2 kilometers per hour, the walk takes her 2 hours and 24 minutes, including t minutes spent in the coffee shop. Suppose Aya walks at s + 1/2 kilometers per hour. Find the number of minutes the walk takes her, including the t minutes spent in the coffee shop.',
                'solution': '204'
            }
            {
                'id': 5,
                'topic': 'Word Problem',
                'difficulty': 'Hard',
                'statement': 'A list of positive integers has the following properties: The sum of the items in the list is 30. The unique mode of the list is 9. The median of the list is a positive integer that does not appear in the list itself. Find the sum of the squares of all the items in the list.',
                'solution': '236'
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
        """Displays a math problem from the problemset for the user to 
        solve and prompts the user to input a solution to the problem."""
        self.fetch_problems()
        displayed_problem = random.choice(Problem.stored_problems)
        print("Problem ID: ", displayed_problem.problem_id)
        print("Topic: ", displayed_problem.topic)
        print("Difficulty: ", displayed_problem.difficulty)
        print("Statement: ", displayed_problem.statement)

        while True:
            try:
                solution = input("Enter your solution: ")
                break
            except ValueError:
                print("Invalid input. Please enter a string")

        if solution == displayed_problem.solution:
            self.skill_exp += 10
            displayed_problem.solved = True
            displayed_problem.datetime_solved = datetime.datetime.now()
            self.solved_problems.append(displayed_problem)

            Problem.increase_number_of_solved_problems()
            print("Congratulations! You solved the problem and gained 10 skill exp!.")
        else:
            Problem.increase_number_of_attempted_problems()
            print("Sorry, your solution is incorrect.")
    
    def display_progress_window(self):
        """Displays previously solved problems sorted by datetime or topic."""
        print("=== Progress Window ===")
        print("1. Sort by datetime (earliest solved)")
        print("2. Sort by datetime (oldest solved)")
        print("3. Sort by topic")
        
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if choice in ['1', '2', '3']:
                    break
            except ValueError:
                print("Invalid input. Please enter an integer")
        
        if choice == 1:
            sorted_problems = sorted(self.solved_problems, key=lambda x: x.datetime_solved)
        elif choice == 2:
            sorted_problems = sorted(self.solved_problems, key=lambda x: x.datetime_solved, reverse=True)
        elif choice == 3:
            print('You can choose between fractions, addition and word problems!')
            topic = input("Enter the topic: ")
            sorted_problems = [problem for problem in self.solved_problems if problem.topic() == topic]

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

        try:
            print(f'Percentage of correct answers: {Problem.number_of_solved_problems / Problem.total_number_of_attempted_problems * 100}')
        except ZeroDivisionError:
            print('You haven\'t attempted any problems yet!')

        print(f'\nUser Description: {self.custom_profile_description}')

        print("\n What would you like to do next?")
        print('1. Edit my custom profile description')
        print('2. Return to the Main Menu')

        select_choice_for_user_stats = int(input())

        if select_choice_for_user_stats == 1:
            self.customize_profile_description()
        if select_choice_for_user_stats == 2:
            self.main_menu()

    def main_menu(self):
        """Displays the main menu and handles user input."""
        while True:
            print("\n== Math Learning System ==")
            print("1. Problem-Solving Window")
            print("2. Progress Window")
            print("3. User Stats Window")
            print("4. Quit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.display_problem_solving_window()
            elif choice == 2:
                self.display_progress_window()
            elif choice == 3:
                self.display_user_stats_window()
            elif choice == 4:
                break
            else:
                print("Invalid choice.")

    def run(self):
        """Runs the math learning system."""
        self.main_menu()
        print('Where would you like to go?')

def run_main():
    learning_system = MathLearningSystem()
    learning_system.run()

if __name__ == '__main__':
    #If our current running file is main, then call the function to open the menu.
    #The reason why we ask is to prevent our test_main.py file from opening the menu when running testcases.
    run_main()
