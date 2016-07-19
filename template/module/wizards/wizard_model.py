# -*- coding: utf-8 -*-
# Copyright 2016 Jairo Llopis <jairo.llopis@tecnativa.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from openerp import api, models


class WizardModel(models.TransientModel):
    _name = "module.wizard_model"

    @api.multi
    def action_accept(self):
        self.ensure_one()
        self.do_something_useful()
