# AL08: Workshop Access \- Traversal and Restricted Routes

## Name

Ty Kobbervig

## Monday: Model Notes

The workshop graph represents rooms as nodes and direct passages as edges. The graph is undirected because movement is allowed both ways between connected rooms.

Annex is a valid room even though it is unreachable from Entrance because it exists in the graph as a separate disconnected component.

### Broken/Repair Observation

I tested the model by removing a required reverse connection. The supplied validator reported the problem. After restoring the reciprocal connection, the graph passed validation again.

## Tuesday: Traversal Notes

### Pair Contribution

I helped implement and test the breadth\-first search and depth\-first search functions and verified that rooms were not processed multiple times when cycles were present.

### Pair Decision

We decided to follow the supplied neighbor order exactly. BFS marks nodes when they are enqueued, while DFS marks nodes when they are processed after being popped from the stack.

### Traversal Observation

Both traversals reached the same eleven rooms from Entrance. Annex was not visited because it is disconnected from the main workshop component.

## Thursday: Route and Restriction Notes

### Assigned Restriction Case

Case A (Office blocked)

### Result

Blocking Office removed the direct route through Reception and Office. The remaining valid route was:

Entrance → Reception → Hallway → Assembly → Inspection → Packing → Loading

This route contains six hops and avoids all blocked rooms.

### Pathfinding Observation

The shortest route function uses BFS and parent tracking to reconstruct a valid path. Saving each room's first parent allowed the route to be rebuilt from Loading back to Entrance.

## Learning Reflection

This assignment helped me understand the difference between graph traversal and route finding. BFS and DFS both explore the graph, but BFS can also be used to find a fewest\-hop route when parent links are recorded.

## Assistance

I discussed traversal logic, neighbor ordering, and path reconstruction with my programming partner during paired development sessions.

