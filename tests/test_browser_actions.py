from pytest_bdd import scenarios
from steps.browser_actions_steps import *
from steps.button_steps import *
from steps.textbox_steps import *
from steps.registration_steps import *
from steps.saucedemo_steps import *
from steps.download_steps import *
from steps.drag_drop_steps import *
from steps.mouserover_steps import *
from steps.alerts_steps import *
scenarios("../features/browser_actions.feature")