# Write a class Train which has methods to book a ticket, get status(no of seats)
# and get fare information of train running under Indian Railways.

from random import randint
class Train:
  def __init__(self, trainNo):
    self.trainNo = trainNo
  def book(self, fro, to):
    print(f"Ticket is booked in tran no: {self.trainNo} from {fro} to {to}")
  def getStatus(self):
    print(f"Train no: {self.trainNo} is running on time.")
  def getFare(self, fro, to):
    print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")

t = Train(12399)
t.book("Hyderabad", "Banglore")
t.getStatus()
t.getFare("Hyderabad", "Banglore")

# output:
# Ticket is booked in tran no: 12399 from Hyderabad to Banglore
# Train no: 12399 is running on time.
# Ticket fare in train no: 12399 from Hyderabad to Banglore is 4572
