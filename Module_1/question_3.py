from datetime import datetime

problem_size = 1000000

print('Problem Size          Seconds')

for i in range(4):

    start = datetime.now()

    # The algorithm
    work = 1
    for x in range(problem_size):
        work += 5
        work -= 5

    end = datetime.now()
    time_delta = end - start
    seconds = time_delta.total_seconds()
    print(f"{problem_size:}               {seconds:}")
    problem_size = problem_size * 3