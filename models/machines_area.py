# -*- coding: utf-8 -*-

from odoo import api, fields, models


class MachinesArea(models.Model):
    _name = 'machines.area'
    _description = 'Area'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')

    model_ids = fields.One2many(
        comodel_name='machines.model', inverse_name='area_id', string='Models')
