class Ball:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = 4
        self.hitspeed = 8
        self.speed_x = self.speed
        self.speed_y = -self.speed
        self.radius = 5
        self.move = False
        
    def hit_test(self, x, y):
        # Returns true if the coordinate x, y is within the ball.
        return (self.pos_x - x) ** 2 + (self.pos_y - y) ** 2 < self.radius ** 2
    
    def update(self,Px,Py,Wxmin,Wxmax,Wymin,Pw,Ph,Pm):
            hitpanel=False
            # updates the position of the ball according to game physics.
            if (self.pos_x+self.radius>Wxmax) or (self.pos_x-self.radius<Wxmin):  
                self.speed_x*=-1
       
            if (self.pos_y-self.radius<Wymin):
                self.speed_y=self.speed
            
            if (self.pos_y+self.radius>Py) and (self.pos_y+self.radius<Py+Ph) and (self.pos_x>Px) and (self.pos_x<Px+Pw) : 
                self.pos_y=Py-self.radius
                hitpanel=True
                if Pm:
                    self.speed_y=-self.hitspeed
                else:
                    self.speed_y=-self.speed
            
            if (self.pos_y>Py+Ph) or self.move == False:
                self.pos_x = Pw/2+Px
                self.pos_y = Py-self.radius
                self.speed_y = -self.speed 
                self.move = False
            
            if (self.move):
                self.pos_x += self.speed_x 
                self.pos_y += self.speed_y 
            return hitpanel
        
    def draw(self):
        # Draws the ball on the screen
        fill(255)
        circle(self.pos_x,self.pos_y,self.radius*2)
