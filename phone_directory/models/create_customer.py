# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class CreateCustomer(models.Model):
    """Create and save Customer"""

    # _name = 'phone_directory.create_customer'
    _inherit = 'res.partner'

    fathername = fields.Char(string="Father's Name")
    mothername = fields.Char(string="Mother's Name")


    # @api.model
    # def create(self, vals):
    #
    #     if vals.get('id', 'New') == 'New':
    #         vals['id'] = self.env['ir.sequence'].next_by_code('phone_directory.id') or '/'
    #     return super(Phonedirectory, self).create(vals)
    #
    # @api.model
    # def save(self, vals):
    #
    #     if vals.get('id', 'New') == 'New':
    #         vals['id'] = self.env['ir.sequence'].next_by_code('phone_directory.id') or '/'
    #     return super(Phonedirectory, self).save(vals)
