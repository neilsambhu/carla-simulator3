import subprocess,os

# os.system("conda activate carla-simulator3")
# subprocess.Popen(['sh', '/data/data1/GitHub/carla-simulator3/CARLA_0.9.13/CarlaUE4.sh'])
# subprocess.Popen(['conda', 'run', '-n', 'carla-simulator3', 'python', '/data/data1/GitHub/carla-simulator3/CARLA_0.9.13/PythonAPI/examples/generate_traffic.py'])
# subprocess.Popen(['conda', 'run', '-n', 'carla-simulator3', 'python', '/data/data1/GitHub/carla-simulator3/CARLA_0.9.13/PythonAPI/examples/dynamic_weather.py'])
# subprocess.Popen(['conda', 'run', '-n', 'carla-simulator3', 'python', '/data/data1/GitHub/carla-simulator3/CARLA_0.9.13/PythonAPI/examples/manual_control.py'])

tmux = 'tmux'
subprocess.Popen(tmux)
subprocess.Popen('pwd')
import pyautogui
pyautogui.hotkey('ctrl', 'b', 'd')