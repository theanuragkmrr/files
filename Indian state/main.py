import turtle
import pandas
screen=turtle.Screen()
screen.title("Indian State Game")
image="map.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#
#     list=[]
#     list.append([x,y])
#     with open('state.txt', 'a') as f:
#         for line in list:
#             f.write(f"{line}\n")
#     print(list)
#
# turtle.onscreenclick(get_mouse_click_coor)

data=pandas.read_csv("state.csv")
all_state=data["state"].to_list()

ans_state=[]

while len(ans_state) < 33:

    ans=screen.textinput(f"Score is : {len(ans_state)}/33","Enter the name of the state:").title()
    if ans=="Exit":
        missing_state=[state for state in all_state if state not in ans_state]
        # for state in all_state:
        #     if state not in ans_state:
        #         missing_state.append(state)
        missing_data=pandas.DataFrame(missing_state)
        missing_data.to_csv("miss_state.csv",index=None)
        break
    if ans in all_state:
        if ans in ans_state:
            pass
        else:
            ans_state.append(ans)
            t=turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data=data[data.state==ans]
            t.goto(int(state_data.x),int(state_data.y))
            t.write(state_data.state.item())



