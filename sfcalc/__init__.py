class Base:
    def __init__(self, q):
        self.q: float = q
        self.m: float
        self.recipe: list

    @property
    def number_of_buildings(self):
        return self.q / self.m

    @property
    def name(self):
        return str(self.__class__)[15:-2]

    def get_components(self):
        if "recipe" in self.__dict__:
            components = []
            for r in self.recipe:
                components.append(r.get_components())
            return components
        else:
            return self

    @staticmethod
    def group(w):
        types = dict()
        for item in w:
            if item.name in types:
                types[item.name].append(item)
            else:
                types[item.name] = []
                types[item.name].append(item)
        return types

    def flatten(self, S):
        if S == []:
            return S
        if isinstance(S[0], list):
            return self.flatten(S[0]) + self.flatten(S[1:])
        return S[:1] + self.flatten(S[1:])

    def __repr__(self):
        return f"{str(self.__class__)[15:-2]} {self.q}"

    def __str__(self):
        return f"{str(self.__class__)[15:-2]} {self.q}"

    def __add__(self, other):
        if self.__class__ == other.__class__:
            return self.__class__(self.q + other.q)
        else:
            return self


class AssemblyDirectorSystem(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 0.75
        self.recipe = [AdaptiveControlUnit(1.5), Supercomputer(0.75)]


class MagneticFieldGenerator(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 1
        self.recipe = [
            VersatileFramework(2.5),
            ElectromagneticControlRod(1),
            Battery(5),
        ]


class ThermalPropulsionRocket(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 1
        self.recipe = [
            ModularEngine(2.5),
            TurboMotor(1),
            CoolingSystem(3),
            FusedModularFrame(1),
        ]


class NuclearPasta(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 0.5
        self.recipe = [CopperPowder(100), PressureConversionCube(0.5)]


class AdaptiveControlUnit(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 1
        self.recipe = [
            AutomatedWiring(7.5),
            CircuitBoard(5),
            HeavyModularFrame(1),
            Computer(1),
        ]


class Supercomputer(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 1.875
        self.recipe = [
            Computer(2),
            AILimiter(3.75),
            HighSpeedConnector(5.625),
            Plastic(52.5),
        ]


class VersatileFramework(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 5
        self.recipe = [SteelBeam(30), ModularFrame(2.5)]


class ElectromagneticControlRod(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 4
        self.recipe = [AILimiter(4), Stator(6)]


class Battery(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 20
        self.recipe = [AluminiaSolution(40), SulfuricAcid(50), AluminumCasing(20)]


class ModularEngine(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 1
        self.recipe = [Rubber(15), Motor(2), SmartPlating(2)]


class TurboMotor(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 1.875
        self.recipe = [
            RadioControlUnit(3.75),
            CoolingSystem(7.5),
            Motor(7.5),
            Rubber(45),
        ]


class CoolingSystem(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 6
        self.recipe = [Heatsink(12), Rubber(12), Water(30), NitrogenGas(150)]


class FusedModularFrame(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 1.5
        self.recipe = [HeavyModularFrame(1.5), AluminumCasing(75), NitrogenGas(37.5)]


class Computer(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 2.5
        self.recipe = [CircuitBoard(25), Cable(22.5), Plastic(45), Screw(130)]


class AILimiter(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 5
        self.recipe = [CopperSheet(25), Quickwire(100)]


class CircuitBoard(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 7.5
        self.recipe = [CopperSheet(2), Plastic(4)]


class HighSpeedConnector(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 3.75
        self.recipe = [Quickwire(210), Cable(37.5), CircuitBoard(3.75)]


class HeavyModularFrame(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 2
        self.recipe = [
            ModularFrame(10),
            SteelPipe(30),
            EncasedIndustrialBeam(10),
            Screw(200),
        ]


class AutomatedWiring(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 2.5
        self.recipe = [Stator(2.5), Cable(50)]


class Cable(Base):
    def __init__(self, q):
        super().__init__(q)
        self.m = 30
        self.q = q
        self.recipe = [Wire(60)]


class Screw(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 52
        self.recipe = [SteelBeam(5)]


class PressureConversionCube(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 1
        self.recipe = [FusedModularFrame(1), RadioControlUnit(2)]


class CopperSheet(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 10
        self.recipe = [CopperIngot(20)]


class Plastic(Base):
    def __init__(self, q):
        super().__init__(q)
        self.m = 20
        self.q = q


class CopperPowder(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 50
        self.recipe = [CopperIngot(300)]


class EncasedIndustrialBeam(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 6
        self.recipe = [SteelBeam(24), Concrete(30)]


class ModularFrame(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 2
        self.recipe = [ReinforcedIronPlate(3), IronRod(12)]


class Quickwire(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 60
        self.recipe = [CateriumIngot(12)]


class IronRod(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 15
        self.recipe = [IronIngot(15)]


class SteelPipe(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 20
        self.recipe = [SteelIngot(30)]


class SteelBeam(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 15
        self.recipe = [SteelIngot(60)]


class Concrete(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 15
        self.recipe = [Limestone(45)]


class Stator(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 5
        self.recipe = [SteelPipe(15), Wire(40)]


class Rotor(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 4
        self.recipe = [IronRod(20), Screw(100)]


class Wire(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 30
        self.recipe = [CopperIngot(15)]


class AluminiaSolution(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q


class SulfuricAcid(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q


class AluminumCasing(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 60
        self.recipe = [AluminumIngot(90)]


class Rubber(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q


class Motor(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 5
        self.recipe = [Rotor(10), Stator(10)]


class SmartPlating(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 2
        self.recipe = [ReinforcedIronPlate(2), Rotor(2)]


class RadioControlUnit(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 2.5
        self.recipe = [AluminumCasing(40), CrystalOscillator(1.25), Computer(1.25)]


class Heatsink(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 7.5
        self.recipe = [AlcladAluminumSheet(5), CopperSheet(3)]


class CrystalOscillator(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 1
        self.recipe = [QuartzCrystal(18), Cable(14)]


class ReinforcedIronPlate(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 5
        self.recipe = [IronPlate(30), Screw(60)]


class IronPlate(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 20
        self.recipe = [IronIngot(30)]


class NitrogenGas(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q


class Water(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q


class QuartzCrystal(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q


class AlcladAluminumSheet(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
        self.m = 30
        self.recipe = [AluminumIngot(30), CopperIngot(10)]


class CopperIngot(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q


class IronIngot(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q


class SteelIngot(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q


class CateriumIngot(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q


class AluminumIngot(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q


class Limestone(Base):
    def __init__(self, q):
        super().__init__(q)
        self.q = q
