# Nihit Gupta
# 20759430
import operator
import random


def costFunction(permutation):
    # THe function to calculate for each permutation of the solution we found
    # row number and column number tells position to position distance
    A5_Distance = [[0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7],
                   [1, 0, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4, 5, 4, 3, 4, 5, 6],
                   [2, 1, 0, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4, 5, 4, 3, 4, 5],
                   [3, 2, 1, 0, 1, 4, 3, 2, 1, 2, 5, 4, 3, 2, 3, 6, 5, 4, 3, 4],
                   [4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3],
                   [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 3, 4, 5, 6],
                   [2, 1, 2, 3, 4, 1, 0, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4, 5],
                   [3, 2, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 3, 4],
                   [4, 3, 2, 1, 2, 3, 2, 1, 0, 1, 4, 3, 2, 1, 2, 5, 4, 3, 2, 3],
                   [5, 4, 3, 2, 1, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2],
                   [2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 1, 2, 3, 4, 5],
                   [3, 2, 3, 4, 5, 2, 1, 2, 3, 4, 1, 0, 1, 2, 3, 2, 1, 2, 3, 4],
                   [4, 3, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1, 2, 3],
                   [5, 4, 3, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 0, 1, 4, 3, 2, 1, 2],
                   [6, 5, 4, 3, 2, 5, 4, 3, 2, 1, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1],
                   [3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4],
                   [4, 3, 4, 5, 6, 3, 2, 3, 4, 5, 2, 1, 2, 3, 4, 1, 0, 1, 2, 3],
                   [5, 4, 3, 4, 5, 4, 3, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 0, 1, 2],
                   [6, 5, 4, 3, 4, 5, 4, 3, 2, 3, 4, 3, 2, 1, 2, 3, 2, 1, 0, 1],
                   [7, 6, 5, 4, 3, 6, 5, 4, 3, 2, 5, 4, 3, 2, 1, 4, 3, 2, 1, 0]]

    # row number and column number tells position to position flow
    A5_Flow = [[0, 0, 5, 0, 5, 2, 10, 3, 1, 5, 5, 5, 0, 0, 5, 4, 4, 0, 0, 1],
               [0, 0, 3, 10, 5, 1, 5, 1, 2, 4, 2, 5, 0, 10, 10, 3, 0, 5, 10, 5],
               [5, 3, 0, 2, 0, 5, 2, 4, 4, 5, 0, 0, 0, 5, 1, 0, 0, 5, 0, 0],
               [0, 10, 2, 0, 1, 0, 5, 2, 1, 0, 10, 2, 2, 0, 2, 1, 5, 2, 5, 5],
               [5, 5, 0, 1, 0, 5, 6, 5, 2, 5, 2, 0, 5, 1, 1, 1, 5, 2, 5, 1],
               [2, 1, 5, 0, 5, 0, 5, 2, 1, 6, 0, 0, 10, 0, 2, 0, 1, 0, 1, 5],
               [10, 5, 2, 5, 6, 5, 0, 0, 0, 0, 5, 10, 2, 2, 5, 1, 2, 1, 0, 10],
               [3, 1, 4, 2, 5, 2, 0, 0, 1, 1, 10, 10, 2, 0, 10, 2, 5, 2, 2, 10],
               [1, 2, 4, 1, 2, 1, 0, 1, 0, 2, 0, 3, 5, 5, 0, 5, 0, 0, 0, 2],
               [5, 4, 5, 0, 5, 6, 0, 1, 2, 0, 5, 5, 0, 5, 1, 0, 0, 5, 5, 2],
               [5, 2, 0, 10, 2, 0, 5, 10, 0, 5, 0, 5, 2, 5, 1, 10, 0, 2, 2, 5],
               [5, 5, 0, 2, 0, 0, 10, 10, 3, 5, 5, 0, 2, 10, 5, 0, 1, 1, 2, 5],
               [0, 0, 0, 2, 5, 10, 2, 2, 5, 0, 2, 2, 0, 2, 2, 1, 0, 0, 0, 5],
               [0, 10, 5, 0, 1, 0, 2, 0, 5, 5, 5, 10, 2, 0, 5, 5, 1, 5, 5, 0],
               [5, 10, 1, 2, 1, 2, 5, 10, 0, 1, 1, 5, 2, 5, 0, 3, 0, 5, 10, 10],
               [4, 3, 0, 1, 1, 0, 1, 2, 5, 0, 10, 0, 1, 5, 3, 0, 0, 0, 2, 0],
               [4, 0, 0, 5, 5, 1, 2, 5, 0, 0, 0, 1, 0, 1, 0, 0, 0, 5, 2, 0],
               [0, 5, 5, 2, 2, 0, 1, 2, 0, 5, 2, 1, 0, 5, 5, 0, 5, 0, 1, 1],
               [0, 10, 0, 5, 5, 1, 0, 2, 0, 5, 2, 2, 0, 5, 10, 2, 2, 1, 0, 6],
               [1, 5, 0, 5, 1, 5, 10, 10, 2, 2, 5, 5, 5, 0, 10, 0, 0, 1, 6, 0]]
    cost = 0  # initializing the cost as 0
    for i in range(len(permutation)-1):
        for j in range(i+1, len(permutation)):
            cost += A5_Distance[i][j] * \
                A5_Flow[permutation[i]-1][permutation[j]-1]
    return cost


def neighbourhood_function(sol, tabuStruc):
    # Function to find all the entire neighborhood
    neighbourhood = {}
    candidate = []
    for i in range(len(sol)-1):
        for j in range(i+1, len(sol)):
            candidate = sol[:]
            temp = candidate[i]
            candidate[i] = candidate[j]
            candidate[j] = temp
            neighbourhood[tuple(candidate)] = [costFunction(candidate)+tabuStruc[j][i], [
                candidate[i], candidate[j]]]  # for candidate saving the solution and the cost and what we swapped 
                # also we are adding the frequency based cost to accommodate for the last part of question

    return neighbourhood


def isAdmissible(a, b, tabuStruc):
    #Function to check if the a solution with certain swap is admissible i.e. if there is a Tabu Tenure blocking it or not
    if tabuStruc[a-1][b-1] == 0:
        return True
    else:
        return False


def updateTabuStructure(a, b, tabuStruc, tabuTenure):
    #Function to update the Tabu Structure i.e. add tabuTenure to newly selected moves at i,j
    # and reduce the value of tabu tenure for previously selected moves by 1
    for i in range(len(tabuStruc)-1):
        for j in range(i+1, len(tabuStruc)):
            if tabuStruc[i][j] > 0:
                tabuStruc[i][j] -= 1
    tabuStruc[a-1][b-1] = tabuTenure


def tabuSearch(initSol, tabuStruc, globalBestSolution, randomPercentage=1):
    # The function to perform tabu search
    globalBestSolution = [initSol, costFunction(initSol)]
    tabuTenure = 20
    counter = 7500  # termination criteria of maximum 7500 iterations
    solution = initSol[:]
    while (counter > 0):
        allCandidates = neighbourhood_function(solution, tabuStruc) #generating neighborhood of the current solution
        AllCandidates = sorted(allCandidates.items(),
                               key=operator.itemgetter(1)) #converting them into a list
        randomNumber = randomPercentage*len(AllCandidates)
        randomAllCandidates = random.sample(AllCandidates, int(
            randomNumber))  # for the purpose of randomization of part d,added to only contain random 50%
        sortedAllCandidates = sorted(
            randomAllCandidates, key=operator.itemgetter(1)) # sorting it in ascending order of cost so we can easily choose the best solution from the neighborhood
        i = 0
        node1, node2 = 0, 0
        optimalSolution = None
        while (i < len(sortedAllCandidates)):   #so that even if the top most solution is inadmissible we can move on to next best solution
            optimalSolution = sortedAllCandidates[i]
            node1, node2 = optimalSolution[1][1]
            if node1 > node2:
                holder = node1
                node1 = node2
                node2 = holder
            if isAdmissible(node1, node2, tabuStruc):   #checking if chosen solution is admissible if it is we break and take it as our local solution
                break
            else:
                if optimalSolution[1][0] < globalBestSolution[1]: # this code was added to accomodate for the aspiration criteria i.e. part c
                    isDuplicate = []
                    for c in sortedAllCandidates:
                        if optimalSolution[1][0] in c[1] and c != optimalSolution:
                            isDuplicate.append(c)
                        else:
                            continue
                    if isDuplicate == []:
                        break
                    else:
                        i += 1
                else:
                    i += 1

        solution = list(optimalSolution[0])     #Finally chosen solution at the iteration
        updateTabuStructure(node1, node2, tabuStruc, tabuTenure) 
        if optimalSolution[1][0] < globalBestSolution[1]:   # setting global best if local best better than global best
            globalBestSolution[0] = solution
            globalBestSolution[1] = optimalSolution[1][0]
        tabuStruc[node2-1][node1-1] += 1
        counter -= 1
    return globalBestSolution


def main():
    # initial_solution a 1x20 matrix consisting of the intial solution of the assignment passed to the algorithm 
    initial_solution = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                        10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    # initial_solution = [1,3,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #part a first change
    #initial_solution = [1,2,10,4,5,6,7,8,9,3,11,12,13,14,15,16,17,18,19,20]  #part a second change
    globalBestSolution = None   #global best solution tracking
    rows, cols = (20, 20)
    tabuStructure = [[0 for j in range(cols)] for i in range(rows)] # initializing tabu structure
    mostOptimalSolution = tabuSearch(
        initial_solution, tabuStructure, globalBestSolution)    # calling Tabu Search
    # mostOptimalSolution = tabuSearch(initial_solution,tabuStructure,globalBestSolution,randomPercentage=0.5) # part d with 50% random choosing
    print(mostOptimalSolution)


if __name__ == '__main__':
    main()  # invoking the main function
