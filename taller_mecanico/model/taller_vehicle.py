# -*- encoding: utf-8 -*-
from osv import osv, fields
from datetime import datetime


class fleet_vehicle_year(osv.osv):
    _name = 'fleet.vehicle'
    _inherit = 'fleet.vehicle'
    years = [(num, str(num)) for num in range(1970, (datetime.now().year)+1)]
    _columns = {
        'year': fields.selection(years, 'Año'),
        'driver_id_custom': fields.many2one('res.partner',
                                            'Cliente',
                                            domain="[('customer','=',True)]",
                                            required="True"),
        'vin_sn_custom': fields.char('Número de serie',
                                     size=40),
        }
