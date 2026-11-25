---
name: download-audio-from-timestamp
description: Save the audio of a YouTube (or other yt-dlp-supported) video to ~/Downloads as an mp3, starting at a given timestamp. Use when the user wants to "record", rip, or save audio from a video link, optionally from a start time like &t=31s.
---

# Download audio from a timestamp

Download directly with yt-dlp instead of recording playback (no quality loss, no BlackHole setup).

1. Check tools: `which yt-dlp ffmpeg` (install with `brew install yt-dlp ffmpeg`).
2. Convert the start time to m:ss (`&t=31s` -> `0:31`).
3. Run:

```
cd ~/Downloads && yt-dlp -x --audio-format mp3 \
  --download-sections "*0:31-inf" \
  -o "%(title)s (from 0m31s).%(ext)s" "<URL>"
```

- `*START-inf` runs to the end; use `*START-END` for a clip.
- Use `--audio-format m4a` or `wav` for other formats.
- Confirm the file with `ls -t ~/Downloads | head`.
- Only do this for content the user has the right to keep.

Fallback if download is blocked: record playback with BlackHole 2ch plus a Multi-Output Device, capturing in QuickTime or Audacity.
