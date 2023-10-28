from assets.icons import ProfileIcons
from components.profile_components.consts import ProfileForm
from models.field import ProfileField
from models.unit_type_parsers.liter_parser import LiterParser
from models.unit_type_parsers.seconds_parser import SecondsParser


class FieldsDisplay:
    inspirium_time = ProfileField(name=ProfileForm.Inputs.INSPIRIUM_TIME,
                                  unit_parser=SecondsParser(),
                                  display_name='Inspirium Time',
                                  icons=[ProfileIcons.BREATH, ProfileIcons.RIGHT_BROKEN_ARROW])
    inspirium_hold_time = ProfileField(name=ProfileForm.Inputs.INSPIRIUM_HOLD_TIME,
                                       unit_parser=SecondsParser(),
                                       display_name='Inspirium Hold Time',
                                       icons=[ProfileIcons.BREATH, ProfileIcons.HOLD],
                                       maximum=5000)
    expirium_time = ProfileField(name=ProfileForm.Inputs.EXPIRIUM_TIME,
                                 unit_parser=SecondsParser(),
                                 display_name='Expirium Time',
                                 icons=[ProfileIcons.BREATH, ProfileIcons.LEFT_BROKEN_ARROW])
    expirium_hold_time = ProfileField(name=ProfileForm.Inputs.EXSPIRIUM_HOLD_TIME,
                                      unit_parser=SecondsParser(),
                                      display_name='Expirium Hold Time',
                                      icons=[ProfileIcons.BREATH, ProfileIcons.HOLD],
                                      maximum=5000)
    tidal_volume = ProfileField(name=ProfileForm.Inputs.TIDAL_VOLUME,
                                unit_parser=LiterParser(),
                                display_name='Lungs Volume',
                                icons=[ProfileIcons.LUNGS],
                                maximum=150)
