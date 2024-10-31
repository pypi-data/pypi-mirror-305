#**********************************************************************************
# * Copyright (C) 2024-present Bert Van Acker (B.MKR) <bert.vanacker@uantwerpen.be>
# *
# * This file is part of the roboarch R&D project.
# *
# * RAP R&D concepts can not be copied and/or distributed without the express
# * permission of Bert Van Acker
# **********************************************************************************
class namedObject(object):

    def __init__(self, name='tbd', description='tbd', verbose=False):
        self._name = name
        self._description = description
        self._verbose = verbose

    @property
    def name(self):
        """The name property (read-only)."""
        return self._name

    @property
    def description(self):
        """The description property (read-only)."""
        return self._description

class system(namedObject):

    def __init__(self,name='tbd', description='tbd', verbose=False,systemList = None,processList = None,featureList=None,messageList=None):
        super().__init__(name=name,description = description,verbose=verbose)

        if featureList is not None:
            self._featureList = featureList
        else:
            self._featureList = []
        if systemList is not None:
            self._systemList = systemList
        else:
            self._systemList = []
        if processList is not None:
            self._processList = processList
        else:
            self._processList = []
        if messageList is not None:
            self._messageList = messageList
        else:
            self._messageList = []

    def addProcess(self,process):
        """Add a process to the process list """
        self._processList.append(process)

    @property
    def processes(self):
        return self._processList

    @property
    def systems(self):
        return self._systemList
    def addSystem(self,system):
        """Add a system to the system list """
        self._systemList.append(system)

    def addFeature(self,feature):
        """Add a feature to the system """
        self._featureList.append(feature)

    def addMessage(self,message):
        """Add a process to the process list """
        self._messageList.append(message)

    @property
    def messages(self):
        return self._messageList


class process(namedObject):

    def __init__(self, name='tbd',description='tbd',verbose=False,featureList = None,threadList=None):
        super().__init__(name=name, description=description, verbose=verbose)

        if featureList is not None:
            self._featureList = featureList
        else:
            self._featureList = []

        if threadList is not None:
            self._threadList = threadList
        else:
            self._threadList = []

    @property
    def features(self):
        return self._featureList

    def addFeature(self, feature):
        """Add a feature to the system """
        self._featureList.append(feature)

    @property
    def threads(self):
        return self._threadList

    def addThread(self, t):
        """Add a thread to the system """
        self._threadList.append(t)

class thread(namedObject):

    def __init__(self, name='tbd',description='tbd',verbose=False,featureList = None,eventTrigger=None):
        super().__init__(name=name, description=description, verbose=verbose)

        if featureList is not None:
            self._featureList = featureList
        else:
            self._featureList = []

        self._eventTrigger = eventTrigger

    @property
    def features(self):
        return self._featureList
    def addFeature(self, feature):
        """Add a feature to the system """
        self._featureList.append(feature)

    @property
    def eventTrigger(self):
        return self._eventTrigger

class characteristic(namedObject):

    def __init__(self, name='tbd',description='tbd',verbose=False,value="",dataType='-'):
        super().__init__(name=name, description=description, verbose=verbose)

        self._value = value
        self._dataType = dataType

class event(namedObject):

    def __init__(self, name='tbd',description='tbd',verbose=False):
        super().__init__(name=name, description=description, verbose=verbose)

class mode(namedObject):

    def __init__(self, name='tbd',description='tbd',verbose=False,callback = None):
        super().__init__(name=name, description=description, verbose=verbose)

        self._callback = callback

    @property
    def callback(self):
        """The callback property (read-only)."""
        return self._callback

class transition(namedObject):

    def __init__(self, name='tbd',description='tbd',verbose=False,callback = None,source=None,destination=None):
        super().__init__(name=name, description=description, verbose=verbose)

        self._source = source
        self._destination = destination
        self._callback = callback

    @property
    def source(self):
        """The source (read-only)."""
        return self._source

    @property
    def destination(self):
        """The source (read-only)."""
        return self._destination

    @property
    def callback(self):
        """The callback property (read-only)."""
        return self._callback

class feature(namedObject):

    def __init__(self, name='tbd',description='tbd',verbose=False,featureType="feature"):
        super().__init__(name=name, description=description, verbose=verbose)

        self._featureType = featureType

    @property
    def featureType(self):
        return self._featureType

    @featureType.setter
    def featureType(self,type):
        self._featureType = type

class port(feature):

    def __init__(self, name='tbd',description='tbd',initialValue = 1.0,valueReference=1,type='data',message=None,verbose=False):
        super().__init__(name=name, description=description, verbose=verbose)

        self._featureType = 'port'
        self._initialValue = initialValue
        self._valueReference = valueReference
        self._type = type
        self._message = message


    @property
    def value(self):
        """The value property (read)."""
        return self._initialValue

    @value.setter
    def value(self,value):
        """The value property (write)."""
        self._initialValue = value

    @property
    def valueReference(self):
        """The valueReference property (read)."""
        return self._valueReference

    @valueReference.setter
    def valueReference(self, value):
        """The valueReference property (write)."""
        self._valueReference = value

    @property
    def type(self):
        """The type property (read-only)."""
        return self._type

    @property
    def message(self):
        """The message property"""
        return self._message

class inport(port):
    def __init__(self, name='tbd',description='tbd',initialValue = 1.0,valueReference=1,type='data',verbose=False,message=None):
        super().__init__(name=name, description=description, verbose=verbose,initialValue=initialValue,valueReference=valueReference,type=type,message=message)

        self._featureType = 'inport'
class outport(port):
    def __init__(self, name='tbd',description='tbd',initialValue = 1.0,valueReference=1,type='data',verbose=False,message=None):
        super().__init__(name=name, description=description, verbose=verbose,initialValue=initialValue,valueReference=valueReference,type=type,message=message)

        self._featureType = 'outport'

class connection(namedObject):

    def __init__(self, name='tbd',description='tbd',verbose=False,source=None,destination=None):
        super().__init__(name=name, description=description, verbose=verbose)

        self._source = source
        self._destination = destination

    @property
    def source(self):
        """The source (read-only)."""
        return self._source

    @property
    def destination(self):
        """The source (read-only)."""
        return self._destination

class message(namedObject):

    def __init__(self, name='tbd',description='tbd',verbose=False,featureList = None):
        super().__init__(name=name, description=description, verbose=verbose)

        if featureList is not None:
            self._featureList = featureList
        else:
            self._featureList = []

    @property
    def features(self):
        return self._featureList

    def addFeature(self, feature):
        """Add a feature to the system """
        self._featureList.append(feature)

class data(feature):

    def __init__(self, name='tbd',description='tbd',dataType='Float_64',verbose=False):
        super().__init__(name=name, description=description, verbose=verbose)

        self._dataType = dataType

    @property
    def dataType(self):
        return self._dataType

class processor(namedObject):

    def __init__(self,name='tbd', description='tbd', verbose=False,featureList = None,propertyList = None):
        super().__init__(name=name,description = description,verbose=verbose)

        if featureList is not None:
            self._featureList = featureList
        else:
            self._featureList = []
        if propertyList is not None:
            self._propertyList = propertyList
        else:
            self._propertyList = []

    def addFeature(self, feature):
        """Add a feature to the system """
        self._featureList.append(feature)

    def addProperty(self, p):
        """Add a property to the system """
        self._propertyList.append(p)

class memory(namedObject):

    def __init__(self,name='tbd', description='tbd', verbose=False,propertyList = None):
        super().__init__(name=name,description = description,verbose=verbose)

        if propertyList is not None:
            self._propertyList = propertyList
        else:
            self._propertyList = []

    def addProperty(self, p):
        """Add a property to the system """
        self._propertyList.append(p)

class bus(namedObject):

    def __init__(self,name='tbd', description='tbd', verbose=False,propertyList = None):
        super().__init__(name=name,description = description,verbose=verbose)

        if propertyList is not None:
            self._propertyList = propertyList
        else:
            self._propertyList = []

        self._connectionList = []

    def addProperty(self, p):
        """Add a property to the bus """
        self._propertyList.append(p)

    def addConnection(self, p):
        """Add a connection to the bus """
        self._connectionList.append(p)



