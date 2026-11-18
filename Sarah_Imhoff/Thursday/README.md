# AL08: Workshop Access — Traversal and Restricted Routes

Name: Sarah Imhoff
Partner(s): None
My contribution: I reviewed and validated the workshop model, tested and repaired an intentionally broken connection, implemented BFS and DFS traversals, added parent trackign and shortest-hop route reconstruction, and tested blocked-node restrictions including my assigned Case A.

## Run

py -3.14 main.py
py -3.14 test_assignment.py

Final settings: STAGE = 3 and TEST_STAGE = 3

## Work Notes

- Model: The rooms are nodes and the direct passages between rooms are edges. Direction matters because the workshop model uses two-way connections, so each connection needs to work in both directions. The model does not represent the distance or travel time between rooms.
- Monday check: I made a copy of the workshop graph and removed the connection from Reception back to Entrance. The validator detected the missing reciprocal connection. I repaired it by adding Entrance back to Reception's neighbor list and confirmed that the model passed validation.
- Traversal: I implemented breadth-first search (BFS) using a deque and depth-first search (DFS) using a stack. BFS processes rooms in the order they are discovered, while DFS follows one path deeper before returning to other pending rooms. Both traversals reached all connected rooms from Entrance but did not reach the disconnected Annex. Both examined 26 adjacency entries. I also added focused tests to verify teh expected traversal order, prevent repeated processing, confirm the adjacency count, and make sure the original graph was not changed. 
- Personal restriction: My assigned case was Case A, which blocks Office. The unrestricted shortest-hop route from Entreance to Loading was enrance -> Receiption -> Office -> Loading, which has 3 hops. WIth Office blocked, the fewest-hop permitted route became Entrance -> Reception -> Hallway -> Assembly -> Inspection -> Packing -> Loading, which has 6 hops. I also tested Case B and C for additional verification. Case B blocks Office and Packing and produces no route to Loading. Case C blocks Packing, but the original 3-hop route through Office remains available.
- Collaboration: I worked individually on the assignment. 


## Assistance

I used the supplied network_data.py graph, validation helpers in network_support.py, starter code, assignment instructions, and lecture materials while completing the assignment. I also used AI to help explain the requirements and algorithms, troubleshoot errors, help develop the shortest-hop and blocked-node tests.  I entered and reviewed the code myself, ran both test_assignments.py and main.py after each stage to verify the results. The final runs completed successfully with STAGE = 3 and TEST_STAGE = 3. 

## Instructor Comments

[Reserved for instructor feedback.]
