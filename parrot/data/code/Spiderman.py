from config.config import *
from lib.modes.base_mode import *

class TutorialMode(BaseMode):
    patterns = [
        {
            'name': 'loud',
            'sounds': ['4mouthclick'],
            'threshold': {
                'percentage': 70,
            },
            'throttle': {
                'loud': 0.3
            }
        },
        {
            'name': 'louder',
            'sounds': ['4a'],
            'threshold': {
                'percentage': 30,
            },
            'throttle': {
                'louder': 0.3
            }
        },
        {
            'name': 'down_key',
            'sounds': ['4oh'],
            'threshold': {
                'percentage': 70,
            },
            'throttle': {
                'down_key': 0.3
            }
        },
        {
            'name': 'right_key',
            'sounds': ['4ooo'],
            'threshold': {
                'percentage': 30,
            },
            'throttle': {
                'right_key': 0.3
            }
        },
        {
            'name': 'up_key',
            'sounds': ['4i'],
            'threshold': {
                'percentage': 70,
            },
            'throttle': {
                'up_key': 0.3
            }
        },
        {
            'name': 'right_key',
            'sounds': ['uu'],
            'threshold': {
                'percentage': 50,
            },
            'throttle': {
                'right_key': 0.3
            }
        },
        {
            'name': 'kiss_key',
            'sounds': ['vvv'],
            'threshold': {
                'percentage': 50,
            },
            'throttle': {
                'kiss_key': 0.3
            }
        },
 
    ]
    use_direct_keys = True
    input_release_lag = 0.0
    
    def handle_sounds(self, dataDicts):
        if self.detect('louder'):
            self.press('k')  # Changed 'a' to 'k'
        elif self.detect('down_key'):
            self.press('n')  # Changed 'o' to 'n'
        elif self.detect('up_key'):
            self.press('m')  # Changed 'i' to 'm'
        elif self.detect('loud'):
            self.press('r')
        elif self.detect('right_key'):
            self.press('y')
        elif self.detect('kiss_key'):
            self.press('t')