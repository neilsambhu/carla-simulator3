# carla-simulator3
3/6/2022 10:07 PM: CARLA simulator on C000134 in USF ENB 221

3/9/2022 12:26 PM: example message

3/9/2022 1:45 PM: downgrade from Python 3.8.12 to 3.7:

https://github.com/carla-simulator/carla/issues/1466#issuecomment-522797557

/home/nsambhu/data1/GitHub/carla-simulator3/CARLA_0.9.13/PythonAPI/carla/carla-0.9.13-py3.7-linux-x86_64.egg

TODO: back up Python 3.8.12 environment to carla-simulator3.yml and carla-simulator3-2022-03-09-1352.yml

3/10/2022 10:00 PM: downgrade from Python 3.8.12 to 3.7.11 complete

3/10/2022 10:02 PM: successfully installed carla python module (https://github.com/carla-simulator/carla/issues/1466#issuecomment-522797557) for generate_traffic.py script

3/10/2022 10:13 PM: created environments directory; backed up Python 3.7.11 environment to carla-simulator3-2022-03-10-2210.yml

3/10/2022 10:31 PM: CARLA 0.9.13 autopilot is jerky for cars with multiple gears. Tesla Cybertruck is smoother than the gas car. Autopilot drives very slowly. SDC stops abruptly when approaching a car from behind, regardless of initial following distance: I see the SDC jerk back after every full stop.

3/24/2022 5:34 PM: 
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/scenario_runner$ python scenario_runner.py --scenario 00_scenario_name --record recording_files
Traceback (most recent call last):
  File "scenario_runner.py", line 35, in <module>
    from srunner.scenarioconfigs.openscenario_configuration import OpenScenarioConfiguration
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenarioconfigs/openscenario_configuration.py", line 24, in <module>
    from srunner.tools.openscenario_parser import OpenScenarioParser, ParameterRef
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/tools/openscenario_parser.py", line 26, in <module>
    from srunner.scenariomanager.scenarioatomics.atomic_behaviors import (TrafficLightStateSetter,
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenariomanager/scenarioatomics/atomic_behaviors.py", line 32, in <module>
    from agents.navigation.basic_agent import BasicAgent
  File "/home/nsambhu/anaconda3/envs/carla-simulator3/lib/python3.7/site-packages/agents/__init__.py", line 22, in <module>
    from . import scripts
  File "/home/nsambhu/anaconda3/envs/carla-simulator3/lib/python3.7/site-packages/agents/scripts/__init__.py", line 21, in <module>
    from . import train
  File "/home/nsambhu/anaconda3/envs/carla-simulator3/lib/python3.7/site-packages/agents/scripts/train.py", line 33, in <module>
    from agents.scripts import configs
  File "/home/nsambhu/anaconda3/envs/carla-simulator3/lib/python3.7/site-packages/agents/scripts/configs.py", line 26, in <module>
    from agents.scripts import networks
  File "/home/nsambhu/anaconda3/envs/carla-simulator3/lib/python3.7/site-packages/agents/scripts/networks.py", line 30, in <module>
    tfd = tf.contrib.distributions
AttributeError: module 'tensorflow' has no attribute 'contrib'
