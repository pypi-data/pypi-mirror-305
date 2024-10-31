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
from __future__ import annotations

from GridCalEngine.IO.base.units import UnitMultiplier, UnitSymbol
from GridCalEngine.IO.cim.cgmes.cgmes_v3_0_0.devices.acdc_terminal import ACDCTerminal
from GridCalEngine.IO.cim.cgmes.cgmes_enums import cgmesProfile


class DCBaseTerminal(ACDCTerminal):
	def __init__(self, rdfid='', tpe='DCBaseTerminal'):
		ACDCTerminal.__init__(self, rdfid, tpe)

		from GridCalEngine.IO.cim.cgmes.cgmes_v3_0_0.devices.dc_node import DCNode
		self.DCNode: DCNode | None = None
		from GridCalEngine.IO.cim.cgmes.cgmes_v3_0_0.devices.dc_topological_node import DCTopologicalNode
		self.DCTopologicalNode: DCTopologicalNode | None = None

		self.register_property(
			name='DCNode',
			class_type=DCNode,
			multiplier=UnitMultiplier.none,
			unit=UnitSymbol.none,
			description='''The DC connectivity node to which this DC base terminal connects with zero impedance.''',
			profiles=[]
		)
		self.register_property(
			name='DCTopologicalNode',
			class_type=DCTopologicalNode,
			multiplier=UnitMultiplier.none,
			unit=UnitSymbol.none,
			description='''See association end Terminal.TopologicalNode.''',
			profiles=[]
		)
