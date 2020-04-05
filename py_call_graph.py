import pytest
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
from pycallgraph.config import Config
from pycallgraph.globbing_filter import GlobbingFilter


@pytest.fixture(autouse=True)
def record_call_graph(request):
    import time
    current_millis = int(round(time.time() * 1000))
    # import pdb
    # pdb.set_trace()
    with PyCallGraph(output=GraphvizOutput(output_file='dynCG.png', dot_file='./dotFiles/%s.dot' %
                                                                             (current_millis)),
                     config=Config(debug=True,
                                   trace_filter=GlobbingFilter(
                                       exclude=['pycallgraph.*', 'utils.*','fire_import_test.*','interact_test.*','decorators_test.*','test_components_test.*','docstrings_test.*','trace_test.*','helptext_test.*','fire_test.*','completion_test.*','parser_test.*','custom_descriptions_test.*','core_test.*','parser_fuzz_test.*','formatting_test.*','docstrings_fuzz_test.*','main_test.*','testutils_test.*','inspectutils_test.*'],
                                       include=['fire.*'],
                                   )
                                   )):
        yield
