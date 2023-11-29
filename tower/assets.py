import importlib.resources
import pygame

SPRITES = {
    "game_logo": "game_logo.png",
    "land": "land.png",
    "road": "road.png"
}
IMAGE_SPRITES = None

CHANNELS = {
    "footsteps": None,
    "turrets": None,
    "score": None,
}

def load(module_path, name):
    return importlib.resources.path(module_path, name)

def import_image(asset_name: str):
    with load("tower.assets.gfx", asset_name) as resource:
        return pygame.image.load(resource).convert_alpha()
    
def import_sound(asset_name: str):
    """
    Imports, as a sound effect, `asset_name`.
    """
    with load("tower.assets.audio", asset_name) as resource:
        return pygame.mixer.Sound(resource)
    
for sprite_index, sprite_name in SPRITES.items():
    img = import_image(sprite_name)
    for flipped_x in (True, False):
        for flipped_y in (True, False):
            new_img = pygame.transform.flip(img, flip_x=flipped_x, flip_y=flipped_y)
            IMAGE_SPRITES[(flipped_x, flipped_y, sprite_index)] = new_img

for channel_id, channel_name in enumerate(CHANNELS):
    CHANNELS[channel_name] = pygame.mixer.Channel(channel_id)
    # Configure the volume here.
    CHANNELS[channel_name].set_volume(1.0)