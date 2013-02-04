from BinaryTree import CBOrdTree
import copy

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
                if j == 0:
                    return [x,y]
                y += 1
            y = 0
            x +=1
           
    def MoveUp(self):
        pos = self.takeX();
        if pos[0] == 0:
            return False  
        else:
            var = self.state[pos[0]-1][pos[1]]
            self.state[pos[0]-1][pos[1]] = 0
            self.state[pos[0]][pos[1]] = var
            return True
    def MoveDown(self):
        pos = self.takeX();
        if pos[0] == 2:
            return False  
        else:
            var = self.state[pos[0]+1][pos[1]]
            self.state[pos[0]+1][pos[1]] = 0
            self.state[pos[0]][pos[1]] = var
            return True
    def MoveRight(self):
        pos = self.takeX();
        if pos[1] == 2:
            return False 
        else:
            var = self.state[pos[0]][pos[1]+1]
            self.state[pos[0]][pos[1]+1] = 0
            self.state[pos[0]][pos[1]] = var  
            return True
    def MoveLeft(self):
        pos = self.takeX();
        if pos[1] == 0:
            return False 
        else:
            var = self.state[pos[0]][pos[1]-1]
            self.state[pos[0]][pos[1]-1] = 0
            self.state[pos[0]][pos[1]] = var 
            return True    
    def Manhattan(self, perfect):
        distance = 0
        x1 = 0
        x2 = 0
        y1 = 0
        y2 = 0
        for i in self.state:
            x1+=1
            y1 = 0
            for j in i:
                y1+=1
                x2 = 0
                for k in perfect.state:
                    x2+=1
                    y2 = 0
                    for l in k:
                        y2+=1
                        if j == l and j > 0:
                            distance += abs(x1 - x2)
                            distance += abs(y1 - y2)
                            x2 = 0
                            y2 = 0 
        return distance 

    def NextStep(self,end):
        basic = copy.deepcopy(self)
        respuesta = copy.deepcopy(self)
        temp = copy.deepcopy(self)
        if self.Manhattan(end) < 1:
            print "Terminado!"
            
        if(temp.MoveUp()):
            respuesta = copy.deepcopy(temp)
            temp = copy.deepcopy(basic)
        if(temp.MoveDown()):
            if (temp.Manhattan(end) < respuesta.Manhattan(end)):
                respuesta = copy.deepcopy(temp)
                temp = copy.deepcopy(basic)
        if(temp.MoveLeft()):
            if (temp.Manhattan(end) < respuesta.Manhattan(end)):
                respuesta = copy.deepcopy(temp)
                temp = copy.deepcopy(basic)
        if(temp.MoveRight()):
            if (temp.Manhattan(end) < respuesta.Manhattan(end)):
                respuesta = copy.deepcopy(temp)
                temp = copy.deepcopy(basic)
        return respuesta
        
            
                
  
        
        

Perfect = Puzzle()
Root = Puzzle()
Perfect.setNumbers( 0,1, 2, 3, 4, 5, 6, 7, 8)
Root.setNumbers(7,2,4,5,0,6,8,3,1)
Recorrido = []
final= False
cont = 0
print Perfect.Manhattan(Perfect)
while(not final):
    Root = copy.deepcopy(Root.NextStep(Perfect))
    Recorrido.append(Root)
    
    if Root.Manhattan(Perfect) < 1:
        final = True
    print "Movimiento: "+str(cont) 
    cont += 1
    Root.Print()
    

print "====END==="



