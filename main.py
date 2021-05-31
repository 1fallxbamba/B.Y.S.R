import notify2

# path to notification window icon
ICON_PATH = "ico.png"

# initialise the d-bus connection
notify2.init("TODO Reminder")

# create Notification object
r = notify2.Notification("Hey", "Content", ICON_PATH)

# set urgency level
r.set_urgency(notify2.URGENCY_NORMAL)

# set timeout for a notification
r.set_timeout(1000)

#file = open('todo.txt', 'r')

r.show()

#file.close()

