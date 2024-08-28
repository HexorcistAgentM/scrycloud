# TekMajik: Scrycloud

**TekMajik: Scrycloud** is an adaptation of [ScryCloud from Technomancy 101](https://technomancy101.com/scrycloud/) recreated from Scratch in Python using the Pygame library.

## Description
Scrycloud generates shifting difference clouds, offering a visual medium for divining through pareidolia and liminal imagery. The program features a customizable sigil with adjustable brightness and an ambient music track playing in the background.

## How to Use
Before using Scrycloud, it is recommended to meditate and set a sacred space. A suggested ritual is [Thee Holy Rite of Konami](https://www.facebook.com/photo/?fbid=110582964071583&set=a.109709474158932) by TekMage Occult. After performing your evocation, you can gaze into the clouds and scry. 

Press `ESC` to exit at any time.

## Customization
- **Sigil**: Replace `sigil.png` with a sigil of your choice. Only the white areas will be visible, as the program treats black as transparency.
- **Music**: Replace `music.wav` with your own audio file. Pygame supports WAV, MP3, and OGG formats. If you use MP3 or OGG, you'll need to update the code on line 57:
  ```python
  music = pygame.mixer.Sound('sc_img/music.wav')

## Credits
The music track is “Beneath the Lights and Salts” by Century of Aeroplanes.
