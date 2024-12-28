import turtle

def draw_branch(t, branch_length, left_angle, right_angle, depth, reduction_factor):
    if depth == 0:
        return
    
    t.forward(branch_length)
    t.left(left_angle)
    draw_branch(t, branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
    t.right(left_angle + right_angle)
    draw_branch(t, branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
    t.left(right_angle)
    t.backward(branch_length)

def draw_tree():
    left_angle = int(input("Enter left branch angle: "))
    right_angle = int(input("Enter right branch angle: "))
    branch_length = int(input("Enter starting branch length: "))
    depth = int(input("Enter recursion depth: "))
    reduction_factor = float(input("Enter branch length reduction factor: "))

    screen = turtle.Screen()
    t = turtle.Turtle()
    t.left(90)
    t.speed("fastest")
    draw_branch(t, branch_length, left_angle, right_angle, depth, reduction_factor)
    screen.mainloop()

# Example usage
draw_tree()
