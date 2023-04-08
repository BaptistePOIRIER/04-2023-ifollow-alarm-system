import keyboard

pressed_keys = set()

def key_event(event):
    key_name = event.name

    # Check if it's a key press event
    if event.event_type == keyboard.KEY_DOWN:
        if key_name not in pressed_keys:
            pressed_keys.add(key_name)
            print(f'Key Pressed: {key_name}')
    # Check if it's a key release event
    elif event.event_type == keyboard.KEY_UP:
        if key_name in pressed_keys:
            pressed_keys.remove(key_name)
            print(f'Key Pressed: {key_name}')

# Register the event handler
keyboard.hook(key_event)

# Wait for events
keyboard.wait()