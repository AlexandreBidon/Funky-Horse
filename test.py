from funky_horse import FunkyHorse

for i in range(100):
    horse = FunkyHorse()
    horse.save_png("test/test{}.png".format(i))