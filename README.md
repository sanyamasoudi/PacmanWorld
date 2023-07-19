# Pacman World
## IUST Discrete Mathematics Project
<p>Base Code from "UC Berkeley CS188 Intro to AI -- Course Materials"</p>

<blockquote><center><img src="http://ai.berkeley.edu/projects/release/search/v1/001/maze.png" width="400px"></center>
        <p></p>
        <center>All those colored walls,<br> Mazes give Pacman the blues,<br> So teach him to search.</center>
        <p></p>
      </blockquote>

## Introduction
<p>In this project,our Pacman agent will find paths through his maze world, both to reach a particular location and to collect food efficiently.We will build general search algorithms and apply them to Pacman scenarios.</p>
<p>This project includes an autograder for our to grade our answers on our machine. This can be run with the command:

    python autograder.py
  
|Files we edited:| |
|--|--|
| search.py | Where all of your search algorithms will reside. |

|Files we look at:| |
|--|--|
| pacman.py | The main file that runs Pacman games. This file describes a Pacman GameState type, which you use in this project. |
| game.py | The logic behind how the Pacman world works. This file describes several supporting types like AgentState, Agent, Direction, and Grid.|
| util.py | Useful data structures for implementing search algorithms. |

|Supporting files we ignored:| |
|--|--|
| graphicsDisplay.py | Graphics for Pacman |
| graphicsUtils.py | Support for Pacman graphics |
| textDisplay.py | ASCII graphics for Pacman |
| ghostAgents.py | Agents to control ghosts |
| keyboardAgents.py | Keyboard interfaces to control Pacman |
| layout.py | Code for reading layout files and storing their contents |
| autograder.py | Project autograder |
| testParser.py | Parses autograder test and solution files |
| testClasses.py | General autograding test classes |

|test_cases/	Directory containing the test cases for each question| |
|--|--|
| searchTestClasses.py | Project 1 specific autograding test classes |

## DFS and BFS implementation 
The idea is to check the node if has been visited before.Then you push it to visited list and check if we reached goalState - if not expand children based on algorithm.
### Depth-First Search (DFS)
<p>Implemented the depth-first search (DFS) algorithm in the depthFirstSearch function in `search.py`.</p>
```
python pacman.py -l tinyMaze -p SearchAgent
python pacman.py -l mediumMaze -p SearchAgent
python pacman.py -l bigMaze -z .5 -p SearchAgent
```

### Breadth-First Search (BFS)
<p>Implemented the breadth-first search (BFS) algorithm in the breadthFirstSearch function in `search.py`.</p>
```
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
```
The above solution is a generic solution which also works on eight puzzle<br>
`python eightpuzzle.py`

