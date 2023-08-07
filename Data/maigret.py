#!/usr/bin/env python3
import asyncio
import sys
import os
import subprocess
from maigret.maigret import main

def run():
    try:
        if sys.version_info.minor >= 10:
            asyncio.run(main())
        else:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())
    except KeyboardInterrupt:
        print('Maigret is interrupted.')
        dragon_tools_path = os.path.expanduser(r'"C:\Program Files\DragonTools\DragonTools-main.exe"')
        subprocess.run(['start', dragon_tools_path], shell=True)

    # Une fois que le script actuel est terminé, exécutez DragonTools-main.py
    input("Press enter for exit...")
    dragon_tools_path = os.path.expanduser(r'"C:\Program Files\DragonTools\DragonTools-main.exe"')
    subprocess.run(['start', dragon_tools_path], shell=True)

if __name__ == "__main__":
    run()
