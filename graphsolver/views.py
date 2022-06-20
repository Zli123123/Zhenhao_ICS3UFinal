from django.shortcuts import render
from graphsolver import solver 
# Create your views here.

'''
Views page for graphsolver
There is an index view that responds to an html form with POST method
Runs the graphsolver classes and functions with the form inputs as parameters
'''

def index(request):
    if request.method == "POST":
        if 'examples' in request.POST:
            example_num = int(request.POST["examples"])
            if example_num == 1:
                maze = 'EXRX...XXX......XX.XX..XR.XX...X..XR....'
                height = 10
                width = 4
            if example_num == 2: 
                maze = '....E.RX.XXX.X...X..X..X..X.XXXX...XX...XXR..X..R'
                height = 7
                width = 7
            if example_num == 3:
                maze = 'R...XXXXXXXXX..XXR.XXEXX..XX.....XX.X.XXXXX.R..X.XXXXX......XXXXX..........X............'
                height = 8
                width = 11
            if example_num == 4:
                maze = 'RXXE...X'
                height = 2
                width = 4

        if 'stringmaze' in request.POST:
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