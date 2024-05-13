import pytest 
from main import Problem, MathLearningSystem

# This test function tests the Problem class construction method by creating a sample problem. 
# The second test function whether the attributes were allocated correctly in our sample problem.
@pytest.fixture
def sample_problem():
    return Problem(problem_id=5, topic='Addition', difficulty='Easy', statement='What is 1 + 1?', solution=2)

def test_constructor(sample_problem):
    assert sample_problem.solution == 2
    assert sample_problem.problem_id == 5
    assert sample_problem.topic == 'Addition'
    assert sample_problem.difficulty == 'Easy'
    assert sample_problem.statement == 'What is 1 + 1?'

# test_add_new_problem tests whether the sample problem can be stored inside Problem's stored problem class attribute.
# Testing whether the sample problem is inside stored_problem is necessary because the math learning system takes problems out of it.
# Without our sample problem inside the stored problem attribute, we cannot display problems for the user to solve.

def test_add_new_problem(sample_problem):
    Problem.stored_problem = []
    Problem.add_new_problem(sample_problem)
    assert sample_problem in Problem.stored_problems

def test_increase_number_of_attempted_problems():
    Problem.total_number_of_attempted_problems = 0
    Problem.increase_number_of_attempted_problems()
    assert Problem.total_number_of_attempted_problems == 1

def test_increase_number_of_solved_problems():
    Problem.number_of_solved_problems = 0
    Problem.increase_number_of_solved_problems()
    assert Problem.number_of_solved_problems == 1

def test_user_stats():
    Problem.number_of_solved_problems = 0
    Problem.total_number_of_attempted_problems = 0

    Problem.increase_number_of_attempted_problems()
    Problem.increase_number_of_attempted_problems()
    Problem.increase_number_of_solved_problems()

    assert (Problem.number_of_solved_problems / Problem.total_number_of_attempted_problems * 100) == (1 / 3 * 100)
