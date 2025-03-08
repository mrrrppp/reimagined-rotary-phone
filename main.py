from jnius import autoclass

# Get the Android Activity class
PythonActivity = autoclass("org.kivy.android.PythonActivity")

def close_app():
    """Closes the app as soon as it opens."""
    activity = PythonActivity.mActivity
    activity.finish()  # Closes the app

# Run close_app() when the app starts
close_app()