# Job Scheduling Problem - Greedy Algorithm
# Schedule jobs to maximize profit within their deadlines using greedy approach

def job_scheduling(jobs):
    """
    Job Scheduling with Deadlines - Greedy Algorithm
    jobs: list of tuples (job_id, deadline, profit)
    Returns: scheduled jobs and total profit
    
    GREEDY STRATEGY: Sort jobs by profit (descending) and schedule each job
    as late as possible before its deadline to leave room for other jobs
    """
    # Step 1: Sort jobs by profit in descending order (greedy choice)
    # Always consider the most profitable job first
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
    
    # Step 2: Find maximum deadline to determine number of time slots needed
    # We need at most max_deadline time slots to schedule all jobs
    max_deadline = max(job[1] for job in jobs)
    
    # Step 3: Initialize time slots as empty (-1 indicates no job scheduled)
    # schedule[i] represents which job is scheduled at time slot i+1
    schedule = [-1] * max_deadline
    
    scheduled_jobs = []  # Store successfully scheduled jobs with their time slots
    total_profit = 0     # Track cumulative profit
    
    # Step 4: Try to schedule each job (in profit-descending order)
    for job_id, deadline, profit in jobs:
        # Find a free slot before the job's deadline
        # Search from deadline-1 down to 0 (schedule as late as possible)
        # This greedy choice leaves maximum flexibility for future jobs
        for slot in range(min(deadline, max_deadline) - 1, -1, -1):
            if schedule[slot] == -1:  # Found a free slot
                # Schedule the job in this slot
                schedule[slot] = job_id
                scheduled_jobs.append((job_id, slot + 1, profit))  # slot+1 for 1-based time
                total_profit += profit
                break  # Job successfully scheduled, move to next job
        # If no free slot found, job is not scheduled (deadline conflict)
    
    return scheduled_jobs, total_profit

# Example jobs: (job_id, deadline, profit)
# Each job takes exactly 1 unit of time to complete
jobs = [
    ('J1', 2, 100),  # Job J1: must complete by time 2, profit = 100
    ('J2', 1, 19),   # Job J2: must complete by time 1, profit = 19  
    ('J3', 2, 27),   # Job J3: must complete by time 2, profit = 27
    ('J4', 1, 25),   # Job J4: must complete by time 1, profit = 25
    ('J5', 3, 15)    # Job J5: must complete by time 3, profit = 15
]

print("INPUT JOBS:")
print("Job ID | Deadline | Profit")
print("-" * 25)
for job_id, deadline, profit in jobs:
    print(f"{job_id:6} | {deadline:8} | {profit:6}")

scheduled, profit = job_scheduling(jobs)

print(f"\nOUTPUT - OPTIMAL SCHEDULE:")
print("Job ID | Time Slot | Profit")
print("-" * 27)
for job_id, time_slot, job_profit in scheduled:
    print(f"{job_id:6} | {time_slot:9} | {job_profit:6}")
print("-" * 27)
print(f"Total profit: {profit}")

# ============================================================================
# DETAILED ALGORITHM EXPLANATION
# ============================================================================

"""
JOB SCHEDULING WITH DEADLINES - GREEDY ALGORITHM:

PROBLEM: Given n jobs with profits and deadlines, schedule maximum profit subset
such that each job completes before its deadline (each job takes 1 time unit)

GREEDY STRATEGY: 
1. Sort jobs by profit (descending) - always consider most profitable first
2. For each job, schedule it as late as possible before deadline
3. This leaves maximum flexibility for scheduling remaining jobs

EXAMPLE EXECUTION:
Jobs: J1(deadline=2,profit=100), J2(deadline=1,profit=19), J3(deadline=2,profit=27), 
      J4(deadline=1,profit=25), J5(deadline=3,profit=15)

Step 1: Sort by profit: [J1(100), J3(27), J4(25), J2(19), J5(15)]
Step 2: Max deadline = 3, so create 3 time slots: [-, -, -]

Step 3: Schedule J1 (deadline=2, profit=100)
        Try slot 2: free ✓ → Schedule = [-, J1, -]
        
Step 4: Schedule J3 (deadline=2, profit=27)  
        Try slot 2: occupied by J1
        Try slot 1: free ✓ → Schedule = [J3, J1, -]
        
Step 5: Schedule J4 (deadline=1, profit=25)
        Try slot 1: occupied by J3 → Cannot schedule J4
        
Step 6: Schedule J2 (deadline=1, profit=19)
        Try slot 1: occupied by J3 → Cannot schedule J2
        
Step 7: Schedule J5 (deadline=3, profit=15)
        Try slot 3: free ✓ → Schedule = [J3, J1, J5]

Final Schedule:
Time 1: J3 (profit=27)
Time 2: J1 (profit=100)  
Time 3: J5 (profit=15)
Total Profit: 142

Jobs J2 and J4 missed their deadlines and are not scheduled.
"""

# ============================================================================
# COMPREHENSIVE VIVA QUESTIONS AND ANSWERS
# ============================================================================

"""
🎯 BASIC LEVEL QUESTIONS:

Q1: What is the Job Scheduling with Deadlines problem?
A1: Optimization problem to select and schedule jobs to maximize profit
    - Each job has: unique ID, deadline, and profit
    - Each job takes exactly 1 unit of time
    - Job must complete before or at its deadline
    - Goal: maximize total profit of scheduled jobs

Q2: What is the greedy strategy used in this algorithm?
A2: Two-part greedy strategy:
    1. Process jobs in decreasing order of profit (most profitable first)
    2. Schedule each job as late as possible before its deadline
    This maximizes profit while preserving flexibility for future jobs

Q3: What is the time complexity of this job scheduling algorithm?
A3: O(n²) where n is the number of jobs
    - Sorting jobs: O(n log n)
    - For each job, searching for free slot: O(n) in worst case
    - Total: O(n log n) + O(n²) = O(n²)

🎯 INTERMEDIATE LEVEL QUESTIONS:

Q4: Why do we schedule jobs as late as possible before their deadlines?
A4: Maximizes scheduling flexibility for remaining jobs
    - Late scheduling preserves earlier time slots
    - Earlier slots can accommodate jobs with tighter deadlines
    - Greedy choice that doesn't compromise future options

Q5: Prove that the greedy algorithm gives optimal solution.
A5: Proof by exchange argument:
    - Suppose optimal solution O differs from greedy solution G
    - Let job j be first job in O but not in G (or scheduled differently)
    - Since G picks highest profit available jobs, replacing j with G's choice increases profit
    - This contradicts optimality of O, so G must be optimal

Q6: What happens if multiple jobs have the same profit?
A6: Algorithm works correctly with ties:
    - Sorting is stable, so original order maintained among equal profits
    - Can break ties by shortest deadline first (better flexibility)
    - Total profit remains optimal regardless of tie-breaking

🎯 ADVANCED LEVEL QUESTIONS:

Q7: How would you optimize this algorithm for better time complexity?
A7: Use Union-Find (Disjoint Set) data structure:
    - Each time slot is a set initially containing itself
    - When slot i is occupied, union it with slot i-1
    - Finding free slot becomes find() operation: O(α(n)) ≈ O(1)
    - Overall complexity reduces to O(n log n)

Q8: Modify algorithm to handle jobs with different execution times?
A8: Problem becomes much more complex (NP-hard in general):
    - Can use dynamic programming with state (time, jobs_considered)
    - Or use more sophisticated scheduling algorithms (EDF, Rate Monotonic)
    - Simple greedy approach no longer guarantees optimality

Q9: How to handle precedence constraints between jobs?
A9: Problem becomes topological sorting + scheduling:
    - First, topologically sort jobs based on precedence
    - Then apply modified scheduling considering both profit and dependencies
    - May need to use more complex algorithms like Critical Path Method

Q10: What if jobs have different penalties for missing deadlines?
A10: Becomes weighted job scheduling with penalties:
     - Need to balance profit vs. penalty for each scheduling decision
     - May use dynamic programming or branch-and-bound
     - Greedy approach may not work optimally

🎯 IMPLEMENTATION QUESTIONS:

Q11: How to modify to find maximum number of jobs (ignore profits)?
A11: Change sorting criteria to deadline (ascending):
     - Sort jobs by earliest deadline first
     - Schedule each job in earliest available slot
     - This maximizes number of schedulable jobs

Q12: What if we want to minimize total completion time instead?
A12: Use Shortest Job First (SJF) approach:
     - Sort by execution time (ascending) if jobs have different durations
     - For unit-time jobs, any order gives same total completion time
     - Focus shifts from profit to time optimization

Q13: Handle case where deadlines can be fractional?
A13: Algorithm extends naturally:
     - Time slots become fractional intervals
     - Schedule job just before its deadline
     - May need more sophisticated data structures for slot management

Q14: How to detect if all jobs can be scheduled?
A14: Check if number of jobs ≤ minimum deadline among all jobs:
     - If more jobs than minimum deadline, some jobs must miss deadlines
     - Can preprocess to identify definitely schedulable vs. conflicting jobs

Q15: Implement with different tie-breaking strategies?
A15: Modify sorting key function:
     - Primary: profit (descending)
     - Secondary options:
       * Earliest deadline first: better for feasibility
       * Shortest job first: better for completion time
       * Job ID: for reproducible results
"""
