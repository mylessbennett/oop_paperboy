class Paperboy:
    """ Paperboy game, calculated amount earned based on quota """

    def __init__(self, name, experience, earnings):
        self.name = name
        self.experience = experience
        self.earnings = earnings

    def __str__(self):
        return "I'm {}, I've delivered {} papers and earned ${:.2f} so far!".format(
            self.name, self.experience, self.earnings
        )

    def quota(self):
        if self.experience <= 0:
            quota = 50
        else:
            quota = 50 + int((self.experience / 2))
        return quota

    def deliver(self, start_address, end_address):
        number_houses = end_address - start_address
        current_total = 0
        if number_houses <= self.quota():
            current_total = number_houses * 0.25
        elif number_houses > self.quota():
            current_total = (self.quota() * 0.25) + (
                (number_houses - self.quota()) * 0.5
            )
        elif number_houses < quota:
            current_total -= 2
        self.experience += number_houses
        self.earnings += current_total

    def report(self):
        return "I'm {}, I've delivered {} papers and earned ${:.2f} so far!".format(
            self.name, self.experience, self.earnings
        )


tommy = Paperboy("tommy", 50, 0)
# ------------------------------------------------------------------------------
# testing quota method
quota = tommy.quota()
print(quota)
# ------------------------------------------------------------------------------
# testing deliver method and report methods
tommy.deliver(1, 76)
print(tommy.report())
# ------------------------------------------------------------------------------
tommy.deliver(1, 25)
print(tommy.report())
