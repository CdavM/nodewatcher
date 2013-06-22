from nodewatcher.core.generator.cgm import base as cgm_base, protocols as cgm_protocols, routers as cgm_routers

class TPLinkWR941NDv2(cgm_routers.RouterBase):
    """
    TP-Link WR941NDv2 device descriptor.
    """

    identifier = "tp-wr941ndv2"
    name = "WR941ND (v2)"
    manufacturer = "TP-Link"
    url = "http://www.tp-link.com/"
    architecture = "ar71xx"
    radios = [
        cgm_routers.IntegratedRadio("wifi0", "Wifi0", [
            cgm_protocols.IEEE80211N(
                cgm_protocols.IEEE80211N.SHORT_GI_20,
                cgm_protocols.IEEE80211N.SHORT_GI_40,
                cgm_protocols.IEEE80211N.RX_STBC1,
                cgm_protocols.IEEE80211N.DSSS_CCK_40,
            )
        ], [
            cgm_routers.AntennaConnector("a1", "Antenna0")
        ])
    ]
    switches = [
        cgm_routers.Switch("sw0", "Switch0",
            ports = 5,
            cpu_port = 0,
            vlans = 16
        )
    ]
    ports = [
        cgm_routers.EthernetPort("wan0", "Wan0"),
        cgm_routers.EthernetPort("lan0", "Lan0")
    ]
    antennas = [
        # TODO this information is probably not correct
        cgm_routers.InternalAntenna(
            identifier = "a1",
            polarization = "horizontal",
            angle_horizontal = 360,
            angle_vertical = 75,
            gain = 2
        )
    ]
    features = [
        cgm_routers.Features.MultipleSSID,
    ]
    port_map = {
        "openwrt": {
            "wifi0" : "radio0",
            "sw0"   : "eth0",
            "wan0"  : "eth1",
            "lan0"  : "eth0",
        }
    }
    profiles = {
        "openwrt": {
            "name" : "TLWR941",
            "files": [
                "openwrt-ar71xx-generic-tl-wr941nd-v2-squashfs-factory.bin"
            ]
        }
    }

class TPLinkWR941NDv3(TPLinkWR941NDv2):
    """
    TP-Link WR941NDv3 device descriptor.
    """

    identifier = "tp-wr941ndv2"
    name = "WR941ND (v2)"
    profiles = {
        "openwrt": {
            "name" : "TLWR941",
            "files": [
                "openwrt-ar71xx-generic-tl-wr941nd-v3-squashfs-factory.bin"
            ]
        }
    }

class TPLinkWR941NDv4(TPLinkWR941NDv2):
    """
    TP-Link WR941NDv4 device descriptor.
    """

    identifier = "tp-wr941ndv4"
    name = "WR941ND (v4)"
    profiles = {
        "openwrt": {
            "name" : "TLWR941",
            "files": [
                "openwrt-ar71xx-generic-tl-wr941nd-v4-squashfs-factory.bin"
            ]
        }
    }

# Register the TP-Link WR941ND router
cgm_base.register_router("openwrt", TPLinkWR941NDv2)
cgm_base.register_router("openwrt", TPLinkWR941NDv3)
cgm_base.register_router("openwrt", TPLinkWR941NDv4)
