from psychopy import visual, core, event, data, gui
import os
from pathlib import Path
import random
import csv

stim_root = "stimulus"
subject_info = {'Participant': ''}
dlg = gui.DlgFromDict(subject_info)
if not dlg.OK:
    core.quit()
win = visual.Window(fullscr=True, color=[0, 0, 0], units='height')
default_keyboard = event.BuilderKeyResponse()

welcome_img = visual.ImageStim(win, image="welcome.png", size=(0.6, 0.6))
welcome_img.draw()
win.flip()
event.waitKeys(keyList=["space", "escape"])

block_info = [
    ('app', 'f_9'),
    ('app', 'f_19'),
    ('sha', 'f_9'),
    ('sha', 'f_19')
]
results = []

for block_num, (feature_type, feature_folder) in enumerate(block_info, 1):
    image_indices = [i for i in range(5, 100, 10)]
    image_paths = [os.path.join(stim_root, feature_type, feature_folder, f"{i}.png") for i in image_indices]

    alex_img = visual.ImageStim(win, image=image_paths[0], pos=(-0.4, 0), size=(0.35, 0.35))
    taylor_img = visual.ImageStim(win, image=image_paths[-1], pos=(0.4, 0), size=(0.35, 0.35))
    instruct_text = visual.TextStim(win, text="Left = Alex [A]\nRight = Taylor [L]\nPress space to start", pos=(0, 0.1), height=0.04)
    alex_img.draw()
    taylor_img.draw()
    instruct_text.draw()
    win.flip()

    key = event.waitKeys(keyList=["space", "escape"])
    if "escape" in key:
        core.quit()
    trial_images = image_paths * 10
    random.shuffle(trial_images)

    for img_path in trial_images:
        if "escape" in event.getKeys(keyList=["escape"]):
            core.quit()
        fixation = visual.TextStim(win, text="+", height=0.2)
        fixation.draw()
        win.flip()
        core.wait(0.3)
        stim = visual.ImageStim(win, image=img_path, size=(0.35, 0.35))
        stim.draw()
        win.flip()
        core.wait(0.5)
        choice_text = visual.TextStim(win, text="Alex [A]     or     Taylor [L]", pos=(0, -0.3), height=0.04)
        stim.draw()
        choice_text.draw()
        win.flip()

        keys = event.waitKeys(keyList=["a", "l", "escape"])
        if "escape" in keys:
            core.quit()

        chosen = "alex" if keys[0] == "a" else "taylor"

        image_name = Path(img_path).stem
        results.append([block_num, int(image_name), chosen])

        win.flip()
        core.wait(0.3)

data_folder = "data"
os.makedirs(data_folder, exist_ok=True)
filename = f"{data_folder}/{subject_info['Participant']}_responses.csv"
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["block", "image_number", "chosen"])
    writer.writerows(results)
thanks = visual.TextStim(win, text="Thank you!\nPress ESC to exit", height=0.05)
thanks.draw()
win.flip()
event.waitKeys(keyList=["escape"])

core.quit()
