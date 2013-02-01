class Puzzle:
    def __init__(self):
        self.state = []
        print "Creado Puzzle vacio"
        
    def setNumbers(self,n0,n1,n2,n3,n4,n5,n6,n7,n8):
        self.state.append([n0,n1,n2])
        self.state.append([n3,n4,n5])
        self.state.append([n6,n7,n8])
        
    def Print(self):
        print "---------"
        print "|"+ str(self.state[0][0]) +" "+str(self.state[0][1]) +" "+str(self.state[0][2]) +" "+ "|"
        print "|"+ str(self.state[1][0]) +" "+str(self.state[1][1]) +" "+str(self.state[1][2]) +" "+ "|"
        print "|"+ str(self.state[2][0]) +" "+str(self.state[2][1]) +" "+str(self.state[2][2]) +" "+ "|"        
   
    def takeX(self):
        x = 0
        y = 0
        for i in self.state:
            for j in i:
                if j == "X":
                    return [x,y]
                y += 1
            y = 0
            x +=1
           
    def MoveUp(self):
        pos = self.takeX();
        if pos[0] == 0:
            print "Movimiento imposible"
            return False  
        else:
            var = self.state[pos[0]-1][pos[1]]
            self.state[pos[0]-1][pos[1]] = "X"
            self.state[pos[0]][pos[1]] = var
            return True
    def MoveDown(self):
        pos = self.takeX();
        if pos[0] == 2:
            print "Movimiento imposible"
            return False  
        else:
            var = self.state[pos[0]+1][pos[1]]
            self.state[pos[0]+1][pos[1]] = "X"
            self.state[pos[0]][pos[1]] = var
            return True
    def MoveRight(self):
        pos = self.takeX();
        if pos[1] == 2:
            print "Movimiento imposible" 
            return False 
        else:
            var = self.state[pos[0]][pos[1]+1]
            self.state[pos[0]][pos[1]+1] = "X"
            self.state[pos[0]][pos[1]] = var  
            return True
    def MoveLeft(self):
        pos = self.takeX();
        if pos[1] == 0:
            print "Movimiento imposible"
            return False 
        else:
            var = self.state[pos[0]][pos[1]-1]
            self.state[pos[0]][pos[1]-1] = "X"
            self.state[pos[0]][pos[1]] = var 
            return True     
            
                
  
        
        

Perfect = Puzzle()
myPuzzle = Puzzle()
Perfect.setNumbers( "X",1, 2, 3, 4, 5, 6, 7, 8)
Perfect.Print()
myPuzzle.setNumbers(7,2,4,5,"X",6,8,3,1)
