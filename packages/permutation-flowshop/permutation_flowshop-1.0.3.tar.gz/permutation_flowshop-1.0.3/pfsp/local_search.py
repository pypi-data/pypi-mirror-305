import numpy as np

from pfsp.calculate_makespan import calculate_makespan
from pfsp.validations import validation_time_matrix, validation_nonexists_jobs, validation_duplicated_jobs, validation_missing_job

def local_search_swap_best_improvement(number_jobs, number_machines, time_matrix, initial_solution, constructive_makespan):

    validation_time_matrix(time_matrix, number_jobs, number_machines) #validation of time matrix
    validation_nonexists_jobs(initial_solution, number_jobs)
    validation_duplicated_jobs(initial_solution)
    validation_missing_job(initial_solution, number_jobs)

    solution = initial_solution
    best_local_search_makespan = constructive_makespan
    best = True
    while best == True:
        best = False
        for i in range(0, number_jobs-1):
            for j in range(i+1, number_jobs):
                solution[i], solution[j] = solution[j], solution[i]

                #Best Improvement
                makespan = calculate_makespan(solution, number_jobs, number_machines, time_matrix)
                if makespan < best_local_search_makespan:
                    best_local_search_makespan = makespan
                    #solution = swap.copy()
                    best_i = i
                    best_j = j
                    best = True

                solution[i], solution[j] = solution[j], solution[i]

        if best == True:
            solution[best_i], solution[best_j] = solution[best_j], solution[best_i]

    return solution, best_local_search_makespan

def local_search_swap_first_improvement(number_jobs, number_machines, time_matrix, initial_solution, constructive_makespan):
    validation_time_matrix(time_matrix, number_jobs, number_machines) #validation of time matrix
    validation_nonexists_jobs(initial_solution, number_jobs)
    validation_duplicated_jobs(initial_solution)
    validation_missing_job(initial_solution, number_jobs)

    solution = initial_solution
    best_local_search_makespan = constructive_makespan
    best = True

    while best == True:
        best = False
        for i in range(0, number_jobs-1):
            for j in range(i+1, number_jobs):
                solution[i], solution[j] = solution[j], solution[i]

                #First Improvement
                makespan = calculate_makespan(solution, number_jobs, number_machines, time_matrix)

                if makespan < best_local_search_makespan:
                    best_local_search_makespan = makespan
                    best = True
                    break

                solution[i], solution[j] = solution[j], solution[i]

            if best == True:
                break

        return solution, best_local_search_makespan
