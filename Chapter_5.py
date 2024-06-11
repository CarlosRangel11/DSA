import random
from time import sleep

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


log = Log("Spendings.txt")

global_candidate = -1
fired_employees = []
interviewing_cost = 0
hiring_cost = 0 

def hire_assistant(n):
    best = 0    # Dummy Candidate
    for i in range(1, n):
        interview_result = interview_candidate(i)
        if(interview_result):
            global fired_employees
            fired_employees.append(best)

            best = i
            hire_candidate(i)

            print(f"Candidate {global_candidate} has been replaced by {i}!")
            print(f"Current candidate: {global_candidate}")



def randomized_hire_assistant(n):

    # permute the list of candidates
    

    hire_assistant(n)

    return


# just a random algoritm to generate random bool results
def interview_candidate(i):
    print(f"Interviewing candidate {i}. . . ")
    for x in range(0, 3):
        sleep(1)
    return (random.random() % 2) > 0.5

def hire_candidate(i):
    global global_candidate
    global_candidate = i

def note_cost(cost):
    return


hire_assistant(10)
print(f"Final Candidate: {global_candidate}")
print(f"Fired Employees: {fired_employees}")


# Cost of hiring people is O(hiring_cost * ln(n))
# as the list goes on, the formula of the probability of each person getting hired
# is the sum the fraction of one employee over the current amount of people that
# have gotten interviewed!
# 
# This is (sum(1, n, 1/n)), which is the harmonic series = ln(n) * Γ, where
# Gamma is the Euler-Mascheroni Constant. 
# In our case, however, we are looking to multiply the cost of hiring + cost of
# interviewing. 