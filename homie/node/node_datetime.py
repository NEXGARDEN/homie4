from .node_base import Node_Base

from homie.node.property.property_datetime import Property_DateTime


class Node_DateTime(Node_Base):
    def __init__(
        self,
        device,
        id="datetime",
        name="DateTime",
        type_="datetime",
        retain=True,
        qos=1,
        set_datetime=None,
    ):
        super().__init__(device, id, name, type_, retain, qos)

        assert set_datetime  # must provide a function to set the value of the datetime

        self.add_property(Property_DateTime(self, set_value=set_datetime))

    def update_datetime(self, dt):
        self.get_property("datetime").value = dt

