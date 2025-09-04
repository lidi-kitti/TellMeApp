#!/bin/bash

# Start Xvfb in the background
Xvfb :99 -screen 0 1024x768x24 -ac +extension GLX +render -noreset &
XVFB_PID=$!

# Wait for Xvfb to start
sleep 3

# Check if Xvfb is running
if ! kill -0 $XVFB_PID 2>/dev/null; then
    echo "Failed to start Xvfb"
    exit 1
fi

# Set display environment
export DISPLAY=:99
export SDL_VIDEODRIVER=x11
export MESA_GL_VERSION_OVERRIDE=3.3

# Start the Python application
python main.py

# Clean up
kill $XVFB_PID
