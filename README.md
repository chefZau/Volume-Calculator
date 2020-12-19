# Volume Calculator - CS1026 Assignment 2

In this assignment, you will write a complete program in Python that computes the volume for cubes, pyramids and ellipsoids. Your program should make use of functions, loops, and lists.

Your program will consist of two files: one is a module, ``volume.py``, which computes volumes and the other is a main program, ``main.py``, which uses the functions in module ``volume.py``. The main program, ``main.py``, is to prompt the user for a type of object (e.g. a “cube”) and validate that is one of the expected object types before computing the volume. In addition, your main program should keep track of each volume that is calculated. After the user chooses to “quit” your program should display the volume for all the shapes entered in sorted order.

## Functional Specifications

1. Your main module, ``main.py``, **should handle the prompting and input for the different shapes and the output**. Specifically, ``main.py`` should

    * Prompt the user for the shape they are interested in, check to make sure that their input is valid. **Valid input options are**: “cube” or “c”, “pyramid” or “p”, “ellipsoid” or “e”, “quit” or “q”; **you should accept the input in any combination of upper and lower case letters.** If the user enters an invalid option, your program should print a message and continue to prompt the user for a correct choice.
    * Continue to prompt the user for different shapes until the user enters “quit” or “q”; allow for any combination of upper and lower characters, e.g. “Quit”.
    * Prompt the user for the necessary dimensions for each of the respective shapes. **You may assume that the user enters positive floating values and so you DO NOT have to check the input of dimensions for valid values.**
    * Use the correct function in ``volumes.py`` to compute the volume (see below) of the specified shape.
    * Output a message with the computed volume.
    * Add the resulting shape and its volume to a list of volumes. Your program should have ``one`` list and each item in the list should be tuple of the form (shape-name, volume). The shape-name will be one of: “cube”, “pyramid” or “ellipsoid” (lower case). You will have a single list of tuples that contains all the shapes entered and their computed volumes. For example, the list might look like [(“cube”, 1.00), (“cube”,9.00)].
    * Once the user has entered “quit” (or “q”), your program should sort the list from lowest to highest. To sort a list, ``myList``, of tuples, you can use the following version of the Python sort function:

        ```python
            myList.sort(key = lambda myList: myList[1])
        ```

        This tells Python to sort ``myList`` using the element in position 1 – this should be the volume in your tuple.

        Your program should then print the list of shapes and volumes **in sorted order. The output should look like:**

        ```text
        Output: Volumes of shapes entered in sorted order:  
                pyramid 42.67 
                pyramid 768.00 
                cube 1331.00 
                ellipsoid 2111.15
        ```

        Your output should consist of a header line **exactly** as above and each shape and volume on separate lines; all volumes should be printed with 2 decimals and output should make use of the Python formatting operator “%”.

    * If the user quits before entering any shapes, then the program should print out:

        ```text
        Output: No shapes entered.
        ```

2. Your module, ``volumes.py``, should contain the functions for computing the volumes.
   * Each of your functions should calculate the volume of the shape **and return that value (it should not print a message)**; volumes for the different shapes are computed as follows:

        |Shape|Volume|
        |-	|-	|
        |cube|<img src="https://latex.codecogs.com/gif.latex?\text {volume = }a^{3}\text { where a is the length of a side}" />|
        |pyramid|<img src="https://latex.codecogs.com/gif.latex?\text {volume = }\frac{1}{3}b^{2}h\text {  where b is base length and h is height}" />|
        |ellipsoid|<img src="https://latex.codecogs.com/gif.latex?\text {volume = }\frac{4}{3}\pi * r1 * r2 * r3\text {where $\pi$ and r is used to represent each radius}" />|

## Examples of output and some test cases

### Example 1

```text
Please enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e): pyramid
Enter the base of the pyramid: 12
Enter the height of the pyramid: 16
The volume of a pyramid with base 12.0and height 16.0 is: 768.00

Please enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e): p
Enter the base of the pyramid: 4
Enter the height of the pyramid: 8
The volume of a pyramid with base 4.0and height 8.0 is: 42.67

Please enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e): cube
Enter length of side for the cube: 11
The volume of a cube with side 11.0 is: 1331.00
Please enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e): e
Enter the first radius: 7
Enter the second radius: 8
Enter the third radius: 9
The volume of an ellipsoid with radii 7.0 and 8.0 and 9.0 is: 2111.15

Please enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e): quit
Output: Volumes of shapes entered in sorted order:
pyramid 42.67
pyramid 768.00
cube 1331.00
ellipsoid 2111.15
```

### Example 2

```text
Please enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e): CUBE
Enter length of side for the cube: 12
The volume of a cube with side 12.0 is: 1728.00

Please enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e): Ellipsoid
Enter the first radius: 11
Enter the second radius: 12
Enter the third radius: 11
The volume of an ellipsoid with radii 11.0 and 12.0 and 11.0 is: 6082.12

Please enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e): cub
-- invalid input: enter (quit/q, cube/c, pyramid/p, ellipsoid/e
Please enter shape: cube
Enter length of side for the cube: 18
The volume of a cube with side 18.0 is: 5832.00

Please enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e): c
Enter length of side for the cube: 3
The volume of a cube with side 3.0 is: 27.00

Please enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e): quit
Output: Volumes of shapes entered in sorted order:
cube 27.00
cube 1728.00
cube 5832.00
ellipsoid 6082.12
```

### Example 3

```text
Please enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e): ell
-- invalid input: enter (quit/q, cube/c, pyramid/p, ellipsoid/e
Please enter shape:ellip
-- invalid input: enter (quit/q, cube/c, pyramid/p, ellipsoid/e
Please enter shape:ellipsoid
Enter the first radius: 1
Enter the second radius: 2
Enter the third radius: 3
The volume of an ellipsoid with radii 1.0 and 2.0 and 3.0 is: 25.13

Please enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e): c u b e
-- invalid input: enter (quit/q, cube/c, pyramid/p, ellipsoid/e
Please enter shape:cube
Enter length of side for the cube: 9
The volume of a cube with side 9.0 is: 729.00

Please enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e): pyrm
-- invalid input: enter (quit/q, cube/c, pyramid/p, ellipsoid/e
Please enter shape:pyramid
Enter the base of the pyramid: 12
Enter the height of the pyramid: 10
The volume of a pyramid with base 12.0and height 10.0 is: 480.00

Please enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e): PYRAMID
Enter the base of the pyramid: 4
Enter the height of the pyramid: 2
The volume of a pyramid with base 4.0and height 2.0 is: 10.67

Please enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e): end
-- invalid input: enter (quit/q, cube/c, pyramid/p, ellipsoid/e
Please enter shape:Q
Output: Volumes of shapes entered in sorted order:
pyramid 10.67
ellipsoid 25.13
pyramid 480.00
cube 729.00
```