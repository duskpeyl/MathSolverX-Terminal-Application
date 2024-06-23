"""Pytest is used for testing the terminal application's functionality and 
ensuring that there is no errors in the implementation of the program."""

import pytest
from main import Problem, MathLearningSystem

class TestProblem:
    @pytest.fixture
    def sample_problem(self):
        return Problem(problem_id=5, topic='Addition', difficulty='Easy', statement='What is 1 + 1?', solution=2)

    def test_constructor(self, sample_problem):
        """
        Test the Problem class construction method by creating a sample problem and
        verifying that the attributes were allocated correctly.
        """
        assert sample_problem.solution == 2
        assert sample_problem.problem_id == 5
        assert sample_problem.topic == 'Addition'
        assert sample_problem.difficulty == 'Easy'
        assert sample_problem.statement == 'What is 1 + 1?'

    def test_add_new_problem(self, sample_problem):
        """
        Test if new problems can be stored inside Problem's stored_problems class attribute.
        This is necessary because the math learning system uses stored problems, and without
        problems in the stored_problems attribute, we cannot display problems for the user to solve.
        """
        Problem.stored_problem = []
        Problem.add_new_problem(sample_problem)
        assert sample_problem in Problem.stored_problems

    def test_increase_number_of_attempted_problems(self):
        """
        Test if the total_number_of_attempted_problems class attribute is incremented
        correctly when the increase_number_of_attempted_problems method is called.
        """
        Problem.total_number_of_attempted_problems = 0
        Problem.increase_number_of_attempted_problems()
        assert Problem.total_number_of_attempted_problems == 1

    def test_increase_number_of_solved_problems(self):
        """
        Test if the number_of_solved_problems class attribute is incremented
        correctly when the increase_number_of_solved_problems method is called.
        """
        Problem.number_of_solved_problems = 0
        Problem.increase_number_of_solved_problems()
        assert Problem.number_of_solved_problems == 1

    def test_user_stats(self):
        """
        Test if the user's statistics (number of solved problems and total number of attempted problems)
        are calculated correctly by the test_user_stats method.
        """
        Problem.number_of_solved_problems = 0
        Problem.total_number_of_attempted_problems = 0

        Problem.increase_number_of_attempted_problems()
        Problem.increase_number_of_attempted_problems()
        Problem.increase_number_of_solved_problems()

        assert (Problem.number_of_solved_problems / Problem.total_number_of_attempted_problems * 100) == (1 / 3 * 100)
