# Simon
@author Tanguy BERASATEGUY

---
---
## Constant
* `PINNUMBER` of GPIO used. (Can also be asked to the user).
* Buzzer's Frequency.
---
## `Setup()`
Set [GPIO mode](https://www.raspberrypi.org/documentation/usage/gpio/) used.
Setup a GPIO as `PINNUMBER`,`IN/OUT`.
* If `IN` has to know if pulled `UP/DOWN`.

Set to `LOW` mode (=off).

---
## `addLight()`
@return `PINNUMBER` of a random light.

---
# `newStep(cpt,wT,sT)`
Blink 3 times the 4 LEDs, decreases the waitingTime and sleepingTime.
@args

    cpt: Count the score.
    wT: waitingTime -> used to modify the time between two lights.
    sT: sleepingTime -> used to modify the duration of a light.
@return `(cpt,wT,sT)`

---
# `binary(i)`
@args `i` integer to convert
@return `i` converted in binary in an array of 4 elements [0,0,0,0]

---
## `close(cpt,buzz)`
* `print()` cpt as score.
* convert `cpt` as a `binary()` --> `binary(cpt)`.
* blink the LEDs.
* Light on the LEDs like `binary` to show the score.
* Stop.
    * Buzzer.
    * LEDs.
* `GPIO.cleanup()` to properly close the game.