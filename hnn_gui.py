import logging
from neuron import h

from geppettoJupyter.geppetto_comm import GeppettoCoreAPI as G
import neuron_utils
import neuron_geometries_utils

class HNN:

    def __init__(self):
        logging.debug('Loading HNN')
        neuron_utils.createProject(name='HNN')
        import run

        self.t_vec = h.Vector()
        self.t_vec.record(h._ref_t)
        neuron_utils.createStateVariable(id='time', name='time',
                              units='ms', python_variable={"record_variable": self.t_vec,
                                                           "segment": None})

        neuron_geometries_utils.extractGeometries()

        logging.debug('HNN loaded')
