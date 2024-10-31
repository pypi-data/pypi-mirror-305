from enum import StrEnum
from pydantic import BaseModel
from types import SimpleNamespace
from typing import Any, Iterator, Literal, Mapping

ThemeType = Literal["light", "dark", "mono"]


class Dictable(Mapping):
    """
    Protocols for subclasses to behave like a dict.
    """

    def __getitem__(self, key: str):
        return getattr(self, key)

    def __setitem__(self, key: str, value: Any) -> None:
        setattr(self, key, value)

    def __iter__(self) -> Iterator[str]:
        return iter(self.__dict__)

    def __len__(self) -> int:
        return len(self.__dict__)

    def update(self, other: Mapping[str, Any] | None = None, **kwargs) -> None:
        """
        Update the attributes with elements from another mapping or from key/value pairs.

        Args:
            other (Mapping[str, Any] | None): A mapping object to update from.
            **kwargs: Additional key/value pairs to update with.
        """
        if other is not None:
            for key, value in other.items():
                setattr(self, key, value)
        for key, value in kwargs.items():
            setattr(self, key, value)


class DotDict(SimpleNamespace, Dictable):
    """
    Extends SimpleNamespace to allow for unpacking and subscript notation access.
    """

    pass


class HouseSys(StrEnum):
    Placidus = "P"
    Koch = "K"
    Equal = "E"
    Campanus = "C"
    Regiomontanus = "R"
    Porphyry = "P"
    Whole_Sign = "W"


class Orb(Dictable, BaseModel):
    """default orb for natal chart"""

    conjunction: int = 7
    opposition: int = 6
    trine: int = 6
    square: int = 6
    sextile: int = 5


class Theme(Dictable, BaseModel):
    """
    Default colors for the chart.
    """

    fire: str = "#ef476f"  # fire, square, Asc
    earth: str = "#ffd166"  # earth, MC
    air: str = "#06d6a0"  # air, trine
    water: str = "#81bce7"  # water, opposition
    points: str = "#118ab2"  # lunar nodes, sextile
    asteroids: str = "#AA96DA"  # asteroids
    positive: str = "#FFC0CB"  # positive
    negative: str = "#AD8B73"  # negative
    others: str = "#FFA500"  # conjunction
    transparency: float = 0.1
    foreground: str
    background: str
    dim: str


class LightTheme(Theme):
    """
    Default light colors.
    """

    foreground: str = "#758492"
    background: str = "#FFFDF1"
    dim: str = "#A4BACD"


class DarkTheme(Theme):
    """
    Default dark colors.
    """

    foreground: str = "#F7F3F0"
    background: str = "#343a40"
    dim: str = "#515860"


class Display(Dictable, BaseModel):
    """
    Display settings for celestial bodies.
    """

    sun: bool = True
    moon: bool = True
    mercury: bool = True
    venus: bool = True
    mars: bool = True
    jupiter: bool = True
    saturn: bool = True
    uranus: bool = True
    neptune: bool = True
    pluto: bool = True
    asc_node: bool = True
    chiron: bool = False
    ceres: bool = False
    pallas: bool = False
    juno: bool = False
    vesta: bool = False
    asc: bool = True
    ic: bool = False
    dsc: bool = False
    mc: bool = True


class Chart(Dictable, BaseModel):
    """
    Chart configuration settings.
    """

    stroke_width: int = 1
    stroke_opacity: float = 1
    font: str = "Noto Sans Symbols, Cardo, sans-serif"
    font_size_fraction: float = 0.55
    inner_min_degree: float = 9
    outer_min_degree: float = 8
    margin_factor: float = 0.1
    ring_thickness_fraction: float = 0.15
    style: str = """
        @import url("https://fonts.googleapis.com/css2?family=Noto+Sans+Symbols&display=swap&text=♈♉♊♋♌♍♎♏♐♑♒♓☽♃♄♇♆♅⚷⚳⚴⚵⚶☌☍⚹🜂🜄🜁🜃");
        @import url("https://fonts.googleapis.com/css2?family=Cardo&display=swap&text=♂♀☿☊");
    """


class Config(Dictable, BaseModel):
    """
    Package configuration model.
    """

    theme_type: ThemeType = "dark"
    house_sys: HouseSys = HouseSys.Placidus
    orb: Orb = Orb()
    light_theme: LightTheme = LightTheme()
    dark_theme: DarkTheme = DarkTheme()
    display: Display = Display()
    chart: Chart = Chart()

    @property
    def theme(self) -> Theme:
        """
        Return theme colors based on the theme type.

        Returns:
            Theme: The theme colors.
        """
        match self.theme_type:
            case "light":
                return self.light_theme
            case "dark":
                return self.dark_theme
            case "mono":
                kwargs = {key: "#888888" for key in self.light_theme.model_dump()}
                kwargs["background"] = "#FFFFFF"
                kwargs["transparency"] = 0
                return Theme(**kwargs)
