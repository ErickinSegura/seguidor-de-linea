import djitellopy as tello

drone = tello.Tello()
drone.connect()

drone.land()