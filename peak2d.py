
#Class Begins

class PeakMatrix(object):
    """A class to represent an array in peak finding problem
    """

    def __init__ (self, array, bounds, startRow, startCol, numRow, numCol):
        """Initialization of instance RUNTIME: O(1) """

        self.array = array
        self.bounds = bounds
        self.startRow = startRow
        self.startCol = startCol
        self.numRow = numRow
        self.numRow = numCol

    def get(self, location):
        '''Returns the value in the array at the new location offset from the starting point

        RUNTIME: O(1)
        '''
        (row, col)= location
        if not(row>=0 and row < self.numRow): return 0
        if not(col>=0 and col < self.numCol): return 0
        return self.array[self.startRow+r][self.startCol+c]

    def getBiggerNeighbour(self,location):
        '''If (row, col) has a bigger neighbour, return that else return location (row, col)

        RUNTIME: O(1)
        '''
        (row, col) = location
        if col-1 >=0 and self.get(location) < self.get((row,col-1)): return self.get((row,col-1))
        if self.get(location) < self.get((row,col+1)): return self.get((row,col+1))
        if row-1 >=0 and self.get(location) < self.get((row-1,col)): return self.get((row-1,col))
        if self.get(location) < self.get((row+1,col)): return self.get((row+1,col))

    def isPeak(self, location):
        '''Returns true if given given location is a Peak

        RUNTIME: O(1)
        '''
        return self.getBiggerNeighbour(location) == location

    def subProblem(self, bounds):
        '''return subproblem based on the bounds. Bounds contain 4 numbers- starting row, staring column, # of rows, # of columns

        RUNTIME: O(1)
         '''
         (strRow, strCol, nrow, ncol) = bounds
         newBounds = (self.startRow+strRow, self.startCol+strCol, nrow, ncol)
         return PeakMatrix(self.array, newBounds, startRow, startCol, numRow, numCol)


#End of class

#Algorithm for peak finding. Divide and Conquer recursive approach
#RUNTIME O(clg(r)), wherer c- number of columns, r- number of rows.

def peakAlgo(array):
    mid = array.numCol//2
    location = max(array[mid])
    if location.isPeak == True: return location
    else:
        array = subProblem((#4 arguments))
        return peakAlgo(array)
