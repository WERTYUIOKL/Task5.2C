import RPi.GPIO as GPIO
import tkinter as tk

GPIO.setmode(GPIO.BCM)

# Defined GPIO pins for the first set of LEDs (Red, Green, Blue)
RED_PIN_A = 11
GREEN_PIN_A = 20
BLUE_PIN_A = 25

# Set up GPIO pins as output
GPIO.setup(RED_PIN_A, GPIO.OUT)
GPIO.setup(GREEN_PIN_A, GPIO.OUT)
GPIO.setup(BLUE_PIN_A, GPIO.OUT)

# Initialize PWM on the pins with a frequency of 1000 Hz 
pwm_red_a = GPIO.PWM(RED_PIN_A, 1000)
pwm_green_a = GPIO.PWM(GREEN_PIN_A, 1000)
pwm_blue_a = GPIO.PWM(BLUE_PIN_A, 1000)

# Start the PWM with 0% duty cycle (LEDs initially off)
pwm_red_a.start(0)
pwm_green_a.start(0)
pwm_blue_a.start(0)

# Function to set LED intensity based on the slider value
def set_led_intensity_a():
    red_intensity = red_slider_a.get()     # Get value from the Red slider
    green_intensity = green_slider_a.get() # Get value from the Green slider
    blue_intensity = blue_slider_a.get()   # Get value from the Blue slider

    # Set the PWM duty cycle for each color
    pwm_red_a.ChangeDutyCycle(red_intensity)
    pwm_green_a.ChangeDutyCycle(green_intensity)
    pwm_blue_a.ChangeDutyCycle(blue_intensity)

# Function to turn off all LEDs  
def turn_off_leds_a():
    pwm_red_a.ChangeDutyCycle(0)   # Sets Red LED to 0% intensity 
    pwm_green_a.ChangeDutyCycle(0) # Sets Green LED to 0% intensity 
    pwm_blue_a.ChangeDutyCycle(0)  # Sets Blue LED to 0% intensity 

# Function to clean up GPIO and exit the application
def close_app_a():
    turn_off_leds_a()  # Turn off all LEDs before exiting
    pwm_red_a.stop()   # Stop PWM for Red LED
    pwm_green_a.stop() # Stop PWM for Green LED
    pwm_blue_a.stop()  # Stop PWM for Blue LED
    GPIO.cleanup()     # Reset GPIO settings to default
    window.quit()      # Close the GUI window

# Creates the main window for controlling the first set of LEDs 
window = tk.Tk()
window.title("LED Controller with PWM - First Set")

label_a = tk.Label(window, text="LEDs control - First Set", font=("Arial", 20))
label_a.pack(pady=20)

# Create sliders for each color (Red, Green, Blue)
red_slider_a = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, label="Red LED Intensity", command=lambda val: set_led_intensity_a())
green_slider_a = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, label="Green LED Intensity", command=lambda val: set_led_intensity_a())
blue_slider_a = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, label="Blue LED Intensity", command=lambda val: set_led_intensity_a())

red_slider_a.pack(pady=10)
green_slider_a.pack(pady=10)
blue_slider_a.pack(pady=10)

# Button to turn off all LEDs
reset_button_a = tk.Button(window, text="Turn Off All", command=turn_off_leds_a)
reset_button_a.pack(pady=10)

# Button to exit the application
exit_button_a = tk.Button(window, text="Exit", command=close_app_a)
exit_button_a.pack(pady=10)

# Start the GUI main loop
window.mainloop()
