# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 13:37:30 2018

@author: Raju
"""
# -*- coding: utf-8 -*-
"""
This module implements NEvent Class for NeuroChaT software

@author: Md Nurul Islam; islammn at tcd dot ie

"""

import logging

from collections import OrderedDict as oDict

import numpy as np

from neurochat.nc_base import NBase
from neurochat.nc_spike import NSpike
from neurochat.nc_lfp import NLfp


class NEvent(NBase):
    """
    This data class is the placeholder for the dataset that contains information
    about external events or stimulus.
    Events are stored as names and tags. Each tag is a number representing particular event.

    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._event_names = []
        self._event_trig_averages = []
        self._curr_tag = []
        self._curr_name = []
        self._timestamp = np.array([], dtype='f')
        self._event_train = np.array([], dtype=int)
        self._type = 'event'

    def get_event_name(self, event_tag=None):
        """
        Returns name of the event from its tag

        Parameters
        ----------
        event_tag : int

        Returns
        -------
        event_name : str
            Name of the event

        """

        if event_tag is None:
            event_name = self._event_names
        elif event_tag in self._event_train:
            event_name = self._event_names[self._event_train.index(event_tag)]
        else:
            event_name = None
        return event_name

    def get_tag(self, event_name=None):
        """
        Returns tag of the event from its name

        Parameters
        ----------
        event_name : str

        Returns
        -------
        event_tag : int
            Tag of the event

        """

        if event_name is None:
            event_tag = self._curr_tag
        elif event_name == 'all':
            event_tag = self._event_trig_averages
        elif event_name in self._event_names:
            event_tag = self._event_train[self._event_names.index(event_name)]
        else:
            event_tag = None

        return event_tag

    def set_curr_tag(self, event):
        """
        Sets current tag of to cosider for analysis

        Parameters
        ----------
        event : str or int
            If str, represent the name of the event. If int, represents event tag

        Returns
        -------
        None

        """

        if event is None:
            pass
        elif event in self._event_train:
            self._curr_tag = event
            self._curr_name = self.get_event_name(event)
        elif event in self._event_names:
            self._curr_tag = self.get_tag(event)
            self._curr_name = event

    def set_curr_name(self, name):
        """
        Sets current event using event name

        Parameters
        ----------
        name : str
            Name of the event

        Returns
        -------
        None

        """

        self.set_curr_tag(name)

    def get_event_stamp(self, event=None):
        """
        Returns timestamps for a particular event

        Parameters
        ----------
        event : str or int
            If str, represent the name of the event. If int, represents event tag

        Returns
        -------
        timestamp : ndarray
            Timestamps of the event

        """

        if event is None:
            event = self._curr_tag
        if event in self._event_names:
            tag = self.get_tag(event)
        elif event in self._event_trig_averages:
            tag = event
        timestamp = self._timestamp[self._event_train == tag]

        return timestamp

    def get_timestamp(self):
        """
        Returns timestamps for all events

        Parameters
        ----------
        None

        Returns
        -------
        timestamp : ndarray
            Timestamps of all the events

        """

        return self._timestamp

    def _set_timestamp(self, timestamp):
        """
        Sets timestamps for all events

        Parameters
        ----------
        timestamp : ndarray

        Returns
        -------
        timestamp : ndarray
            Timestamps of all the events

        """

        self._timestamp = timestamp

    def get_event_train(self):
        """
        Returns tags for all events in the same temporal order as they are presented

        Parameters
        ----------
        None

        Returns
        -------
        ndarray
            Train of events as train of tags

        """

        return self._event_train

    def _set_event_train(self, event_train):
        """
        Sets tags for all events

        Parameters
        ----------
        event_train : ndarray
            Train of events as train of tags

        Returns
        -------
        None

        """

        self._event_train = event_train

    def load(self, filename=None, system=None):
        """
        Reads event file from the recording formats
        (Currently not implemented)

        Parameters
        ----------
        filename : str
            Full file of the event data
        system : str
            Data formta or the recording system

        Returns
        -------
        None

        """

        if system is None:
            system = self._system
        if filename is None:
            filename = self._filename

    def _create_tag(self, name_train):
        """
        Creates tags from event trains if the events are described with their names. 

        Parameters
        ----------
        name_train : list of str
            Trains of events described with their names

        Returns
        -------
        None

        """

        self._event_trig_averages = list(range(0, len(self._event_names), 1))
        if type(name_train).__module__ == np.__name__:
            self._event_train = np.zeros(name_train.shape)
            for i, name in enumerate(self._event_names):
                self._event_train[name_train ==
                                  name] = self._event_trig_averages[i]

    def add_spike(self, spike=None, **kwargs):
        """
        Adds new spike node to current NEvent() object

        Parameters
        ----------
        spike : NSpike
            NSPike object. If None, new object is created

        Returns
        -------
        `:obj:NSpike`
            A new NSpike() object

        """
        new_spike = self._add_node(NSpike, spike, 'spike', **kwargs)
        return new_spike

    def load_spike(self, names='all'):
        """
        Loads datasets of the spike nodes. Name of each node is used for obtaining the
        filenames

        Parameters
        ----------
        names : list of str
            Names of the nodes to load. If 'all', all the spike nodes are loaded

        Returns
        -------
        None

        """

        if names == 'all':
            for spike in self._spikes:
                spike.load()
        else:
            logging.error("Spikes by name has yet to be implemented")
            # for name in names:
            #     spike = self.get_spikes_by_name(name)
            #     spike.load()

    def add_lfp(self, lfp=None, **kwargs):
        """
        Adds new LFP node to current NEvent() object

        Parameters
        ----------
        lfp : NLfp
            NLfp object. If None, new object is created

        Returns
        -------
        `:obj:Nlfp`
            A new NLfp() object

        """

        new_lfp = self._add_node(NLfp, lfp, 'lfp', **kwargs)

        return new_lfp

    def load_lfp(self, names=None):
        """
        Loads datasets of the LFP nodes. Name of each node is used for obtaining the
        filenames

        Parameters
        ----------
        names : list of str
            Names of the nodes to load. If `all`, all LFP nodes are loaded

        Returns
        -------
        None

        """

        if names is None:
            self.load()
        elif names == 'all':
            for lfp in self._lfp:
                lfp.load()
        else:
            logging.error("Lfp by name has yet to be implemented")
            # for name in names:
            # lfp = self.get_lfp_by_name(name)
            # lfp.load()

    def psth(self, event=None, spike=None, **kwargs):
        """
        Calculates peri-stimulus time histogram (PSTH)

        Parameters
        ----------
        event 
            Event name or tag
        spike : NSpike
            NSpike object to characterize

        **kwargs
            Keyword arguments

        Returns
        -------
        dict
            Graphical data of the analysis

        """

        graph_data = oDict()
        if not event:
            event = self._curr_tag
        elif event in self._event_names:
            event = self.get_tag(event)
        if not spike:
            spike = kwargs.get('spike', 'xxxx')
        spike = self.get_spike(spike)
        if event:
            if spike:
                graph_data = spike.psth(self.get_event_stamp(event), **kwargs)
            else:
                logging.error('No valid spike specified')
        else:
            logging.error(str(event) + ' is not a valid event')

        return graph_data

        # Do things on event tag
     # def other functions; check Pradeep's code

    def phase_dist(self, lfp=None, **kwargs):
        """
        Analysis of event to LFP phase distribution

        Delegates to NLfp().phase_dist()

        Parameters
        ----------
        lfp : NLfp
            LFP object which contains the LFP data.
        **kwargs
            Keywrod arguments

        Returns
        -------
        dict
            Graphical data of the analysis

        See also
        --------
        nc_lfp.NLfp().phase_dist()

        """

        if lfp is None:
            logging.error('LFP data not specified!')
        else:
            _lfp = self._get_instance(NLfp, lfp, 'lfp')
            _lfp.phase_dist(self.get_event_stamp(self.get_tag()), **kwargs)

    def plv(self, lfp=None, **kwargs):
        """
        Calculates phase-locking value of event train to underlying LFP signal.

        Delegates to NLfp().plv()

        Parameters
        ----------
        lfp : NLfp
            LFP object which contains the LFP data
        **kwargs
            Keyword arguments

        Returns
        -------
        dict
            Graphical data of the analysis

        See also
        --------
        nc_lfp.NLfp().plv()

        """

        if lfp is None:
            logging.error('LFP data not specified!')
        else:
            _lfp = self._get_instance(NLfp, lfp, 'lfp')
            _lfp.plv(self.get_event_stamp(self.get_tag()), **kwargs)

#    def sfc(self, lfp=None, **kwargs):
#        if lfp is None:
#            logging.error('LFP data not specified!')
#        else:
#            _lfp = self._get_instance(NLfp, lfp, 'lfp')
#            _lfp.sfc(self.get_event_stamp(self.get_tag()), **kwargs)
