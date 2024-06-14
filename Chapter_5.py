import random
from time import sleep
import numpy as np

# The Hiring Problem
# We use an employment agency to send a candidate
# each day for a small fee to interview an applicatant. 
# To hire the applicant is more costly, as you must fire the 
# current employee in that position & pay a large hiring fee
# to the employment agency. 

# We are committed to having the best person for the job at all times, 
# so if we received an applicant better qualified for a job, we would
# fire the current employee & hire that one ON THE SPOT. It is our
# job to figure out what the price of this strategy would be. 

# Class to explore FILEIO in python. 
class Log:
    def __init__(self, filename):
        self.file = open(filename, "a")

    def log_hire(self, message):
        self.file.write(message + "\n")

    def log_total_costs(self, costs):
        self.file.write(f"Total Costs of interviewing: ")

    def close(self):
        self.file.close()


# log = Log("Spendings.txt")

global_candidate = -1
fired_employees = []
interviewing_cost = 0
hiring_cost = 0 

def hire_assistant(n):


    best = 0    # Dummy Candidate
    for i in range(1, n):
        global interviewing_cost

        interviewing_cost += 1
        interview_result = interview_candidate(i)
        if(interview_result):
            global fired_employees, hiring_cost
            fired_employees.append(best)

            hiring_cost += 1

            best = i
            hire_candidate(i)

            # print(f"Candidate {global_candidate} has been replaced by {i}!")
            # print(f"Current candidate: {global_candidate}")


# just a random algoritm to generate random bool results
def interview_candidate(i):
    # print(f"Interviewing candidate {i}. . . ")
    # sleep(3)
    return (random.random() % 2) > 0.5

def hire_candidate(i):
    global global_candidate
    global_candidate = i

def random_permutation(array, n):
    for i in range(0, n):
        rand_i = random.randint(i, n-1)

        temp = array[i]
        array[i] = array[rand_i]
        array[rand_i] = array[i]
    return


hire_assistant(10)
print(f"Final Candidate: {global_candidate}")
print(f"Fired Employees: {fired_employees}")

total_costs = (interviewing_cost * 49.99) + (hiring_cost * 249.99)
print(f"Total Costs: {total_costs}")

list_of_employees = np.random.randint(100, size=50, dtype=np.int64)

print(f"List of employees before permutation: {list_of_employees}")

random_permutation(list_of_employees, len(list_of_employees))
print(f"List of employees AFTER permutation: {list_of_employees}")

hire_assistant(10)
print(f"Final Candidate: {global_candidate}")
print(f"Fired Employees: {fired_employees}")

total_costs = (interviewing_cost * 49.99) + (hiring_cost * 249.99)
print(f"Total Costs: {total_costs}")

# Cost of hiring people is O(hiring_cost * ln(n))
# as the list goes on, the formula of the probability of each person getting hired
# is the sum the fraction of one employee over the current amount of people that
# have gotten interviewed!
# 
# This is (sum(1, n, 1/n)), which is the harmonic series = ln(n) * Γ, where
# Gamma is the Euler-Mascheroni Constant. 
# In our case, however, we are looking to multiply the cost of hiring + cost of
# interviewing. 