from config.config import *
from lib.modes.visual_mode import *
from lib.overlay_manipulation import update_overlay_image
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.0
import math

class HollowknightMode(VisualMode):

    current_overlay_image = 'coords-overlay'

    patterns = [
        {
            'name': 'map',
            'sounds': ['sound_whistle'],
            'threshold': {
                'percentage': 80,
                'power': 10000,
                'below_frequency': 54
            },            
            'throttle': {
                'map': 0.5,
                'inventory': 0.5
            }
        },
        {
            'name': 'inventory',
            'sounds': ['sound_whistle'],
            'threshold': {
                'percentage': 80,
                'power': 10000,
                'frequency': 55
            },            
            'throttle': {
                'map': 0.5,
                'inventory': 0.5
            }
        },
        {
            'name': 'movement_modes',
            'sounds': ['vowel_iy', 'vowel_y'],
            'threshold': {
                'percentage': 80,
                'power': 10000
            },            
            'throttle': {
                'movement_modes': 0.2,
                'spell': 0.2
            }
        },
        {
            'name': 'set_coordinate',
            'sounds': ['vowel_ae'],
            'threshold': {
                'percentage': 80,
                'power': 10000
            },            
            'throttle': {
                'set_coordinate': 0.2
            }
        },
        {
            'name': 'set_coordinate_right',
            'sounds': ['vowel_ow', 'approximant_l'],
            'threshold': {
                'percentage': 87,
                'power': 10000,
            },
            'throttle': {
                'set_coordinate_right': 0.1,
                'set_coordinate_left': 0.1,
                'set_coordinate': 0.2,
                'prepare_attack': 0.1,
            }
        },
        {
            'name': 'set_coordinate_left',
            'sounds': ['vowel_aa', 'thrill_r', 'vowel_ah'],
            'threshold': {
                'percentage': 87,
                'power': 10000,
            },            
            'throttle': {
                'set_coordinate_right': 0.1,
                'set_coordinate_left': 0.1,
                'set_coordinate': 0.2,
            }
        },        
        {
            'name': 'press_arrowkeys',
            'sounds': ['vowel_ah'],
            'threshold': {
                'percentage': 90,
                'power': 10000
            },
            'throttle': {
                'press_arrowkeys': 0.15
            }
        },
        {
            'name': 'hold_arrowkeys',
            'sounds': ['nasal_n', 'nasal_m'],
            'threshold': {
                'percentage': 70,
                'power': 20000
            }
        },        
        {
            'name': 'slash',
            'sounds': ['click_alveolar'],
            'threshold': {
                'percentage': 82,
                'power': 12000
            },
            'throttle': {
                'slash': 0.12
            }
        },
        {
            'name': 'up_slash',
            'sounds': ['click_dental', 'click_lateral'],
            'threshold': {
                'percentage': 80,
                'power': 8000
            },
            'throttle': {
                'jump': 0.1,
                'up_slash': 0.1,
                'down_slash': 0.1,
                'menu': 0.5
            }
        },
        {
            'name': 'down_slash',
            'sounds': ['sibilant_sh'],
            'threshold': {
                'percentage': 90,
                'power': 5000
            },
            'throttle': {
                'jump': 0.1,            
                'down_slash': 0.1,
                'up_slash': 0.1,
                'menu': 0.5
            }
        },
        {
            'name': 'prepare_attack',
            'sounds': ['vowel_oh'],
            'threshold': {
                'percentage': 95,
                'power': 15000
            },
            'throttle': {
                'prepare_attack': 0.2
            }
        },        
        {
            'name': 'dream_nail',
            'sounds': ['sound_pop'],
            'threshold': {
                'percentage': 90,
                'power': 10000
            },
            'throttle': {
                'dream_nail': 0.1,
                'down_slash': 0.1,
                'up_slash': 0.1
            }
        },
        {
            'name': 'charge',
            'sounds': ['approximant_r'],
            'threshold': {
                'percentage': 90,
                'power': 12000,
                'times': 4
            },
            'continual_threshold': {
                'power': 3000,
            },
            'throttle': {
                'slash': 0.1,
                'spell': 0.2
            }
        },
        {
            'name': 'attack_charge',
            'sounds': ['vowel_e'],
            'threshold': {
                'percentage': 90,
                'power': 20000,
                'times': 3
            },
            'continual_threshold': {
                'power': 3000,
            },
            'throttle': {
                'movement_modes': 0.2
            }
        },
        {
            'name': 'spell',
            'sounds': ['thrill_thr'],
            'threshold': {
                'percentage': 95,
                'power': 12000
            },
            'throttle': {
                'spell': 0.2
            }
        },
        {
            'name': 'directional_spell',
            'sounds': ['stop_implosive_velar', 'thrill_bilabial'],
            'threshold': {
                'percentage': 95,
                'power': 100000,
                'times': 2
            },
            'throttle': {
                'directional_spell': 0.2
            }
        },        
        {
            'name': 'dash',
            'sounds': ['fricative_f'],
            'threshold': {
                'percentage': 96,
                'power': 12000
            },
            'throttle': {
                'dash': 0.3,
                'invert_movement': 0.3
            }
        },
        {
            'name': 'hyper_dash',
            'sounds': ['sibilant_zh'],
            'threshold': {
                'percentage': 90,
                'power': 12000,
                'times': 4
            },
            'continual_threshold': {
                'power': 3000,
            },
            'throttle': {
                'jump': 0.2
            }
        },
        {
            'name': 'jump',
            'sounds': ['sibilant_s', 'sibilant_z'],
            'threshold': {
                'percentage': 90,
                'power': 4000
            },
            'continual_threshold': {
                'percentage': 32,
                'power': 2500
            },
            'throttle': {
                'up_slash': 0.05
            }
        },
        {
            'name': 'inverse_jump',
            'sounds': ['fricative_v'],
            'threshold': {
                'percentage': 95,
                'power': 20000,
                'times': 3
            },
            'continual_threshold': {
                'power': 2000
            },
            'throttle': {
                'jump': 0.13
            }            
        },        
        {
            'name': 'jump_horizontal',
            'sounds': ['sibilant_s'],
            'threshold': {
                'power': 40000
            },
            'continual_threshold': {
                'power': 20000
            }            
        },
        {
            'name': 'menu',
            'sounds': ['sound_finger_snap'],
            'threshold': {
                'percentage': 99,
                'power': 60000,
                'times': 3
            },
            'throttle': {
                'menu': 0.5
            }
        },
        {
            'name': 'mute',
            'sounds': ['sound_call_bell'],
            'threshold': {
                'percentage': 95,
                'power': 50000,
                'times': 5
            },
            'throttle': {
                'mute': 0.5
            }
        }
    ]
    
    file_skip_number = 0
    hold_arrow_keys = []
    
    def start(self):
        super().start()
        self.enable('single-press-grid')
        self.disable('actions-muted')
        update_overlay_image(self.current_overlay_image)
        
    def handle_input( self, dataDicts ):
        super().handle_input( dataDicts )  
        
        if (not self.detect("actions-muted")):
            self.file_skip_number = self.file_skip_number + 1
        
            if ("X-" in self.detector.tickActions or "F-" in self.detector.tickActions ):
                self.release('down')
                
                # Reapply the horizontal movement afterwards
                for key in self.hold_arrow_keys:
                    if ( key in ['left', 'right', 'down'] ):
                        self.hold( key )
            elif ("X+" in self.detector.tickActions or "F+" in self.detector.tickActions):
                self.release('up')

                # Reapply the horizontal movement afterwards
                for key in self.hold_arrow_keys:
                    if ( key in ['left', 'right', 'up'] ):
                        self.hold( key )

            # Only update the overlay file every 15 frames
            # For performance reasons
            if (self.file_skip_number > 15):
                self.file_skip_number = 0
                x_diff = self.detector.pointerController.detect_origin_difference('x')
                if (self.detect('movement_inverted')):
                    x_diff = x_diff * -1
                x_distance = abs(x_diff)
                new_overlay_image = self.current_overlay_image
                if (x_distance < 50):
                    new_overlay_image = 'coords-overlay'
                elif (x_distance >= 50 and x_distance < 200):
                    new_overlay_image = 'coords-overlay-medium' if x_diff < 0 else 'coords-overlay-medium-right'
                elif (x_distance >= 200):
                    new_overlay_image = 'coords-overlay-long' if x_diff < 0 else 'coords-overlay-long-right'
                    
                if (self.detect('attack_prepared')):
                    new_overlay_image = 'primed-' + new_overlay_image
                    
                if (new_overlay_image != self.current_overlay_image):
                    update_overlay_image(new_overlay_image)
                    self.current_overlay_image = new_overlay_image
        return self.detector.tickActions
            
    def handle_sounds( self, dataDicts ):
        disable_movement = False
        
        # MUTE actions except the unmute action
        if (self.detect("actions-muted")):
            if (self.detect('mute')):
                self.disable('actions-muted')
                self.print_key('UNMUTE')
            return
    
        if (self.detect('slash')):
            self.press('x')
            return
        elif (self.detect('spell')):
            self.press('f')
            return
        elif (self.detect('dash')):
            self.press('c')
            return
        elif (self.detect('up_slash')):
            # Release horizontal movement temporarily
            for key in self.hold_arrow_keys:
                if ( key in ['left', 'right', 'down'] ):
                    self.release( key )
            self.hold('up')
            self.press('x')
            self.print_key('X+')
            disable_movement = True
        elif (self.detect('down_slash')):
            # Release horizontal movement temporarily
            for key in self.hold_arrow_keys:
                if ( key in ['left', 'right', 'up'] ):
                    self.release( key )
                                  
            self.hold('down')
            self.press('x')
            self.print_key('X-')
            disable_movement = True
        elif (self.detect('directional_spell')):
            # Release horizontal movement temporarily
            for key in self.hold_arrow_keys:
                if ( key in ['left', 'right'] ):
                    self.release( key )

            # Do a spell cast depend on the location where the user is looking
            if (self.quadrant3x3 <= 3 ):
                self.release('down')
                self.hold('up')
                self.press('f')
                self.print_key('F+')
            elif (self.quadrant3x3 >= 7 ):
                self.release('up') 
                self.hold('down')
                self.press('f')
                self.print_key('F-')
            else:
                self.detector.clear_throttle('directional_spell')
            disable_movement = True            
        elif (self.detect('menu')):
            self.press('esc')
            self.toggle_singlepress(True)
        elif (self.detect('movement_modes')):
            self.toggle_singlepress(True)
            self.print_key('Stop')
        elif (self.detect('set_coordinate')):
            self.detector.pointerController.update_origin_coords()
            self.print_key('Point')            
            return
        elif (self.detect('set_coordinate_left')):
            self.detector.pointerController.set_origin_coords_center_left()
            self.disable('movement_inverted')
            self.print_key('<Point')
            return
        elif (self.detect('set_coordinate_right')):
            self.detector.pointerController.set_origin_coords_center_right()
            self.disable('movement_inverted')            
            self.print_key('Point>')
            return
        elif (self.detect("mute")):
            self.enable('actions-muted')
            self.print_key('MUTE')
            self.release_arrowkeys()
            self.current_overlay_image = 'coords-overlay'
            update_overlay_image(self.current_overlay_image)
            return
        elif (self.detect('dream_nail')):
            self.toggle('dream_nail_held')
            if (self.detect('dream_nail_held')):
                self.inputManager.keyDown('d')
                self.print_key('D')
            else:
                self.inputManager.keyUp('d')
             
        # Toggle the map open
        elif (self.detect('map')):
            self.toggle('tab')
            if (self.detect('tab')):
                self.inputManager.keyDown('tab')
                self.print_key('TAB')                
            else:
                self.inputManager.keyUp('tab')                
        elif (self.detect('inventory')):
            self.press('i')
            self.toggle_singlepress(True)
        
        # Make it possible to jump for various lengths of time
        regular_jump_held = self.detect('jump')
        inverse_jump_held = not regular_jump_held and self.detect('inverse_jump')
        if (inverse_jump_held):
            self.enable('movement_inverted')
        else:
            self.disable('movement_inverted')

        if (regular_jump_held or inverse_jump_held):
            if (self.detect('aerial-movement') == False):
                self.inputManager.keyDown('space')
                self.enable('aerial-movement')
                self.print_key('SPACE')
        elif (self.detect('aerial-movement')):
            self.inputManager.keyUp('space')
            self.disable('aerial-movement')
            self.release_arrowkeys()
            # If an attack was stored - Release it in the up direction
            self.check_attack_prepared('down')
            
        # Make it possible to charge A
        if (self.detect('charge')):
            disable_movement = True
            if (self.detect('charge-held') == False):
                self.inputManager.keyDown('a')
                self.print_key('a')
                self.enable('charge-held')
        elif (self.detect('charge-held')):
            self.inputManager.keyUp('a')
            self.disable('charge-held')
            
        # Make it possible to charge X
        if (self.detect('attack_charge')):
            if (self.detect('attack-held') == False):
                self.inputManager.keyDown('x')
                self.print_key('x')
                self.enable('attack-held')
        elif (self.detect('attack-held')):
            self.inputManager.keyUp('x')
            self.disable('attack-held')
            
        # Make it possible to charge S
        if (self.detect('hyper_dash')):
            disable_movement = True
            if (self.detect('dash-held') == False):
                self.inputManager.keyDown('s')
                self.print_key('S')
                self.enable('dash-held')
        elif (self.detect('dash-held')):
            self.inputManager.keyUp('s')
            self.disable('dash-held')

        if (self.detect('hold_arrowkeys')):
            if (self.detect('manual-movement') == False):
                self.enable('manual-movement')
        elif (self.detect('manual-movement')):
            self.disable('manual-movement')
            self.release_arrowkeys()
                    
        # Prepare an attack for the future whenever movement changes
        if (self.detect('prepare_attack')):
            self.enable('attack_prepared')
            self.print_key('delay X')
            disable_movement = True
            
        # Movement types
        # Aerial movement
        if (self.detect('aerial-movement')):
            #if (self.detect('jump_horizontal')):
            self.handle_arrowkeys(dataDicts, "relative", False, 60, ['left', 'right'])
            #else:
            #    if ( len(self.hold_arrow_keys) > 0 ):
            #        for key in self.hold_arrow_keys:
            #            self.release( key )
            #        self.hold_arrow_keys = []
            
        # Manual movement
        elif (self.detect('manual-movement')):
            self.disable('precision-movement')
            self.handle_arrowkeys(dataDicts, "relative", True, 60, ['left', 'right'])
            
        # Precision movement - Button presses
        elif (self.detect('precision-movement')):
            if (self.detect('press_arrowkeys')):
                self.press_arrowkeys(dataDicts)

        # Regular eyetracker movement
        elif ( not disable_movement ):
            self.handle_arrowkeys(dataDicts, "relative", False, 200)

    def check_attack_prepared(self, direction='regular'):
        if (self.detect('attack_prepared')):
            if (direction == 'up'):
                self.inputManager.keyDown('up')
            elif (direction == 'down'):
                self.inputManager.keyDown('down')

            self.press('x')
            if (direction == 'up'):
                self.inputManager.keyUp('up')
            elif (direction == 'down'):
                self.inputManager.keyUp('down')
                
            self.disable('attack_prepared')

    def toggle_singlepress( self, enable=False ):
        print( 'Toggling arrowkey mode' )
        if (enable == True):
            self.enable('precision-movement')
        else:
            self.toggle('precision-movement')
        self.release_arrowkeys()

    def release_arrowkeys( self ):
        if ( len(self.hold_arrow_keys) > 0 ):
            for key in self.hold_arrow_keys:
                self.release( key )

        self.hold_arrow_keys = []    
                
    def handle_arrowkeys( self, dataDicts, mode = "edges", log=False, radius=100, valid_edges=['left', 'up', 'right', 'down']):
        edges = self.handle_grid(mode, radius)                   
        if ( len(self.hold_arrow_keys) > 0 ):
            for key in self.hold_arrow_keys:
                if ( key not in edges ):
                    self.release( key )

        if ( len(edges) > 0 ):
            for key in edges:
                if ( key not in self.hold_arrow_keys and key in valid_edges ):
                    self.hold( key )
                    if (log == True):
                        self.print_key( key )
        self.hold_arrow_keys = edges

    def press_arrowkeys( self, dataDicts):
        edges = self.handle_grid()
        if ( len(edges) > 0 ):
            for key in edges:
                self.press( key )

    def handle_grid( self, mode = "edges", radius=100 ):
        if (mode == "edges" ):
            hold_arrowkeys = self.detector.detect_mouse_screen_edge( 200 )
                
            if ('left' not in hold_arrowkeys and ( self.quadrant3x3 == 1 or self.quadrant3x3 == 4 or self.quadrant3x3 == 7 ) ):
                hold_arrowkeys.append( 'left' )
            elif ('right' not in hold_arrowkeys and ( self.quadrant3x3 == 3 or self.quadrant3x3 == 6 or self.quadrant3x3 == 9 ) ):
                hold_arrowkeys.append( 'right' )
        elif (mode == "relative"):
            hold_arrowkeys = self.detector.pointerController.detect_origin_directions( radius, 400, self.detect('movement_inverted'))
            
        return hold_arrowkeys
