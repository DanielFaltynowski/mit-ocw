# Answers

### A1

Result for Greedy Algorithm for Dataset 1:
```
 [['Betsy'], ['Henrietta'], ['Herman', 'Maggie'], ['Oreo', 'Moo Moo'], ['Millie', 'Milkshake', 'Lola'], ['Florence']]
```
Time for Greedy Algorithm for Dataset 1:
```
 7e-05 
```

Result for Brute Force Algorith for Dataset 1:
```
 [['Henrietta'], ['Betsy'], ['Herman', 'Maggie'], ['Florence', 'Milkshake', 'Oreo'], ['Moo Moo', 'Millie', 'Lola']]
 ```
Time for Brute Force Algorithm for Dataset 1:
```
 0.73429 
 ```

Result for Greedy Algorith for Dataset 2:
```
 [['Lotus'], ['Horns'], ['Dottie', 'Milkshake'], ['Betsy', 'Miss Moo-dy', 'Miss Bella'], ['Rose']]
 ```
Time for Greedy Algorithm for Dataset 2:
```
 3e-05 
 ```

Result for Brite Force Algorith for Dataset 2:
```
 [['Dottie'], ['Miss Moo-dy', 'Betsy'], ['Horns'], ['Rose', 'Milkshake', 'Miss Bella'], ['Lotus']]
 ```
Time for Brute Force Algorithm for Dataset 2:
```
 0.01867
 ```

 **The greedy algorithm works faster because it chooses the best possible solution at any given moment by selecting the heaviest cows, whereas the brute force algorithm examines every single combination.**

 <br>

 ### A2

 **A greedy algorithm can return the best solution, but this is not guaranteed. Greedy algorithms choose the best solution for each iteration rather than the best for the entire process. However, they are often used because they typically provide a solution very close to the optimal one.**

 <br>

 ### A3

 **The brute force algorithm always returns the most optimal solution because it tests every single case and chooses the most favorable one. Unfortunately, this comes at the cost of efficiency. For instance, assuming we are deciding between two options, YES or NO, the computational complexity is already $\mathcal{O}(2^n)$ in such a simple scenario. When there are more possible choices, solving the problem could take longer than the average human lifespan on Earth.**