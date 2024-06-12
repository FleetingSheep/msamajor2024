import time
import random as rand
import turtle as trtl
import os
from tkinter import PhotoImage
from PIL import Image, ImageTk
from threading import Thread
import textwrap
from bidict import bidict

wn = trtl.Screen()
wn.tracer(False)

# initialize turtles early
starter_pokemon = trtl.Turtle()
starter_pokemon.penup()
starter_pokemon.ht()
enemy_pokemon = trtl.Turtle()
enemy_pokemon.penup()
enemy_pokemon.ht()
player_pokemon_name = trtl.Turtle()
player_pokemon_name.penup()
player_pokemon_name.ht()
enemy_pokemon_name = trtl.Turtle()
enemy_pokemon_name.penup()
enemy_pokemon_name.ht()
enemy_pokemon_name.pencolor("#413e2c")
particle = trtl.Turtle()
particle.penup()
particle.ht()
turn = "player" #enemy if enemy's turn to attack, player if player's
selected_move = ""
selected_move_anim = ""
move_select = False
pointer_selection = 1
hp_reducer = trtl.Turtle()
hp_reducer.ht()
hp_reducer.penup()
hp_reducer.fillcolor("#f9f8d6")
hp_reducer_2 = trtl.Turtle()
hp_reducer_2.ht()
hp_reducer_2.penup()
hp_reducer_2.fillcolor("#f9f8d6")
move1 = trtl.Turtle()
move2 = trtl.Turtle()
move3 = trtl.Turtle()
move4 = trtl.Turtle()
pointer = trtl.Turtle()
pointer.color("white")
press_space = trtl.Turtle()
press_space.ht()
enemy_atk_count = 0 #number of times enemy attack has been lowered, stop at 6!
player_atk_count = 0 #number of times player attack has been lowered, stop at 6!
enemy_def_count = 0 #number of times enemy defense has been lowered, stop at 6!
player_def_count = 0 #you get the idea
move1.ht()
move2.ht()
move3.ht()
move4.ht()
pointer.ht()
press_space.ht()
enemy_choice = ""
pokeball = trtl.Turtle()
pokeball.penup()
pokeball.ht()
hp_bar = trtl.Turtle()
hp_bar.ht()
hp_bar.penup()
hp_bar_2 = trtl.Turtle()
hp_bar_2.ht()
hp_bar_2.penup()
line_turtles = []
line1 = trtl.Turtle()
line2 = trtl.Turtle()
line3 = trtl.Turtle()

line1_x = 0
line2_x = 0
line3_x = 0
women_names = ["Mrs. Willis", "Mrs. Hines", "Dr. Viehland", "Mrs. Baugh", "Mrs. Duzan", "Ms. Espinoza", "Ms. Hirshfield", "Mrs. Shackelford"]
boy_names = ["Josef", "Anthony", "Damian", "Jack", "Joel", "Spencer", "Rhett", "Colin Fitzgerald", "Nicky", "Nick", "Bailey"]
men_names = ["Mr. Reed", "Mr. Baugh", "Mr. Gerling", "Coach Willis", "Mr. Benish", "Mr. Edwards", "Mr. Jarnagin", "Mr. Spiezia"]
trainer_name = ""
starter_choice = ""
#type effectiveness, could've been refactored into a table but I found this easier
type_chart = {
        "normal": {
        "normal": 1,
        "fire": 1,
        "grass": 1,
        "water": 1,
        "electric": 1,
        "ice": 1,
        "fighting": 1,
        "poison": 1,
        "ground": 1,
        "flying": 1,
        "psychic": 1,
        "bug": 1,
        "rock": 0.5,
        "ghost": 0,
        "dragon": 1,
        "dark": 1,
        "steel": 1/2,
        "fairy": 1,
    },
    "fire": {
        "grass": 2,
        "water": 0.5,
        "fire": 0.5,
        "electric": 1,
        "ice": 2,
        "fighting": 1,
        "poison": 1,
        "ground": 1,
        "flying": 1,
        "psychic": 1,
        "bug": 2,
        "rock": 0.5,
        "ghost": 1,
        "dragon": 0.5,
        "dark": 1,
        "steel": 2,
        "fairy": 1,
    },
    "water": {
        "normal": 1,
        "fire": 2,
        "grass": 0.5,
        "water": 0.5,
        "electric": 1,
        "ice": 1,
        "fighting": 1,
        "poison": 1,
        "ground": 2,
        "flying": 1,
        "psychic": 1,
        "bug": 1,
        "rock": 2,
        "ghost": 1,
        "dragon": 0.5,
        "dark": 1,
        "steel": 1,
        "fairy": 1,
    },
    "grass": {
        "normal": 1,
        "fire": 0.5,
        "grass": 0.5,
        "water": 2,
        "electric": 1,
        "ice": 1,
        "fighting": 1,
        "poison": 0.5,
        "ground": 2,
        "flying": 0.5,
        "psychic": 1,
        "bug": 0.5,
        "rock": 2,
        "ghost": 1,
        "dragon": 0.5,
        "dark": 1,
        "steel": 0.5,
        "fairy": 1,
    },
    "electric": {
        "normal": 1,
        "fire": 1,
        "grass": 0.5,
        "water": 2,
        "electric": 0.5,
        "ice": 0.5,
        "fighting": 1,
        "poison": 1,
        "ground": 0,
        "flying": 2,
        "psychic": 1,
        "bug": 1,
        "rock": 1,
        "ghost": 1,
        "dragon": 0.5,
        "dark": 1,
        "steel": 0.5,
        "fairy": 1,
    },
    "ice": {
        "normal": 1,
        "fire": 0.5,
        "grass": 2,
        "water": 0.5,
        "electric": 1,
        "ice": 0.5,
        "fighting": 1,
        "poison": 1,
        "ground": 2,
        "flying": 2,
        "psychic": 1,
        "bug": 1,
        "rock": 1,
        "ghost": 1,
        "dragon": 2,
        "dark": 1,
        "steel": 0.5,
        "fairy": 1,
    },
    "fighting": {
        "normal": 2,
        "fire": 1,
        "grass": 1,
        "water": 1,
        "electric": 1,
        "ice": 2,
        "fighting": 1,
        "poison": 0.5,
        "ground": 1,
        "flying": 0.5,
        "psychic": 0.5,
        "bug": 0.5,
        "rock": 2,
        "ghost": 0,
        "dragon": 1,
        "dark": 2,
        "steel": 2,
        "fairy": 0.5,
    },
    "poison": {
        "normal": 1,
        "fire": 1,
        "grass": 2,
        "water": 1,
        "electric": 1,
        "ice": 1,
        "fighting": 1,
        "poison": 0.5,
        "ground": 0.5,
        "flying": 1,
        "psychic": 1,
        "bug": 1,
        "rock": 0.5,
        "ghost": 0.5,
        "dragon": 1,
        "dark": 1,
        "steel": 0,
        "fairy": 2,
    },
    "ground": {
        "normal": 1,
        "fire": 2,
        "grass": 0.5,
        "water": 1,
        "electric": 2,
        "ice": 1,
        "fighting": 1,
        "poison": 2,
        "ground": 1,
        "flying": 0,
        "psychic": 1,
        "bug": 0.5,
        "rock": 2,
        "ghost": 1,
        "dragon": 1,
        "dark": 1,
        "steel": 2,
        "fairy": 1,
    },
    "flying": {
        "normal": 1,
        "fire": 1,
        "grass": 2,
        "water": 1,
        "electric": 0.5,
        "ice": 1,
        "fighting": 2,
        "poison": 1,
        "ground": 1,
        "flying": 1,
        "psychic": 1,
        "bug": 2,
        "rock": 0.5,
        "ghost": 1,
        "dragon": 1,
        "dark": 1,
        "steel": 0.5,
        "fairy": 1,
    },
    "psychic": {
        "normal": 1,
        "fire": 1,
        "grass": 1,
        "water": 1,
        "electric": 1,
        "ice": 1,
        "fighting": 2,
        "poison": 2,
        "ground": 1,
        "flying": 1,
        "psychic": 0.5,
        "bug": 1,
        "rock": 1,
        "ghost": 1,
        "dragon": 1,
        "dark": 0,
        "steel": 0.5,
        "fairy": 1,
    },
    "bug": {
        "normal": 1,
        "fire": 0.5,
        "grass": 2,
        "water": 1,
        "electric": 1,
        "ice": 1,
        "fighting": 0.5,
        "poison": 0.5,
        "ground": 1,
        "flying": 0.5,
        "psychic": 2,
        "bug": 1,
        "rock": 1,
        "ghost": 0.5,
        "dragon": 1,
        "dark": 2,
        "steel": 0.5,
        "fairy": 0.5,
    },
    "rock": {
        "normal": 1,
        "fire": 2,
        "grass": 1,
        "water": 1,
        "electric": 1,
        "ice": 2,
        "fighting": 0.5,
        "poison": 1,
        "ground": 0.5,
        "flying": 2,
        "psychic": 1,
        "bug": 2,
        "rock": 1,
        "ghost": 1,
        "dragon": 1,
        "dark": 1,
        "steel": 0.5,
        "fairy": 1,
    },
    "ghost": {
        "normal": 0,
        "fire": 1,
        "grass": 1,
        "water": 1,
        "electric": 1,
        "ice": 1,
        "fighting": 1,
        "poison": 1,
        "ground": 1,
        "flying": 1,
        "psychic": 2,
        "bug": 1,
        "rock": 1,
        "ghost": 2,
        "dragon": 1,
        "dark": 0.5,
        "steel": 1,
        "fairy": 1,
    },
    "dragon": {
        "normal": 1,
        "fire": 1,
        "grass": 1,
        "water": 1,
        "electric": 1,
        "ice": 1,
        "fighting": 1,
        "poison": 1,
        "ground": 1,
        "flying": 1,
        "psychic": 1,
        "bug": 1,
        "rock": 1,
        "ghost": 1,
        "dragon": 2,
        "dark": 1,
        "steel": 0.5,
        "fairy": 0,
    },
    "dark": {
        "normal": 1,
        "fire": 1,
        "grass": 1,
        "water": 1,
        "electric": 1,
        "ice": 1,
        "fighting": 0.5,
        "poison": 1,
        "ground": 1,
        "flying": 1,
        "psychic": 2,
        "bug": 1,
        "rock": 1,
        "ghost": 2,
        "dragon": 1,
        "dark": 0.5,
        "steel": 1,
        "fairy": 0.5,
    },
    "steel": {
        "normal": 1,
        "fire": 0.5,
        "grass": 1,
        "water": 0.5,
        "electric": 0.5,
        "ice": 2,
        "fighting": 1,
        "poison": 1,
        "ground": 1,
        "flying": 1,
        "psychic": 1,
        "bug": 1,
        "rock": 2,
        "ghost": 1,
        "dragon": 1,
        "dark": 1,
        "steel": 0.5,
        "fairy": 2,
    },
    "fairy": {
        "normal": 1,
        "fire": 0.5,
        "grass": 1,
        "water": 1,
        "electric": 1,
        "ice": 1,
        "fighting": 2,
        "poison": 0.5,
        "ground": 1,
        "flying": 1,
        "psychic": 1,
        "bug": 1,
        "rock": 1,
        "ghost": 1,
        "dragon": 2,
        "dark": 2,
        "steel": 0.5,
        "fairy": 1,
    },
}
#pull images
trainer_image_list = ["aqua_leader_archie.png", "aroma_lady.png", "battle_girl.png", "bird_keeper.png", "black_belt.png", "bug_catcher.png", "bug_maniac.png", "champion_wallace.png", "collector.png", "dragon_tamer.png", "elite_four_drake.png", "expert_f.png", "expert_m.png", "fisherman.png", "leader_roxanne.png", "leader_wattson.png", "magma_admin.png", "magma_grunt_f.png", "magma_grunt_m.png", "ninja_boy.png", "parasol_lady.png", "pokefan_f.png", "pokefan_m.png", "pokemaniac.png", "pokemon_ranger_m.png", "ruin_maniac.png", "sailor.png", "wally.png", "young_couple.png", "gentleman.png", "guitarist.png", "hiker.png", "kindler.png", "lady.png"]
trainer_pick = rand.choice(trainer_image_list)
def resize(image, resize_factor):
    image_string = image
    image = Image.open(image)
    width, height = image.size
    w = int(width*resize_factor)
    h = int(height*resize_factor)
    image = image.resize( (w, h) )
    image = ImageTk.PhotoImage(image)
    wn.addshape(image_string, trtl.Shape("image", image))
    return image_string

def resize_grow(turtle, image, move_down):
    wn.tracer(False)
    image_string = image
    image = Image.open(image)
    width, height = image.size
    w = int(width*0.5)
    h = int(height*0.5)
    image = image.resize( (w, h) )
    not_imagetk = image
    image = ImageTk.PhotoImage(image)
    wn.addshape(image_string, trtl.Shape("image", image))
    turtle.shape(image_string)
    image = not_imagetk
    wn.tracer(True)
    turtle.setheading(270)
    for i in range(10):
        width, height = image.size
        resize_factor = 1 + (i*0.06)
        w = int(width*resize_factor)
        h = int(height*resize_factor)
        image = image.resize( (w, h) )
        not_imagetk = image
        image = ImageTk.PhotoImage(image)
        wn.addshape(image_string, trtl.Shape("image", image))
        if move_down == True:
            turtle.forward(3.5)
        turtle.shape(image_string)
        image = not_imagetk
        time.sleep(0.01)
        
#choose starter pokemon -- expand to more?
def choose_starter():
    global starter_choice, enemy_choice
    starter_choice = wn.textinput("Question", "Would you like Bulbasaur, Squirtle, or Charmander?")
    if starter_choice == None:
        print("You need to enter a name.")
        choose_starter()
        return
    elif starter_choice.isnumeric():
        print("You need to enter the name of the Pokemon, not a number.")
        choose_starter()
        return
    elif starter_choice.lower() != "bulbasaur" and starter_choice.lower() != "squirtle" and starter_choice.lower() != "charmander":
        print("That was not any of the starters. Did you misspell it?")
        choose_starter()
        return
    else:
        return
#pokemon properties class object
class Pokemon:
    def __init__(self, hp, atk, defense, spatk, spdef, spe, ability, type1, type2, name):
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.spatk = spatk
        self.spdef = spdef
        self.spe = spe
        self.ability = ability
        self.type1 = type1
        self.type2 = type2
        self.name = name
#starter stats as class objects
charmander = Pokemon(18, 10, 9, 11, 10, 11, "blaze", "fire", "none", "Charmander")
squirtle = Pokemon(19, 9, 11, 10, 11, 9, "torrent", "water", "none", "Squirtle")
bulbasaur = Pokemon(19, 9, 9, 11, 11, 9, "overgrow", "grass", "poison", "Bulbasaur")


#characteristics of a move -- sp is physical/special/status split to indicate what to do with the move
class Move:
    def __init__(self, bp, acc, effect, element, sp, effect_chance, name):
        self.bp = bp
        self.acc = acc
        self.effect = effect
        self.element = element
        self.sp = sp
        self.effect_chance = effect_chance
        self.name = name
#all moves between starters
scratch = Move(40, 90, None, "normal", "physical", 0, "Scratch")
tackle = Move(40, 90, None, "normal", "physical", 0, "Tackle")
growl = Move(0, 100, "lower_atk", "normal", "status", 100, "Growl")
tail_whip = Move(0, 100, "lower_defense", "normal", "status", 100, "Tail Whip")
vine_whip = Move(45, 90, None, "grass", "physical", 0, "Vine Whip")
ember = Move(40, 90, "burn", "fire", "special", 10, "Ember")
water_gun = Move(40, 90, None, "water", "special", 0, "Water Gun")

thisdict = bidict({
    bulbasaur : "bulbasaur",
    charmander : 'charmander',
    squirtle : "squirtle",
    scratch : "Scratch",
    tackle : "Tackle",
    growl : "Growl",
    tail_whip : "Tail Whip",
    vine_whip : "Vine Whip",
    ember : "Ember",
    water_gun : "Water Gun",
})
def draw_hp_box(turtle, which):
    global enemy_choice, starter_choice
    wn.tracer(False)
    turtle.fillcolor("#f9f8d6")
    turtle.pencolor("#1f300e")
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(285)
        turtle.right(90)
        turtle.forward(15)
        turtle.left(90)
        turtle.forward(15)
        turtle.right(90)
        turtle.forward(85)
        turtle.right(90)
        turtle.forward(15)
        turtle.left(90)
        turtle.forward(15)
        turtle.right(90)
    turtle.end_fill()
    wn.tracer(False)
    #draw info box for which enemy or rainer
    if which == "enemy":
        enemy_pokemon_name.goto(turtle.xcor() + 10, turtle.ycor() - 55)
        enemy_pokemon_name.write(enemy_choice.upper(), True, font=("fixedsys", 24, "normal"))
        enemy_pokemon_name.penup()
        enemy_pokemon_name.goto(enemy_pokemon_name.xcor() + 25, enemy_pokemon_name.ycor())
        enemy_pokemon_name.write("Lv5", font=("fixedsys", 24, "normal"))
        hp_bar.color("#5dbc8e")
        hp_bar.ht()
        hp_bar.shape("square")
        hp_bar.goto(turtle.xcor() + 142, turtle.ycor() - 80)
        hp_bar.shapesize(1, 12)
        hp_bar.stamp()
        hp_reducer.setheading(180)
        hp_reducer.goto(hp_bar.xcor() + 122, hp_bar.ycor() - 12)
    else:
        player_pokemon_name.pencolor("#413e2c")
        player_pokemon_name.goto(turtle.xcor() + 10, turtle.ycor() - 55)
        player_pokemon_name.write(starter_choice.upper(), True, font=("fixedsys", 24, "normal"))
        player_pokemon_name.penup()
        player_pokemon_name.goto(player_pokemon_name.xcor() + 20, player_pokemon_name.ycor())
        player_pokemon_name.write("Lv5", font=("fixedsys", 24, "normal"))
        hp_bar_2.color("#5dbc8e")
        hp_bar_2.shape("square")
        hp_bar_2.goto(turtle.xcor() + 142, turtle.ycor() - 80)
        hp_bar_2.shapesize(1, 12)
        hp_bar_2.stamp()
        hp_bar_2.ht()
        hp_reducer_2.setheading(180)
        hp_reducer_2.goto(hp_bar_2.xcor() + 122, hp_bar_2.ycor() - 12)
    turtle.penup()

    wn.update()

def faint(which):
    global enemy_choice, trainer_name, starter_choice, enemy_string
    if which == "enemy":
        remove_text()
        temp_text = enemy_choice.title() + " fainted!"
        do_text(temp_text)
        time.sleep(0.5)
        wn.tracer(True)
        enemy_pokemon.goto(enemy_pokemon.xcor(), enemy_pokemon.ycor() - 100)
        enemy_pokemon.ht()
        remove_text()
        do_text("You won! Get well soon!")
        time.sleep(2)
        os.abort()
    else:
        remove_text()
        temp_text = starter_choice.title() + " fainted!"
        do_text(temp_text)
        wn.tracer(True)
        starter_pokemon.goto(starter_pokemon.xcor(), starter_pokemon.ycor() - 100)
        starter_pokemon.ht()
        remove_text()
        do_text("You lost! Keep yourself safe and try again!")
        time.sleep(2)
        os.abort()
def reduce_hp(which): # which == "enemy" or "player"   # percent_damage is percent * 100 for range()
        global enemy_maxhp, player_maxhp, temp_enemy, temp_player
        wn.tracer(False)
        if which == "enemy": #hp_reducer
            hp_proportion = temp_enemy.hp / enemy_maxhp #hp_proportion = 10 / 8 = 4/5
            hp_proportion = 240 - (240 * hp_proportion) #hp_proportion = 240 - (192)
            if temp_enemy.hp <= 0:
                hp_reducer.begin_fill()
                hp_reducer.forward(242)
                hp_reducer.right(90)
                hp_reducer.forward(30)
                hp_reducer.right(90)
                hp_reducer.forward(242)
                hp_reducer.right(90)
                hp_reducer.forward(30)
                hp_reducer.end_fill()
                faint("enemy")
            hp_reducer.begin_fill()
            hp_reducer.forward(hp_proportion)
            hp_reducer.right(90)
            hp_reducer.forward(30)
            hp_reducer.right(90)
            hp_reducer.forward(hp_proportion)
            hp_reducer.right(90)
            hp_reducer.forward(30)
            hp_reducer.right(90)
            hp_reducer.end_fill()
        elif which == "player": #hp_reducer_2
            hp_proportion = temp_player.hp / player_maxhp #hp_proportion = 10 / 8 = 4/5
            hp_proportion = 240 - (240 * hp_proportion) #hp_proportion = 240 - (192)
            if temp_player.hp <= 0:
                hp_reducer_2.begin_fill()
                hp_reducer_2.forward(242)
                hp_reducer_2.right(90)
                hp_reducer_2.forward(30)
                hp_reducer_2.right(90)
                hp_reducer_2.forward(242)
                hp_reducer_2.right(90)
                hp_reducer_2.forward(30)
                hp_reducer_2.end_fill()
                faint("player") #lose condition
            hp_reducer_2.begin_fill()
            hp_reducer_2.forward(hp_proportion)
            hp_reducer_2.right(90)
            hp_reducer_2.forward(30)
            hp_reducer_2.right(90)
            hp_reducer_2.forward(hp_proportion)
            hp_reducer_2.right(90)
            hp_reducer_2.forward(30)
            hp_reducer_2.right(90)
            hp_reducer_2.end_fill()
        else:
            return
        wn.tracer(True)

def move_player():
    player_turtle.goto(-300, -99)
def move_enemy():
    enemy_turtle.goto(300, 200)
def do_text(words):
    wn.tracer(True)
    global line1_x, line2_x, line3_x
    wrapper = textwrap.TextWrapper(width=50)
    split_text = wrapper.wrap(text=words)
    line1.clear()
    line2.clear()
    line3.clear()
    line1.speed(0)
    line2.speed(0)
    line3.speed(0)
    chosen_line = 1
    line1_x = line1.xcor()
    line2_x = line2.xcor()
    line3_x = line3.xcor()
    for letter in split_text[0]:
        line1.write(letter, True, align="left", font=("fixedsys", 30, "normal"))
        time.sleep(0.01)
    if len(split_text) > 1:
        for letter in split_text[1]:
            line2.write(letter, True, align="left", font=("fixedsys", 30, "normal"))
            time.sleep(0.01)
    if len(split_text) > 2:
            for letter in split_text[2]:
                line3.write(letter, True, align="left", font=("fixedsys", 30, "normal"))
                time.sleep(0.01)
    
    if len(split_text) > 3:
        time.sleep(0.1)
        i_substitute = 3
        for i in range((len(split_text) - 3)):
            line1.goto(line1_x, line1.ycor())
            line2.goto(line2_x, line2.ycor())
            line3.goto(line3_x, line3.ycor())
            wn.tracer(False)
            line1.clear()
            line1.write(split_text[i_substitute - 2], True, align="left", font=("fixedsys", 30, "normal"))
            line2.clear()
            line2.write(split_text[i_substitute - 1], True, align="left", font=("fixedsys", 30, "normal"))
            line3.clear()
            wn.update()
            wn.tracer(True)
            for letter in split_text[i_substitute]:
                line3.write(letter, True, align="left", font=("fixedsys", 30, "normal"))
                time.sleep(0.01)
            i_substitute += 1
    wn.tracer(False)
def remove_text():
    line1.goto(line1_x, line1.ycor())
    line2.goto(line2_x, line2.ycor())
    line3.goto(line3_x, line3.ycor())
    line1.clear()
    line2.clear()
    line3.clear()
    move1.clear()
    move2.clear()
    move3.clear()
    move4.clear()
    press_space.clear()
    pointer.ht()
def trainer_approaches():
    global trainer_pick, trainer_name
    trainer_name = trainer_pick
    list_type = ""
    if "_f.png" in trainer_name:
        list_type = "lady"
        trainer_name = trainer_name.replace("_f.png", ".png")
    elif "_m.png" in trainer_name:
        list_type = "man"
        trainer_name = trainer_name.replace("_m.png", ".png")
    trainer_name = trainer_name.replace("_", " ").title()
    trainer_name = trainer_name.replace(".Png", "")
    if trainer_name == "Champion Wallace" or trainer_name == "Aqua Leader Archie" or trainer_name == "Elite_Four_Drake" or trainer_name == "Magma Leader Maxie" or trainer_name == "Leader Roxanne" or trainer_name == "Wally" or trainer_name == "Leader Wattson":
        pass
    elif trainer_name == "Aroma Lady" or trainer_name == "Battle Girl" or trainer_name == "Lady" or trainer_name == "Parasol Lady":
        list_type = "lady"
    elif trainer_name == "Bug Catcher" or trainer_name == "Ninja Boy":
        list_type = "boy"
    elif trainer_name == "Bird Keeper" or trainer_name == "Black Belt" or trainer_name == "Bug Maniac" or trainer_name == "Collector" or trainer_name == "Dragon Tamer" or trainer_name == "Fisherman" or trainer_name == "Gentleman" or trainer_name == "Guitarist" or trainer_name == "Hiker" or trainer_name == "Kindler" or trainer_name == "Pokemaniac" or trainer_name == "Ruin Maniac" or trainer_name == "Sailor" or trainer_name == "Magma Admin":
        list_type = "man"
    elif trainer_name == "Young Couple":
        list_type = "both"
    match list_type:
        case "man":
            trainer_name = trainer_name + " " + rand.choice(men_names)
        case "boy":
            trainer_name = trainer_name + " " + rand.choice(boy_names)
        case "lady":
            trainer_name = trainer_name + " " + rand.choice(women_names)
        case "both":
            trainer_name = trainer_name + " " + rand.choice(men_names) + " & " + rand.choice(women_names)
    if list_type == "both":
        trainer_wants_battle = trainer_name + " want to battle!"
    else:
        trainer_wants_battle = trainer_name + " wants to battle!"
    return trainer_wants_battle
def drop_pokeball():
    global enemy_choice, trainer_name, starter_choice, enemy_string
    wn.tracer(False)
    pokeball.st()
    #do stupid initializing for rescaling pokeball
    pokeball.shape(resize("pokeball.png", 3))

    #actually do pokeball stuff

    pokeball.goto(enemy_turtle.xcor() - 10, enemy_turtle.ycor() - 150)
    remove_text()
    wn.update()
    wn.tracer(True)
    do_text(trainer_name + " sent out " + enemy_choice.title() + "!")
    enemy_turtle.speed(5)
    wn.tracer(True)
    enemy_turtle.goto(enemy_turtle.xcor() + 600, enemy_turtle.ycor())
    pokeball.shape(resize("open_pokeball.png", 3))
    time.sleep(0.1)

    #summon enemy pokemon
    wn.tracer(False)
    enemy_pokemon.st()
    enemy_pokemon.goto(pokeball.xcor() - 30, pokeball.ycor() + 75)
    enemy_string = enemy_choice.lower() + "_front_pink.png"
    enemy_pokemon.shape(resize_grow(enemy_pokemon, enemy_string, False))
    pokeball.ht()
    enemy_string = enemy_choice.lower() + "_front.png"
    enemy_pokemon.shape(resize(enemy_string, 4))
    #set up pokeball again for red to throw
    pokeball.goto(-465, -55)
    pokeball.shape("pokeball.png")
    pokeball.ht()
    wn.update()
    wn.tracer(True)
    
    
def move_red(): # slide character off screen while throwing pokeball
    global starter_choice
    remove_text()
    player_turtle.speed(2)
    y = player_turtle.ycor()
    temp_text = "Go! " + starter_choice.title() + "!"
    do_text(temp_text)
    wn.tracer(True)
    player_turtle.goto(player_turtle.xcor() - 125, y)
    player_turtle.shape(resize("red_throw1.png", 5.5))
    player_turtle.goto(player_turtle.xcor() - 125, y)
    player_turtle.shape(resize("red_throw2.png", 5.5))
    player_turtle.goto(player_turtle.xcor() - 75, y)
    player_turtle.shape(resize("red_throw3.png", 5.5))
    player_turtle.speed(4)
    pokeball.st()
    #pokeball appears, red rushes off to complete throwing animation
    player_turtle.goto(player_turtle.xcor() - 75, y)
    player_turtle.shape(resize("red_throw4.png", 5.5))
    player_turtle.goto(player_turtle.xcor() - 225, y)
    pokeball.circle(-100, 90)
    pokeball.setheading(270)
    pokeball.forward(45)
    time.sleep(0.1)
    pokeball.shape("open_pokeball.png")
    # grow trainer pokemon
    wn.tracer(False)
    starter_pokemon.st()
    starter_pokemon.goto(pokeball.xcor() - 30, pokeball.ycor() + 75)
    starter_string = starter_choice.lower() + "_back_pink.png"
    enemy_bg.goto(300, -100)
    enemy_bg.penup()
    draw_hp_box(enemy_bg, "player")
    starter_pokemon.shape(resize_grow(starter_pokemon, starter_string, True))
    pokeball.ht()
    starter_string = starter_choice.lower() + "_back.png"
    starter_pokemon.shape(resize(starter_string, 4))

def choose_move():
    global move_select, pointer_selection, turn
    pointer.st()
    turn = "player"
    if player_move_list[0] != None:
        move1.write(player_move_list[0].upper(), False, align="center", font=("fixedsys", 30, "normal"))
    if player_move_list[1] != None:
        move2.write(player_move_list[1].upper(), False, align="center", font=("fixedsys", 30, "normal"))
    if player_move_list[2] != None:
        move3.write(player_move_list[2].upper(), False, align="center", font=("fixedsys", 30, "normal"))
    if player_move_list[3] != None:
        move4.write(player_move_list[3].upper(), False, align="center", font=("fixedsys", 30, "normal"))
    press_space.write("(press space to select move)", False, align="center", font=("fixedsys", 25, "normal"))
      
    move_select = True
def shift_pointer():
    global pointer_selection
    wn.tracer(False)
    match pointer_selection:
        case 1:
            pointer.goto(move1.xcor() - 150, move1.ycor() + 25)
        case 2:
            pointer.goto(move2.xcor() - 150, move2.ycor() + 25)
        case 3:
            pointer.goto(move3.xcor() - 150, move3.ycor() + 25)
        case 4:
            pointer.goto(move4.xcor() - 150, move4.ycor() + 25)
    wn.tracer(True)
# when you get back, finish this to get pointer shuffling to each move depending on where you go
def move_down():
    global move_select, pointer_selection
    if move_select == True:
        match pointer_selection:
            case 1:
                pointer_selection = 3
            case 2:
                pointer_selection = 4
            case 3:
                pointer_selection = 1
            case 4:
                pointer_selection = 2
        shift_pointer()

def move_left():
    global move_select, pointer_selection
    if move_select == True:
        match pointer_selection:
            case 1:
                pointer_selection = 2
            case 2:
                pointer_selection = 1
            case 3:
                pointer_selection = 4
            case 4:
                pointer_selection = 3
        shift_pointer()

def reset_battle_state():
    pass
def try_critical():
    crit = rand.randint(1, 24)
    if crit == 24:
        do_text("A critical hit!")
        time.sleep(0.5)
        remove_text()
        return True
    else:
        return False
def calc_type_effectiveness(attacking_type, defendingtype1, defendingtype2):
    effectiveness = 1
    effectiveness *= type_chart.get(attacking_type, {}).get(defendingtype1, 1)
    if defendingtype2 is not None:
        effectiveness *= type_chart.get(attacking_type, {}).get(defendingtype2, 1)
    return effectiveness

def do_anim(move, turn):
    wn.tracer(False)
    particle.st()
    if move.lower() == "water gun":
        if turn == "enemy":
            particle.shape(resize("enemy_surf.png", 3))
            particle.goto(enemy_pokemon.xcor(), enemy_pokemon.ycor() - 100)
            wn.tracer(True)
            particle.speed(1)
            particle.goto(starter_pokemon.xcor(), starter_pokemon.ycor() - 100)
        else:
            particle.shape(resize("player_surf.png", 3))
            wn.tracer(False)
            particle.goto(starter_pokemon.xcor(), starter_pokemon.ycor() + 100)
            wn.tracer(True)
            particle.speed(2)
            particle.goto(enemy_pokemon.xcor(), enemy_pokemon.ycor() + 100)
    elif move.lower() == "ember":
        particle.shape(resize("ember.png", 4))
        if turn == "enemy":
            particle.speed(3)
            particle.goto(enemy_pokemon.xcor(), enemy_pokemon.ycor() - 20)
            wn.tracer(True)
            particle.goto(starter_pokemon.xcor(), starter_pokemon.ycor() - 20)
        else:
            particle.speed(3)
            particle.goto(starter_pokemon.xcor(), starter_pokemon.ycor() - 20)
            wn.tracer(True)
            particle.goto(enemy_pokemon.xcor(), enemy_pokemon.ycor() - 20)
    elif move.lower() == "vine whip":
        particle.shape(resize("vinewhip.png", 4))
        if turn == "enemy":
            particle.speed(3)
            particle.goto(enemy_pokemon.xcor(), enemy_pokemon.ycor() - 20)
            wn.tracer(True)
            particle.goto(starter_pokemon.xcor(), enemy_pokemon.ycor() - 20)
        else:
            particle.speed(3)
            particle.goto(starter_pokemon.xcor(), starter_pokemon.ycor() - 20)
            wn.tracer(True)
            particle.goto(enemy_pokemon.xcor(), enemy_pokemon.ycor() - 20)
    elif move.lower() == "growl":
        particle.shape(resize("growl.png", 2))
        if turn == "enemy":
            particle.goto(enemy_pokemon.xcor(), enemy_pokemon.ycor() + 60)
            wn.tracer(True)
            time.sleep(0.5)
            starter_pokemon.speed(4)
            starter_pokemon.goto(starter_pokemon.xcor(), starter_pokemon.ycor() + 30)
            starter_pokemon.goto(starter_pokemon.xcor(), starter_pokemon.ycor() - 30)
            time.sleep(0.5)
        else:
            particle.goto(starter_pokemon.xcor(), starter_pokemon.ycor() + 60)
            wn.tracer(True)
            time.sleep(0.5)
            enemy_pokemon.speed(4)
            enemy_pokemon.goto(enemy_pokemon.xcor(), enemy_pokemon.ycor() + 30)
            enemy_pokemon.goto(enemy_pokemon.xcor(), enemy_pokemon.ycor() - 30)
            time.sleep(0.5)
    elif move.lower() =="tail whip":
        particle.shape(resize("tailwhip.png", 3))
        if turn == "enemy":
            particle.goto(starter_pokemon.xcor(), starter_pokemon.ycor() + 200)
            particle.backward(10)
            particle.speed(1)
            wn.tracer(True)
            particle.circle(10)
        else:
            particle.goto(enemy_pokemon.xcor(), enemy_pokemon.ycor() + 200)
            particle.backward(10)
            particle.speed(1)
            wn.tracer(True)
            particle.circle(10)
    elif move.lower() == "scratch":
        particle.shape(resize("scratch.png", 3))
        particle.speed(1)
        if turn == "enemy":
            particle.goto(starter_pokemon.xcor() + 120, starter_pokemon.ycor() + 200)
            wn.tracer(True)
            particle.goto(starter_pokemon.xcor() - 120, starter_pokemon.ycor())
        else:
            particle.goto(enemy_pokemon.xcor() + 120, enemy_pokemon.ycor() + 200)
            wn.tracer(True)
            particle.goto(enemy_pokemon.xcor() - 120, enemy_pokemon.ycor())
    elif move.lower() == "tackle":
        particle.shape(resize("tackle.png", 3))
        wn.tracer(True)
        if turn == "enemy":
            pre_xcor = enemy_pokemon.xcor()
            pre_ycor = enemy_pokemon.ycor()
            enemy_pokemon.speed(10)
            enemy_pokemon.goto(starter_pokemon.xcor(), starter_pokemon.ycor())
            wn.tracer(False)
            particle.goto(starter_pokemon.xcor(), starter_pokemon.ycor())
            wn.tracer(True)
            enemy_pokemon.goto(pre_xcor, pre_ycor)
            time.sleep(0.4)
        else:
            pre_xcor = starter_pokemon.xcor()
            pre_ycor = starter_pokemon.ycor()
            starter_pokemon.speed(10)
            starter_pokemon.goto(enemy_pokemon.xcor(), enemy_pokemon.ycor())
            wn.tracer(False)
            particle.goto(enemy_pokemon.xcor(), enemy_pokemon.ycor())
            wn.tracer(True)
            starter_pokemon.goto(pre_xcor, pre_ycor)
            time.sleep(0.4)
    particle.ht()
    time.sleep(1)

def damage_calc(newmove):
    global starter_choice, enemy_choice, turn, player_atk_count, enemy_atk_count, player_def_count, enemy_def_count, player_perma_atk, player_perma_defense, enemy_perma_atk, enemy_perma_defense, enemy_maxhp, player_maxhp
    move = thisdict.inverse[newmove.title()]
    if turn == "enemy":
        attacker = thisdict.inverse[enemy_choice]
        defender = thisdict.inverse[starter_choice]
    if turn == "player":
        attacker = thisdict.inverse[starter_choice]
        defender = thisdict.inverse[enemy_choice]
    temp_text = attacker.name + " used " + move.name + "!"
    do_text(temp_text)
    do_anim(newmove, turn)
    time.sleep(0.5)
    remove_text()
    if move.bp > 0:
        x = (4 * move.bp * (attacker.atk / defender.defense)) / 50
        x += 2
        temp_type_effectiveness = calc_type_effectiveness(move.element, defender.type1, defender.type2)
        if temp_type_effectiveness > 1:
            do_text("It was super effective!")
            time.sleep(0.5)
            remove_text()
        if temp_type_effectiveness < 1:
            do_text("It's not very effective...")
            time.sleep(0.5)
            remove_text()
        x*= temp_type_effectiveness
        if attacker.type1 == move.element or attacker.type2 == move.element:
            x *= 1.5
            time.sleep(0.5)
            remove_text()
        if try_critical() == True:
            x*=1.5
        x*= (rand.randint(85, 100) / 100)
        if x > 1:
            x = round(x)
        else:
            x = 1
        accuracy = rand.randint(1, 100)
        if move.acc > accuracy:
            defender.hp -= x
            if turn == "player":
                reduce_hp("enemy")
            else:
                reduce_hp("player")
        else:
            do_text("But it missed!")
            time.sleep(0.5)
            remove_text()
    else:
        if move.effect == "lower_defense":
            if turn == "enemy":
                if player_def_count > 5: #if stat is lowered 6 times
                    do_text("But their defense can't be lowered any further!")
                    time.sleep(0.5)
                    remove_text()
                else:
                    player_def_count += 1
                    temp_text = starter_choice.title() + "'s defense fell!"
                    match player_def_count:
                        case 0:
                            defender.defense = round((player_perma_defense * 2/3))
                        case 1:
                            defender.defense = round((player_perma_defense * 2/4))
                        case 2:
                            defender.defense = round((player_perma_defense * 2/5))
                        case 3:
                            defender.defense = round((player_perma_defense * 2/6))
                        case 4:
                            defender.defense = round((player_perma_defense * 2/7))
                        case 5:
                            defender.defense = round((player_perma_defense * 2/8))
                    do_text(temp_text)
                    time.sleep(0.5)
                    remove_text()
            else:
                if player_def_count > 5: #if stat is lowered 6 times
                    do_text("But their defense can't be lowered any further!")
                    time.sleep(0.5)
                    remove_text()
                else:
                    enemy_def_count += 1
                    temp_text = enemy_choice.title() + "'s defense fell!"
                    match enemy_def_count:
                        case 0:
                            defender.defense = round((enemy_perma_defense * 2/3))
                        case 1:
                            defender.defense = round((enemy_perma_defense * 2/4))
                        case 2:
                            defender.defense = round((enemy_perma_defense * 2/5))
                        case 3:
                            defender.defense = round((enemy_perma_defense * 2/6))
                        case 4:
                            defender.defense = round((enemy_perma_defense * 2/7))
                        case 5:
                            defender.defense = round((enemy_perma_defense * 2/8))
                    do_text(temp_text)
                    time.sleep(0.5)
                    remove_text()
        if move.effect == "lower_atk":
            #ATTACK ATTACK ATTACK
            if turn == "enemy":
                if player_atk_count > 5: #if stat is lowered 6 times
                    do_text("But their attack can't be lowered any further!")
                    time.sleep(0.5)
                    remove_text()
                else:
                    player_atk_count += 1
                    temp_text = starter_choice.title() + "'s attack fell!"
                    match player_atk_count:
                        case 0:
                            defender.atk = round((player_perma_atk * 2/3))
                        case 1:
                            defender.atk = round((player_perma_atk * 2/4))
                        case 2:
                            defender.atk = round((player_perma_atk * 2/5))
                        case 3:
                            defender.atk = round((player_perma_atk * 2/6))
                        case 4:
                            defender.atk = round((player_perma_atk * 2/7))
                        case 5:
                            defender.atk = round((player_perma_atk * 2/8))
                    do_text(temp_text)
                    time.sleep(0.5)
                    remove_text()
            else:
                if enemy_atk_count > 5: #if stat is lowered 6 times
                    do_text("But their attack can't be lowered any further!")
                    time.sleep(0.5)
                    remove_text()
                else:
                    enemy_atk_count += 1
                    temp_text = enemy_choice.title() + "'s attack fell!"
                    match player_atk_count:
                        case 0:
                            defender.atk = round((player_perma_atk * 2/3))
                        case 1:
                            defender.atk = round((player_perma_atk * 2/4))
                        case 2:
                            defender.atk = round((player_perma_atk * 2/5))
                        case 3:
                            defender.atk = round((player_perma_atk * 2/6))
                        case 4:
                            defender.atk = round((player_perma_atk * 2/7))
                        case 5:
                            defender.atk = round((player_perma_atk * 2/8))
                    do_text(temp_text)
                    time.sleep(0.5)
                    remove_text()
    if turn == "enemy":
        choose_move()
    else:
        use_enemy_move()



def decide_first():
    global starter_choice, enemy_choice
    temp_enemy = None
def use_enemy_move():
    global pointer_selection, selected_move, move_select, selected_move_anim, starter_choice, turn
    turn = "enemy"
    move_select = False
    remove_text()
    move = rand.choice(enemy_move_list)

    damage_calc(move.lower())
def use_player_move():
    global pointer_selection, selected_move, move_select, selected_move_anim, starter_choice, turn
    if move_select == True:
        if player_move_list[pointer_selection - 1] != None:
            turn = "player"
            move_select = False
            remove_text()
            move = player_move_list[pointer_selection - 1]
            damage_calc(move.lower())


#call functions#
#os.chdir('c:\\Users\\msa-jwalker1\\Downloads\\pokemon - Copy\\battle.py')
#setup screen
choose_starter()
if starter_choice.lower() == "bulbasaur":
    player_move_list = ["Tackle", "Growl", "Vine Whip", None]
elif starter_choice.lower() == "charmander":
    player_move_list = ["Scratch", "Growl", "Ember", None]
elif starter_choice.lower() == "squirtle":
    player_move_list = ["Tackle", "Tail Whip", "Water Gun", None]
temp_enemy_choice = rand.randint(1, 3)
match temp_enemy_choice:
    case 1:
        if starter_choice == "charmander":
            temp_enemy_choice = rand.randint(1, 2)
            if temp_enemy_choice == 1:
                enemy_choice = "squirtle"
                enemy_move_list = ["Tackle", "Tail Whip", "Water Gun"]
            else:
                enemy_choice = "bulbasaur"
                enemy_move_list = ["Tackle", "Growl", "Vine Whip"]
        else:
            enemy_choice = "charmander"
            enemy_move_list = ["Scratch", "Growl", "Ember"]
    case 2:
        if starter_choice == "squirtle":
            temp_enemy_choice = rand.randint(1, 2)
            if temp_enemy_choice == 1:
                enemy_choice = "charmander"
                enemy_move_list = ["Scratch", "Growl", "Ember"]
            else:
                enemy_choice = "bulbasaur"
                enemy_move_list = ["Tackle", "Growl", "Vine Whip"]
        else:
            enemy_choice = "squirtle"
            enemy_move_list = ["Tackle", "Tail Whip", "Water Gun"]
    case 3:
        if starter_choice == "bulbasaur":
            temp_enemy_choice = rand.randint(1, 2)
            if temp_enemy_choice == 1:
                enemy_choice = "squirtle"
                enemy_move_list = ["Tackle", "Tail Whip", "Water Gun"]
            else:
                enemy_choice = "charmander"
                enemy_move_list = ["Scratch", "Growl", "Ember"]
        else:
            enemy_choice = "bulbasaur"
            enemy_move_list = ["Tackle", "Growl", "Vine Whip"]
temp_player = thisdict.inverse[starter_choice]
temp_enemy = thisdict.inverse[enemy_choice]
player_perma_defense = temp_player.defense
enemy_perma_defense = temp_player.defense
player_perma_atk = temp_player.atk
enemy_perma_atk = temp_enemy.defense
player_maxhp = temp_player.hp
enemy_maxhp = temp_enemy.hp
wn.tracer(False)
#move name turtles
move1.penup()
move2.penup()
move3.penup()
move4.penup()
pointer.penup()
press_space.penup()

move1.goto(-300, -300)
move2.goto(300, -300)
move3.goto(-300, -400)
move4.goto(300, -400)
press_space.goto(0, -450)
pointer.turtlesize(2, 2)
pointer.goto(move1.xcor() - 150, move1.ycor() + 25)

move1.pencolor("white")
move2.pencolor("white")
move3.pencolor("white")
move4.pencolor("white")
press_space.pencolor("white")
wn.setup(width=1400, height=1000)
wn.title("Pokemon")
wn.screensize(1000, 400)
# wn._root.resizable(False, False)
bg_sub = trtl.Turtle()
bg_sub.penup()
bg_sub.goto(0, 130)
open('background.gif')
wn.register_shape("background.gif")
bg_sub.shape('background.gif')
#create trainer image shapes, add pokemon here later i guess


#text box
text_box = trtl.Turtle()
text_box.fillcolor("#5885b8")
text_box.ht()
text_box.pencolor("#242c36")
text_box.pensize(5)
text_box.penup()
text_box.goto(-696, -232)
text_box.pendown()
text_box.begin_fill()
text_box.forward(1380)
text_box.right(90)
text_box.forward(250)
text_box.right(90)
text_box.forward(1380)
text_box.right(90)
text_box.forward(250)
text_box.end_fill()


#text turtles that wrap around
line_turtles.append(line1)
line_turtles.append(line2)
line_turtles.append(line3)
line_increment = 0
for line in line_turtles:
    line.pencolor("white")
    line.ht()
    line.penup()
    line.goto(-675, -300 - line_increment)
    line_increment += 75
#move trainers into frame
enemy_turtle = trtl.Turtle(resize(trainer_pick, 4.5))
player_turtle = trtl.Turtle(resize("red_back.png", 5.5))
enemy_turtle.penup()
player_turtle.penup()
enemy_turtle.speed(4.5)
player_turtle.speed(4.5)
enemy_turtle.goto(-800, 200)
player_turtle.goto(800, -99)
wn.tracer(True)

wn.ontimer(move_player, 1)
wn.ontimer(move_enemy, 1)
approaching_trainer = trainer_approaches()
do_text(approaching_trainer)
time.sleep(1)
remove_text()
drop_pokeball()
wn.tracer(False)
enemy_bg = trtl.Turtle()
enemy_bg.ht()
enemy_bg.penup()
enemy_bg.goto(-600, 425)
#draw enemy hp box
draw_hp_box(enemy_bg, "enemy")
move_red()
remove_text()
choose_move()
wn.update()
wn.tracer(True)
wn.onkeypress(move_down, "s")
wn.onkeypress(move_down, "w")
wn.onkeypress(move_left, "a")
wn.onkeypress(move_left, "d")
wn.onkeypress(use_player_move, "space")
wn.listen()
wn.mainloop()