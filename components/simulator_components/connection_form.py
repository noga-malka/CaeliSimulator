from dash import Output, State, Input
from dash_extensions.enrich import callback, DashLogger

from cnc.simulator_cnc import SimulatorCnc
from components.consts import Placeholder
from components.general_components.modal import create_modal
from components.simulator_components.connect_devices.utilities import build_connection_devices_dropdown, \
    connection_status_change
from components.simulator_components.consts import SimulatorModal, ConnectionStatus
from utilities import ui_logger

simulator_connection_modal = create_modal('Connect to Simulator', SimulatorModal.ID,
                                          build_connection_devices_dropdown(SimulatorModal.DEVICE_DROPDOWN,
                                                                            SimulatorModal.SYNC_DEVICES,
                                                                            SimulatorModal.CONNECT_DEVICE))


@callback(Output(SimulatorModal.DEVICE_DROPDOWN, 'options'),
          Input(SimulatorModal.SYNC_DEVICES, 'n_clicks'))
def sync_devices(sync_button_clicked: int):
    return SimulatorCnc().connection.discover()


@callback(Output(Placeholder.ID, Placeholder.Fields.CLICKS_TIMESTAMP),
          State(SimulatorModal.DEVICE_DROPDOWN, 'value'),
          Input(SimulatorModal.CONNECT_DEVICE, 'n_clicks'),
          prevent_initial_call=True,
          log=True)
def connect_selected_device(device: str, button_clicked: int, dash_logger: DashLogger):
    cnc = SimulatorCnc()
    if not device:
        return ui_logger(dash_logger, 'Device must be selected')
    cnc.connection.connect(device)


@callback(Output(ConnectionStatus.ID, 'className'),
          Input(Placeholder.ID, Placeholder.Fields.CLICKS_TIMESTAMP),
          Input(Placeholder.ID, Placeholder.Fields.KEY))
def connect_selected_device(*button_clicks: list[int]):
    return connection_status_change(SimulatorCnc())
