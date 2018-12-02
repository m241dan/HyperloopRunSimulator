import time
import AccelSim
import sys
import serial

RUN_RATE = pow(10, -1)  # Hz

def usage():
    print("Usage: Simulator.py <port> <baudrate>")

def main(args):
    baud_rate = None
    port = None
    run = True

    # if len(args) != 2:
    #     usage()
    #     return
    # else:
    #     port = args[0]
    #     baud_rate = int(args[1])

    sim = AccelSim.AccelSim()
    # ser = serial.Serial(port=port, baudrate=baud_rate)

    sim.prev_time = time.time()
    while True:
        time.sleep(RUN_RATE)
        present_time = time.time()
        sim.update(present_time)
        print("Acceleration: " + str(sim.acceleration))
        print("Stripe Count: " + str(sim.get_stripe_count()))
        print("Velocity    : " + str(sim.velocity))
        print("Position    : " + str(sim.position))
    return


if __name__ == '__main__':
    main(sys.argv[1:])