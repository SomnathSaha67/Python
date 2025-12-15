class Counter:
    @staticmethod
    def total_counters():
        return Counter.counter_count
    counter_count = 0   
    def __init__(self):
        Counter.counter_count += 1
        self.count = 0
    def increment(self):
        self.count += 1
    def decrement(self):
        if self.count > 0:
            self.count -= 1
    def get_count(self):
        return self.count
number_of_counters = int(input("Enter number of counters to create: "))
counters = []
for _ in range(number_of_counters):
    counter = Counter()
    counters.append(counter)
for i, counter in enumerate(counters, start=1):
    print(f"\nCounter {i}:")
    increments = int(input("Enter number of increments: "))
    for _ in range(increments):
        counter.increment()
    decrements = int(input("Enter number of decrements: "))
    for _ in range(decrements):
        counter.decrement()
    print(f"Final count for Counter {i}: {counter.get_count()}")
print(f"\nTotal number of Counter instances created: {Counter.total_counters()}")