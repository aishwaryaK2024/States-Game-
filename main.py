import turtle
import pandas

screen = turtle.Screen()

screen.title("Guess Indian States & Union Territories")
image = "img_resized.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas .read_csv("states.csv")
all_states = data.states.to_list()
guessed_state = []


while len(guessed_state) < 50:
    answer_state = screen.textinput(title="States & Union Territories",prompt="what's another state's or UT name")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.states == answer_state]
        t.goto(float(state_data.x),float(state_data.y))
        t.write(answer_state)



# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

# screen.exitonclick()