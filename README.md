# cdj-booth-sim

A practice booth in one HTML file: two CDJ-3000 players and a DJM-2000NXS mixer. It is meant for someone who knows the XDJ-RX3 and is about to play a club booth for the first time.

Open `index.html` in a desktop browser. The first click turns the sound on. The page needs no server and no build step; fonts load from Google Fonts.

## What is in it

- **Missions.** Step-by-step tasks highlight the control to press next.
  - **Booth / player:** USB and browse, PRO DJ LINK, MASTER and BEAT SYNC, beatmatching by hand, hot cues, loops, tempo range and MASTER TEMPO, ejecting the USB safely.
  - **Mixer differences from the RX3:** finding your channel, the input selector, the INST FX filter, BEAT EFFECT, the touch panel's FREQUENCY MIX, EQ versus ISOLATOR, crossfader assign and curve, headphones, level meters.
- **Mixer layout.** It follows the control panel diagram and the INST FX, BEAT EFFECT and TOUCH PANEL EFFECT chapters of the DJM-2000NXS operating instructions (DRB1636A, pages 11–18 and 25). Each mixer mission names the manual page it comes from.
- **Player layout.** It follows the CDJ-3000 operating instructions (DRI1586A): top panel (pp. 14–16), touch display (pp. 21–23), jog display (p. 26). The loop, hot cue and beat jump buttons behave as pp. 54–62 describe. Above the big waveform, the strip of p. 22 item 10 shows the offset from the sync master. It shows the master's waveform and beat grid at the same scale, with the offset in ms. Touching the strip switches it to the phase meter.
- **Your own USB.** Choose the root folder of a rekordbox export USB. The page reads the following, and plays the files in the browser:
  - from `PIONEER/rekordbox/export.pdb`: tracks, artists, keys and playlists;
  - from each track's ANLZ `.DAT`: the beat grid, hot cues and memory cues.

  Plain audio files also work; their BPM and first beat are estimated. Everything is read locally and nothing is written to the USB.

## Limits

- **Sound.** The demo tracks are synthesized in the browser.
  - The mixer effects are approximations. ZIP, GATE, PHASER and REV ROLL are simplified.
  - BEAT SLICE REMIX, SIDECHAIN REMIX and LIVE SAMPLER show their screens only.
- **Uploaded tracks.** MASTER TEMPO does not apply to uploaded tracks; changing their tempo also changes their pitch.
- **Tested so far.** The `export.pdb` parser was checked against two real exports. ANLZ cue reading has not been checked against a real file.
