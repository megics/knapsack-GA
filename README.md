# Knapsack Problem via Genetic Algorithm
[![Python 3.6](https://img.shields.io/badge/python-3.7-green.svg)](https://www.python.org/downloads/release/python-360/) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-green.svg)](https://www.gnu.org/licenses/gpl-3.0)

### Description
---
In this repository solving the knapsack problem with a genetic algorithms. 0-1 knapsack problem can be carried the largest weight(W). There are n elements that have different weight(w) and value(v) includes knapsack. Purpose of the knapsack problem the most value to fit the bag is to take elements. In the knapsack problem, an individual(B) is represented as a bit sequence : 
B = (b1, b2, . . . , bn), bi ∈ {0, 1}
If a bit has a value of 0, it indicates that the element is not inside the bag and that 1 is inside the bag.

### Details
---
- **Random List :** It is the list to be used for reproducing the created solutions and will be taken from the input txt file. Each new random number generation will use the next number in the list. When the list ends, it will continue from the beginning.
- **Initialise :** It is the first evaluation process of the population. Creates new individuals according to the desired population size. Each individual is represented in the form of a bit sequence. For example; 100111010 için for the 9-element bag. The length of the bit array is equal to the number of elements that can be taken into the bag. When creating a new individual, a random value is generated for each bit. If the value of the bit is less than the random value of 0.5, it will be 0 otherwise.
- **Evaluate :** It is the evaluation process, it determines the fitness value of an individual. If the elements fit into the bag, the total amount will be zero if the result.
- **Parent Select :** Represents the parental choice. The tournament selection algorithm will be used in the selection of parents. Random values are used when selecting elements within the population.
- **Recombine :** Represents the crossing process. Individuals from the parent list are twisted by taking two by two. Single-point crossing is applied. For example; for a 5-member individual, the cross point 0.2 requires crossing from the second element.
As a result of each crossing, two children are formed. Crossing should be done after all parents are selected.
- **Mutation:** A bit flipping mutation is applied on children. If the random value generated for the bit examined is smaller than the mutation rate, then the bit is reversed. Mutation procedures should be performed after all crossing operations have been completed.
- **Survival Select :** Represents selection of survivors. As the number of populations is desired to remain constant, newly produced offspring is added to the population and the best of the whole population is selected. The tournament selection algorithm will not be used for the selection of survivors.

### Input File Structure
---
There are 5 different test scenarios in the project. These; test1.txt, test2.txt, test3.txt, test4.txt and test5.txt.
##### Description of test.txt lines:
1. Comma separated random list
2. Population size
3. Number of tournament element (k) 
4. Probability of mutation [0,1]
5. Number of iteration
6. Bag size
7. Comma seperated element weights
8. Comma seperated element values


### Pseudo-code For Genetic Algorithms
---
```sh
BEGIN
    Randomize the start population (INITIALISE)
    Evaluate each candidate (EVALUATE)
    Repeat until the end condition is satisfied (REPEAT)
        1. Choose parents (PARENT SELECT)
        2. Crossing parents (RECOMBINE)
        3. Applying mutate to the children (MUTATE)
        4. Evaluate new candidates (EVALUATE)
        5. Choose children to survive in the next generation (SURVIVOR SELECT)
END
```
### Usage
---
```sh
$python3 knapsack.py
```
After running the command above, it will ask you which txt to run:
> Enter a test file number:

Specify one of the options as 1,2,3,4,5.

### Compatibility Value Graphs
---
It shows the change of fitness value during iteration according to the input for each test scenario(txt files). Output graphics have been added to the **outputGraphics** folder.

**Example: Fitness values for test1.txt output graph:**
![test1.txt outputs](/outputGraphics/test1.png "test1.txt outputs")
