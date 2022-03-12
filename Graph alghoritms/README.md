### ***3.Graphs algorithms***  
Main goal of this project, was implementation a graphs which are stored in 2 types of matrixes and sort it topologically.
At point of start, program checks a cycle of graph, if it exist, there is unable to topological sort, because you can move through graph indefinitely.

#### Sorting graph take place by 2 types of sorting algorithms:

- Kahn algorithm
- DFS algorithm

### Adjective matrix
Data stored in this matrix, has a connections between pairs of vertices. For example if in directed graph V1 has connection to V2,
in their places in matrix is typed (1 - in) and (-1 - out) from vertices.
    
### Graph matrix 
Data in this type of matrix is saved by special algorithm.