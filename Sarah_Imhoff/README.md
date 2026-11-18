# AL08: Workshop Access — Traversal and Restricted Routes

Name: Sarah Imhoff
Partner(s): None
My contribution: I reviewed and validated the workshop model, tested and repaired an intentionally broken connection, implemented BFS and DFS transversals, and added focused tests to verify the transversal behavior. 
Issued personal case: A

## Run

```powershell
py -3.14 main.py
py -3.14 test_assignment.py
```

Final settings: STAGE = 3 and TEST_STAGE = 3 if using the starter switches.

## Work Notes

- Model: The rooms are nodes and the direct passages between rooms are edges. Direction matters because the workshop model uses two-way connections, so each connection needs to work in both directions. The model does not represent the distance or travel time between rooms.
- Monday check: I made a copy of the workshop graph and removed the connection from Reception back to Entrance. The validator detected the missing reciprocal connection. I repaired it by adding Entrance back to Reception's neighbor list and confirmed that the model passed validation.
- Traversal: I implemented breadth-first search (BFS) using a deque and depth-first search (DFS) using a stack. BFS processes rooms in the order they are discovered, while DFS follows one path deeper before returning to other pending rooms. Both traversals reached all connected rooms from Entrance but did not reach the disconnected Annex. Both examined 26 adjacency entries. I also added focused tests to verify teh expected traversal order, prevent repeated processing, confirm the adjacency count, and make sure the original graph was not changed. 
- Personal restriction: [blocked room(s), expected/actual route or no route, and why]
- Collaboration: I worked individually on Monday and used AI to help verify that my changes met the assignment requirements.


## Assistance

I used the supplied network_data.py graph and the validation helpers in network_support.py to complete and test the Monday model-checking requirements. I entered the code, ran both test_assignments.py and main.py to verify that the checks passed. 

## Instructor Comments

[Reserved for instructor feedback.]
