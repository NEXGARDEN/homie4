#!/usr/bin/env python

from homie.device_base import Device_Base
from homie.node.node_datetime import Node_DateTime
import logging

logger = logging.getLogger(__name__)
logger.setLevel("INFO")


class Device_DateTime(Device_Base):
    def __init__(
        self, device_id=None, name=None, homie_settings=None, mqtt_settings=None
    ):
        super().__init__(device_id, name, homie_settings, mqtt_settings)
        
        self.add_node(Node_DateTime(self, id="datetime", set_datetime=self.set_datetime))

        self.start()

    def update_datetime(self, dt):  # sends updates to clients
        self.get_node("datetime").update_datetime(dt)
        logger.debug("Datetime Update {}".format(dt))

    def set_datetime(self, dt):  # received commands from clients
        logger.debug("Datetime Set {}".format(dt))

