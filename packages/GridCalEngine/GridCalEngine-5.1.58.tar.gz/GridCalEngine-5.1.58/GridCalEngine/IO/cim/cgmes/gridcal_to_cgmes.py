# GridCal
# Copyright (C) 2015 - 2024 Santiago Peñate Vera
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
import numpy as np

from datetime import datetime
from GridCalEngine.DataStructures.numerical_circuit import (compile_numerical_circuit_at, NumericalCircuit)
from GridCalEngine.Devices import MultiCircuit
from GridCalEngine.Devices.Substation.bus import Bus
from GridCalEngine.IO.cim.cgmes.base import get_new_rdfid, form_rdfid
from GridCalEngine.IO.cim.cgmes.cgmes_circuit import CgmesCircuit
from GridCalEngine.IO.cim.cgmes.cgmes_enums import (cgmesProfile,
                                                    WindGenUnitKind,
                                                    RegulatingControlModeKind,
                                                    UnitMultiplier,
                                                    TransformerControlMode)
from GridCalEngine.IO.cim.cgmes.cgmes_utils import (find_object_by_uuid,
                                                    find_object_by_vnom, find_object_by_cond_eq_uuid,
                                                    get_ohm_values_power_transformer, find_tn_by_name,
                                                    find_object_by_attribute)
from GridCalEngine.IO.cim.cgmes.cgmes_v2_4_15.devices.full_model import FullModel
from GridCalEngine.IO.cim.cgmes.base import Base
import GridCalEngine.Devices as gcdev
from GridCalEngine.Simulations.PowerFlow.NumericalMethods.common_functions import compute_zip_power
from GridCalEngine.Simulations.PowerFlow.power_flow_results import PowerFlowResults
from GridCalEngine.enumerations import CGMESVersions, TapChangerTypes
from GridCalEngine.IO.cim.cgmes.cgmes_enums import (SynchronousMachineOperatingMode, SynchronousMachineKind)

from GridCalEngine.data_logger import DataLogger
from typing import List, Union


# region create new classes for CC

def create_cgmes_headers(cgmes_model: CgmesCircuit,
                         profiles_to_export: List[cgmesProfile],
                         desc: str = "",
                         scenariotime: str = "",
                         modelingauthorityset: str = "", version: str = ""):
    """

    :param cgmes_model:
    :param profiles_to_export:
    :param desc:
    :param scenariotime:
    :param modelingauthorityset:
    :param version:
    :return:
    """
    if cgmes_model.cgmes_version == CGMESVersions.v2_4_15:
        fm_list = [FullModel(rdfid=get_new_rdfid(), tpe="FullModel"),
                   FullModel(rdfid=get_new_rdfid(), tpe="FullModel"),
                   FullModel(rdfid=get_new_rdfid(), tpe="FullModel"),
                   FullModel(rdfid=get_new_rdfid(), tpe="FullModel"),
                   FullModel(rdfid=get_new_rdfid(), tpe="FullModel")]
    elif cgmes_model.cgmes_version == CGMESVersions.v3_0_0:
        fm_list = [FullModel(rdfid=get_new_rdfid(), tpe="FullModel"),
                   FullModel(rdfid=get_new_rdfid(), tpe="FullModel"),
                   FullModel(rdfid=get_new_rdfid(), tpe="FullModel"),
                   FullModel(rdfid=get_new_rdfid(), tpe="FullModel"),
                   FullModel(rdfid=get_new_rdfid(), tpe="FullModel"),
                   FullModel(rdfid=get_new_rdfid(), tpe="FullModel"),
                   FullModel(rdfid=get_new_rdfid(), tpe="FullModel")]
    else:
        raise ValueError(
            f"CGMES format not supported {cgmes_model.cgmes_version}")

    for fm in fm_list:
        fm.scenarioTime = scenariotime
        if modelingauthorityset != "":
            fm.modelingAuthoritySet = modelingauthorityset
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        fm.created = formatted_time
        fm.version = version
        fm.description = desc

    if cgmes_model.cgmes_version == CGMESVersions.v2_4_15:
        profile_uris = {
            "EQ": ["http://entsoe.eu/CIM/EquipmentCore/3/1",
                   "http://entsoe.eu/CIM/EquipmentOperation/3/1",
                   "http://entsoe.eu/CIM/EquipmentShortCircuit/3/1"],
            "SSH": ["http://entsoe.eu/CIM/SteadyStateHypothesis/1/1"],
            "TP": ["http://entsoe.eu/CIM/Topology/4/1"],
            "SV": ["http://entsoe.eu/CIM/StateVariables/4/1"],
            "GL": ["http://entsoe.eu/CIM/GeographicalLocation/2/1"]
        }
    elif cgmes_model.cgmes_version == CGMESVersions.v3_0_0:
        profile_uris = {
            "EQ": ["http://iec.ch/TC57/ns/CIM/CoreEquipment-EU/3.0"],
            "OP": ["http://iec.ch/TC57/ns/CIM/Operation-EU/3.0"],
            "SC": ["http://iec.ch/TC57/ns/CIM/ShortCircuit-EU/3.0"],
            "SSH": ["http://iec.ch/TC57/ns/CIM/SteadyStateHypothesis-EU/3.0"],
            "TP": ["http://iec.ch/TC57/ns/CIM/Topology-EU/3.0"],
            "SV": ["http://iec.ch/TC57/ns/CIM/StateVariables-EU/3.0"],
            "GL": ["http://iec.ch/TC57/ns/CIM/GeographicalLocation-EU/3.0"]
        }
    else:
        raise ValueError(
            f"CGMES format not supported {cgmes_model.cgmes_version}")

    if cgmes_model.cgmes_version == CGMESVersions.v2_4_15:
        prof = profile_uris.get("EQ")
        fm_list[0].profile = [prof[0]]
        if cgmesProfile.OP in profiles_to_export:
            fm_list[0].profile.append(prof[1])
        if cgmesProfile.SC in profiles_to_export:
            fm_list[0].profile.append(prof[2])
    elif cgmes_model.cgmes_version == CGMESVersions.v3_0_0:
        fm_list[0].profile = profile_uris.get("EQ")
        fm_list[5].profile = profile_uris.get("OP")
        fm_list[6].profile = profile_uris.get("SC")
    else:
        raise ValueError(
            f"CGMES format not supported {cgmes_model.cgmes_version}")

    fm_list[1].profile = profile_uris.get("SSH")
    fm_list[2].profile = profile_uris.get("TP")
    fm_list[3].profile = profile_uris.get("SV")
    fm_list[4].profile = profile_uris.get("GL")
    if cgmes_model.cgmes_version == CGMESVersions.v2_4_15:  # if 2.4 than no need in SV in 3.0 we need all
        fm_list[3].modelingAuthoritySet = None

    # DependentOn
    eqbd_id = ""
    tpbd_id = ""
    try:
        for bd in cgmes_model.elements_by_type_boundary.get("FullModel"):
            if ("http://entsoe.eu/CIM/EquipmentBoundary/3/1" in bd.profile or
                    "http://iec.ch/TC57/ns/CIM/EquipmentBoundary-EU" in bd.profile):
                eqbd_id = bd.rdfid
            if "http://entsoe.eu/CIM/TopologyBoundary/3/1" in bd.profile:  # no TPBD in 3.0
                tpbd_id = bd.rdfid

        fm_list[0].DependentOn = [eqbd_id]
        fm_list[1].DependentOn = [fm_list[0].rdfid]
        fm_list[2].DependentOn = [fm_list[0].rdfid]
        if tpbd_id != "":
            fm_list[3].DependentOn = [tpbd_id, fm_list[1].rdfid,
                                      fm_list[2].rdfid]
        else:
            fm_list[3].DependentOn = [fm_list[1].rdfid, fm_list[2].rdfid]
        fm_list[2].DependentOn = [fm_list[0].rdfid, eqbd_id]
        fm_list[4].DependentOn = [fm_list[0].rdfid]
        if cgmes_model.cgmes_version == CGMESVersions.v3_0_0:
            fm_list[5].DependentOn = [fm_list[0].rdfid]
            fm_list[6].DependentOn = [fm_list[0].rdfid]
    except TypeError:
        print("Missing default boundary files")
        fm_list[1].DependentOn = [fm_list[0].rdfid]
        fm_list[2].DependentOn = [fm_list[0].rdfid]
        fm_list[3].DependentOn = [fm_list[0].rdfid, fm_list[1].rdfid,
                                  fm_list[2].rdfid]
        fm_list[4].DependentOn = [fm_list[0].rdfid]
        if cgmes_model.cgmes_version == CGMESVersions.v3_0_0:
            fm_list[5].DependentOn = [fm_list[0].rdfid]
            fm_list[6].DependentOn = [fm_list[0].rdfid]

    cgmes_model.cgmes_assets.FullModel_list = fm_list
    return cgmes_model


def create_cgmes_terminal(mc_bus: Bus,
                          seq_num: Union[int, None],
                          cond_eq: Union[None, Base],
                          cgmes_model: CgmesCircuit,
                          logger: DataLogger):
    """
    Creates a new Terminal in CGMES model,
    and connects it the relating Topologinal Node
    :param mc_bus:
    :param seq_num:
    :param cond_eq:
    :param cgmes_model:
    :param logger:
    :return:
    """

    new_rdf_id = get_new_rdfid()
    terminal_template = cgmes_model.get_class_type("Terminal")
    term = terminal_template(new_rdf_id)
    term.name = f'{cond_eq.name} - T{seq_num}' if cond_eq is not None else ""
    # term.shortName =
    if seq_num is not None:
        term.sequenceNumber = seq_num

    # further properties
    # term.phases =
    # term.energyIdentCodeEic =

    cond_eq_type = cgmes_model.get_class_type("ConductingEquipment")
    if cond_eq and isinstance(cond_eq, cond_eq_type):
        term.ConductingEquipment = cond_eq
    term.connected = True

    tn = find_object_by_uuid(
        cgmes_model=cgmes_model,
        object_list=cgmes_model.cgmes_assets.TopologicalNode_list,
        target_uuid=mc_bus.idtag
    )
    if isinstance(tn, cgmes_model.get_class_type("TopologicalNode")):
        term.TopologicalNode = tn
        term.ConnectivityNode = tn.ConnectivityNodes
    else:
        logger.add_error(msg='No found TopologinalNode',
                         device=mc_bus,
                         device_class=gcdev.Bus)

    cgmes_model.add(term)

    return term


def create_cgmes_load_response_char(load: gcdev.Load,
                                    cgmes_model: CgmesCircuit,
                                    logger: DataLogger):
    """

    :param load:
    :param cgmes_model:
    :param logger:
    :return:
    """
    new_rdf_id = get_new_rdfid()
    lrc_template = cgmes_model.get_class_type("LoadResponseCharacteristic")
    lrc = lrc_template(rdfid=new_rdf_id)
    lrc.name = f'LoadRespChar_{load.name}'
    # lrc.shortName = load.name
    lrc.exponentModel = False
    # SUPPOSING that
    lrc.pConstantImpedance = 0.0
    lrc.qConstantImpedance = 0.0
    # Expression got simpler
    lrc.pConstantPower = np.round(load.P / (load.Ir + load.P), 4)
    lrc.qConstantPower = np.round(load.Q / (load.Ii + load.Q), 4)
    lrc.pConstantCurrent = np.round(1 - lrc.pConstantPower, 4)
    lrc.qConstantCurrent = np.round(1 - lrc.qConstantPower, 4)

    # Legacy
    # lrc.pConstantCurrent = load.Ir / load.P if load.P != 0.0 else 0
    # lrc.qConstantCurrent = load.Ii / load.Q if load.Q != 0.0 else 0
    # lrc.pConstantImpedance = load.G / load.P if load.P != 0.0 else 0
    # lrc.qConstantImpedance = load.B / load.Q if load.Q != 0.0 else 0
    # lrc.pConstantPower = 1 - lrc.pConstantCurrent - lrc.pConstantImpedance
    # lrc.qConstantPower = 1 - lrc.qConstantCurrent - lrc.qConstantImpedance
    # if lrc.pConstantPower < 0 or lrc.qConstantPower < 0:
    #     logger.add_error(msg='Constant Impedance/Current parameters are not correct',
    #                      device=load,
    #                      device_class=gcdev.Load)
    # sum for 3 for p = 1
    # TODO B only 1 lrc for every load
    # if it not supports voltage dependent load, lf wont be the same
    cgmes_model.add(lrc)
    return lrc


def create_cgmes_generating_unit(gen: gcdev.Generator,
                                 cgmes_model: CgmesCircuit):
    """
    Creates the appropriate CGMES GeneratingUnit object
    from a MultiCircuit Generator.
    """

    new_rdf_id = get_new_rdfid()

    if len(gen.technologies) == 0:
        object_template = cgmes_model.get_class_type("GeneratingUnit")
        sm = object_template(new_rdf_id)
        cgmes_model.add(sm)
        return sm
    else:
        for tech_association in gen.technologies:

            if tech_association.api_object.name == 'General':
                object_template = cgmes_model.get_class_type("GeneratingUnit")
                sm = object_template(new_rdf_id)
                cgmes_model.add(sm)
                return sm

            if tech_association.api_object.name == 'Thermal':
                object_template = cgmes_model.get_class_type(
                    "ThermalGeneratingUnit")
                tgu = object_template(new_rdf_id)
                cgmes_model.add(tgu)
                return tgu

            if tech_association.api_object.name == 'Hydro':
                object_template = cgmes_model.get_class_type(
                    "HydroGeneratingUnit")
                hgu = object_template(new_rdf_id)
                cgmes_model.add(hgu)
                return hgu

            if tech_association.api_object.name == 'Solar':
                object_template = cgmes_model.get_class_type(
                    "SolarGeneratingUnit")
                sgu = object_template(new_rdf_id)
                cgmes_model.add(sgu)
                return sgu

            if tech_association.api_object.name == 'Wind Onshore':
                object_template = cgmes_model.get_class_type(
                    "WindGeneratingUnit")
                wgu = object_template(new_rdf_id)
                wgu.windGenUnitType = WindGenUnitKind.onshore
                cgmes_model.add(wgu)
                return wgu

            if tech_association.api_object.name == 'Wind Offshore':
                object_template = cgmes_model.get_class_type(
                    "WindGeneratingUnit")
                wgu = object_template(new_rdf_id)
                wgu.windGenUnitType = WindGenUnitKind.offshore
                cgmes_model.add(wgu)
                return wgu

            if tech_association.api_object.name == 'Nuclear':
                object_template = cgmes_model.get_class_type(
                    "NuclearGeneratingUnit")
                ngu = object_template(new_rdf_id)
                cgmes_model.add(ngu)
                return ngu

    return None


def create_cgmes_regulating_control(cgmes_syn,
                                    mc_gen: gcdev.Generator,
                                    cgmes_model: CgmesCircuit,
                                    logger: DataLogger):
    """
    Create Regulating Control for Generators

    :param cgmes_syn: Cgmes Synchronous Machine
    :param mc_gen: MultiCircuit Generator
    :param cgmes_model: CgmesCircuit
    :param logger:
    :return:
    """
    new_rdf_id = get_new_rdfid()
    object_template = cgmes_model.get_class_type("RegulatingControl")
    rc = object_template(rdfid=new_rdf_id)

    # RC for EQ
    rc.name = f'_RC_{mc_gen.name}'
    rc.shortName = rc.name
    rc.mode = RegulatingControlModeKind.voltage
    rc.Terminal = create_cgmes_terminal(mc_bus=mc_gen.bus,
                                        seq_num=1,
                                        cond_eq=cgmes_syn,
                                        cgmes_model=cgmes_model,
                                        logger=logger)

    rc.RegulatingCondEq = cgmes_syn
    rc.discrete = False
    rc.targetDeadband = 0.5
    rc.targetValueUnitMultiplier = UnitMultiplier.k
    rc.enabled = True  # todo correct?
    rc.targetValue = mc_gen.Vset * mc_gen.bus.Vnom
    # TODO control_cn.Vnom

    cgmes_model.add(rc)

    return rc


def create_cgmes_tap_changer_control(
        tap_changer,
        tcc_mode,
        tcc_enabled,
        mc_trafo: Union[gcdev.Transformer2W, gcdev.Transformer3W],
        cgmes_model: CgmesCircuit,
        logger: DataLogger):
    """
    Create Tap Changer Control for Tap changers.

    :param tap_changer: Cgmes tap Changer
    :param tcc_mode: TapChangerContol mode attr (RegulatingControlModeKind.voltage)
    :param tcc_enabled: TapChangerContol enabled
    :param mc_trafo: MultiCircuit Transformer
    :param cgmes_model: CgmesCircuit
    :param logger: DataLogger
    :return:
    """
    new_rdf_id = get_new_rdfid()
    object_template = cgmes_model.get_class_type("TapChangerControl")
    tcc = object_template(rdfid=new_rdf_id)

    # EQ
    tcc.name = f'_tcc_{mc_trafo.name}'
    tcc.shortName = tcc.name
    tcc.mode = tcc_mode
    tcc.Terminal = tap_changer.TransformerEnd.Terminal
    # SSH
    tcc.discrete = True
    tcc.targetDeadband = 0.5
    tcc.targetValueUnitMultiplier = UnitMultiplier.k
    tcc.enabled = tcc_enabled
    if tcc.enabled:
        tcc.targetValue = 0.0  # TODO # if enabled it should be calculated
    else:
        tcc.targetValue = None
    # tcc.RegulatingCondEq not required .?
    # control_cn.Vnom ?

    cgmes_model.add(tcc)

    return tcc


def create_cgmes_current_limit(terminal,
                               rate: float,
                               # mc_elm: Union[gcdev.Line,
                               #               # gcdev.Transformer2W,
                               #               # gcdev.Transformer3W
                               #               ],
                               cgmes_model: CgmesCircuit,
                               logger: DataLogger):
    new_rdf_id = get_new_rdfid()
    object_template = cgmes_model.get_class_type("CurrentLimit")
    curr_lim = object_template(rdfid=new_rdf_id)
    curr_lim.name = f'{terminal.name} - CL-1'
    curr_lim.shortName = f'CL-1'
    curr_lim.description = f'Ratings for element {terminal.ConductingEquipment.name} - Limit'

    curr_lim.value = rate

    op_lim_set_1 = create_operational_limit_set(terminal, cgmes_model, logger)
    if op_lim_set_1 is not None:
        curr_lim.OperationalLimitSet = op_lim_set_1
    else:
        logger.add_error(msg='No operational limit created')

    # curr_lim.OperationalLimitType

    cgmes_model.add(curr_lim)
    return


def create_operational_limit_set(terminal,
                                 cgmes_model: CgmesCircuit,
                                 logger: DataLogger):
    """

    :param terminal:
    :param cgmes_model:
    :param logger:
    :return:
    """
    new_rdf_id = get_new_rdfid()
    object_template = cgmes_model.get_class_type("OperationalLimitSet")
    op_lim_set = object_template(rdfid=new_rdf_id)
    term_num = terminal.sequenceNumber if terminal.sequenceNumber is not None else 1
    op_lim_set.name = f'OpertinalLimit at Term-{term_num}'
    op_lim_set.description = f'OpertinalLimit at Port1'

    terminal_type = cgmes_model.get_class_type('Terminal')
    if isinstance(terminal, terminal_type):
        op_lim_set.Terminal = terminal

    cgmes_model.add(op_lim_set)
    return op_lim_set


def create_operational_limit_type(mc_elm: gcdev.Line,
                                  cgmes_model: CgmesCircuit,
                                  logger: DataLogger):
    """

    :param mc_elm:
    :param cgmes_model:
    :param logger:
    :return:
    """
    new_rdf_id = get_new_rdfid()
    object_template = cgmes_model.get_class_type("OperationalLimitSet")
    op_lim_type = object_template(rdfid=new_rdf_id)

    cgmes_model.add(op_lim_type)
    return op_lim_type


def add_location(cgmes_model: CgmesCircuit,
                 device: Base,
                 longitude: float,
                 latitude: float,
                 logger: DataLogger):
    """

    :param cgmes_model:
    :param device:
    :param longitude:
    :param latitude:
    :param logger:
    :return:
    """
    object_template = cgmes_model.get_class_type("Location")
    location = object_template(rdfid=get_new_rdfid(), tpe="Location")

    location.CoordinateSystem = cgmes_model.cgmes_assets.CoordinateSystem_list[
        0]
    location.PowerSystemResource = device

    position_point_t = cgmes_model.get_class_type("PositionPoint")
    pos_point = position_point_t(rdfid=get_new_rdfid(), tpe="PositionPoint")
    pos_point.Location = location
    pos_point.sequenceNumber = 1
    pos_point.xPosition = str(longitude)
    pos_point.yPosition = str(latitude)
    location.PositionPoint = pos_point
    cgmes_model.cgmes_assets.CoordinateSystem_list[0].Locations.append(
        location)
    cgmes_model.add(location)
    cgmes_model.add(pos_point)

    device.Location = location


# endregion

# region Convert functions from MC to CC


def get_cgmes_geograpical_regions(multi_circuit_model: MultiCircuit,
                                  cgmes_model: CgmesCircuit,
                                  logger: DataLogger):
    """

    :param multi_circuit_model:
    :param cgmes_model:
    :param logger:
    :return:
    """
    for mc_class in [multi_circuit_model.countries, multi_circuit_model.areas]:
        for mc_elm in mc_class:
            object_template = cgmes_model.get_class_type("GeographicalRegion")
            geo_region = object_template(rdfid=form_rdfid(mc_elm.idtag))
            geo_region.name = mc_elm.name
            geo_region.description = mc_elm.code

            cgmes_model.add(geo_region)
    if len(cgmes_model.cgmes_assets.GeographicalRegion_list) == 0:
        logger.add_error(
            msg='Country or Area is not defined and GeographicalRegion cannot be exported',
            device_class="GeographicalRegion",
            comment="The CGMES export will not be valid!")


def get_cgmes_subgeograpical_regions(multi_circuit_model: MultiCircuit,
                                     cgmes_model: CgmesCircuit,
                                     logger: DataLogger):
    """

    :param multi_circuit_model:
    :param cgmes_model:
    :param logger:
    :return:
    """
    for mc_class in [multi_circuit_model.communities,
                     multi_circuit_model.zones]:
        for mc_elm in mc_class:
            object_template = cgmes_model.get_class_type(
                "SubGeographicalRegion")
            sub_geo_region = object_template(rdfid=form_rdfid(mc_elm.idtag))
            sub_geo_region.name = mc_elm.name
            sub_geo_region.description = mc_elm.code

            region_id = ""
            if hasattr(mc_elm, "country"):
                if mc_elm.country:
                    region_id = mc_elm.country.idtag
            elif hasattr(mc_elm, "area"):
                if mc_elm.area:
                    region_id = mc_elm.area.idtag

            region = find_object_by_uuid(
                cgmes_model=cgmes_model,
                object_list=cgmes_model.cgmes_assets.GeographicalRegion_list,
                target_uuid=region_id
            )
            if region is not None:
                sub_geo_region.Region = region
            else:
                try:
                    sub_geo_region.Region = \
                        cgmes_model.cgmes_assets.GeographicalRegion_list[0]
                except:
                    sub_geo_region.Region = None
                logger.add_warning(
                    msg='GeographicalRegion not found for SubGeographicalRegion',
                    device_class="SubGeographicalRegion")

            cgmes_model.add(sub_geo_region)
    if len(cgmes_model.cgmes_assets.SubGeographicalRegion_list) == 0:
        logger.add_error(
            msg='Community or Zone is not defined and SubGeographicalRegion cannot be exported',
            device_class="SubGeographicalRegion",
            comment="The CGMES export will not be valid!")


def get_base_voltage_from_boundary(cgmes_model: CgmesCircuit, vnom: float):
    """

    :param cgmes_model:
    :param vnom:
    :return:
    """
    bv_list = cgmes_model.elements_by_type_boundary.get("BaseVoltage")
    if bv_list is not None:
        for bv in bv_list:
            if bv.nominalVoltage == vnom:
                return bv
    return None


def get_cgmes_base_voltages(multi_circuit_model: MultiCircuit,
                            cgmes_model: CgmesCircuit,
                            logger: DataLogger) -> None:
    """

    :param multi_circuit_model:
    :param cgmes_model:
    :param logger:
    :return:
    """
    base_volt_set = set()
    for bus in multi_circuit_model.buses:

        if bus.Vnom not in base_volt_set and get_base_voltage_from_boundary(
                cgmes_model, vnom=bus.Vnom) is None:
            base_volt_set.add(bus.Vnom)

            new_rdf_id = get_new_rdfid()
            object_template = cgmes_model.get_class_type("BaseVoltage")
            base_volt = object_template(rdfid=new_rdf_id)
            base_volt.name = f'_BV_{int(bus.Vnom)}'
            base_volt.nominalVoltage = bus.Vnom

            cgmes_model.add(base_volt)
    return


def get_cgmes_substations(multi_circuit_model: MultiCircuit,
                          cgmes_model: CgmesCircuit,
                          logger: DataLogger) -> None:
    """

    :param multi_circuit_model:
    :param cgmes_model:
    :param logger:
    :return:
    """
    for mc_elm in multi_circuit_model.substations:
        object_template = cgmes_model.get_class_type("Substation")
        substation = object_template(rdfid=form_rdfid(mc_elm.idtag))
        substation.name = mc_elm.name
        region = find_object_by_uuid(
            cgmes_model=cgmes_model,
            object_list=cgmes_model.cgmes_assets.SubGeographicalRegion_list,
            target_uuid=mc_elm.community.idtag if mc_elm.community is not None else ""
            # TODO Community.idtag!
        )

        if region is not None:
            substation.Region = region
        else:
            try:
                substation.Region = cgmes_model.cgmes_assets.SubGeographicalRegion_list[0]
            except:
                substation.Region = None
            logger.add_warning(msg='Region not found for Substation',
                               device_class="SubGeographicalRegion")

        add_location(cgmes_model, substation, mc_elm.longitude,
                     mc_elm.latitude, logger)

        cgmes_model.add(substation)


def get_cgmes_voltage_levels(multi_circuit_model: MultiCircuit,
                             cgmes_model: CgmesCircuit,
                             logger: DataLogger) -> None:
    """

    :param multi_circuit_model:
    :param cgmes_model:
    :param logger:
    :return:
    """
    for mc_elm in multi_circuit_model.voltage_levels:
        object_template = cgmes_model.get_class_type("VoltageLevel")
        vl = object_template(rdfid=form_rdfid(mc_elm.idtag))
        vl.name = mc_elm.name
        vl.BaseVoltage = find_object_by_vnom(
            cgmes_model=cgmes_model,
            object_list=cgmes_model.cgmes_assets.BaseVoltage_list,
            target_vnom=mc_elm.Vnom
        )
        # vl.Bays = later
        # vl.TopologicalNode added at tn_nodes func

        if mc_elm.substation is not None:
            substation = find_object_by_uuid(
                cgmes_model=cgmes_model,
                object_list=cgmes_model.cgmes_assets.Substation_list,
                target_uuid=mc_elm.substation.idtag
            )

            if isinstance(substation, cgmes_model.get_class_type("Substation")):
                vl.Substation = substation

                # link back
                if substation.VoltageLevels is None:
                    substation.VoltageLevels = list()
                substation.VoltageLevels.append(vl)
            else:
                logger.add_error(
                    msg=f'Substation not found for VoltageLevel {vl.name}',
                    device=mc_elm,
                    device_class=gcdev.Bus)
        cgmes_model.add(vl)


def get_cgmes_tn_nodes(multi_circuit_model: MultiCircuit,
                       cgmes_model: CgmesCircuit,
                       logger: DataLogger) -> None:
    """

    :param multi_circuit_model:
    :param cgmes_model:
    :param logger:
    :return:
    """
    for bus in multi_circuit_model.buses:

        if not bus.is_internal:

            tn = find_object_by_uuid(
                cgmes_model=cgmes_model,
                object_list=cgmes_model.cgmes_assets.TopologicalNode_list,
                target_uuid=bus.idtag
            )
            if tn is not None:
                continue

            object_template = cgmes_model.get_class_type("TopologicalNode")
            tn = object_template(rdfid=form_rdfid(bus.idtag))
            tn.name = bus.name
            tn.shortName = bus.name
            tn.description = bus.code
            tn.BaseVoltage = find_object_by_vnom(
                cgmes_model=cgmes_model,
                object_list=cgmes_model.cgmes_assets.BaseVoltage_list,
                target_vnom=bus.Vnom
            )

            if bus.voltage_level is not None and cgmes_model.cgmes_assets.VoltageLevel_list:  # VoltageLevel
                vl = find_object_by_uuid(
                    cgmes_model=cgmes_model,
                    object_list=cgmes_model.cgmes_assets.VoltageLevel_list,
                    target_uuid=bus.voltage_level.idtag
                )
                tn.ConnectivityNodeContainer = vl
                # link back
                vl.TopologicalNode = tn
            else:
                print(f'Bus.voltage_level.idtag is None for {bus.name}')
                # TODO logger

            add_location(cgmes_model, tn, bus.longitude, bus.latitude, logger)

            cgmes_model.add(tn)

    return


def get_cgmes_cn_nodes_from_tn_nodes(multi_circuit_model: MultiCircuit,
                                     cgmes_model: CgmesCircuit,
                                     logger: DataLogger) -> None:
    """

    :param multi_circuit_model:
    :param cgmes_model:
    :param logger:
    :return:
    """
    for tn in cgmes_model.cgmes_assets.TopologicalNode_list:
        new_rdf_id = get_new_rdfid()
        object_template = cgmes_model.get_class_type("ConnectivityNode")
        cn = object_template(rdfid=new_rdf_id)
        cn.name = tn.name
        cn.shortName = tn.shortName
        cn.description = tn.description
        cn.BaseVoltage = tn.BaseVoltage

        tn.ConnectivityNodes = cn
        cn.TopologicalNode = tn

        if tn.ConnectivityNodeContainer:
            tn.ConnectivityNodeContainer.ConnectivityNodes = cn
            cn.ConnectivityNodeContainer = tn.ConnectivityNodeContainer

        cgmes_model.add(cn)


# def get_cgmes_cn_nodes_from_cns(multi_circuit_model: MultiCircuit,
#                                 cgmes_model: CgmesCircuit,
#                                 logger: DataLogger) -> None:
#     if not multi_circuit_model.connectivity_nodes:
#         get_cgmes_cn_nodes_from_buses(multi_circuit_model, cgmes_model, logger)
#         return
#
#     for mc_elm in multi_circuit_model.connectivity_nodes:
#         object_template = cgmes_model.get_class_type("ConnectivityNode")
#         cn = object_template(rdfid=form_rdfid(mc_elm.idtag))
#         cn.name = mc_elm.name
#         if mc_elm.default_bus is not None:
#             tn = find_object_by_uuid(
#                 cgmes_model=cgmes_model,
#                 object_list=cgmes_model.cgmes_assets.TopologicalNode_list,
#                 target_uuid=mc_elm.default_bus.idtag
#             )
#             if tn is not None:
#                 cn.TopologicalNode = tn
#                 cn.ConnectivityNodeContainer = tn.ConnectivityNodeContainer
#                 tn.ConnectivityNodes = cn  # link back
#             else:
#                 logger.add_error(msg='No TopologinalNode found',
#                                  device=cn.name,
#                                  device_class=cn.tpe)
#         else:
#             logger.add_error(msg='Connectivity Node has no default bus',
#                              device=mc_elm.name,
#                              device_class=mc_elm.device_type)
#             # print(f'Topological node not found for cn: {cn.name}')
#
#         cgmes_model.add(cn)
#
#     return


def get_cgmes_loads(multicircuit_model: MultiCircuit,
                    cgmes_model: CgmesCircuit,
                    logger: DataLogger):
    """
    Converts every Multi Circuit load into CGMES ConformLoad.

    :param multicircuit_model:
    :param cgmes_model:
    :param logger:
    :return:
    """

    for mc_elm in multicircuit_model.loads:
        object_template = cgmes_model.get_class_type("ConformLoad")
        cl = object_template(rdfid=form_rdfid(mc_elm.idtag))
        cl.Terminals = create_cgmes_terminal(mc_elm.bus, None, cl, cgmes_model,
                                             logger)
        cl.name = mc_elm.name

        if mc_elm.bus.voltage_level:
            vl = find_object_by_uuid(
                cgmes_model=cgmes_model,
                object_list=cgmes_model.cgmes_assets.VoltageLevel_list,
                target_uuid=mc_elm.bus.voltage_level.idtag
            )
            cl.EquipmentContainer = vl

        cl.BaseVoltage = find_object_by_vnom(cgmes_model=cgmes_model,
                                             object_list=cgmes_model.cgmes_assets.BaseVoltage_list,
                                             target_vnom=mc_elm.bus.Vnom)

        if mc_elm.Ii != 0.0:
            cl.LoadResponse = create_cgmes_load_response_char(load=mc_elm,
                                                              cgmes_model=cgmes_model,
                                                              logger=logger)
            # cl.LoadGroup = ConformLoadGroup ..?
            cl.p = mc_elm.P / cl.LoadResponse.pConstantPower
            cl.q = mc_elm.Q / cl.LoadResponse.qConstantPower
        else:
            cl.p = mc_elm.P
            cl.q = mc_elm.Q

        cl.description = mc_elm.code

        cgmes_model.add(cl)


def get_cgmes_equivalent_injections(multicircuit_model: MultiCircuit,
                                    cgmes_model: CgmesCircuit,
                                    logger: DataLogger):
    """
    Converts every Multi Circuit external grid
    into CGMES equivalent injection.

    :param multicircuit_model:
    :param cgmes_model:
    :param logger:
    :return:
    """

    for mc_elm in multicircuit_model.external_grids:
        object_template = cgmes_model.get_class_type("EquivalentInjection")
        ei = object_template(rdfid=form_rdfid(mc_elm.idtag))
        ei.description = mc_elm.code
        ei.name = mc_elm.name
        ei.p = mc_elm.P
        ei.q = mc_elm.Q
        ei.BaseVoltage = find_object_by_vnom(cgmes_model=cgmes_model,
                                             object_list=cgmes_model.cgmes_assets.BaseVoltage_list,
                                             target_vnom=mc_elm.bus.Vnom)
        ei.Terminals = create_cgmes_terminal(mc_elm.bus, None, ei, cgmes_model,
                                             logger)
        ei.regulationCapability = False

        cgmes_model.add(ei)


def get_cgmes_ac_line_segments(multicircuit_model: MultiCircuit,
                               cgmes_model: CgmesCircuit,
                               logger: DataLogger):
    """
    Converts every Multi Circuit line
    into CGMES AC line segment.

    :param multicircuit_model:
    :param cgmes_model:
    :param logger:
    :return:
    """
    sbase = multicircuit_model.Sbase
    for mc_elm in multicircuit_model.lines:
        object_template = cgmes_model.get_class_type("ACLineSegment")
        line = object_template(rdfid=form_rdfid(mc_elm.idtag))
        line.description = mc_elm.code
        line.name = mc_elm.name
        line.BaseVoltage = find_object_by_vnom(cgmes_model=cgmes_model,
                                               object_list=cgmes_model.cgmes_assets.BaseVoltage_list,
                                               target_vnom=mc_elm.get_max_bus_nominal_voltage()
                                               )  # which Vnom we need?
        line.Terminals = [
            create_cgmes_terminal(mc_elm.bus_from, 1, line, cgmes_model,
                                  logger),
            create_cgmes_terminal(mc_elm.bus_to, 2, line, cgmes_model, logger)]
        line.length = mc_elm.length

        current_rate = mc_elm.rate * 1e3 / (
                mc_elm.get_max_bus_nominal_voltage() * 1.73205080756888)
        current_rate = np.round(current_rate, 4)
        create_cgmes_current_limit(line.Terminals[0], current_rate,
                                   cgmes_model, logger)
        create_cgmes_current_limit(line.Terminals[1], current_rate,
                                   cgmes_model, logger)

        vnom = line.BaseVoltage.nominalVoltage

        if vnom is not None:
            # Calculate Zbase
            zbase = (vnom * vnom) / sbase
            ybase = 1.0 / zbase

            line.r = mc_elm.R * zbase
            line.x = mc_elm.X * zbase
            # line.gch = mc_elm.G * Ybase
            line.bch = mc_elm.B * ybase
            line.r0 = mc_elm.R0 * zbase
            line.x0 = mc_elm.X0 * zbase
            # line.g0ch = mc_elm.G0 * Ybase
            line.b0ch = mc_elm.B0 * ybase

        cgmes_model.add(line)


def get_cgmes_generators(multicircuit_model: MultiCircuit,
                         cgmes_model: CgmesCircuit,
                         logger: DataLogger):
    """
    Converts Multi Circuit generators
    into approriate CGMES Generating Unit.

    :param multicircuit_model:
    :param cgmes_model:
    :param logger:
    :return:
    """

    for mc_elm in multicircuit_model.generators:
        # Generating Units ---------------------------------------------------
        cgmes_gen = create_cgmes_generating_unit(
            gen=mc_elm, cgmes_model=cgmes_model
        )
        cgmes_gen.name = mc_elm.name
        cgmes_gen.description = mc_elm.code
        # cgmes_gen.EquipmentContainer: cgmes.Substation
        if cgmes_model.cgmes_assets.Substation_list:
            subs = find_object_by_uuid(
                cgmes_model=cgmes_model,
                object_list=cgmes_model.cgmes_assets.Substation_list,
                target_uuid=mc_elm.bus.substation.idtag
            )
            if subs is not None:
                cgmes_gen.EquipmentContainer = subs
                # link back
                if isinstance(subs.Equipments, list):
                    subs.Equipment.append(cgmes_gen)
                else:
                    subs.Equipment = [cgmes_gen]
            else:
                print(f'No substation found for generator {mc_elm.name}')
                # TODO logger

        cgmes_gen.initialP = mc_elm.P
        cgmes_gen.maxOperatingP = mc_elm.Pmax
        cgmes_gen.minOperatingP = mc_elm.Pmin

        # Synchronous Machine ------------------------------------------------
        object_template = cgmes_model.get_class_type("SynchronousMachine")
        cgmes_syn = object_template(rdfid=form_rdfid(mc_elm.idtag))
        cgmes_syn.description = mc_elm.code
        cgmes_syn.name = mc_elm.name
        # cgmes_syn.aggregate is optional, not exported
        if mc_elm.bus.is_slack:
            cgmes_syn.referencePriority = 1
            cgmes_gen.normalPF = 1  # in gridcal the participation factor is the cost
        else:
            cgmes_syn.referencePriority = 0
            cgmes_gen.normalPF = 0
        # TODO cgmes_syn.EquipmentContainer: VoltageLevel

        # has_control: do we have control
        # control_type: voltage or power control, ..
        # is_controlled: enabling flag (already have)
        if mc_elm.is_controlled:
            cgmes_syn.RegulatingControl = (
                create_cgmes_regulating_control(cgmes_syn, mc_elm, cgmes_model,
                                                logger))
            cgmes_syn.controlEnabled = True
        else:
            cgmes_syn.controlEnabled = False

        # Todo cgmes_syn.ratedPowerFactor = 1.0
        cgmes_syn.ratedS = mc_elm.Snom
        cgmes_syn.GeneratingUnit = cgmes_gen  # linking them together
        cgmes_gen.RotatingMachine = cgmes_syn  # linking them together
        cgmes_syn.maxQ = mc_elm.Qmax
        cgmes_syn.minQ = mc_elm.Qmin
        cgmes_syn.r = mc_elm.R1 if mc_elm.R1 != 1e-20 else None  # default value not exported
        cgmes_syn.p = -mc_elm.P  # negative sign!
        cgmes_syn.q = -mc_elm.P * np.tan(np.arccos(mc_elm.Pf))
        # TODO cgmes_syn.qPercent =
        if mc_elm.q_curve is not None:
            pMin = mc_elm.q_curve.get_Pmin()
        else:
            pMin = mc_elm.Pmin
        if cgmes_syn.p < 0:
            cgmes_syn.operatingMode = SynchronousMachineOperatingMode.generator
            if pMin < 0:
                cgmes_syn.type = SynchronousMachineKind.generatorOrMotor
            elif pMin == 0:
                cgmes_syn.type = SynchronousMachineKind.generatorOrCondenser
            else:
                cgmes_syn.type = SynchronousMachineKind.generator
        elif cgmes_syn.p == 0:
            cgmes_syn.operatingMode = SynchronousMachineOperatingMode.condenser
            if pMin < 0:  # TODO We don't have all the types
                cgmes_syn.type = SynchronousMachineKind.motorOrCondenser
            elif pMin == 0:
                cgmes_syn.type = SynchronousMachineKind.generatorOrCondenser
            else:
                cgmes_syn.type = SynchronousMachineKind.generatorOrCondenser
        else:
            cgmes_syn.operatingMode = SynchronousMachineOperatingMode.motor
            if pMin < 0:
                cgmes_syn.type = SynchronousMachineKind.generatorOrMotor
            elif pMin == 0:
                cgmes_syn.type = SynchronousMachineKind.motorOrCondenser
            else:
                cgmes_syn.type = SynchronousMachineKind.generatorOrMotor

        # generatorOrCondenser = 'generatorOrCondenser'
        # generator = 'generator'
        # generatorOrMotor = 'generatorOrMotor'
        # motor = 'motor'
        # motorOrCondenser = 'motorOrCondenser'
        # generatorOrCondenserOrMotor = 'generatorOrCondenserOrMotor'
        # condenser = 'condenser'

        if mc_elm.bus.voltage_level:
            vl = find_object_by_uuid(
                cgmes_model=cgmes_model,
                object_list=cgmes_model.cgmes_assets.VoltageLevel_list,
                target_uuid=mc_elm.bus.voltage_level.idtag
            )
            cgmes_syn.EquipmentContainer = vl

        cgmes_syn.BaseVoltage = find_object_by_vnom(cgmes_model=cgmes_model,
                                                    object_list=cgmes_model.cgmes_assets.BaseVoltage_list,
                                                    target_vnom=mc_elm.bus.Vnom)
        cgmes_model.add(cgmes_syn)


def get_cgmes_power_transformers(multicircuit_model: MultiCircuit,
                                 cgmes_model: CgmesCircuit,
                                 logger: DataLogger):
    """
    Creates all transformer related CGMES classes from GridCal transformer.

    :param multicircuit_model:
    :param cgmes_model:
    :param logger:
    :return:
    """
    for mc_elm in multicircuit_model.transformers2w:
        object_template = cgmes_model.get_class_type("PowerTransformer")
        cm_transformer = object_template(rdfid=form_rdfid(mc_elm.idtag))
        cm_transformer.uuid = mc_elm.idtag
        cm_transformer.description = mc_elm.code
        cm_transformer.name = mc_elm.name
        cm_transformer.Terminals = [
            create_cgmes_terminal(mc_elm.bus_from, 1, cm_transformer,
                                  cgmes_model, logger),
            create_cgmes_terminal(mc_elm.bus_to, 2, cm_transformer,
                                  cgmes_model, logger)]
        cm_transformer.aggregate = False  # what is this?
        if mc_elm.bus_from.substation:
            cm_transformer.EquipmentContainer = find_object_by_uuid(
                cgmes_model=cgmes_model,
                object_list=cgmes_model.cgmes_assets.Substation_list,
                target_uuid=mc_elm.bus_from.substation.idtag
            )

        cm_transformer.PowerTransformerEnd = list()
        object_template = cgmes_model.get_class_type("PowerTransformerEnd")
        pte1 = object_template()
        pte1.PowerTransformer = cm_transformer
        pte1.Terminal = cm_transformer.Terminals[0]
        pte1.BaseVoltage = find_object_by_vnom(
            cgmes_model=cgmes_model,
            object_list=cgmes_model.cgmes_assets.BaseVoltage_list,
            target_vnom=mc_elm.bus_from.Vnom
        )

        current_rate = mc_elm.rate * 1e3 / (
                mc_elm.get_max_bus_nominal_voltage() * 1.73205080756888)
        current_rate = np.round(current_rate, 4)
        create_cgmes_current_limit(cm_transformer.Terminals[0], current_rate,
                                   cgmes_model, logger)
        create_cgmes_current_limit(cm_transformer.Terminals[1], current_rate,
                                   cgmes_model, logger)

        (pte1.r,
         pte1.x,
         pte1.g,
         pte1.b,
         pte1.r0,
         pte1.x0,
         pte1.g0,
         pte1.b0) = get_ohm_values_power_transformer(r=mc_elm.R,
                                                     x=mc_elm.X,
                                                     g=mc_elm.G,
                                                     b=mc_elm.B,
                                                     r0=mc_elm.R0,
                                                     x0=mc_elm.X0,
                                                     g0=mc_elm.G0,
                                                     b0=mc_elm.B0,
                                                     nominal_power=mc_elm.Sn,
                                                     rated_voltage=mc_elm.HV)

        pte1.ratedU = mc_elm.HV
        pte1.ratedS = mc_elm.Sn
        pte1.endNumber = 1

        pte2 = object_template()
        pte2.PowerTransformer = cm_transformer
        pte2.Terminal = cm_transformer.Terminals[1]
        pte2.BaseVoltage = find_object_by_vnom(
            cgmes_model=cgmes_model,
            object_list=cgmes_model.cgmes_assets.BaseVoltage_list,
            target_vnom=mc_elm.bus_to.Vnom
        )

        # TODO: Shouldn't this be half?
        pte2.r = 0.0
        pte2.x = 0.0
        pte2.g = 0.0
        pte2.b = 0.0
        pte2.r0 = 0.0
        pte2.x0 = 0.0
        pte2.g0 = 0.0
        pte2.b0 = 0.0
        pte2.ratedU = mc_elm.LV
        pte2.ratedS = mc_elm.Sn
        pte2.endNumber = 2

        # -------------------- RATIO TAP  & PHASE TAP -----------------------
        # RatioTapChanger (tcc: voltage, disabled)	<--	-->	NoRegulation
        # RatioTapChanger (tcc: voltage, enabled)	<--	-->	Voltage
        # PhaseTapChangerSymmetrical	<--	-->	Symmetrical
        # PhaseTapChangerAsymmetrical	<--	-->	Asymmetrical
        #                         TAP Changer EQ

        tcc_mode = RegulatingControlModeKind.voltage
        tcc_enabled = False

        if mc_elm.tap_changer.tc_type == TapChangerTypes.NoRegulation:
            object_template = cgmes_model.get_class_type("RatioTapChanger")
        elif mc_elm.tap_changer.tc_type == TapChangerTypes.VoltageRegulation:
            object_template = cgmes_model.get_class_type("RatioTapChanger")
            tcc_enabled = True
        elif mc_elm.tap_changer.tc_type == TapChangerTypes.Symmetrical:
            object_template = cgmes_model.get_class_type("PhaseTapChangerSymmetrical")
            tcc_enabled = True
            tcc_mode = RegulatingControlModeKind.activePower
        elif mc_elm.tap_changer.tc_type == TapChangerTypes.Asymmetrical:
            object_template = cgmes_model.get_class_type("PhaseTapChangerAsymmetrical")
            tcc_enabled = True
            tcc_mode = RegulatingControlModeKind.activePower
        else:
            logger.add_error(msg='No TapChangerType found for TapChanger',
                             device=mc_elm.tap_changer,
                             device_class=gcdev.TapChanger,
                             value=mc_elm.tap_changer)
        new_rdf_id = get_new_rdfid()
        tap_changer = object_template(rdfid=new_rdf_id)
        tap_changer.name = f'_tc_{mc_elm.name}'
        tap_changer.shortName = f'_tc_{mc_elm.name}'

        tap_changer.neutralU = pte1.BaseVoltage.nominalVoltage
        tap_changer.TransformerEnd = pte1

        # STEPs
        tap_changer.total_pos = mc_elm.tap_changer.total_positions
        (tap_changer.lowStep,
         tap_changer.highStep,
         tap_changer.normalStep,
         tap_changer.neutralStep,
         voltageIncr,
         tap_changer.step) = mc_elm.tap_changer.get_cgmes_values()

        try:
            tap_changer.stepVoltageIncrement = voltageIncr
        except:
            tap_changer.voltageStepIncrement = voltageIncr
        finally:
            logger.add_error(msg='stepVoltageIncerment cannot be filled fot TapChanger',
                             device=mc_elm,
                             device_class=gcdev.Transformer2W,
                             value=mc_elm.idtag)

        # CONTROL
        tap_changer.ltcFlag = False  # load tap changing capability
        tap_changer.TapChangerControl = create_cgmes_tap_changer_control(
            tap_changer=tap_changer,
            tcc_mode=tcc_mode,
            tcc_enabled=tcc_enabled,
            mc_trafo=cm_transformer,
            cgmes_model=cgmes_model,
            logger=logger
        )
        # tculControlMode not used, but be set to something: volt/react ..
        tap_changer.tculControlMode = TransformerControlMode.volt
        #                   TAP Changer SSH
        tap_changer.controlEnabled = tcc_enabled
        # Specifies the regulation status of the equipment.  True is regulating, false is not regulating.
        # why, why not?

        #                   TAP Changer SV
        new_rdf_id = get_new_rdfid()
        object_template = cgmes_model.get_class_type("SvTapStep")
        sv_tap_step = object_template(rdfid=new_rdf_id, tpe="SvTapStep")
        # TODO def EA same as step? should it come from the results?
        # PowerFlowResults: tap_module, tap_angle (for SvTapStep), get the closest tap pos for the object.
        sv_tap_step.position = mc_elm.tap_changer.tap_position
        sv_tap_step.TapChanger = tap_changer

        # -----------------------------------------------------------------
        cgmes_model.add(tap_changer)
        cgmes_model.add(sv_tap_step)

        cm_transformer.PowerTransformerEnd.append(pte1)
        cgmes_model.add(pte1)
        cm_transformer.PowerTransformerEnd.append(pte2)
        cgmes_model.add(pte2)

        cgmes_model.add(cm_transformer)

    # ------------------------------------------------------------------------------------------------------------------
    # Create the 3W transformers
    # ------------------------------------------------------------------------------------------------------------------

    for mc_elm in multicircuit_model.transformers3w:
        object_template = cgmes_model.get_class_type("PowerTransformer")
        cm_transformer = object_template(rdfid=form_rdfid(mc_elm.idtag))
        cm_transformer.uuid = mc_elm.idtag
        cm_transformer.description = mc_elm.code
        cm_transformer.name = mc_elm.name
        cm_transformer.Terminals = [
            create_cgmes_terminal(mc_elm.bus1, 1, cm_transformer, cgmes_model,
                                  logger),
            create_cgmes_terminal(mc_elm.bus2, 2, cm_transformer, cgmes_model,
                                  logger),
            create_cgmes_terminal(mc_elm.bus3, 3, cm_transformer, cgmes_model,
                                  logger)]

        cm_transformer.PowerTransformerEnd = []
        object_template = cgmes_model.get_class_type("PowerTransformerEnd")

        cm_transformer.EquipmentContainer = find_object_by_uuid(
            cgmes_model=cgmes_model,
            object_list=cgmes_model.cgmes_assets.Substation_list,
            target_uuid=mc_elm.bus1.substation.idtag
        )

        # TODO tr3w rates?
        # current_rate = mc_elm.rate * 1e3 / (mc_elm.get_max_bus_nominal_voltage() * 1.73205080756888)
        # current_rate = np.round(current_rate, 4)
        # create_cgmes_current_limit(cm_transformer.Terminals[0], current_rate, cgmes_model, logger)
        # create_cgmes_current_limit(cm_transformer.Terminals[1], current_rate, cgmes_model, logger)

        # Winding 1 ----------------------------------------------------------------------------------------------------
        pte1 = object_template()
        pte1.PowerTransformer = cm_transformer
        pte1.Terminal = cm_transformer.Terminals[0]
        pte1.BaseVoltage = find_object_by_vnom(
            cgmes_model=cgmes_model,
            object_list=cgmes_model.cgmes_assets.BaseVoltage_list,
            target_vnom=mc_elm.bus1.Vnom
        )
        pte1.ratedU = mc_elm.V1
        pte1.ratedS = mc_elm.rate1
        pte1.endNumber = 1

        (pte1.r,
         pte1.x,
         pte1.g,
         pte1.b,
         pte1.r0,
         pte1.x0,
         pte1.g0,
         pte1.b0) = get_ohm_values_power_transformer(r=mc_elm.winding1.R,
                                                     x=mc_elm.winding1.X,
                                                     g=mc_elm.winding1.G,
                                                     b=mc_elm.winding1.B,
                                                     r0=mc_elm.winding1.R0,
                                                     x0=mc_elm.winding1.X0,
                                                     g0=mc_elm.winding1.G0,
                                                     b0=mc_elm.winding1.B0,
                                                     nominal_power=mc_elm.winding1.rate,
                                                     rated_voltage=mc_elm.winding1.HV)

        # Winding 2 ----------------------------------------------------------------------------------------------------
        pte2 = object_template()
        pte2.PowerTransformer = cm_transformer
        pte2.Terminal = cm_transformer.Terminals[1]
        pte2.BaseVoltage = find_object_by_vnom(
            cgmes_model=cgmes_model,
            object_list=cgmes_model.cgmes_assets.BaseVoltage_list,
            target_vnom=mc_elm.bus2.Vnom
        )
        pte2.ratedU = mc_elm.V2
        pte2.ratedS = mc_elm.rate2
        pte2.endNumber = 2

        (pte2.r,
         pte2.x,
         pte2.g,
         pte2.b,
         pte2.r0,
         pte2.x0,
         pte2.g0,
         pte2.b0) = get_ohm_values_power_transformer(r=mc_elm.winding2.R,
                                                     x=mc_elm.winding2.X,
                                                     g=mc_elm.winding2.G,
                                                     b=mc_elm.winding2.B,
                                                     r0=mc_elm.winding2.R0,
                                                     x0=mc_elm.winding2.X0,
                                                     g0=mc_elm.winding2.G0,
                                                     b0=mc_elm.winding2.B0,
                                                     nominal_power=mc_elm.winding2.rate,
                                                     rated_voltage=mc_elm.winding2.HV)

        # TODO: what is this?
        # if cgmes_model.cgmes_version == CGMESVersions.v2_4_15:
        #     pte2.r0 = r0
        #     pte2.x0 = x0
        #     pte2.g0 = g0
        #     pte2.b0 = b0

        # Winding 3 ----------------------------------------------------------------------------------------------------
        pte3 = object_template()
        pte3.PowerTransformer = cm_transformer
        pte3.Terminal = cm_transformer.Terminals[2]
        pte3.BaseVoltage = find_object_by_vnom(
            cgmes_model=cgmes_model,
            object_list=cgmes_model.cgmes_assets.BaseVoltage_list,
            target_vnom=mc_elm.bus3.Vnom
        )
        pte3.ratedU = mc_elm.V3
        pte3.ratedS = mc_elm.rate3
        pte3.endNumber = 3

        (pte3.r,
         pte3.x,
         pte3.g,
         pte3.b,
         pte3.r0,
         pte3.x0,
         pte3.g0,
         pte3.b0) = get_ohm_values_power_transformer(r=mc_elm.winding3.R,
                                                     x=mc_elm.winding3.X,
                                                     g=mc_elm.winding3.G,
                                                     b=mc_elm.winding3.B,
                                                     r0=mc_elm.winding3.R0,
                                                     x0=mc_elm.winding3.X0,
                                                     g0=mc_elm.winding3.G0,
                                                     b0=mc_elm.winding3.B0,
                                                     nominal_power=mc_elm.winding3.rate,
                                                     rated_voltage=mc_elm.winding3.HV)

        # compose transformer ------------------------------------------------------------------------------------------
        cm_transformer.PowerTransformerEnd.append(pte1)
        cgmes_model.add(pte1)
        cm_transformer.PowerTransformerEnd.append(pte2)
        cgmes_model.add(pte2)
        cm_transformer.PowerTransformerEnd.append(pte3)
        cgmes_model.add(pte3)

        cgmes_model.add(cm_transformer)


def get_cgmes_linear_shunts(multicircuit_model: MultiCircuit,
                            cgmes_model: CgmesCircuit,
                            logger: DataLogger):
    """
    Converts Multi Circuit shunts
    into CGMES Linear shunt compensator

    :param multicircuit_model:
    :param cgmes_model:
    :param logger:
    :return:
    """

    for mc_elm in multicircuit_model.shunts:

        object_template = cgmes_model.get_class_type("LinearShuntCompensator")
        lsc = object_template(rdfid=form_rdfid(mc_elm.idtag))
        lsc.name = mc_elm.name
        lsc.description = mc_elm.code
        if mc_elm.bus.voltage_level:
            vl = find_object_by_uuid(
                cgmes_model=cgmes_model,
                object_list=cgmes_model.cgmes_assets.VoltageLevel_list,
                target_uuid=mc_elm.bus.voltage_level.idtag
            )
            lsc.EquipmentContainer = vl

        lsc.BaseVoltage = find_object_by_vnom(cgmes_model=cgmes_model,
                                              object_list=cgmes_model.cgmes_assets.BaseVoltage_list,
                                              target_vnom=mc_elm.bus.Vnom)
        # lsc.RegulatingControl = False  # TODO: Should be an object
        lsc.controlEnabled = False
        lsc.maximumSections = 1

        lsc.nomU = mc_elm.bus.Vnom
        lsc.bPerSection = mc_elm.B / (lsc.nomU ** 2)
        lsc.gPerSection = mc_elm.G / (lsc.nomU ** 2)
        if mc_elm.active:
            lsc.sections = 1
        else:
            lsc.sections = 0
        lsc.normalSections = lsc.sections

        lsc.Terminals = create_cgmes_terminal(mc_elm.bus, None, lsc,
                                              cgmes_model, logger)

        cgmes_model.add(lsc)


def get_cgmes_sv_voltages(cgmes_model: CgmesCircuit,
                          pf_results: PowerFlowResults,
                          logger: DataLogger) -> None:
    """
    Creates a CgmesCircuit SvVoltage_list
    from PowerFlow results of the numerical circuit.

    Args:
        cgmes_model: CgmesCircuit
        pf_results: PowerFlowResults
        logger (DataLogger): The data logger for error handling.

    Returns:
        CgmesCircuit: A CgmesCircuit object with SvVoltage_list populated.
    """
    # SvVoltage: v, (a?) -> TopologicalNode

    for i, voltage in enumerate(pf_results.voltage):
        object_template = cgmes_model.get_class_type("SvVoltage")
        new_rdf_id = get_new_rdfid()
        sv_voltage = object_template(rdfid=new_rdf_id, tpe='SvVoltage')

        tp_list_with_boundary = (
                cgmes_model.cgmes_assets.TopologicalNode_list +
                cgmes_model.elements_by_type_boundary.get(
                    'TopologicalNode', None))
        sv_voltage.TopologicalNode = tp_list_with_boundary[i]

        # as the ORDER of the results is the same as the order of buses (=tn)
        bv = tp_list_with_boundary[i].BaseVoltage
        sv_voltage.v = np.abs(voltage) * bv.nominalVoltage
        sv_voltage.angle = np.angle(voltage, deg=True)

        # Add the SvVoltage instance to the SvVoltage_list
        cgmes_model.add(sv_voltage)


def get_cgmes_sv_power_flow(multi_circuit: MultiCircuit,
                            nc: NumericalCircuit,
                            cgmes_model: CgmesCircuit,
                            pf_results: PowerFlowResults,
                            logger: DataLogger) -> None:
    """
    Creates a CgmesCircuit SvPowerFlow_list from PowerFlow results of the numerical circuit.

    :param multi_circuit:
    :param nc:
    :param cgmes_model:
    :param pf_results:
    :param logger:
    :return: SvVoltage_list is populated in CgmesCircuit.
    """
    # SVPowerFlow: p, q -> Terminals
    # SvPowerFlow class is required to be instantiated for the following classes:
    # subclasses of the RotatingMachine,
    # subclasses of the EnergyConsumer,
    # EquivalentInjection,
    # ShuntCompensator,
    # StaticVarCompensator and
    # EnergySource.

    # Generators ------------------------------------------------------------
    gen_objects = multi_circuit.generators

    gen_ps = nc.generator_data.p
    gen_qs = pf_results.gen_q

    for (gen, gen_p, gen_q) in zip(gen_objects, gen_ps, gen_qs):

        term = find_object_by_cond_eq_uuid(
            object_list=cgmes_model.cgmes_assets.Terminal_list,
            cond_eq_target_uuid=gen.idtag
        )
        if isinstance(term, cgmes_model.get_class_type("Terminal")):

            create_sv_power_flow(
                cgmes_model=cgmes_model,
                p=gen_p,
                q=gen_q,
                terminal=term
            )

        else:
            logger.add_error(msg='No Terminal found for Generator',
                             device=gen,
                             device_class=gcdev.Generator,
                             value=gen.idtag)

    # Load-like devices -----------------------------------------------------
    # loads, static_generators, external_grids, current_injections
    load_objects = multi_circuit.get_load_like_devices()

    load_power = compute_zip_power(
        S0=nc.load_data.S,
        I0=nc.load_data.I,
        Y0=nc.load_data.Y,
        Vm=np.abs(pf_results.voltage[nc.load_data.get_bus_indices()])
    )

    for (mc_load_like, load_power) in zip(load_objects, load_power):

        term = find_object_by_cond_eq_uuid(
            object_list=cgmes_model.cgmes_assets.Terminal_list,
            cond_eq_target_uuid=mc_load_like.idtag  # missing Load uuid
        )
        if isinstance(term, cgmes_model.get_class_type("Terminal")):

            create_sv_power_flow(
                cgmes_model=cgmes_model,
                p=load_power.real,
                q=load_power.imag,
                terminal=term
            )

        else:
            logger.add_error(msg='No Terminal found for Load-like device',
                             device=mc_load_like,
                             device_class=gcdev.Load,
                             value=mc_load_like.idtag)

    # Shunts ----------------------------------------------------------------
    # shunts, controllable shunts
    shunt_objects = multi_circuit.get_shunt_like_devices()

    shunt_qs = pf_results.shunt_q

    for (mc_shunt_like, shunt_q) in zip(shunt_objects, shunt_qs):

        term = find_object_by_cond_eq_uuid(
            object_list=cgmes_model.cgmes_assets.Terminal_list,
            cond_eq_target_uuid=mc_shunt_like.idtag  # missing Load uuid
        )
        if isinstance(term, cgmes_model.get_class_type("Terminal")):

            create_sv_power_flow(
                cgmes_model=cgmes_model,
                p=0.0,
                q=shunt_q,
                terminal=term
            )

        else:
            logger.add_error(msg='No Terminal found for Shunt-like device',
                             device=mc_shunt_like,
                             device_class=gcdev.Load,
                             value=mc_shunt_like.idtag)

    # TODO pf_results.loading is what?


def create_sv_power_flow(cgmes_model: CgmesCircuit,
                         p: float,
                         q: float,
                         terminal) -> None:
    """
    Creates a SvPowerFlow instance

    :param cgmes_model:
    :param p: The active power flow. Load sign convention is used,
                i.e. positive sign means flow out
                from a TopologicalNode (bus) into the conducting equipment.
    :param q:
    :param terminal:
    :return:
    """
    object_template = cgmes_model.get_class_type("SvPowerFlow")
    new_rdf_id = get_new_rdfid()
    sv_pf = object_template(rdfid=new_rdf_id)

    sv_pf.p = p
    sv_pf.q = q
    sv_pf.Terminal = terminal

    cgmes_model.add(sv_pf)


def create_sv_shunt_compensator_sections(cgmes_model: CgmesCircuit,
                                         sections: int,
                                         cgmes_shunt_compensator) -> None:
    """
    Creates a SvShuntCompensatorSections instance

    :param cgmes_model: Cgmes Circuit
    :param sections:
    :param cgmes_shunt_compensator: Linear or Non-linear
        ShuntCompensator instance from cgmes model
    :return:
    """
    object_template = cgmes_model.get_class_type("SvShuntCompensatorSections")
    new_rdf_id = get_new_rdfid()
    sv_scs = object_template(rdfid=new_rdf_id)

    # sections: The number of sections in service as a continous variable.
    # To get integer value scale with ShuntCompensator.bPerSection.
    sv_scs.sections = sections
    sv_scs.ShuntCompensator = cgmes_shunt_compensator

    cgmes_model.add(sv_scs)


def create_sv_status(cgmes_model: CgmesCircuit,
                     in_service: int,
                     cgmes_conducting_equipment) -> None:
    """
    Creates a SvStatus instance

    :param cgmes_model: Cgmes Circuit
    :param in_service: is active paramater
    :param cgmes_conducting_equipment: cgmes CondEq
    :return:
    """
    object_template = cgmes_model.get_class_type("SvStatus")
    new_rdf_id = get_new_rdfid()
    sv_status = object_template(rdfid=new_rdf_id)

    sv_status.inService = in_service
    # TODO sv_status.ConductingEquipment = cgmes_conducting_equipment

    cgmes_model.add(sv_status)


def get_cgmes_sv_tap_step(multi_circuit: MultiCircuit,
                          nc: NumericalCircuit,
                          cgmes_model: CgmesCircuit,
                          pf_results: PowerFlowResults,
                          logger: DataLogger) -> None:
    branch_objects = multi_circuit.get_branches_wo_hvdc()

    tap_modules = pf_results.tap_module

    for (branch, t_m) in zip(branch_objects, tap_modules):

        if isinstance(branch, gcdev.Transformer2W):
            pass
            # branch.tap_changer.h

    pass


def get_cgmes_topological_island(multicircuit_model: MultiCircuit,
                                 cgmes_model: CgmesCircuit,
                                 logger: DataLogger):
    # TODO get nc as an input
    nc = compile_numerical_circuit_at(multicircuit_model)
    nc_islands = nc.split_into_islands()
    tpi_template = cgmes_model.get_class_type("TopologicalIsland")
    i = 0
    for nc_i in nc_islands:
        i = i + 1
        new_island = tpi_template(get_new_rdfid())
        new_island.name = "TopologicalIsland" + str(i)
        new_island.TopologicalNodes = []
        bus_names = nc_i.bus_names
        mc_buses = []
        for tn_name in bus_names:
            tn = find_tn_by_name(cgmes_model, tn_name)
            if tn:
                new_island.TopologicalNodes.append(tn)
                mc_bus = find_object_by_attribute(multicircuit_model.buses,
                                                  "name", tn_name)
                mc_buses.append(mc_bus)
        if mc_buses:
            slack_bus = find_object_by_attribute(mc_buses, "is_slack", True)
            if slack_bus:
                slack_tn = find_object_by_uuid(cgmes_model,
                                               cgmes_model.cgmes_assets.TopologicalNode_list,
                                               slack_bus.idtag)
                new_island.AngleRefTopologicalNode = slack_tn
                for tn in new_island.TopologicalNodes:
                    tn.AngleRefTopologicalIsland = slack_tn
            else:
                logger.add_warning(
                    msg="AngleRefTopologicalNode missing from TopologicalIsland!",
                    device=new_island.name,
                    device_property="AngleRefTopologicalNode")
        cgmes_model.add(new_island)


def make_coordinate_system(cgmes_model: CgmesCircuit,
                           logger: DataLogger):
    object_template = cgmes_model.get_class_type("CoordinateSystem")
    coo_sys = object_template(rdfid=get_new_rdfid())

    coo_sys.name = "EPSG4326"
    coo_sys.crsUrn = "urn:ogc:def:crs:EPSG::4326"
    coo_sys.Locations = []

    cgmes_model.add(coo_sys)


# endregion


def gridcal_to_cgmes(gc_model: MultiCircuit,
                     num_circ: NumericalCircuit,
                     pf_results: Union[None, PowerFlowResults],
                     cgmes_model: CgmesCircuit,
                     logger: DataLogger) -> CgmesCircuit:
    """
    Converts the input Multi circuit to a new CGMES Circuit.

    :param gc_model: Multi circuit object
    :param num_circ: Numerical circuit complied from MC
    :param cgmes_model: CGMES circuit object
    :param pf_results: power flow results from GridCal
    :param logger: Logger object
    :return: CGMES circuit (as a new object)
    """

    get_cgmes_geograpical_regions(gc_model, cgmes_model, logger)
    get_cgmes_subgeograpical_regions(gc_model, cgmes_model, logger)

    make_coordinate_system(cgmes_model, logger)

    get_cgmes_base_voltages(gc_model, cgmes_model, logger)

    get_cgmes_substations(gc_model, cgmes_model, logger)
    get_cgmes_voltage_levels(gc_model, cgmes_model, logger)

    get_cgmes_tn_nodes(gc_model, cgmes_model, logger)
    get_cgmes_cn_nodes_from_tn_nodes(gc_model, cgmes_model, logger)
    # TODO BusbarSection
    # get_cgmes_cn_nodes_from_cns(gc_model, cgmes_model, logger)

    get_cgmes_loads(gc_model, cgmes_model, logger)
    get_cgmes_equivalent_injections(gc_model, cgmes_model, logger)
    get_cgmes_generators(gc_model, cgmes_model, logger)

    get_cgmes_ac_line_segments(gc_model, cgmes_model, logger)
    # transformers, windings
    get_cgmes_power_transformers(gc_model, cgmes_model, logger)

    # shunts
    get_cgmes_linear_shunts(gc_model, cgmes_model, logger)

    # results: sv classes
    if pf_results:
        # if converged == True...

        # SvVoltage for every TopoNode
        get_cgmes_sv_voltages(cgmes_model, pf_results, logger)

        # PowerFlow: P, Q results for every terminal
        get_cgmes_sv_power_flow(gc_model, num_circ, cgmes_model, pf_results, logger)
        # TODO check: two elements on one bus! (loads or gens, shunts)

        # SV Status: for ConductingEquipment
        # TODO create_sv_status() elements.active parameter

        # SVTapStep: handled at transformer function
        get_cgmes_sv_tap_step(gc_model, num_circ, cgmes_model, pf_results, logger)

        # SvShuntCompensatorSections:
        # create_sv_shunt_compensator_sections()
        # TODO call it from shunt function or write get_cgmes.. func

        # Topo Islands
        get_cgmes_topological_island(gc_model, cgmes_model, logger)

    else:
        logger.add_error(msg="Missing power flow result for CGMES export.")

    if logger.__len__() != 0:
        print("Logger is not empty! (cgmes export)")
    return cgmes_model
