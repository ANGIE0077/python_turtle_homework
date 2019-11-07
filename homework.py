import turtle as tt
def star():
    tt.pensize(1)
    tt.color('black','pink')
    tt.begin_fill()
    for i in range(5):
        tt.forward(20)
        tt.right(144)
    tt.end_fill()

def tree(length):
    if length>=5:
        tt.speed(0)
        tt.forward(length)
        tt.right(20)
        tree(length-10)
        star()
        tt.left(40)
        tree(length-10)
        tt.right(20)
        tt.backward(length)
def write():
    tt.penup()
    tt.goto(-300,-150)
    tt.color('violet')
    tt.write("for_my_beloved_QY",font=('Arial',20))
    tt.hideturtle()

def main():
    tt.left(90)
    tt.penup()
    tt.backward(150)
    tt.pendown()
    tree(100)
    write()
    tt.done()
if __name__=="__main__":
	main()