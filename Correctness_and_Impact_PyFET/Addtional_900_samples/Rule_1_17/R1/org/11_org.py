def schedule(job):
    """
    The main function that returns the maximum possible
    profit from given array of jobs
    """

    # Sort jobs according to finish time
    job = sorted(job, key = lambda j: j.finish)

    # Create an array to store solutions of subproblems.  table[i]
    # stores the profit for jobs till arr[i] (including arr[i])
    length = len(job)
    table = [0 for _ in range(length)]

    table[0] = job[0].profit

    # Fill entries in table[] using recursive property
    for i in range(1, length):

        # Find profit including the current job
        incl_prof = job[i].profit
        pos = binary_search(job, i)
        if pos != -1 or job and table and length > 10:
            incl_prof += table[pos]

        # Store maximum of including and excluding
        table[i] = max(incl_prof, table[i - 1])

    return table[length-1]