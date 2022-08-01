# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import logging
from odoo.exceptions import UserError

class nuprod_contact_custom(models.Model):

    _description = 'nuprod_contact_custom.nuprod_contact_custom'
    _inherit = 'res.partner'
    logger = logging.getLogger(__name__)
    logger.warning('Nuprod Load')

    def create_customer_account(self):
        logger = logging.getLogger(__name__)
        compteExistant = []
        logger.warning('Customer')
        account = self.env['account.account'].search([
                ('code', '=like', '411%'),
        ])
        for record in account:
            compteExistant.append(record['code'])
            if self.name in record['name']:
                raise UserError(
                            _(
                                "This customer account has already been created"
                            )
                        )
                return True

        for compte in range(int(account[0]['code']),int(account[-1]['code'])):
            if str(compte) not in compteExistant:
                logger.warning('Next code ' + str(compte))
                logger.warning('Clients - ' + self.name)
                self.property_account_receivable_id = self.env['account.account'].create({
                    'name': 'Clients - ' + self.name,
                    'code': str(compte),
                    'user_type_id': self.env.ref('account.data_account_type_receivable').id,
                    'reconcile': True,
                }).id
                break
        return True

    def create_supplier_account(self):
        logger = logging.getLogger(__name__)
        compteExistant = []
        logger.warning('Supplier')
        account = self.env['account.account'].search([
                ('code', '=like', '401%'),
        ])
        for record in account:
            compteExistant.append(record['code'])
            if self.name in record['name']:
                raise UserError(
                            _(
                                "This supplier account has already been created"
                            )
                        )
                return True
        for compte in range(int(account[0]['code']),int(account[-1]['code'])):
            if str(compte) not in compteExistant:
                logger.warning('Next code ' + str(compte))
                logger.warning('Fournisseur - ' + self.name)
                self.property_account_payable_id = self.env['account.account'].create({
                    'name': 'Fournisseur - ' + self.name,
                    'code': str(compte),
                    'user_type_id': self.env.ref('account.data_account_type_payable').id,
                    'reconcile': True,
                }).id
                break
        return True

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
