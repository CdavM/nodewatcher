from nodewatcher.core.generator.cgm import base as cgm_base, protocols as cgm_protocols, routers as cgm_routers


class UBNTRocketM5(cgm_routers.DeviceBase):
    """
    UBNT Rocket M5 device descriptor.
    """

    identifier = 'ub-rocket-m5'
    name = "Rocket"
    manufacturer = "Ubiquity"
    url = 'http://www.ubnt.com/'
    architecture = 'ar71xx'
    radios = [
        cgm_routers.IntegratedRadio('wifi0', "Wifi0", [
            cgm_protocols.IEEE80211N(
                cgm_protocols.IEEE80211N.SHORT_GI_40,
                cgm_protocols.IEEE80211N.TX_STBC1,
                cgm_protocols.IEEE80211N.RX_STBC1,
                cgm_protocols.IEEE80211N.DSSS_CCK_40,
            )
        ], [
            cgm_routers.AntennaConnector('a1', "Antenna0")
        ])
    ]
    switches = []
    ports = [
        cgm_routers.EthernetPort('lan0', "Lan0")
    ]
    antennas = [
        # TODO: This information is probably not correct
        cgm_routers.InternalAntenna(
            identifier='a1',
            polarization='horizontal',
            angle_horizontal=360,
            angle_vertical=75,
            gain=2,
        )
    ]
    features = [
        cgm_routers.Features.MultipleSSID,
    ]
    port_map = {
        'openwrt': {
            'wifi0': 'radio0',
            'lan0': 'eth0',
        }
    }
    drivers = {
        'openwrt': {
            'wifi0': 'mac80211'
        }
    }
    profiles = {
        'openwrt': {
            'name': 'UBNT',
            'files': [
                'openwrt-ar71xx-generic-ubnt-rocket-m-squashfs-factory.bin'
            ]
        }
    }

# Register the UBNT Rocket router
cgm_base.register_device('openwrt', UBNTRocketM5)
