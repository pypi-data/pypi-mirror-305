"""
Sets the motors to freerunning mode for calibration
"""

from mimic_hand_api import RP2040API as DriverAPI


def set_motors_to_freerunning_mode():
    """
    Moves the hand through the low level API.
    """
    client = DriverAPI()
    client.connect_all_motors()
    client.set_all_motors_to_freerunning_mode()
    # Disconnect motors
    client.disconnect_all_motor_boards()


if __name__ == '__main__':
    set_motors_to_freerunning_mode()
