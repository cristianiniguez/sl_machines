# -*- coding: utf-8 -*-

from odoo import api, fields, models


class MachinesMachine(models.Model):
    _name = 'machines.machine'
    _description = 'Machine'

    name = fields.Char(string='Code')
    model_id = fields.Many2one(comodel_name='machines.model', string='Model')
