"""Funkcje pomocnicze dla planszy gry."""

import numpy as np
import random
import pygame
from constants import GREY

def draw_grid(win, rows, width):
    """Rysuje linie siatki na planszy."""
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def play_random_pitch(sound, min_pitch=0.8, max_pitch=1.2):
    """
    Modulates the pitch of a Pygame sound by resampling its data array.
    min_pitch and max_pitch are multipliers (1.0 is original pitch).
    """
    # 1. Extract the raw sound data as a NumPy array
    sound_array = pygame.sndarray.array(sound)
    
    # 2. Generate a random pitch multiplier
    pitch_factor = random.uniform(min_pitch, max_pitch)
    
    # 3. Calculate the new length of the audio array
    new_length = int(len(sound_array) / pitch_factor)
    
    # 4. Create an array of indices to sample from the original audio
    # This stretches or squashes the sound wave (nearest-neighbor interpolation)
    indices = np.linspace(0, len(sound_array) - 1, new_length).astype(int)
    
    # 5. Apply the indices to create the new resampled array
    resampled_array = sound_array[indices]
    
    # 6. Convert the modified array back into a Pygame Sound object
    pitched_sound = pygame.sndarray.make_sound(resampled_array)
    
    # 7. Play the modulated sound
    pitched_sound.play()
    
    return pitched_sound