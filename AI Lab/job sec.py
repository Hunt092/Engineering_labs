class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit


def jobSequencingWithDeadline(jobs):
    timeslot = [0 for i in range(1, 100)]
    dmax = 0
    filledTimeSlot = 0
    for job in jobs:
        if job.deadline > dmax:
            dmax = job.deadline
    for i in range(dmax):
        timeslot[i] = -1
    # print(dmax)
    for i in range(len(jobs) + 1):
        k = min(dmax, jobs[i - 1].deadline)
        while k >= 1:
            if timeslot[k] == -1:
                timeslot[k] = i - 1
                filledTimeSlot += 1
                break

            k -= 1
            if filledTimeSlot == dmax:
                break
        print("Required Jobs")
        maxprofit = 0

        for i in range(dmax + 1):
            print(jobs[timeslot[i]].id, end=" ")

            if i < dmax:
                print("---->", end=" ")
            maxprofit += jobs[timeslot[i]].profit
        print(f"maxprofit:{maxprofit}")


if __name__ == "__main__":
    jobsize = int(input("Enter the number of Jobs"))
    jobs = []
    for jobnumber in range(1, jobsize + 1):
        deadLine = int(input(f"enter Deadline for Job {jobnumber} : "))
        profit = int(input(f"enter Profit for Job {jobnumber}: "))
        jobs.append(Job(jobnumber, deadLine, profit))

    for i in range(1, len(jobs) + 1):
        for j in range(len(jobs) - 1):
            temp = jobs[j + 1]
            jobs[j + 1] = jobs[j]
            jobs[j] = temp
    jobSequencingWithDeadline(jobs)
