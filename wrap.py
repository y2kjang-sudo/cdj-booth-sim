#!/usr/bin/env python3
"""Turn the booth page into a standalone index.html.

The page is written in Claude artifact form: no <!doctype>, <html>, <head> or
<body> tags, because the artifact host wraps it in a skeleton that adds them.
GitHub Pages serves the file as it is, so this script adds that skeleton:
- a doctype and <html lang="ko">;
- a <head> with the charset, a viewport meta (viewport-fit=cover) and a zero
  body margin;
- a <body> around the page content.

Usage:  python3 wrap.py booth.html index.html
"""
import sys

SPLIT = "</style>"  # the page's head material ends with its first <style> block


def wrap(src: str) -> str:
    if src.lstrip().lower().startswith("<!doctype"):
        return src  # already standalone
    i = src.find(SPLIT)
    if i < 0:
        raise SystemExit("no </style> found; cannot tell head from body")
    i += len(SPLIT)
    head, body = src[:i], src[i:]
    head = head.replace('<meta charset="utf-8">', "", 1).lstrip()
    return (
        "<!doctype html>\n<html lang=\"ko\">\n<head>\n"
        "<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
        "<style>html,body{margin:0}:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}</style>\n"
        + head
        + "\n</head>\n<body>\n"
        + body.strip("\n")
        + "\n</body>\n</html>\n"
    )


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    with open(sys.argv[1], encoding="utf-8") as f:
        out = wrap(f.read())
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        f.write(out)
