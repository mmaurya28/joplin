from .test_cases.title import title
from .test_cases.mission import mission
from .test_cases.kitchen_sink import kitchen_sink

# You can import any test_case fixture individually
# Or you can load them all with this function
def load_all():
    title()
    mission()
    kitchen_sink()
