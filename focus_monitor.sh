#!/bin/bash
while true; do
  window_id=$(xdotool getwindowfocus)
  window_name=$(xdotool getwindowfocus getwindowname)
  echo "$window_id|$window_name"
  sleep 1
done

