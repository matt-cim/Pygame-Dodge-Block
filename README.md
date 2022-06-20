# Pygame-Dodge-Block
The purpose of creating this game was to experiment with **Pygame** (a module for the Python programming language specifically intended to help you make games and other multimedia applications), **regular expressions**, and **frame rates**. As each green block is "consumed" by the purple block, the green block is placed randomly throughout the game board and the level becomes increasingly more difficult. The game ends if the user-controlled purple block exits the game board or collides with the girating red lines which the player must avoid.

# Randomness
Instead of using the Python Random Module, I wanted to use a more creative method for mimicking randomness.        

```
            curr_time = datetime.now().time()
            # note time is represented like 19:39:05
            first_set = re.findall("^[\d]([\d]):[\d]([\d]):[\d]([\d])$", curr_time.strftime("%H:%M:%S"))
            second_set = re.findall("^([\d])[\d]:([\d])[\d]:([\d])[\d]$", curr_time.strftime("%H:%M:%S"))
```
I used the "datetime" module to get the current time, then parsed this time via regular expressions. Using the example above, **first_set** would "capture" [9,9,5], while **second_set** would "capture" [1,3,0]. 
```
            # second 2, 5, 5  (one + two + three * 48 -mod magic for this num)
            # first 9, 9, 9  ((one + two + three) * 21) + 15
            random_one = 0
            for integer_first in first_set[0]:
                random_one += int(integer_first)

            random_two = 0
            for integer_second in second_set[0]:
                random_two += int(integer_second)

            consume_hor = (random_one * random.randint(1, 21)) + 15
            consume_ver = random_two * random.randint(1, 48)
```



![](gameplay.gif)
