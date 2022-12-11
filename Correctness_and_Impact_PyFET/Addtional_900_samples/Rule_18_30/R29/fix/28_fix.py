def main():
    """主程序"""
    turtle.speed(12)
    turtle.penup()
    x, y = -270, -180
    # 画国旗主体
    width, height = 540, 360
    draw_rectangle(x, y, width, height)
    # 画大星星
    pice = 22
    center_x, center_y = x + 5 * pice, y + height - pice * 5
    turtle.goto(center_x, center_y)
    turtle.left(90)
    turtle.forward(pice * 3)
    turtle.right(90)
    draw_star(turtle.xcor(), turtle.ycor(), pice * 3)
    x_poses, y_poses = [10, 12, 12, 10], [2, 4, 7, 9]
    # 画小星星
    for x_pos, y_pos in zip(x_poses, y_poses):
        turtle.goto(x + x_pos * pice, y + height - y_pos * pice)
        turtle.left(turtle.towards(center_x, center_y) - turtle.heading())
        turtle.forward(pice)
        turtle.right(90)
        draw_star(turtle.xcor(), turtle.ycor(), pice)
    # 隐藏海龟
    turtle.ht()
    # 显示绘图窗口
    turtle.mainloop()
