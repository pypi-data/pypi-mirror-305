# GridCal
# Copyright (C) 2015 - 2023 Santiago Peñate Vera
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
from GridCalEngine.IO.base.units import UnitMultiplier, UnitSymbol
from GridCalEngine.IO.cim.cgmes.cgmes_v2_4_15.devices.energy_consumer import EnergyConsumer
from GridCalEngine.IO.cim.cgmes.cgmes_enums import cgmesProfile


class ConformLoad(EnergyConsumer):
	def __init__(self, rdfid='', tpe='ConformLoad'):
		EnergyConsumer.__init__(self, rdfid, tpe)

		from GridCalEngine.IO.cim.cgmes.cgmes_v2_4_15.devices.conform_load_group import ConformLoadGroup
		self.LoadGroup: ConformLoadGroup | None = None

		self.register_property(
			name='LoadGroup',
			class_type=ConformLoadGroup,
			multiplier=UnitMultiplier.none,
			unit=UnitSymbol.none,
			description='''Group of this ConformLoad.''',
			profiles=[]
		)
