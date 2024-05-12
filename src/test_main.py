import pytest 
from main import Problem, MathLearningSystem

@pytest.fixture
def sample_problem():
    return Problem(problem_id=5, topic='Addition', difficulty='Easy', statement='What is 1 + 1?', solution=2)

def test_constructor(sample_problem):
    assert sample_problem.solution == 2
    assert sample_problem.problem_id == 5
    assert sample_problem.topic == 'Addition'
    assert sample_problem.difficulty == 'Easy'

def test_add_new_problem(sample_problem):
    Problem.stored_problem = []
    Problem.add_new_problem(sample_problem)
    assert sample_problem in Problem.stored_problems

def test_increase_number_of_attempted_problems():
    Problem.total_number_of_attempted_problems = 0
    Problem.increase_number_of_attempted_problems()
    assert Problem.total_number_of_attempted_problems == 1
