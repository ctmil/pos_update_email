from odoo import api, fields, models, tools, _

class PosOrder(models.Model):
    _inherit = 'pos.order'

    def action_receipt_to_customer(self, name, client, ticket):
        res = super(PosOrder, self).action_receipt_to_customer(name,client,ticket)
        mail = client.get('email')
        if mail:
            for record in self:
                partner = record.partner_id
                # if customer is consumidor final, creates new partner
                if partner.l10n_latam_identification_type_id.name == 'Sigd':
                    vals_partner = {
                        'name': mail,
                        'email': mail,
                        'customer_rank': 1,
                        }
                    self.env['res.partner'].create(vals_partner)
                else:
                    partner.email = mail
        return res

