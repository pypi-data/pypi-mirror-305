__all__ = ["build_xml", "MediaFile", "replace_cachebusting", "Tracker"]

import dataclasses as dc
import re
from typing import Literal, Optional, TypedDict

from lxml import etree


@dc.dataclass
class MediaFile:
    url: str
    mimetype: str
    width: int
    height: int
    bitrate: int = 15000
    delivery: Literal["progressive"] = "progressive"


class Attribute(TypedDict):
    name: str
    value: str


@dc.dataclass
class Tracker:
    type: Literal["clickthrough", "impression", "error", "event"]
    url: str
    attributes: Optional[list[Attribute]] = None

    def __hash__(self):
        return hash(
            (self.type, self.url, tuple(self.attributes) if self.attributes else None)
        )


def build_xml(
    *,
    id: str,
    name: str,
    description: str,
    duration: int,
    files: [MediaFile],
    ad_choices: Optional[bool] = False,
    skipoffset: Optional[int] = 0,
    trackers: Optional[list[Tracker]] = None,
    version: Optional[str] = "3.0",
) -> bytes:
    """Construct a VAST XML.

    Note that all trackers support multiple occurences except "clickthrough".
    """
    tracking = {"errors": [], "impressions": [], "events": [], "clickthrough": None}
    for tracker in trackers or []:
        if tracker.type == "error":
            tracking["errors"].append(tracker)
        elif tracker.type == "impression":
            tracking["impressions"].append(tracker)
        elif tracker.type == "event":
            tracking["events"].append(tracker)
        elif tracker.type == "clickthrough":
            tracking["clickthrough"] = tracker

    """Root element

    <VAST xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="vast.xsd"
        version="3.0">
        <Ad id="Placement ID">
            ...
        </Ad>
    </VAST>

    """
    ns_xsi = "http://www.w3.org/2001/XMLSchema-instance"
    root = etree.Element(
        "VAST",
        attrib={
            f"{{{ns_xsi}}}noNamespaceSchemaLocation": "vast.xsd",
            "version": version,
        },
    )

    ad = etree.SubElement(root, "Ad")
    ad.set("id", id)

    """<Inline> element

        <InLine>
            <AdSystem>System</AdSystem>
            <AdTitle>Title</AdTitle>
            <Description><![CDATA[Description]]></Description>
            <Error><![CDATA[...]]></Error>
            <Impression><![CDATA[...]]></Impression>
        </InLine>

    <AdSystem>, <AdTitle> and <Impression> are required elements.
    """
    inline = etree.SubElement(ad, "InLine")

    ad_system = etree.SubElement(inline, "AdSystem")
    ad_system.text = "Scoota"

    ad_title = etree.SubElement(inline, "AdTitle")
    ad_title.text = name

    ad_description = etree.SubElement(inline, "Description")
    ad_description.text = description

    # <Error/>
    for tracker in tracking["errors"]:
        error = etree.SubElement(inline, "Error")
        error.text = etree.CDATA(tracker.url)

    # <Impression/>
    for tracker in tracking["impressions"]:
        error = etree.SubElement(inline, "Impression", attrib=tracker.attributes)
        error.text = etree.CDATA(tracker.url)

    """<Creatives> element.

    The <Creatives> element provides details about the files for each placement to be included
    as part of the ad experience.

        <Creatives>
            <Creative>
                <Linear>
                    <Duration>HH:MM:SS.mmm</Duration>
                    <MediaFiles>
                        <MediaFile
                            delivery="progressive"
                            type="video/mp4"
                            width="300"
                            height="250">
                            <![CDATA[http://path/to/video.mp4]]>
                        </MediaFile>
                    </MediaFiles>
                    <TrackingEvents>
                        <Tracking><![CDATA[...]]></Tracking>
                    </TrackingEvents>
                    <VideoClicks>
                        <ClickThrough><![CDATA[...]]></ClickThrough>
                    </VideoClicks>
                    <Icon />
                </Linear>
            </Creative>
        </Creatives>

    A <Linear> element has two required child elements, <Duration> and <MediaFiles>.

    `delivery`, `type`, `width` and `height` are all required attributes of <MediaFile>. The
    `delivery` attribute defaults to progressive as we currently do not support streaming video.
    """
    creatives = etree.SubElement(inline, "Creatives")
    creative = etree.SubElement(creatives, "Creative")
    linear = etree.SubElement(creative, "Linear")

    if skipoffset:
        linear.set("skipoffset", milliseconds_to_HHMMSSmmm(skipoffset))

    # <Duration> element.
    ad_duration = etree.SubElement(linear, "Duration")
    ad_duration.text = milliseconds_to_HHMMSSmmm(duration)

    # Required <MediaFiles> element.
    media_files = etree.SubElement(linear, "MediaFiles")
    for file in files:
        media_file = etree.SubElement(
            media_files,
            "MediaFile",
            attrib={
                "height": str(file.height),
                "delivery": file.delivery,
                "maintainAspectRatio": "true",
                "scalable": "true",
                "type": file.mimetype,
                "width": str(file.width),
                "bitrate": str(file.bitrate),
            },
        )
        media_file.text = etree.CDATA(file.url)

    """Tracking <TrackingEvents> and <VideoClicks> elements.

        <TrackingEvents>
            <Tracking event="firstQuartile">
                <![CDATA[http://path/to/first/quartile]]>
            </Tracking>
        </TrackingEvents>
        <VideoClicks>
            <ClickThrough>
                <![CDATA[http://path/to/clickthrough]]>
            </ClickThrough>
        </VideoClicks>

    """
    if len(tracking["events"]):
        events = etree.SubElement(linear, "TrackingEvents")
        for tracker in tracking["events"]:
            event = etree.SubElement(events, "Tracking", attrib=tracker.attributes)
            event.text = etree.CDATA(tracker.url)

    if tracking["clickthrough"]:
        tracker = tracking["clickthrough"]
        video_clicks = etree.SubElement(linear, "VideoClicks")
        clickthrough = etree.SubElement(
            video_clicks, "ClickThrough", attrib=tracker.attributes
        )
        clickthrough.text = etree.CDATA(tracker.url)

    """AdChoices <Icon> element.

    Display AdChoices icon and will click through to //info.evidon.com/more_info/130210.
    """
    if ad_choices:
        icons = etree.SubElement(linear, "Icons")
        icon = etree.SubElement(
            icons,
            "Icon",
            attrib={
                "height": "15",
                "program": "AdChoices",
                "width": "77",
                "xPosition": "right",
                "yPosition": "top",
            },
        )
        static_resource = etree.SubElement(
            icon,
            "StaticResource",
            attrib={
                "creativeType": "image/png",
            },
        )
        static_resource.text = etree.CDATA("//c.betrad.com/icon/c_30_us.png")
        icon_clicks = etree.SubElement(icon, "IconClicks")
        icon_clickthrough = etree.SubElement(icon_clicks, "IconClickThrough")
        icon_clickthrough.text = etree.CDATA("//info.evidon.com/more_info/130210")

    return etree.tostring(root, encoding="UTF-8", xml_declaration=False)


def milliseconds_to_HHMMSSmmm(milliseconds: int) -> str:
    """Convert milliseconds to HH:MM:SS.mmm string format."""
    hours, rem = divmod(milliseconds / 1000.0, 3600)
    minutes, seconds = divmod(rem, 60)

    return "{:0>2}:{:0>2}:{:06.3f}".format(int(hours), int(minutes), seconds)


def replace_cachebusting(url):
    """Replace [timestamp] and [cachebuster] macros with [CACHEBUSTING] macro."""
    return re.sub(
        pattern=r"\[(timestamp|cachebuster)\]",
        repl="[CACHEBUSTING]",
        string=url,
        flags=re.I,
    )
