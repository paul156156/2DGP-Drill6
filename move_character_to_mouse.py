from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

hand_x = random.randint(0, TUK_WIDTH)
hand_y = random.randint(0, TUK_HEIGHT)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def move_towards(x, y, target_x, target_y, speed):
    dx, dy = target_x - x, target_y - y
    distance = (dx**2 + dy**2) ** 0.5
    if distance == 0:
        return x, y
    dx, dy = dx / distance, dy / distance
    return x + dx * speed, y + dy * speed

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()
speed = 1
direction = 0

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if direction == 0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    hand.draw(hand_x, hand_y)
    update_canvas()
    frame = (frame + 1) % 8

    new_x, new_y = move_towards(x, y, hand_x, hand_y, speed)
    if new_x < x:
        direction = 1
    elif new_x > x:
        direction = 0
    x, y = new_x, new_y

    if abs(x - hand_x) < speed and abs(y - hand_y) < speed:
        hand_x = random.randint(0, TUK_WIDTH)
        hand_y = random.randint(0, TUK_HEIGHT)

    handle_events()

close_canvas()




