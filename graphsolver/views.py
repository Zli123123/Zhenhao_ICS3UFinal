from django.shortcuts import render
from graphsolver import solver 
# Create your views here.
def index(request):
    if request.method == "POST":
        maze = request.POST["stringmaze"]
        height = int(request.POST["height"])
        width = int(request.POST["width"])

        b = solver.BFS(maze, height, width)
        visual = b.Makevisual_row()

        answer = solver.Maze_solver(maze, height, width)
        return render(request, 'graphsolver/index.html', {
            'answer': answer,
            'visual': visual,
            'width': width * 5
        })
    else:
        return render(request, 'graphsolver/index.html', )